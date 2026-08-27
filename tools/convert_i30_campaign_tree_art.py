#!/usr/bin/env python3
"""Convert I-30 Campaign Tree PNG sources to Vic3 A8R8G8B8 DDS."""

from __future__ import annotations

import os
import sys

from PIL import Image

# Reuse DDS writer from existing tool
sys.path.insert(0, os.path.dirname(__file__))
from convert_sp_icons import fit_square, write_dds_bgra  # noqa: E402

MOD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(MOD, "gfx", "_source", "i30_campaign_tree")
OUT_ICON = os.path.join(MOD, "gfx", "interface", "icons", "sp_campaign_tree")
OUT_ILLUST = os.path.join(MOD, "gfx", "interface", "illustrations", "sp_campaign_tree")
OUT_PREVIEW = os.path.join(MOD, "gfx", "_preview", "i30_campaign_tree")


def even4(im: Image.Image) -> Image.Image:
    w, h = im.size
    return im.crop((0, 0, w - w % 4, h - h % 4))


def force_opaque(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, _a = px[x, y]
            px[x, y] = (r, g, b, 255)
    return im


def resize_cover(im: Image.Image, tw: int, th: int) -> Image.Image:
    """Center-crop to target aspect, then resize."""
    im = im.convert("RGBA")
    w, h = im.size
    target_aspect = tw / th
    src_aspect = w / h
    if src_aspect > target_aspect:
        nw = int(h * target_aspect)
        left = (w - nw) // 2
        im = im.crop((left, 0, left + nw, h))
    else:
        nh = int(w / target_aspect)
        top = (h - nh) // 2
        im = im.crop((0, top, w, top + nh))
    return im.resize((tw, th), Image.Resampling.LANCZOS)


def main() -> None:
    os.makedirs(OUT_ICON, exist_ok=True)
    os.makedirs(OUT_ILLUST, exist_ok=True)
    os.makedirs(OUT_PREVIEW, exist_ok=True)

    # Sidebar: square transparent UI icon
    side = Image.open(os.path.join(SRC, "sp_ct_sidebar_icon.png"))
    side = fit_square(side, 128, pad_ratio=0.06)
    write_dds_bgra(os.path.join(OUT_ICON, "sp_ct_sidebar_icon.dds"), side, mipmaps=True)
    side.save(os.path.join(OUT_PREVIEW, "sp_ct_sidebar_icon.png"))

    # Header strip — crop ornate frame, stretch-fill wide HUD strip (no letterbox)
    header = Image.open(os.path.join(SRC, "sp_ct_header_logo.png")).convert("RGBA")
    hw, hh = header.size
    header = header.crop((int(hw * 0.07), int(hh * 0.18), int(hw * 0.93), int(hh * 0.82)))
    header = header.resize((2048, 160), Image.Resampling.LANCZOS)
    header = force_opaque(header)
    write_dds_bgra(os.path.join(OUT_ICON, "sp_ct_header_logo.dds"), header, mipmaps=True)
    header.save(os.path.join(OUT_PREVIEW, "sp_ct_header_logo.png"))

    insp = [
        "sp_ct_insp_tanzimat",
        "sp_ct_insp_post_tanzimat",
        "sp_ct_insp_identity",
        "sp_ct_insp_ottomanism",
        "sp_ct_insp_islamism",
        "sp_ct_insp_turkism",
        "sp_ct_insp_turan",
        "sp_ct_insp_turan_s1",
        "sp_ct_insp_turan_s2",
        "sp_ct_insp_turan_s3",
        "sp_ct_insp_turan_s4",
        "sp_ct_insp_great_ottoman",
        "sp_ct_insp_empty",
    ]
    for name in insp:
        src = os.path.join(SRC, f"{name}.png")
        im = Image.open(src).convert("RGBA")
        im = resize_cover(im, 1024, 512)
        im = force_opaque(im)
        write_dds_bgra(os.path.join(OUT_ILLUST, f"{name}.dds"), im, mipmaps=False)
        im.save(os.path.join(OUT_PREVIEW, f"{name}.png"))

    print("DONE")


if __name__ == "__main__":
    main()
