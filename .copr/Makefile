# Copr: SRPM build method = make_srpm
# Invoked as:
#   make -f .copr/Makefile srpm outdir=... spec=/pkg/linux/fedora/atlas-rt.spec
#
# Copr UI:
#   Spec file:     /pkg/linux/fedora/atlas-rt.spec
#   Subdirectory:  (empty)
#   Build method:  make_srpm  (NOT tito)

#!/bin/bash

.PHONY: srpm

srpm:
	@set -euo pipefail; \
	spec="$(spec)"; \
	outdir="$(outdir)"; \
	[ -n "$$spec" ] && [ -n "$$outdir" ]; \
	mkdir -p "$$outdir"; \
	name=$$(rpmspec -q "$$spec" --qf '%{NAME}'); \
	version=$$(rpmspec -q "$$spec" --qf '%{VERSION}'); \
	tarball="$$outdir/$$name-$$version.tar.gz"; \
	git archive --format=tar.gz --prefix="rt-$$version/" HEAD > "$$tarball"; \
	rpmbuild -bs "$$spec" \
	  --define "_sourcedir $$outdir" \
	  --define "_srcrpmdir $$outdir" \
	  --define "_rpmdir $$outdir" \
	  --define "_specdir $$(dirname "$$spec")" \
	  --define "_builddir $$outdir/build"; \
	ls -la "$$outdir"/*.src.rpm
