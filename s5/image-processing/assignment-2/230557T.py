## Image Sources
#
# Reference image taken from: https://www.pinterest.com/pin/7881368092832945/
# Test image taken from my own camera

## AI ASSISTANCE DISCLOSURE:
# Used Claude Code to:
# - Add documentation for each utility function
# - Fix minor type issues in the code
# - Extract repeated code into utility functions
# - Optimize the code for performance

from pathlib import Path
from typing import cast

from PIL import Image, ImageDraw

INDEX_NO = "230557T"
SCRIPT_DIR = Path(__file__).resolve().parent


def load(path: Path) -> tuple[Image.Image, int, int]:
    """Open an image as RGB and return it along with its dimensions."""
    img = Image.open(path).convert("RGB")
    return img, img.width, img.height


def split_channels(img: Image.Image, w: int, h: int) -> tuple[list[int], list[int], list[int]]:
    """Extract R, G, B channels as flat 0-255 lists in a single pass over the pixels."""
    pixels = img.load()
    if pixels is None:
        raise ValueError("Image pixels are None")

    r_chan = [0] * (w * h)
    g_chan = [0] * (w * h)
    b_chan = [0] * (w * h)
    for y in range(h):
        for x in range(w):
            r, g, b = cast(tuple[int, int, int], pixels[x, y])
            i = y * w + x
            r_chan[i] = r
            g_chan[i] = g
            b_chan[i] = b
    return r_chan, g_chan, b_chan


def to_grayscale(r_chan: list[int], g_chan: list[int], b_chan: list[int]) -> list[int]:
    """Combine R, G, B channels into a flat list of grey levels using luminance weights."""
    return [int(r * 0.299 + g * 0.587 + b * 0.114) for r, g, b in zip(r_chan, g_chan, b_chan)]


def histogram(gray: list[int]) -> list[int]:
    """Count occurrences of each grey level 0-255."""
    hist = [0] * 256
    for v in gray:
        hist[v] += 1
    return hist


def cdf(hist: list[int]) -> list[float]:
    """Cumulative distribution function of a histogram, normalized to [0, 1]."""
    total = sum(hist)
    result = [1.0 / total] * 256
    running = 0
    for i, count in enumerate(hist):
        running += count
        result[i] *= running
    return result


def render_bars(values: list[float], draw: ImageDraw.ImageDraw, ox: int, oy: int, w: int, h: int) -> None:
    """Draw a simple bar chart of 256 values into a region of an image."""
    peak = max(values) or 1
    bar_w = w / 256
    for i, v in enumerate(values):
        bar_h = v / peak * h
        x0 = ox + i * bar_w
        draw.rectangle([x0, oy + h - bar_h, x0 + bar_w, oy + h], fill="black")


def save_histogram_plot(hist: list[int], path: Path) -> None:
    """Render a histogram's PDF and CDF side by side and save as a PNG."""
    total = sum(hist)
    pdf = [c / total for c in hist]
    cumulative = cdf(hist)

    w, h, pad = 800, 600, 60
    img = Image.new("RGB", (2 * w, h), "white")
    draw = ImageDraw.Draw(img)

    render_bars(pdf, draw, pad, pad, w - 2 * pad, h - 2 * pad)
    draw.text((pad, 10), "PDF", fill="black")

    render_bars(cumulative, draw, w + pad, pad, w - 2 * pad, h - 2 * pad)
    draw.text((w + pad, 10), "CDF", fill="black")

    img.save(path)
    print(f"  saved {path.name}")


def match_histogram(test_cdf: list[float], ref_cdf: list[float]) -> list[int]:
    """Build a 256-entry grey-level lookup table that maps test levels onto
    the reference distribution: each test level is sent to the reference
    level whose CDF value is closest to the test level's own CDF value."""
    mapping = [0] * 256
    for g, target in enumerate(test_cdf):
        best_level = 0
        best_diff = abs(ref_cdf[0] - target)
        for level in range(1, 256):
            diff = abs(ref_cdf[level] - target)
            if diff < best_diff:
                best_level = level
                best_diff = diff
        mapping[g] = best_level
    return mapping


print(f"Loading test_{INDEX_NO}.jpg and ref_{INDEX_NO}.jpg ...")
test_image = load(SCRIPT_DIR / f"test_{INDEX_NO}.jpg")
ref_image = load(SCRIPT_DIR / f"ref_{INDEX_NO}.jpg")

_, test_w, test_h = test_image
_, ref_w, ref_h = ref_image
print(f"  test image: {test_w}x{test_h}")
print(f"  ref image:  {ref_w}x{ref_h}")

print("Extracting R/G/B channels ...")
test_channels = split_channels(test_image[0], test_w, test_h)
ref_channels = split_channels(ref_image[0], ref_w, ref_h)

print("Computing reference grey-level histogram ...")
ref_hist = histogram(to_grayscale(*ref_channels))
save_histogram_plot(ref_hist, SCRIPT_DIR / f"rhist_{INDEX_NO}.png")

print("Matching R/G/B channels against the reference distribution ...")
matched_channels: list[list[int]] = []
for name, test_channel, ref_channel in zip(("R", "G", "B"), test_channels, ref_channels):
    test_cdf = cdf(histogram(test_channel))
    ref_cdf = cdf(histogram(ref_channel))
    mapping = match_histogram(test_cdf, ref_cdf)
    matched_channels.append([mapping[v] for v in test_channel])
    print(f"  {name} channel matched")

matched_pixels = list(zip(*matched_channels))
matched_image = Image.new("RGB", (test_w, test_h))
matched_image.putdata(matched_pixels)
matched_image.save(SCRIPT_DIR / f"matched_{INDEX_NO}.jpg")
print(f"  saved matched_{INDEX_NO}.jpg")

print("Computing matched image's grey-level histogram ...")
matched_hist = histogram(to_grayscale(*matched_channels))
save_histogram_plot(matched_hist, SCRIPT_DIR / f"thist_{INDEX_NO}.png")

print("Done.")
