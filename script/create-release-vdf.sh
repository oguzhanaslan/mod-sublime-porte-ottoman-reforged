#!/usr/bin/env bash
# Generate workshop.vdf for SteamCMD workshop_build_item.
#
# Usage:
#   ./script/create-release-vdf.sh MOD_DIR DESC_FILE PUBLISHED_FILE_ID [CHANGENOTE_FILE] [OUT_VDF]
#
# Env:
#   CREATE_NEW=1   allow publishedfileid 0 (first Workshop item only)
#   VISIBILITY=N   write visibility (0 public, 1 friends, 2 hidden, 3 unlisted)
#
# SteamCMD stores VDF \n as literal \n on the Workshop page, so the description
# is flattened to BBCode-only structure (no newline escapes).
set -euo pipefail

if [[ $# -lt 3 ]]; then
  printf 'Usage: %s MOD_DIR DESC_FILE PUBLISHED_FILE_ID [CHANGENOTE_FILE] [OUT_VDF]\n' "$0" >&2
  exit 1
fi

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  printf 'python3 or python is required\n' >&2
  exit 1
fi

MOD_DIR="$1"
DESC_FILE="$2"
MOD_ID="$3"
CHANGENOTE_FILE="${4:-}"
OUT_VDF="${5:-workshop.vdf}"
CREATE_NEW="${CREATE_NEW:-0}"
VISIBILITY="${VISIBILITY:-}"

if [[ ! -d "$MOD_DIR" ]]; then
  printf 'Missing mod directory: %s\n' "$MOD_DIR" >&2
  exit 1
fi
MOD_PATH="$(cd "$MOD_DIR" && pwd)"

if [[ ! -f "$DESC_FILE" ]]; then
  printf 'Missing Steam description file: %s\n' "$DESC_FILE" >&2
  exit 1
fi

META="$MOD_PATH/.metadata/metadata.json"
if [[ ! -f "$META" ]]; then
  printf 'Missing metadata.json under mod directory\n' >&2
  exit 1
fi

if [[ ! -f "$MOD_PATH/thumbnail.png" ]]; then
  printf 'Missing thumbnail.png under mod directory\n' >&2
  exit 1
fi

if [[ -z "$MOD_ID" ]]; then
  printf 'publishedfileid is empty\n' >&2
  exit 1
fi

if [[ "$MOD_ID" == "0" && "$CREATE_NEW" != "1" ]]; then
  printf 'publishedfileid must be a non-zero existing Workshop item id\n' >&2
  printf 'To create a new item locally, set CREATE_NEW=1 (GitHub Actions must never do this).\n' >&2
  exit 1
fi

if [[ "$MOD_ID" == "0" && "$CREATE_NEW" == "1" && -z "$VISIBILITY" ]]; then
  VISIBILITY=2
fi

export CREATE_NEW VISIBILITY
"$PYTHON" - "$MOD_PATH" "$DESC_FILE" "$MOD_ID" "$CHANGENOTE_FILE" "$OUT_VDF" <<'PY'
import json
import os
import pathlib
import sys

mod_path_raw = sys.argv[1]
if len(mod_path_raw) >= 3 and mod_path_raw[0] == "/" and mod_path_raw[2] == "/":
    mod_path_raw = mod_path_raw[1].upper() + ":" + mod_path_raw[2:].replace("/", "\\")
mod_path = pathlib.Path(mod_path_raw)
desc_path = pathlib.Path(sys.argv[2])
mod_id = sys.argv[3]
changenote_file = sys.argv[4]
out_vdf = pathlib.Path(sys.argv[5])
visibility = os.environ.get("VISIBILITY") or ""


def steam_vdf_path(p: pathlib.Path) -> str:
    return str(p).replace("\\", "\\\\")


def vdf_escape(s: str) -> str:
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = s.replace("\n", "\\n").replace("\t", "\\t")
    return s


def workshop_description(raw: str) -> str:
    s = raw.replace("\r\n", "\n").replace("\r", "\n")
    s = s.replace("[c]", "[code]").replace("[/c]", "[/code]")
    # SteamCMD does not unescape \n; BBCode supplies structure.
    s = s.replace("\n", "").replace("\t", " ")
    if len(s) > 8000:
        raise SystemExit(
            f"ERROR: Steam Workshop description max is 8000 characters (got {len(s)}). "
            "Shorten STEAM_PAGE.bbcode."
        )
    return s.replace("\\", "\\\\").replace('"', '\\"')


meta = json.loads((mod_path / ".metadata" / "metadata.json").read_text(encoding="utf-8"))
title = vdf_escape(meta["name"])
description = workshop_description(desc_path.read_text(encoding="utf-8"))
content = steam_vdf_path(mod_path)
preview = steam_vdf_path(mod_path / "thumbnail.png")

changenote = ""
if changenote_file:
    cn = pathlib.Path(changenote_file)
    if cn.is_file():
        changenote = vdf_escape(cn.read_text(encoding="utf-8"))

lines = [
    '"workshopitem"',
    "{",
    '\t"appid" "529340"',
    f'\t"publishedfileid" "{mod_id}"',
    f'\t"contentfolder" "{content}"',
    f'\t"previewfile" "{preview}"',
]
if visibility:
    lines.append(f'\t"visibility" "{visibility}"')
lines.append(f'\t"title" "{title}"')
lines.append(f'\t"description" "{description}"')
if changenote:
    lines.append(f'\t"changenote" "{changenote}"')
lines.append("}")
out_vdf.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {out_vdf}")
PY
