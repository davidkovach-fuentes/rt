#!/usr/bin/env bash

set -euo pipefail

# Package Information
VERSION="${VERSION:-0.1.1}"
REPO="${REPO:-atlas-brown/rt}"
TARBALL_URL="https://github.com/${REPO}/archive/refs/tags/v${VERSION}.tar.gz"
PKG_ITERATION="${PKG_ITERATION:-1}"
MAINTAINER="${RT_PACKAGE_MAINTAINER:-maintainer@email.com}"

# Layout
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKAGING_DIR="$REPO_ROOT/packaging"
WORK_DIR="$PACKAGING_DIR/work"
OUT_DIR="$PACKAGING_DIR/dist"

echo "==> Cleaning Previous Release Artifacts"
rm -rf "$WORK_DIR" "$OUT_DIR"
mkdir -p "$WORK_DIR" "$OUT_DIR"

echo "==> Fetching release source v${VERSION}"
curl -fsSL "$TARBALL_URL" -o "$WORK_DIR/rt.tar.gz"
tar -xzf "$WORK_DIR/rt.tar.gz" -C "$WORK_DIR"
SRC_WORK="$WORK_DIR/rt-${VERSION}"

echo "==> Staging package tree"
FPM_ROOT="$WORK_DIR/fpm-root"
mkdir -p "$FPM_ROOT/usr/bin"
cp "$SRC_WORK/scripts/run-in-container.sh" "$FPM_ROOT/usr/bin/rt"
chmod 755 "$FPM_ROOT/usr/bin/rt"
ln -sf rt "$FPM_ROOT/usr/bin/rti"

PKG_ARGS=(
  --name "rt"
  --version "$VERSION"
  --iteration "$PKG_ITERATION"
  --maintainer "$MAINTAINER"
  --url "https://github.com/${REPO}"
  --description "Rt: an overlay type system for shell pipelines"
  --license "See upstream repository"
  --architecture all
  -s dir
  --chdir "$FPM_ROOT"
)

echo "==> Building .deb (Debian/Ubuntu)"
fpm "${PKG_ARGS[@]}" \
  -t deb \
  --package "$OUT_DIR/" \
  --depends "docker.io" \
  usr

echo "==> Building .rpm (Fedora/RHEL)"
fpm "${PKG_ARGS[@]}" \
  -t rpm \
  --package "$OUT_DIR/" \
  --depends "moby-engine" \
  usr

echo "==> Done. Packages in $OUT_DIR:"
ls -la "$OUT_DIR"
