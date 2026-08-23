#!/usr/bin/env bash
# Local Copr-equivalent SRPM build (run from repo root, needs git + rpmbuild).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
SPEC="$REPO_ROOT/pkg/linux/fedora/atlas-rt.spec"
OUTDIR="${1:-$REPO_ROOT/pkg/linux/fedora/dist}"

mkdir -p "$OUTDIR"
make -f "$REPO_ROOT/.copr/Makefile" srpm "spec=$SPEC" "outdir=$OUTDIR"
echo "SRPM: $OUTDIR"/*.src.rpm
