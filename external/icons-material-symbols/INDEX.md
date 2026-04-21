# Material Symbols

- Upstream: https://github.com/google/material-design-icons
- Distribution used: `@material-symbols/svg-400` v0.44.2 (npm tarball)
- Site: https://fonts.google.com/icons
- License: Apache 2.0 (see `LICENSE`)
- Acquired: 2026-04-21 via npm tarball (the full git repo is 5GB+; tarball is the clean SVG-only distribution)

## Why tarball instead of git clone

`git clone --depth 1 --filter=blob:none --sparse google/material-design-icons` still ships a 4.8M-file tree index and full metadata for every weight / grade / fill / size combination of every icon across outlined/rounded/sharp. Extracting even a single weight via `git sparse-checkout` pulls gigabytes and fails to stay under the 200MB ceiling. The npm package `@material-symbols/svg-400` publishes exactly what is useful: weight-400 SVGs for all three styles, fill and no-fill, 24px.

## Count

- Total icons: **23148** (7716 names x 3 styles)
  - `icons/outlined/`: 7716 (both `.svg` and `-fill.svg` per name)
  - `icons/rounded/`: 7716
  - `icons/sharp/`: 7716
- Unique icon names: ~3858 (each has a no-fill and a fill variant)
- Size on disk: ~90 MB

## Sample filenames (outlined)

```
10k-fill.svg
10k.svg
account_circle-fill.svg
account_circle.svg
add.svg
alarm-fill.svg
alarm.svg
arrow_forward.svg
bolt.svg
bookmark-fill.svg
bookmark.svg
build.svg
calendar_month.svg
check_circle-fill.svg
check_circle.svg
cloud-fill.svg
cloud.svg
dashboard.svg
delete-fill.svg
delete.svg
```

Identical name pool in `rounded/` and `sharp/`.

## Notes

- Weight 400 only (no 100/300/500/700 variants).
- Fill is encoded as `-fill.svg` suffix; grade and size are fixed at the defaults.
- For the Clawmachine stitch, `outlined/` is the sensible default; `rounded/` reads friendlier, `sharp/` reads more technical.
- Naming is snake_case (Google convention), unlike most other kits which use kebab-case.
