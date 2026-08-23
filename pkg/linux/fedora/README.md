# packaging/dist

Local output from `tito` / `packaging.sh` (`.src.rpm`, `.rpm`, `.tar.gz`, `.deb`).

These artifacts are **gitignored** (`*.rpm`, `*.tar.gz`, `*.deb` in the repo root `.gitignore`). Build them locally and upload to Copr / GitHub Releases; do not commit the binaries.

```sh
tito build --srpm --offline -o pkg/linux/fedora
copr-cli build YOUR_PROJECT pkg/linux/fedora/rt-*.src.rpm
```
