#!/usr/bin/env python3
"""Validate SP custom DDS icons against vanilla A8R8G8B8 expectations."""

from __future__ import annotations

import os
import struct
import sys

from PIL import Image

MOD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def dds_info(path: str) -> dict:
    with open(path, "rb") as f:
        if f.read(4) != b"DDS ":
            return {"error": "bad magic", "path": path}
        f.read(4)
        flags = struct.unpack("<I", f.read(4))[0]
        h = struct.unpack("<I", f.read(4))[0]
        w = struct.unpack("<I", f.read(4))[0]
        pitch = struct.unpack("<I", f.read(4))[0]
        f.read(4)
        mips = struct.unpack("<I", f.read(4))[0]
        f.read(44)
        f.read(4)
        pfflags = struct.unpack("<I", f.read(4))[0]
        fourcc = f.read(4)
        bits = struct.unpack("<I", f.read(4))[0]
        r = struct.unpack("<I", f.read(4))[0]
        g = struct.unpack("<I", f.read(4))[0]
        b = struct.unpack("<I", f.read(4))[0]
        a = struct.unpack("<I", f.read(4))[0]
        size = os.path.getsize(path)
    expected = 128
    cw, ch = w, h
    n = mips if mips > 0 else 1
    for _ in range(n):
        expected += cw * ch * 4
        cw = max(1, cw // 2)
        ch = max(1, ch // 2)
    return {
        "path": path,
        "w": w,
        "h": h,
        "mips": mips,
        "pitch": pitch,
        "bits": bits,
        "pfflags": pfflags,
        "fourcc": fourcc,
        "R": r,
        "G": g,
        "B": b,
        "A": a,
        "size": size,
        "expected": expected,
        "size_ok": size == expected,
        "alpha": bool(pfflags & 1),
        "rgb": bool(pfflags & 0x40),
        "masks_ok": (r, g, b, a) == (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000),
        "uncompressed": fourcc == b"\x00\x00\x00\x00",
    }


def load_top(path: str) -> Image.Image:
    with open(path, "rb") as f:
        if f.read(4) != b"DDS ":
            raise ValueError(f"bad DDS magic: {path}")
        f.read(4)  # header size
        f.read(4)  # flags
        h = struct.unpack("<I", f.read(4))[0]
        w = struct.unpack("<I", f.read(4))[0]
        # Skip remainder of 128-byte DDS header (pitch/depth/mips/reserved/PF/caps).
        f.read(128 - 20)
        data = f.read(w * h * 4)
    return Image.frombytes("RGBA", (w, h), data, "raw", "BGRA")

def main() -> int:
    ours = [
        ("company", "gfx/interface/icons/company_icons/historical_company_icons/sp_company_sirket_i_hayriye.dds", 256, 256, True),
        ("je", "gfx/interface/icons/event_icons/sp_je_hunkar_iskelesi.dds", 150, 150, True),
        ("je", "gfx/interface/icons/event_icons/sp_je_post_tanzimat_era.dds", 150, 150, True),
        ("je", "gfx/interface/icons/event_icons/sp_je_armenian_question.dds", 150, 150, True),
        ("je", "gfx/interface/icons/event_icons/sp_i10b_officer_event.dds", 150, 150, True),
        ("scene", "gfx/event_pictures/sp_i10b_officer_event_scene.dds", 1024, 576, False),
    ]
    fails = 0
    for kind, rel, ew, eh, expect_alpha_corners in ours:
        path = os.path.join(MOD, rel)
        info = dds_info(path)
        ok = (
            info.get("size_ok")
            and info.get("bits") == 32
            and info.get("uncompressed")
            and info.get("masks_ok")
            and info.get("alpha")
            and info.get("w") == ew
            and info.get("h") == eh
        )
        if kind == "scene":
            ok = ok and info.get("mips") in (0, 1)
        else:
            ok = ok and info.get("mips") >= 1
        status = "PASS" if ok else "FAIL"
        if not ok:
            fails += 1
        print(
            f"{status} {os.path.basename(path)}: {info['w']}x{info['h']} "
            f"mips={info['mips']} bits={info['bits']} size={info['size']}/{info['expected']} "
            f"alpha={info['alpha']} masks={info['masks_ok']}"
        )
        if expect_alpha_corners:
            im = load_top(path)
            corners = [
                im.getpixel((0, 0))[3],
                im.getpixel((im.width - 1, 0))[3],
                im.getpixel((0, im.height - 1))[3],
                im.getpixel((im.width - 1, im.height - 1))[3],
            ]
            alphas = list(im.getchannel("A").get_flattened_data())
            opaque = sum(1 for a in alphas if a > 200)
            pct = 100.0 * opaque / (im.width * im.height)
            corner_ok = all(a == 0 for a in corners) and 15.0 <= pct <= 85.0
            print(f"  corners_alpha={corners} opaque_pct={pct:.1f} corner_ok={corner_ok}")
            if not corner_ok:
                fails += 1
                print("  FAIL alpha corner/opaque coverage")
        else:
            im = load_top(path)
            alphas = list(im.getchannel("A").get_flattened_data())
            if any(a < 255 for a in alphas):
                fails += 1
                print("  FAIL scene must be fully opaque")
            else:
                print("  scene opaque=OK")
    # vanilla size twin check
    v_company = dds_info(
        r"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game\gfx\interface\icons\company_icons\historical_company_icons\ap_moller.dds"
    )
    v_event = dds_info(
        r"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game\gfx\interface\icons\event_icons\event_trade.dds"
    )
    ours_c = dds_info(os.path.join(MOD, ours[0][1]))
    ours_e = dds_info(os.path.join(MOD, ours[1][1]))
    print(
        f"VANILLA twin company size: ours={ours_c['size']} vanilla={v_company['size']} match={ours_c['size']==v_company['size']}"
    )
    print(
        f"VANILLA twin event size: ours={ours_e['size']} vanilla={v_event['size']} match={ours_e['size']==v_event['size']}"
    )
    if ours_c["size"] != v_company["size"] or ours_e["size"] != v_event["size"]:
        fails += 1

    print("RESULT", "PASS" if fails == 0 else f"FAIL ({fails})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
