# Copr SRPM build (method: make_srpm).
#
#   make -f .copr/Makefile srpm \
#     outdir=pkg/linux/fedora/artifacts \
#     spec=pkg/linux/fedora/atlas-rt.spec \
#     version=0.1.5 \
#     release=1
#
# Copr package settings:
#   Spec file:     /pkg/linux/fedora/atlas-rt.spec
#   Subdirectory:  (empty)
#   Build method:  make_srpm

# Ubuntu's /bin/sh is dash; recipes need bash.
SHELL := /bin/bash
.SHELLFLAGS := -euo pipefail -c

.PHONY: srpm

srpm:
	@spec="$(spec)"; \
	outdir="$(outdir)"; \
	version="$(version)"; \
	release="$(release)"; \
	[ -n "$$spec" ] && [ -n "$$outdir" ]; \
	mkdir -p "$$outdir"; \
	if [ -z "$$version" ]; then \
	  version=$$(rpmspec -q "$$spec" --qf '%{VERSION}'); \
	fi; \
	if [ -z "$$release" ]; then \
	  release=1; \
	fi; \
	name=$$(rpmspec -q \
	  --define "rt_version $$version" \
	  --define "rt_release $$release" \
	  "$$spec" --qf '%{NAME}'); \
	tarball="$$outdir/$$name-$$version.tar.gz"; \
	echo "Building $$name-$$version-$$release (rt_version=$$version rt_release=$$release)"; \
	git archive --format=tar.gz --prefix="rt-$$version/" HEAD > "$$tarball"; \
	rpmbuild -bs "$$spec" \
	  --define "rt_version $$version" \
	  --define "rt_release $$release" \
	  --define "_sourcedir $$outdir" \
	  --define "_srcrpmdir $$outdir" \
	  --define "_rpmdir $$outdir" \
	  --define "_specdir $$(dirname "$$spec")" \
	  --define "_builddir $$outdir/build"; \
	ls -la "$$outdir"/*.src.rpm
