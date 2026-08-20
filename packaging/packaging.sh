#!/usr/bin/env bash

set -euo pipefail

# Package Information
VERSION="${VERSION:-0.1.1}"
REPO="${REPO:-atlas-brown/rt}"
PKG_ITERATION="${PKG_ITERATION:-1}"
MAINTAINER="${RT_PACKAGE_MAINTAINER:-maintainer@email.com}"

# Layout — package the current checkout (CI already checks out the release tag)
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKAGING_DIR="$REPO_ROOT/packaging"
WORK_DIR="$PACKAGING_DIR/work"
OUT_DIR="$PACKAGING_DIR/dist"
SRC_WORK="$REPO_ROOT"

echo "==> Purging"
rm -rf "$WORK_DIR" "$OUT_DIR"
mkdir -p "$WORK_DIR" "$OUT_DIR"

echo "==> Staging package tree from $SRC_WORK"
FPM_ROOT="$WORK_DIR/fpm-root"
mkdir -p "$FPM_ROOT/usr/bin"
cp "$SRC_WORK/scripts/run-in-container.sh" "$FPM_ROOT/usr/bin/rt"
chmod 755 "$FPM_ROOT/usr/bin/rt"
ln -sf rt "$FPM_ROOT/usr/bin/rti"

OPTS=(
  --name "rt"
  --version "$VERSION"
  --iteration "$PKG_ITERATION"
  --maintainer "$MAINTAINER"
  --url "https://github.com/${REPO}"
  --description "Rt: an overlay type system for shell pipelines"
  --architecture all
  -s dir
  --chdir "$FPM_ROOT"
)

echo "==> Building DEB"
fpm "${OPTS[@]}" \
  -t deb \
  --package "$OUT_DIR/" \
  --depends "docker.io" \
  usr

echo "==> Building RPM"
fpm "${OPTS[@]}" \
  -t rpm \
  --package "$OUT_DIR/" \
  --depends "moby-engine" \
  usr

echo "==> Done. Packages in $OUT_DIR:"
ls -la "$OUT_DIR"
