#!/usr/bin/env bash
# Build an atlas-rt source RPM (same path Copr uses via make_srpm).
#
# Usage:
#   VERSION=v0.1.5 ./scripts/build-srpm.sh [outdir]
#
# VERSION comes from the env, else the latest git tag, else 0.1.0.
# Leading "v" / "atlas-rt-" and a trailing "-N" release suffix are stripped.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SPEC="$REPO_ROOT/pkg/linux/fedora/atlas-rt.spec"
OUTDIR="${1:-$REPO_ROOT/pkg/linux/fedora/artifacts}"

normalize_version() {
  local v="$1"
  v="${v#refs/tags/}"
  v="${v#v}"
  v="${v#atlas-rt-}"
  # atlas-rt-0.1.5-1 or 0.1.5-1 → 0.1.5
  if [[ "$v" =~ ^([0-9]+\.[0-9]+\.[0-9]+) ]]; then
    v="${BASH_REMATCH[1]}"
  fi
  printf '%s' "$v"
}

if [[ -n "${VERSION:-}" ]]; then
  RT_VERSION="$(normalize_version "$VERSION")"
elif tag="$(git -C "$REPO_ROOT" describe --tags --abbrev=0 2>/dev/null)"; then
  RT_VERSION="$(normalize_version "$tag")"
else
  RT_VERSION="0.1.0"
fi

mkdir -p "$OUTDIR"
make -f "$REPO_ROOT/.copr/Makefile" srpm \
  "spec=$SPEC" \
  "outdir=$OUTDIR" \
  "version=$RT_VERSION"
echo "SRPM: $OUTDIR"/*.src.rpm
