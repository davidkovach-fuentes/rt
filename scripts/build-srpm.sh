#!/usr/bin/env bash
# Build an atlas-rt source RPM (same path Copr uses via make_srpm).
#
# Usage:
#   VERSION=v0.1.5 ./scripts/build-srpm.sh [outdir]
#
# Version resolution (first match wins):
#   1. VERSION env (required in CI)
#   2. latest git tag
#   3. .tito/packages/atlas-rt
#
# Always writes .tito/packages/atlas-rt and passes version/release to
# rpmbuild via --define.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SPEC="$REPO_ROOT/pkg/linux/fedora/atlas-rt.spec"
OUTDIR="${1:-$REPO_ROOT/pkg/linux/fedora/artifacts}"
TITO_PKG="$REPO_ROOT/.tito/packages/atlas-rt"
PKG_RELDIR="pkg/linux/fedora/"

parse_nvr() {
  local raw="$1"
  raw="${raw#refs/tags/}"
  raw="${raw#v}"
  raw="${raw#atlas-rt-}"

  local ver="" rel="1"
  if [[ "$raw" =~ ^([0-9]+\.[0-9]+\.[0-9]+)-([0-9]+)([._].*)?$ ]]; then
    ver="${BASH_REMATCH[1]}"
    rel="${BASH_REMATCH[2]}"
  elif [[ "$raw" =~ ^([0-9]+\.[0-9]+\.[0-9]+) ]]; then
    ver="${BASH_REMATCH[1]}"
  fi

  if [[ -z "$ver" ]]; then
    echo "error: cannot parse a X.Y.Z version from '$1'" >&2
    return 1
  fi
  RT_VERSION="$ver"
  RT_RELEASE="$rel"
}

read_tito_packages() {
  [[ -f "$TITO_PKG" ]] || return 1
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

echo "build-srpm: VERSION='${VERSION:-}' CI='${CI:-}' GITHUB_REF_NAME='${GITHUB_REF_NAME:-}'"

if [[ -n "${VERSION:-}" ]]; then
  parse_nvr "$VERSION"
elif [[ -n "${CI:-}" ]]; then
  echo "error: VERSION is required in CI (pass the release tag, e.g. v0.1.8)" >&2
  exit 1
elif [[ -n "${GITHUB_REF_NAME:-}" ]] && parse_nvr "$GITHUB_REF_NAME" 2>/dev/null; then
  :
elif tag="$(git -C "$REPO_ROOT" describe --tags --abbrev=0 2>/dev/null)"; then
  parse_nvr "$tag"
elif read_tito_packages; then
  echo "build-srpm: using .tito/packages/atlas-rt (local fallback)"
else
  echo "error: set VERSION to a release tag (e.g. VERSION=v0.1.8)" >&2
  exit 1
fi

echo "build-srpm: resolved rt_version=$RT_VERSION rt_release=$RT_RELEASE"
write_tito_packages

mkdir -p "$OUTDIR"
make -f "$REPO_ROOT/.copr/Makefile" srpm \
  "spec=$SPEC" \
  "outdir=$OUTDIR" \
  "version=$RT_VERSION" \
  "release=$RT_RELEASE"

shopt -s nullglob
srpms=("$OUTDIR"/atlas-rt-"$RT_VERSION"-*.src.rpm)
if [[ ${#srpms[@]} -eq 0 ]]; then
  echo "error: expected SRPM atlas-rt-${RT_VERSION}-*.src.rpm missing; got:" >&2
  ls -la "$OUTDIR" >&2 || true
  exit 1
fi
echo "SRPM: ${srpms[*]}"
