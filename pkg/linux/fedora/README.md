# Fedora / Copr

Docker-wrapper RPM for `scripts/run-in-container.sh`.

## Copr settings (required)

| Field | Value |
|---|---|
| Clone URL | `https://github.com/davidkovach-fuentes/rt.git` |
| Committish | your branch (e.g. `fpm-ubuntu-fedora`) |
| Spec file | **`/pkg/linux/fedora/atlas-rt.spec`** |
| Subdirectory | *(leave empty)* |
| SRPM build method | **`make_srpm`** |

Do **not** use `tito` — it only packs `pkg/linux/fedora/` and `scripts/` is missing.

`.copr/Makefile` runs `git archive` of the **full repo**, then `rpmbuild -bs`.

## Local test

```sh
./pkg/linux/fedora/build-srpm.sh
# or upload pkg/linux/fedora/dist/*.src.rpm via Copr web UI
```
