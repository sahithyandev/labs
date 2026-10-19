import os
import tempfile
import unittest

from PIL import Image

from JR_230557T import Color, Jpeg, Matrix, clamp

IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lighthouse.bmp")

# 8x8 luma block from Wallace (1992), as used in the report's worked example
WALLACE_BLOCK = [
    [52, 55, 61, 66, 70, 61, 64, 73],
    [63, 59, 55, 90, 109, 85, 69, 72],
    [62, 59, 68, 113, 144, 104, 66, 73],
    [63, 58, 71, 122, 154, 106, 70, 69],
    [67, 61, 68, 104, 126, 88, 68, 70],
    [79, 65, 60, 70, 77, 68, 58, 75],
    [85, 71, 64, 59, 55, 61, 65, 83],
    [87, 79, 69, 68, 65, 76, 78, 94],
]
SHIFTED_BLOCK = [[sample - 128 for sample in row] for row in WALLACE_BLOCK]

# The real photo (512 wide, 768 tall) and a crop of it that is not a multiple of 16
PHOTO = Image.open(IMAGE_PATH).convert("RGB")
CROP = PHOTO.crop((101, 200, 138, 221))  # 37 wide, 21 tall


class TestPhoto(unittest.TestCase):
    def test_reads_photo_size(self):
        self.assertEqual(PHOTO.size, (512, 768))


class TestColor(unittest.TestCase):
    def test_worked_example_pixel(self):
        y, cb, cr = Color.rgb_to_ycbcr(200, 100, 50)
        self.assertAlmostEqual(y, 124.2, 1)
        self.assertAlmostEqual(cb, 86.1, 1)
        self.assertAlmostEqual(cr, 182.1, 1)

    def test_round_trip(self):
        r, g, b = Color.ycbcr_to_rgb(*Color.rgb_to_ycbcr(200, 100, 50))
        self.assertEqual((clamp(r, 0, 255), clamp(g, 0, 255), clamp(b, 0, 255)), (200, 100, 50))

    def test_clamp(self):
        self.assertEqual(clamp(-5.2, 0, 255), 0)
        self.assertEqual(clamp(300.7, 0, 255), 255)
        self.assertEqual(clamp(127.6, 0, 255), 128)


class TestPlanes(unittest.TestCase):
    def test_padded_size(self):
        self.assertEqual(Jpeg.padded_size(37, 21), (48, 32))
        self.assertEqual(Jpeg.padded_size(32, 16), (32, 16))

    def test_pad_repeats_last_column_and_row(self):
        padded = Jpeg.pad([[1, 2], [3, 4]], 4, 3)
        self.assertEqual(padded, [[1, 2, 2, 2], [3, 4, 4, 4], [3, 4, 4, 4]])

    def test_subsample_averages_2x2_groups(self):
        plane = [[10, 20, 0, 0],
                 [30, 40, 0, 8]]
        self.assertEqual(Jpeg.subsample(plane), [[25, 2]])

    def test_upsample_repeats_samples(self):
        self.assertEqual(Jpeg.upsample([[1, 2]]), [[1, 1, 2, 2], [1, 1, 2, 2]])

    def test_split_and_join_blocks(self):
        plane = [[x + 16 * y for x in range(16)] for y in range(16)]
        grid = Jpeg.split_into_blocks(plane)
        self.assertEqual((len(grid), len(grid[0])), (2, 2))
        self.assertEqual(grid[0][1][0], plane[0][8:16])  # top-right block, first row
        self.assertEqual(grid[1][0][0], plane[8][0:8])  # bottom-left block, first row
        self.assertEqual(Jpeg.join_blocks(grid), plane)


class TestMatrix(unittest.TestCase):
    def test_transpose(self):
        self.assertEqual(Matrix([[1, 2, 3], [4, 5, 6]]).transpose().rows, [[1, 4], [2, 5], [3, 6]])

    def test_product(self):
        product = Matrix([[1, 2], [3, 4]]) @ Matrix([[5, 6], [7, 8]])
        self.assertEqual(product.rows, [[19, 22], [43, 50]])


class TestDct(unittest.TestCase):
    def setUp(self):
        self.jpeg = Jpeg()

    def test_worked_example_coefficients(self):
        coefficients = self.jpeg.dct_forward(SHIFTED_BLOCK)
        self.assertAlmostEqual(coefficients[0][0], -415.4, 1)
        self.assertAlmostEqual(coefficients[0][1], -30.2, 1)

    def test_inverse_recovers_block(self):
        back = self.jpeg.dct_inverse(self.jpeg.dct_forward(SHIFTED_BLOCK))
        for row, back_row in zip(SHIFTED_BLOCK, back):
            for sample, back_sample in zip(row, back_row):
                self.assertAlmostEqual(sample, back_sample, 6)

    def test_flat_block_has_only_dc(self):
        coefficients = self.jpeg.dct_forward([[10] * 8 for _ in range(8)])
        self.assertAlmostEqual(coefficients[0][0], 80)  # 8 * mean
        self.assertAlmostEqual(coefficients[3][4], 0)


class TestQuantizer(unittest.TestCase):
    def test_quality_50_keeps_table(self):
        self.assertEqual(Jpeg(50).tables[0], Jpeg.LUMA)

    def test_higher_quality_gives_smaller_divisors(self):
        low, high = Jpeg(20).tables[0], Jpeg(90).tables[0]
        self.assertGreater(low[7][7], high[7][7])

    def test_divisors_stay_in_range(self):
        for quality in (1, 100):
            for table in Jpeg(quality).tables:
                for row in table:
                    for divisor in row:
                        self.assertTrue(1 <= divisor <= 255)

    def test_chroma_table_is_coarser(self):
        quantizer = Jpeg(50)
        self.assertGreater(quantizer.tables[1][0][1], quantizer.tables[0][0][1])

    def test_worked_example(self):
        quantized = Jpeg(50).quantize(Jpeg().dct_forward(SHIFTED_BLOCK), 0)
        self.assertEqual(quantized[0], [-26, -3, -6, 2, 2, -1, 0, 0])

    def test_dequantize_multiplies_by_table(self):
        block = [[1] * 8 for _ in range(8)]
        self.assertEqual(Jpeg(50).dequantize(block, 0), Jpeg.LUMA)


class TestZigZag(unittest.TestCase):
    def test_order_starts_and_ends(self):
        self.assertEqual(Jpeg.ZIGZAG_ORDER[:6], [(0, 0), (0, 1), (1, 0), (2, 0), (1, 1), (0, 2)])
        self.assertEqual(Jpeg.ZIGZAG_ORDER[-1], (7, 7))

    def test_order_visits_every_cell_once(self):
        self.assertEqual(len(set(Jpeg.ZIGZAG_ORDER)), 64)

    def test_scan_and_unscan(self):
        block = [[8 * u + v for v in range(8)] for u in range(8)]
        scan = Jpeg.zigzag_scan(block)
        self.assertEqual(scan[:4], [0, 1, 8, 16])
        self.assertEqual(Jpeg.zigzag_unscan(scan), block)

    def test_worked_example_scan(self):
        quantized = Jpeg(50).quantize(Jpeg().dct_forward(SHIFTED_BLOCK), 0)
        scan = Jpeg.zigzag_scan(quantized)
        self.assertEqual(scan[:19], [-26, -3, 0, -3, -2, -6, 2, -4, 1, -3, 1, 1, 5, 1, 2, -1, 1, -1, 2])


class TestSymbols(unittest.TestCase):
    def test_size(self):
        self.assertEqual([Jpeg.symbol_size(v) for v in (0, 1, -3, 5, 255)], [0, 1, 2, 3, 8])

    def test_value_bits(self):
        self.assertEqual(Jpeg.value_bits(3), "11")
        self.assertEqual(Jpeg.value_bits(-3), "00")
        self.assertEqual(Jpeg.value_bits(0), "")

    def test_bits_value_inverts_value_bits(self):
        for value in range(-300, 301):
            self.assertEqual(Jpeg.bits_value(Jpeg.value_bits(value)), value)

    def test_rle_worked_example(self):
        quantized = Jpeg(50).quantize(Jpeg().dct_forward(SHIFTED_BLOCK), 0)
        symbols = Jpeg.rle(Jpeg.zigzag_scan(quantized)[1:])
        self.assertEqual(len(symbols), 20)  # 19 pairs + EOB
        self.assertEqual(symbols[1], (0x12, -3))  # 0 zeros, size 2
        self.assertEqual(symbols[-3], (0x51, -1))  # five zeros, then -1
        self.assertEqual(symbols[-1], (Jpeg.END_OF_BLOCK, 0))

    def test_rle_long_run_uses_zrl(self):
        ac = [0] * 20 + [1] + [0] * 42
        self.assertEqual(Jpeg.rle(ac), [(Jpeg.ZRL, 0), (0x41, 1), (Jpeg.END_OF_BLOCK, 0)])

    def test_rle_all_zero_is_just_eob(self):
        self.assertEqual(Jpeg.rle([0] * 63), [(Jpeg.END_OF_BLOCK, 0)])


def codes_of(symbols):
    return Jpeg.huffman_codes(*Jpeg.huffman_table(symbols))


class TestHuffman(unittest.TestCase):
    def test_codes_are_prefix_free(self):
        codes = codes_of("aaaabbbccd")
        for a in codes.values():
            for b in codes.values():
                self.assertTrue(a == b or not b.startswith(a))

    def test_frequent_symbols_get_shorter_codes(self):
        codes = codes_of("aaaabbbccd")
        self.assertLessEqual(len(codes["a"]), len(codes["d"]))

    def test_single_symbol_gets_one_bit(self):
        self.assertEqual(codes_of("zzz"), {"z": "0"})

    def test_no_symbols(self):
        self.assertEqual(Jpeg.huffman_table([]), ([0] * 16, []))
        self.assertEqual(codes_of([]), {})

    def test_no_code_is_all_ones(self):
        # JPEG reserves the all-ones code. Two equal symbols would use "0" and "1".
        for symbols in ("ab", "aab", "aaaabbbccd"):
            for code in codes_of(symbols).values():
                self.assertNotEqual(code, "1" * len(code))

    def test_codes_are_limited_to_16_bits(self):
        # Fibonacci counts give the deepest possible Huffman tree: 25 symbols need 24 bits.
        symbols = []
        a, b = 1, 1
        for symbol in range(25):
            symbols.extend([symbol] * a)
            a, b = b, a + b
        codes = codes_of(symbols)
        self.assertEqual(len(codes), 25)
        longest = max(len(code) for code in codes.values())
        self.assertLessEqual(longest, 16)
        codes = list(codes.values())
        for first in codes:
            for second in codes:
                self.assertTrue(first == second or not second.startswith(first))

    def test_codes_follow_from_the_stored_table(self):
        length_counts, symbols = Jpeg.huffman_table([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5])
        self.assertEqual(sum(length_counts), len(symbols))
        self.assertEqual(Jpeg.huffman_codes(length_counts, symbols), codes_of([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]))


class TestPackBits(unittest.TestCase):
    def test_bits_become_bytes(self):
        self.assertEqual(Jpeg.pack_bits(["10100101", "0001"]), bytes([0b10100101, 0b00011111]))  # last byte padded with 1s

    def test_ff_byte_is_followed_by_zero(self):
        self.assertEqual(Jpeg.pack_bits(["11111111", "00000001"]), bytes([0xFF, 0x00, 0x01]))

    def test_nothing_written(self):
        self.assertEqual(Jpeg.pack_bits([]), b"")


class TestReadBits(unittest.TestCase):
    def test_read_and_read_symbol(self):
        jpeg = Jpeg()
        jpeg.bits = "0110100"
        self.assertEqual(jpeg.read_bits(2), "01")
        self.assertEqual(jpeg.read_symbol({"10": "x", "1": "y"}), "y")  # stops at the first match
        self.assertEqual(jpeg.read_bits(3), "010")


class TestJpeg(unittest.TestCase):
    def test_output_is_a_jpeg_file(self):
        file_bytes = Jpeg(75).encode(CROP)
        self.assertEqual(file_bytes[:2], b"\xFF\xD8")  # start of image
        self.assertEqual(file_bytes[2:4], b"\xFF\xE0")  # JFIF header
        self.assertEqual(file_bytes[6:11], b"JFIF\x00")
        self.assertEqual(file_bytes[-2:], b"\xFF\xD9")  # end of image

    def test_full_photo_round_trip(self):
        file_bytes = Jpeg(75).encode(PHOTO)
        decoded = Jpeg().decode(file_bytes)
        self.assertEqual((len(decoded), len(decoded[0])), (768, 512))
        self.assertGreater(Jpeg.psnr(PHOTO, decoded), 30)
        self.assertGreater(768 * 512 * 3 / len(file_bytes), 10)  # BMP pixel bytes / file bytes

    def test_crop_with_padding(self):
        decoded = Jpeg().decode(Jpeg(90).encode(CROP))
        self.assertEqual((len(decoded), len(decoded[0])), (21, 37))
        self.assertGreater(Jpeg.psnr(CROP, decoded), 30)

    def test_lower_quality_gives_smaller_file_and_lower_psnr(self):
        low = Jpeg(20).encode(PHOTO)
        high = Jpeg(90).encode(PHOTO)
        self.assertLess(len(low), len(high))
        self.assertLess(Jpeg.psnr(PHOTO, Jpeg().decode(low)), Jpeg.psnr(PHOTO, Jpeg().decode(high)))

    def test_flat_image_is_nearly_lossless(self):
        flat = Image.new("RGB", (16, 16), (120, 60, 200))
        decoded = Jpeg().decode(Jpeg(75).encode(flat))
        self.assertGreater(Jpeg.psnr(flat, decoded), 40)

    def test_file_stores_the_quantization_table(self):
        file_bytes = Jpeg(30).encode(CROP)
        marker = file_bytes.index(b"\xFF\xDB")  # first DQT segment: luma table
        stored = file_bytes[marker + 5:marker + 5 + 64]  # after marker, length and table id
        expected = Jpeg.zigzag_scan(Jpeg(30).tables[0])
        self.assertEqual(list(stored), expected)

    def test_decoder_rejects_other_files(self):
        with self.assertRaises(ValueError):
            Jpeg().decode(b"not a jpeg at all")


class TestPsnr(unittest.TestCase):
    def test_identical_images_give_infinity(self):
        self.assertEqual(Jpeg.psnr(CROP, [[CROP.getpixel((x, y)) for x in range(CROP.width)] for y in range(CROP.height)]), float("inf"))

    def test_known_value(self):
        self.assertAlmostEqual(Jpeg.psnr(Image.new("RGB", (1, 1)), [[(1, 1, 1)]]), 48.13, 2)  # 10 * log10(255^2)


if __name__ == "__main__":
    unittest.main()
