#!/usr/bin/env bash
# Build an atlas-rt source RPM (same path Copr uses via make_srpm).
#
# Usage:
#   VERSION=v0.1.5 ./scripts/build-srpm.sh [outdir]
#
# Version resolution (first match wins):
#   1. VERSION env (release tag / ref)
#   2. latest git tag
#   3. .tito/packages/atlas-rt  (tito-style metadata)
#   4. 0.1.0-1
#
# After resolving, writes .tito/packages/atlas-rt (same format tito tag uses)
# and passes version/release to rpmbuild via --define.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SPEC="$REPO_ROOT/pkg/linux/fedora/atlas-rt.spec"
OUTDIR="${1:-$REPO_ROOT/pkg/linux/fedora/artifacts}"
TITO_PKG="$REPO_ROOT/.tito/packages/atlas-rt"
PKG_RELDIR="pkg/linux/fedora/"

# Sets RT_VERSION and RT_RELEASE from a tag/NVR-ish string.
parse_nvr() {
  local raw="$1"
  raw="${raw#refs/tags/}"
  raw="${raw#v}"
  raw="${raw#atlas-rt-}"

  local ver rel="1"
  if [[ "$raw" =~ ^([0-9]+\.[0-9]+\.[0-9]+)-([0-9]+) ]]; then
    ver="${BASH_REMATCH[1]}"
    rel="${BASH_REMATCH[2]}"
  elif [[ "$raw" =~ ^([0-9]+\.[0-9]+\.[0-9]+) ]]; then
    ver="${BASH_REMATCH[1]}"
  else
    ver="$raw"
  fi
  RT_VERSION="$ver"
  RT_RELEASE="$rel"
}

read_tito_packages() {
  [[ -f "$TITO_PKG" ]] || return 1
  # file format: "<version>-<release> <reldir>"
  local first
  first="$(awk '{ print $1; exit }' "$TITO_PKG")"
  [[ -n "$first" ]] || return 1
  parse_nvr "$first"
}

write_tito_packages() {
  mkdir -p "$(dirname "$TITO_PKG")"
  printf '%s-%s %s\n' "$RT_VERSION" "$RT_RELEASE" "$PKG_RELDIR" > "$TITO_PKG"
  echo "Updated $TITO_PKG -> $(cat "$TITO_PKG")"
}

if [[ -n "${VERSION:-}" ]]; then
  parse_nvr "$VERSION"
elif tag="$(git -C "$REPO_ROOT" describe --tags --abbrev=0 2>/dev/null)"; then
  parse_nvr "$tag"
elif read_tito_packages; then
  :
else
  RT_VERSION="0.1.0"
  RT_RELEASE="1"
fi

write_tito_packages

mkdir -p "$OUTDIR"
make -f "$REPO_ROOT/.copr/Makefile" srpm \
  "spec=$SPEC" \
  "outdir=$OUTDIR" \
  "version=$RT_VERSION" \
  "release=$RT_RELEASE"
echo "SRPM: $OUTDIR"/*.src.rpm
