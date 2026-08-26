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

Skip `tito` for the Copr SRPM. Tito only packs this directory, so `scripts/` never makes it into the source tree.

`.copr/Makefile` archives the whole git repo, then runs `rpmbuild -bs` with
`--define "rt_version …"` / `--define "rt_release …"`.

`scripts/build-srpm.sh` also updates `.tito/packages/atlas-rt` (tito's
`version-release reldir` metadata) so it tracks the NVR you just built.

## Local build

```sh
VERSION=v0.1.5 ./scripts/build-srpm.sh
# or rely on the latest git tag / .tito/packages/atlas-rt
./scripts/build-srpm.sh
cat .tito/packages/atlas-rt
```

Upload `pkg/linux/fedora/artifacts/*.src.rpm` in the Copr UI, or:

```sh
copr-cli build USER/atlas-rt pkg/linux/fedora/artifacts/*.src.rpm
```
