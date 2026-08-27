#!/usr/bin/env bash
# Build a clean Steam-ready staging directory for Sublime Porte: Ottoman Reforged.
# Usage: ./script/package-steam-release.sh DEST_DIR
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${1:-}"

if [[ -z "$DEST" ]]; then
  printf 'Usage: %s DEST_DIR\n' "$0" >&2
  exit 1
fi

rm -rf "$DEST"
mkdir -p "$DEST"

copy_tree() {
  local src="$1"
  local dst="$2"
  mkdir -p "$dst"
  # Prefer rsync when available; fall back to cp -a
  if command -v rsync >/dev/null 2>&1; then
    rsync -a "$src"/ "$dst"/
  else
    cp -a "$src"/. "$dst"/
  fi
}

# Runtime-required Victoria 3 mod content (allowlist).
for dir in common events gui localization map_data music .metadata; do
  [[ -d "$ROOT/$dir" ]] || { printf 'Missing required directory: %s\n' "$dir" >&2; exit 1; }
  copy_tree "$ROOT/$dir" "$DEST/$dir"
done

[[ -f "$ROOT/descriptor.mod" ]] || { printf 'Missing descriptor.mod\n' >&2; exit 1; }
[[ -f "$ROOT/thumbnail.png" ]] || { printf 'Missing thumbnail.png\n' >&2; exit 1; }
cp -a "$ROOT/descriptor.mod" "$DEST/descriptor.mod"
cp -a "$ROOT/thumbnail.png" "$DEST/thumbnail.png"

# gfx: include runtime art, exclude source/preview workspaces
[[ -d "$ROOT/gfx" ]] || { printf 'Missing gfx/\n' >&2; exit 1; }
mkdir -p "$DEST/gfx"
if command -v rsync >/dev/null 2>&1; then
  rsync -a \
    --exclude '_preview/' \
    --exclude '_source/' \
    --exclude '*Kopya*' \
    --exclude '*Copy*' \
    --exclude '*.psd' \
    --exclude '*.xcf' \
    --exclude '*.blend' \
    "$ROOT/gfx"/ "$DEST/gfx"/
else
  copy_tree "$ROOT/gfx" "$DEST/gfx"
  rm -rf "$DEST/gfx/_preview" "$DEST/gfx/_source"
  find "$DEST/gfx" -type f \( -name '*Kopya*' -o -name '*Copy*' -o -name '*.psd' -o -name '*.xcf' -o -name '*.blend' \) -delete
fi

# Strip development / editor junk that may have been copied with trees
find "$DEST" -type d -name '__pycache__' -prune -exec rm -rf {} + 2>/dev/null || true
find "$DEST" -type f \( -name '*.pyc' -o -name '.DS_Store' -o -name 'Thumbs.db' -o -name 'Desktop.ini' -o -name '*~' -o -name '*.bak' -o -name '*.tmp' \) -delete

# Safety: never ship these even if present under allowlisted trees
rm -rf \
  "$DEST/.git" \
  "$DEST/.github" \
  "$DEST/.cursor" \
  "$DEST/.tiger-bin" \
  "$DEST/tools" \
  "$DEST/script" \
  "$DEST/docs" \
  "$DEST/tiger-output" \
  "$DEST/validation-output" \
  "$DEST/image"

# Required staging checks
[[ -f "$DEST/.metadata/metadata.json" ]] || { printf 'Staging missing .metadata/metadata.json\n' >&2; exit 1; }
[[ -f "$DEST/thumbnail.png" ]] || { printf 'Staging missing thumbnail.png\n' >&2; exit 1; }
[[ -d "$DEST/common" && -d "$DEST/localization" && -d "$DEST/gui" ]] || {
  printf 'Staging incomplete (common/localization/gui)\n' >&2
  exit 1
}

printf 'Steam staging ready: %s\n' "$DEST"
