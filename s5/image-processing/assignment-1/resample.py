"""
Resample an image with nearest-neighbour and bilinear interpolation.

Usage: python resample.py input.jpg 0.5      # scale factor (e.g. 0.5 = half size, 2 = double)
"""

import sys
from typing import Any, cast
from PIL import Image
from math import floor, ceil

## AI ASSISTANCE DISCLOSURE (Claude Code):
# - Asked it to explain the assignment task and the conceptual difference
#   between nearest-neighbour and bilinear interpolation before writing code.
# - Had it scaffold the file structure (load/resize/main, CLI arg parsing).
# - Wrote the bilinear interpolation logic myself; asked Claude to review it
#   and it identified certain bugs in weight formula and coordinate calculations.
#   I fixed them with help from Claude.
# - Asked it to fix minor type do a final review on the code.
# - Asked it to do a final cleanup and extract repeated code into utility functions.

RGB = tuple[int, int, int]
PixelAccess = Any  # PIL doesn't export a proper type for img.load()'s return value
OUTPUT_PATH = "out.png"


def load(path: str) -> tuple[Image.Image, int, int]:
    img = Image.open(path).convert("RGB")
    return img, img.width, img.height


def _new_canvas(dst_w: int, dst_h: int) -> tuple[Image.Image, PixelAccess]:
    dst = Image.new("RGB", (dst_w, dst_h))
    dst_px = dst.load()
    if dst_px is None:
        raise RuntimeError("dst_px is None")
    return dst, dst_px


def _clip(px: int, py: int, src_w: int, src_h: int) -> tuple[int, int]:
    return min(src_w - 1, max(0, px)), min(src_h - 1, max(0, py))


def nearest_neighbour(img: Image.Image, src_w: int, src_h: int, dst_w: int, dst_h: int) -> Image.Image:
    src_px = img.load()
    if src_px is None:
        raise RuntimeError("src_px is None")

    scale_x = dst_w / src_w
    scale_y = dst_h / src_h
    dst, dst_px = _new_canvas(dst_w, dst_h)

    for y in range(dst_h):
        for x in range(dst_w):
            sx = x / scale_x
            sy = y / scale_y

            candidates = [
                _clip(round(sx), floor(sy), src_w, src_h),  # top
                _clip(round(sx), ceil(sy), src_w, src_h),   # bottom
                _clip(floor(sx), round(sy), src_w, src_h),  # left
                _clip(ceil(sx), round(sy), src_w, src_h),   # right
            ]
            nx, ny = min(candidates, key=lambda p: (p[0] - sx) ** 2 + (p[1] - sy) ** 2)

            dst_px[x, y] = src_px[nx, ny]

    return dst


def bilinear(img: Image.Image, src_w: int, src_h: int, dst_w: int, dst_h: int) -> Image.Image:
    src_px = img.load()
    if src_px is None:
        raise RuntimeError("src_px is None")

    scale_x = dst_w / src_w
    scale_y = dst_h / src_h
    dst, dst_px = _new_canvas(dst_w, dst_h)

    for y in range(dst_h):
        for x in range(dst_w):
            sx = x / scale_x
            sy = y / scale_y

            sx_floor, sy_floor = _clip(floor(sx), floor(sy), src_w, src_h)
            sx_ceil, sy_ceil = _clip(ceil(sx), ceil(sy), src_w, src_h)

            fx = sx - sx_floor
            fy = sy - sy_floor

            top_left = cast(RGB, src_px[sx_floor, sy_floor])
            top_right = cast(RGB, src_px[sx_ceil, sy_floor])
            bottom_left = cast(RGB, src_px[sx_floor, sy_ceil])
            bottom_right = cast(RGB, src_px[sx_ceil, sy_ceil])

            dst_px[x, y] = tuple(
                round(
                    top_left[c] * (1 - fx) * (1 - fy) +
                    top_right[c] * fx * (1 - fy) +
                    bottom_left[c] * (1 - fx) * fy +
                    bottom_right[c] * fx * fy
                )
                for c in range(3)
            )

    return dst


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: python resample.py <image_path> <scale_factor>")
        sys.exit(1)

    path, scale = sys.argv[1], float(sys.argv[2])
    img, src_w, src_h = load(path)
    dst_w = max(1, round(src_w * scale))
    dst_h = max(1, round(src_h * scale))

    print(f"Resampling {path} from {src_w}x{src_h} to {dst_w}x{dst_h}")

    nn = nearest_neighbour(img, src_w, src_h, dst_w, dst_h)
    output_path = "out_nearest.png"
    nn.save(output_path)
    print(f"saved {output_path}")
    
    
    bl = bilinear(img, src_w, src_h, dst_w, dst_h)
    output_path = "out_bilinear.png"
    bl.save(output_path)
    print(f"saved {output_path}")


if __name__ == "__main__":
    main()
