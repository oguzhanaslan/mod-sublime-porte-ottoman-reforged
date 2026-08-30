#!/usr/bin/env bash
# Static release gates for Sublime Porte: Ottoman Reforged.
# Must pass before any version bump, GitHub Release, or Steam publish.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

fail() {
  printf 'ERROR: %s\n' "$*" >&2
  exit 1
}

warn() {
  printf 'WARN: %s\n' "$*" >&2
}

pass() {
  printf 'OK: %s\n' "$*"
}

# --- metadata.json ---
META=".metadata/metadata.json"
[[ -f "$META" ]] || fail "$META is missing"

python3 - <<'PY' || fail "metadata.json is not valid JSON or failed schema checks"
import json, sys
from pathlib import Path

path = Path(".metadata/metadata.json")
try:
    data = json.loads(path.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"JSON parse failed: {exc}", file=sys.stderr)
    sys.exit(1)

required = ["name", "id", "version", "game_id", "supported_game_version", "relationships"]
missing = [k for k in required if k not in data]
if missing:
    print(f"missing keys: {', '.join(missing)}", file=sys.stderr)
    sys.exit(1)

if data.get("game_id") != "victoria3":
    print(f"unexpected game_id: {data.get('game_id')}", file=sys.stderr)
    sys.exit(1)

version = str(data.get("version", ""))
parts = version.split(".")
if len(parts) != 3 or not all(p.isdigit() for p in parts):
    print(f"version must be semver X.Y.Z (digits only), got: {version!r}", file=sys.stderr)
    sys.exit(1)

cmf_id = "com.github.Victoria-3-Modding-Co-op.Community-Mod-Framework"
csf_id = "com.github.Victoria-3-Modding-Co-op.Community-State-Framework"
rels = data.get("relationships") or []
dep_ids = {
    r.get("id")
    for r in rels
    if isinstance(r, dict) and r.get("rel_type") == "dependency"
}
if cmf_id not in dep_ids:
    print(f"CMF dependency missing (expected id {cmf_id})", file=sys.stderr)
    sys.exit(1)
if csf_id not in dep_ids:
    print(f"CSF dependency missing (expected id {csf_id})", file=sys.stderr)
    sys.exit(1)

print(f"metadata version={version} deps={sorted(dep_ids)}")
PY
pass "metadata.json valid with CMF/CSF dependencies"

# --- thumbnail ---
[[ -f "thumbnail.png" ]] || fail "thumbnail.png missing at repository root"
[[ -f ".metadata/thumbnail.png" ]] || fail ".metadata/thumbnail.png missing"
pass "thumbnail.png present (root + .metadata)"

# --- descriptor.mod sync ---
[[ -f "descriptor.mod" ]] || fail "descriptor.mod missing"
META_VER="$(python3 -c 'import json; print(json.load(open(".metadata/metadata.json", encoding="utf-8"))["version"])')"
DESC_VER="$(grep -E '^version=' descriptor.mod | head -n1 | sed -E 's/^version="//; s/"$//')"
[[ "$DESC_VER" == "$META_VER" ]] || fail "descriptor.mod version ($DESC_VER) != metadata.json version ($META_VER)"

grep -q 'Community Mod Framework' descriptor.mod || fail "descriptor.mod missing Community Mod Framework dependency"
grep -q 'Community State Framework' descriptor.mod || fail "descriptor.mod missing Community State Framework dependency"
pass "descriptor.mod version and dependencies match metadata"

# --- STEAM_PAGE + release scripts present ---
[[ -f "STEAM_PAGE.bbcode" ]] || fail "STEAM_PAGE.bbcode missing"
python3 -c 'from pathlib import Path
n = len(Path("STEAM_PAGE.bbcode").read_text(encoding="utf-8"))
if n > 8000:
    raise SystemExit(f"STEAM_PAGE.bbcode is {n} chars; SteamCMD max is 8000")
print(f"STEAM_PAGE.bbcode {n} chars")
' || fail "STEAM_PAGE.bbcode exceeds Steam description limit"
[[ -f "script/create-release-vdf.sh" ]] || fail "script/create-release-vdf.sh missing"
[[ -f "script/package-steam-release.sh" ]] || fail "script/package-steam-release.sh missing"
pass "Steam release source files present"

# --- brace balance (conservative) ---
python3 - <<'PY' || fail "brace balance check failed"
import sys
from pathlib import Path

roots = ["common", "events", "gui", "map_data", "music"]
exts = {".txt", ".gui"}
bad = []
for root in roots:
    base = Path(root)
    if not base.exists():
        continue
    for path in base.rglob("*"):
        if path.suffix.lower() not in exts or not path.is_file():
            continue
        # Skip obvious non-script binaries/text copies
        name = path.name
        if "Kopya" in name or "Copy" in name:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        # Strip // line comments roughly; ignore # only at line start (Paradox)
        lines = []
        for line in text.splitlines():
            if "//" in line:
                line = line.split("//", 1)[0]
            lines.append(line)
        body = "\n".join(lines)
        opens = body.count("{")
        closes = body.count("}")
        if opens != closes:
            bad.append(f"{path.as_posix()}: '{{'={opens} '}}'={closes}")

if bad:
    print("Unbalanced braces:", file=sys.stderr)
    for row in bad[:50]:
        print(f"  {row}", file=sys.stderr)
    if len(bad) > 50:
        print(f"  ... and {len(bad) - 50} more", file=sys.stderr)
    sys.exit(1)
print(f"checked paradox script files under {', '.join(roots)}")
PY
pass "brace balance"

# --- EN/TR localization parity + missing/empty values ---
python3 - <<'PY' || fail "localization parity / missing loc check failed"
import re
import sys
from pathlib import Path

key_re = re.compile(r"^ ([A-Za-z0-9_.]+):")

def load_keys(path: Path):
    text = path.read_text(encoding="utf-8-sig")
    keys = {}
    for i, line in enumerate(text.splitlines(), 1):
        m = key_re.match(line)
        if not m:
            continue
        key = m.group(1)
        # Paradox loc: key:0 "value"
        rest = line[m.end() :]
        empty = False
        vm = re.search(r':?\s*\d*\s*"(.*)"\s*$', rest)
        if vm is not None and vm.group(1) == "":
            empty = True
        elif re.search(r':?\s*\d*\s*$', rest) and '"' not in rest:
            empty = True
        keys[key] = (i, empty)
    return keys

en_dir = Path("localization/english")
tr_dir = Path("localization/turkish")
if not en_dir.is_dir() or not tr_dir.is_dir():
    print("localization/english or localization/turkish missing", file=sys.stderr)
    sys.exit(1)

en_files = sorted(en_dir.glob("*.yml"))
tr_files = sorted(tr_dir.glob("*.yml"))
if not en_files:
    print("no English localization files", file=sys.stderr)
    sys.exit(1)

# Pair by stem with language suffix stripped
def stem_key(p: Path):
    name = p.name
    for suf in ("_l_english.yml", "_l_turkish.yml"):
        if name.endswith(suf):
            return name[: -len(suf)]
    return p.stem

en_map = {stem_key(p): p for p in en_files}
tr_map = {stem_key(p): p for p in tr_files}

only_en = sorted(set(en_map) - set(tr_map))
only_tr = sorted(set(tr_map) - set(en_map))
if only_en or only_tr:
    if only_en:
        print("EN files without TR pair:", file=sys.stderr)
        for k in only_en:
            print(f"  {en_map[k]}", file=sys.stderr)
    if only_tr:
        print("TR files without EN pair:", file=sys.stderr)
        for k in only_tr:
            print(f"  {tr_map[k]}", file=sys.stderr)
    sys.exit(1)

errors = 0
total_keys = 0
for stem in sorted(en_map):
    en_keys = load_keys(en_map[stem])
    tr_keys = load_keys(tr_map[stem])
    total_keys += len(en_keys)
    en_only = sorted(set(en_keys) - set(tr_keys))
    tr_only = sorted(set(tr_keys) - set(en_keys))
    if en_only or tr_only:
        errors += 1
        print(f"Key mismatch in {stem}:", file=sys.stderr)
        for k in en_only[:20]:
            print(f"  EN-only: {k}", file=sys.stderr)
        for k in tr_only[:20]:
            print(f"  TR-only: {k}", file=sys.stderr)
    for k, (line, empty) in en_keys.items():
        if empty:
            errors += 1
            print(f"Empty EN value: {en_map[stem]}:{line} {k}", file=sys.stderr)
    for k, (line, empty) in tr_keys.items():
        if empty:
            errors += 1
            print(f"Empty TR value: {tr_map[stem]}:{line} {k}", file=sys.stderr)
    # BOM check
    for label, path in (("EN", en_map[stem]), ("TR", tr_map[stem])):
        raw = path.read_bytes()
        if not raw.startswith(b"\xef\xbb\xbf"):
            errors += 1
            print(f"Missing UTF-8 BOM ({label}): {path}", file=sys.stderr)

if errors:
    sys.exit(1)
print(f"parity ok: {len(en_map)} file pairs, {total_keys} EN keys")
PY
pass "EN/TR localization parity and missing/empty loc check"

printf '\nAll static release validation gates passed.\n'
