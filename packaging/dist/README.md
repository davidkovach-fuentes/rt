# packaging/dist

Local output from `tito` / `packaging.sh` (`.src.rpm`, `.rpm`, `.tar.gz`, `.deb`).

These artifacts are **gitignored** (`*.rpm`, `*.tar.gz`, `*.deb` in the repo root `.gitignore`). Build them locally and upload to Copr / GitHub Releases; do not commit the binaries.

```sh
tito build --srpm --offline -o packaging/dist
copr-cli build YOUR_PROJECT packaging/dist/rt-*.src.rpm
```
