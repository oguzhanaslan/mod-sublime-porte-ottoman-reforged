#!/usr/bin/env python3
"""Convert ChatGPT PNG/JPG sources to Victoria 3 A8R8G8B8 DDS icons/pictures."""

from __future__ import annotations

import os
import struct
from collections import deque

from PIL import Image

MOD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(MOD, "assets")


def find(substr: str) -> str:
    if not os.path.isdir(ASSETS):
        raise FileNotFoundError(f"source assets directory not found: {ASSETS}")
    substr = substr.lower()
    for name in os.listdir(ASSETS):
        if substr in name.lower():
            return os.path.join(ASSETS, name)
    raise FileNotFoundError(substr)


def flood_remove_black(im: Image.Image, thresh: int = 28, soft: int = 12) -> Image.Image:
    """Remove near-black background connected to edges; keep interior dark pixels."""
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    visited = [[False] * w for _ in range(h)]
    q: deque[tuple[int, int]] = deque()

    def is_bg(r: int, g: int, b: int, a: int) -> bool:
        return a < 8 or max(r, g, b) <= thresh

    for x in range(w):
        for y in (0, h - 1):
            r, g, b, a = px[x, y]
            if is_bg(r, g, b, a):
                q.append((x, y))
                visited[y][x] = True
    for y in range(h):
        for x in (0, w - 1):
            if visited[y][x]:
                continue
            r, g, b, a = px[x, y]
            if is_bg(r, g, b, a):
                q.append((x, y))
                visited[y][x] = True

    bg = [[False] * w for _ in range(h)]
    while q:
        x, y = q.popleft()
        bg[y][x] = True
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                r, g, b, a = px[nx, ny]
                if is_bg(r, g, b, a):
                    visited[ny][nx] = True
                    q.append((nx, ny))

    out = Image.new("RGBA", (w, h))
    opx = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if bg[y][x]:
                opx[x, y] = (r, g, b, 0)
                continue
            m = max(r, g, b)
            if m <= thresh + soft:
                near = False
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < w and 0 <= ny < h and bg[ny][nx]:
                        near = True
                        break
                if near:
                    alpha = int(255 * (m - thresh) / soft) if m > thresh else 0
                    opx[x, y] = (r, g, b, max(0, min(255, alpha)))
                else:
                    opx[x, y] = (r, g, b, a)
            else:
                opx[x, y] = (r, g, b, a)
    return out


def fit_square(im: Image.Image, size: int, pad_ratio: float = 0.06) -> Image.Image:
    im = im.convert("RGBA")
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    max_inner = int(size * (1 - 2 * pad_ratio))
    tw, th = im.size
    scale = min(max_inner / tw, max_inner / th)
    nw = max(1, int(tw * scale))
    nh = max(1, int(th * scale))
    im2 = im.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas.paste(im2, ((size - nw) // 2, (size - nh) // 2), im2)
    return canvas


def write_dds_bgra(path: str, im: Image.Image, mipmaps: bool = True) -> None:
    im = im.convert("RGBA")
    w, h = im.size
    levels: list[Image.Image] = []
    cur = im
    while True:
        levels.append(cur)
        if not mipmaps or (cur.width <= 1 and cur.height <= 1):
            break
        nw = max(1, cur.width // 2)
        nh = max(1, cur.height // 2)
        if nw == cur.width and nh == cur.height:
            break
        cur = cur.resize((nw, nh), Image.Resampling.LANCZOS)
        if len(levels) > 16:
            break

    ddsd_caps = 0x1
    ddsd_height = 0x2
    ddsd_width = 0x4
    ddsd_pitch = 0x8
    ddsd_pixelformat = 0x1000
    ddsd_mipmapcount = 0x20000
    flags = ddsd_caps | ddsd_height | ddsd_width | ddsd_pitch | ddsd_pixelformat
    if mipmaps and len(levels) > 1:
        flags |= ddsd_mipmapcount

    ddpf_alphapixels = 0x1
    ddpf_rgb = 0x40
    ddscaps_texture = 0x1000
    ddscaps_mipmap = 0x400000
    ddscaps_complex = 0x8
    caps = ddscaps_texture
    if mipmaps and len(levels) > 1:
        caps |= ddscaps_mipmap | ddscaps_complex

    header = bytearray(128)
    header[0:4] = b"DDS "
    struct.pack_into("<I", header, 4, 124)
    struct.pack_into("<I", header, 8, flags)
    struct.pack_into("<I", header, 12, h)
    struct.pack_into("<I", header, 16, w)
    struct.pack_into("<I", header, 20, w * 4)
    struct.pack_into("<I", header, 24, 0)
    struct.pack_into("<I", header, 28, len(levels) if mipmaps else 0)
    struct.pack_into("<I", header, 76, 32)
    struct.pack_into("<I", header, 80, ddpf_alphapixels | ddpf_rgb)
    struct.pack_into("<I", header, 84, 0)
    struct.pack_into("<I", header, 88, 32)
    struct.pack_into("<I", header, 92, 0x00FF0000)
    struct.pack_into("<I", header, 96, 0x0000FF00)
    struct.pack_into("<I", header, 100, 0x000000FF)
    struct.pack_into("<I", header, 104, 0xFF000000)
    struct.pack_into("<I", header, 108, caps)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(header)
        for level in levels:
            f.write(level.tobytes("raw", "BGRA"))
    print(f"WROTE {path} {w}x{h} mips={len(levels)} bytes={os.path.getsize(path)}")


def main() -> None:
    # Company 256 (already transparent)
    im = fit_square(Image.open(find("sp_company_sirket_i_hayriye")), 256, pad_ratio=0.04)
    write_dds_bgra(
        os.path.join(
            MOD,
            "gfx/interface/icons/company_icons/historical_company_icons/sp_company_sirket_i_hayriye.dds",
        ),
        im,
        mipmaps=True,
    )

    # JE icons 150
    for key, fname in (
        ("hunkariskelesi", "sp_je_hunkar_iskelesi.dds"),
        ("post-tanzimat_era", "sp_je_post_tanzimat_era.dds"),
        ("armenian_question", "sp_je_armenian_question.dds"),
    ):
        im = flood_remove_black(Image.open(find(key)), thresh=30, soft=14)
        im = fit_square(im, 150, pad_ratio=0.05)
        write_dds_bgra(
            os.path.join(MOD, "gfx/interface/icons/event_icons", fname),
            im,
            mipmaps=True,
        )

    # I-10B event icon 150
    im = flood_remove_black(Image.open(find("sp_i10b_officer_event_icon")), thresh=22, soft=10)
    im = fit_square(im, 150, pad_ratio=0.05)
    write_dds_bgra(
        os.path.join(MOD, "gfx/interface/icons/event_icons/sp_i10b_officer_event.dds"),
        im,
        mipmaps=True,
    )

    # I-10B event scene texture (opaque, no mips)
    scene = Image.open(find("sp_i10b_officer_event_scene")).convert("RGBA")
    w, h = scene.size
    scene = scene.crop((0, 0, w - w % 4, h - h % 4))
    px = scene.load()
    for y in range(scene.height):
        for x in range(scene.width):
            r, g, b, _a = px[x, y]
            px[x, y] = (r, g, b, 255)
    write_dds_bgra(
        os.path.join(MOD, "gfx/event_pictures/sp_i10b_officer_event_scene.dds"),
        scene,
        mipmaps=False,
    )


if __name__ == "__main__":
    main()
