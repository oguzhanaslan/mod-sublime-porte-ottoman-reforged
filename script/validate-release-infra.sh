#!/usr/bin/env bash
# Static validation of release infrastructure (does not bump version or publish).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
pass() { printf 'OK: %s\n' "$*"; }

required=(
  .github/workflows/build-release.yml
  script/validate-release.sh
  script/package-steam-release.sh
  script/create-release-vdf.sh
  script/run-tiger-release.sh
  script/vic3-tiger.release.conf
  STEAM_PAGE.bbcode
  docs/STEAM_RELEASE.md
)

for f in "${required[@]}"; do
  [[ -f "$f" ]] || fail "missing $f"
done
pass "required release files present"

for sh in script/*.sh; do
  bash -n "$sh" || fail "bash -n failed: $sh"
done
pass "bash -n on script/*.sh"

python3 - <<'PY' || fail "workflow YAML failed structural checks"
from pathlib import Path
import re
import sys

text = Path(".github/workflows/build-release.yml").read_text(encoding="utf-8")
required_snippets = [
    "workflow_dispatch:",
    "release-type:",
    "publish:",
    "workshop-id:",
    "./script/validate-release.sh",
    "./script/run-tiger-release.sh",
    "./script/package-steam-release.sh",
    "create-release-vdf.sh",
    "CyberAndrii/setup-steamcmd@v1",
    "WORKSHOP_USERNAME",
    "WORKSHOP_PASSWORD",
    "TIGER_VALIDATION_REPO",
    "TIGER_VALIDATION_TOKEN",
    "publish == 'true'",
]
missing = [s for s in required_snippets if s not in text]
if missing:
    print("missing workflow snippets:", file=sys.stderr)
    for s in missing:
        print(f"  {s}", file=sys.stderr)
    sys.exit(1)

if re.search(r"default:\s*['\"]0['\"]", text):
    print("workflow must not default workshop-id to 0", file=sys.stderr)
    sys.exit(1)

vdf = Path("script/create-release-vdf.sh").read_text(encoding="utf-8")
if '"description"' not in vdf:
    print("create-release-vdf.sh does not write description field", file=sys.stderr)
    sys.exit(1)

print("workflow structural checks ok")
PY
pass "workflow structural checks"

# Use the process temp directory (works on Linux CI and Git Bash /tmp).
TMP="${TMPDIR:-/tmp}/sp-release-infra-$$"
rm -rf "$TMP"
mkdir -p "$TMP/mod/.metadata"
cleanup() { rm -rf "$TMP"; }
trap cleanup EXIT

printf '%s\n' '{"name":"Test Mod","version":"1.0.0"}' >"$TMP/mod/.metadata/metadata.json"
printf 'preview' >"$TMP/mod/thumbnail.png"
printf 'line1\nline2\t"quote"\n' >"$TMP/desc.bbcode"
printf 'note\n' >"$TMP/note.txt"

bash ./script/create-release-vdf.sh "$TMP/mod" "$TMP/desc.bbcode" "999999" "$TMP/note.txt" "$TMP/workshop.vdf"

# Assert with grep (avoid Windows Python path translation issues for /tmp).
grep -q '"appid" "529340"' "$TMP/workshop.vdf" || fail "VDF missing appid"
grep -q '"publishedfileid" "999999"' "$TMP/workshop.vdf" || fail "VDF missing publishedfileid"
grep -q '"description"' "$TMP/workshop.vdf" || fail "VDF missing description field"
grep -q 'line1\\nline2\\t\\"quote\\"' "$TMP/workshop.vdf" || fail "VDF description escapes incorrect"
grep -q '"changenote"' "$TMP/workshop.vdf" || fail "VDF missing changenote"
grep -q '"title" "Test Mod"' "$TMP/workshop.vdf" || fail "VDF missing title"
pass "create-release-vdf.sh dry-run (description + escapes)"

if bash ./script/create-release-vdf.sh "$TMP/mod" "$TMP/desc.bbcode" "0" "$TMP/note.txt" "$TMP/bad.vdf" 2>/dev/null; then
  fail "create-release-vdf.sh should reject publishedfileid=0"
fi
pass "create-release-vdf.sh rejects id 0"

printf '\nRelease infrastructure static validation passed.\n'
