#!/usr/bin/env bash
# Generate workshop.vdf for SteamCMD workshop_build_item.
#
# Usage:
#   ./script/create-release-vdf.sh MOD_DIR DESC_FILE PUBLISHED_FILE_ID [CHANGENOTE_FILE] [OUT_VDF]
#
# IMPORTANT: description from DESC_FILE is written into the VDF (escaped).
set -euo pipefail

if [[ $# -lt 3 ]]; then
  printf 'Usage: %s MOD_DIR DESC_FILE PUBLISHED_FILE_ID [CHANGENOTE_FILE] [OUT_VDF]\n' "$0" >&2
  exit 1
fi

MOD_DIR="$1"
DESC_FILE="$2"
MOD_ID="$3"
CHANGENOTE_FILE="${4:-}"
OUT_VDF="${5:-workshop.vdf}"

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

if [[ -z "$MOD_ID" || "$MOD_ID" == "0" ]]; then
  printf 'publishedfileid must be a non-zero existing Workshop item id\n' >&2
  exit 1
fi

# Escape a string for a VDF quoted value: backslash, quote, newline, tab.
vdf_escape() {
  # Prefer Python for correct Unicode / control-character handling.
  python3 -c 'import sys
s = sys.stdin.read()
s = s.replace("\\", "\\\\")
s = s.replace("\"", "\\\"")
s = s.replace("\r\n", "\n").replace("\r", "\n")
s = s.replace("\n", "\\n")
s = s.replace("\t", "\\t")
sys.stdout.write(s)'
}

TITLE="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["name"])' "$META")"
DESCRIPTION="$(cat "$DESC_FILE" | vdf_escape)"
TITLE_ESC="$(printf '%s' "$TITLE" | vdf_escape)"

CHANGENOTE=""
if [[ -n "$CHANGENOTE_FILE" && -f "$CHANGENOTE_FILE" ]]; then
  CHANGENOTE="$(cat "$CHANGENOTE_FILE" | vdf_escape)"
fi

{
  printf '"workshopitem"\n'
  printf '{\n'
  printf '\t"appid" "529340"\n'
  printf '\t"publishedfileid" "%s"\n' "$MOD_ID"
  printf '\t"contentfolder" "%s"\n' "$MOD_PATH"
  printf '\t"previewfile" "%s/thumbnail.png"\n' "$MOD_PATH"
  printf '\t"title" "%s"\n' "$TITLE_ESC"
  printf '\t"description" "%s"\n' "$DESCRIPTION"
  if [[ -n "$CHANGENOTE" ]]; then
    printf '\t"changenote" "%s"\n' "$CHANGENOTE"
  fi
  printf '}\n'
} > "$OUT_VDF"

printf 'Wrote %s\n' "$OUT_VDF"
