#!/usr/bin/env bash
# Run vic3-tiger for release CI and fail on any remaining fatal/error findings.
#
# Usage:
#   ./script/run-tiger-release.sh GAME_DIR MOD_DIR [CMF_DIR] [REPORT_OUT]
#
# Uses script/vic3-tiger.release.conf (CMF path + known false-positive filter).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GAME_DIR="${1:-}"
MOD_DIR="${2:-}"
CMF_DIR="${3:-}"
REPORT_OUT="${4:-tiger-release-report.txt}"

if [[ -z "$GAME_DIR" || -z "$MOD_DIR" ]]; then
  printf 'Usage: %s GAME_DIR MOD_DIR [CMF_DIR] [REPORT_OUT]\n' "$0" >&2
  exit 1
fi

GAME_DIR="$(cd "$GAME_DIR" && pwd)"
MOD_DIR="$(cd "$MOD_DIR" && pwd)"

TIGER_BIN="${TIGER_BIN:-vic3-tiger}"
if ! command -v "$TIGER_BIN" >/dev/null 2>&1; then
  if [[ -x "$ROOT/.tiger-ci/vic3-tiger" ]]; then
    TIGER_BIN="$ROOT/.tiger-ci/vic3-tiger"
  else
    printf 'vic3-tiger binary not found (set TIGER_BIN)\n' >&2
    exit 1
  fi
fi

CONF_SRC="$ROOT/script/vic3-tiger.release.conf"
[[ -f "$CONF_SRC" ]] || { printf 'Missing %s\n' "$CONF_SRC" >&2; exit 1; }

CONF_DIR="$(mktemp -d)"
CONF="$CONF_DIR/vic3-tiger.conf"
cp "$CONF_SRC" "$CONF"

if [[ -n "$CMF_DIR" ]]; then
  CMF_DIR="$(cd "$CMF_DIR" && pwd)"
  # Append path-based CMF load (workshop_id is unavailable in CI).
  {
    printf '\nload_mod = {\n'
    printf '\tlabel = "CMF"\n'
    printf '\tmod = "%s"\n' "$CMF_DIR"
    printf '}\n'
  } >> "$CONF"
fi

# Tiger reads vic3-tiger.conf from the mod root; temporarily swap.
MOD_CONF="$MOD_DIR/vic3-tiger.conf"
BACKUP=""
if [[ -f "$MOD_CONF" ]]; then
  BACKUP="$(mktemp)"
  cp "$MOD_CONF" "$BACKUP"
fi
cp "$CONF" "$MOD_CONF"

cleanup_conf() {
  if [[ -n "${BACKUP:-}" && -f "$BACKUP" ]]; then
    mv "$BACKUP" "$MOD_CONF"
  else
    rm -f "$MOD_CONF"
  fi
  rm -rf "$CONF_DIR"
}
trap cleanup_conf EXIT

set +e
"$TIGER_BIN" --no-color --game "$GAME_DIR" "$MOD_DIR" >"$REPORT_OUT" 2>&1
TIGER_RC=$?
set -e

# Always show the report in CI logs (truncated if enormous).
if [[ -f "$REPORT_OUT" ]]; then
  if [[ "$(wc -c <"$REPORT_OUT")" -gt 500000 ]]; then
    head -c 500000 "$REPORT_OUT"
    printf '\n... [report truncated]\n'
  else
    cat "$REPORT_OUT"
  fi
fi

# Parse Tiger summary line: fatal: N, error: N, warning: N, ...
SUMMARY="$(grep -E '^fatal: [0-9]+, error: [0-9]+' "$REPORT_OUT" | tail -n1 || true)"
if [[ -z "$SUMMARY" ]]; then
  printf 'Tiger did not produce a summary line (binary exit %s)\n' "$TIGER_RC" >&2
  exit 1
fi

FATAL="$(printf '%s' "$SUMMARY" | sed -E 's/^fatal: ([0-9]+).*/\1/')"
ERROR="$(printf '%s' "$SUMMARY" | sed -E 's/^fatal: [0-9]+, error: ([0-9]+).*/\1/')"

printf 'Tiger summary: %s\n' "$SUMMARY"

if [[ "$FATAL" -gt 0 || "$ERROR" -gt 0 ]]; then
  printf 'Release gate failed: fatal=%s error=%s (both must be 0 after release filters)\n' "$FATAL" "$ERROR" >&2
  exit 1
fi

# Tiger may return non-zero for warnings; release gate only requires fatal/error == 0.
printf 'Tiger release gate passed (fatal=0, error=0)\n'
exit 0
