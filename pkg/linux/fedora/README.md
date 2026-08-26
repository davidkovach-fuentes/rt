# Fedora / Copr

Docker-wrapper RPM that installs `scripts/run-in-container.sh`.

## Copr settings

| Field | Value |
|---|---|
| Clone URL | your fork or upstream git URL |
| Committish | branch or tag to build |
| Spec file | `/pkg/linux/fedora/atlas-rt.spec` |
| Subdirectory | leave empty |
| SRPM build method | `make_srpm` |

Skip `tito` here. Tito only packs this directory, so `scripts/` never makes it into the source tree.

`.copr/Makefile` archives the whole git repo, then runs `rpmbuild -bs`.

## Local build

```sh
VERSION=v0.1.5 ./scripts/build-srpm.sh
# or, with no VERSION, uses the latest git tag
./scripts/build-srpm.sh
```

Upload `pkg/linux/fedora/artifacts/*.src.rpm` in the Copr UI, or:

```sh
copr-cli build USER/atlas-rt pkg/linux/fedora/artifacts/*.src.rpm
```

The version is passed as `rpmbuild --define "rt_version …"` (see `.copr/Makefile`).
