# Boxicons

- Upstream: https://github.com/atisawd/boxicons (branch `master` — the `main` branch is the JS wrapper and ships zero SVGs)
- Site: https://boxicons.com/
- License: MIT (see `LICENSE`)
- Acquired: 2026-04-21 via `git clone --depth 1 --branch master`
- Layout: `icons/regular/`, `icons/solid/`, `icons/logos/`

## Count

- Total icons: **1634**
  - `regular/`: 814 (outline style, `bx-` prefix)
  - `solid/`: 665 (filled style, `bxs-` prefix)
  - `logos/`: 155 (brand marks, `bxl-` prefix)
- Size on disk: ~6.4 MB

## Sample filenames (regular)

```
bx-abacus.svg
bx-accessibility.svg
bx-adjust.svg
bx-alarm.svg
bx-album.svg
bx-align-justify.svg
bx-bell.svg
bx-bookmark.svg
bx-calendar.svg
bx-camera.svg
bx-chat.svg
bx-check.svg
bx-cloud.svg
bx-code.svg
bx-cog.svg
bx-compass.svg
bx-cube.svg
bx-edit.svg
bx-envelope.svg
bx-file.svg
```

## Sample filenames (solid)

```
bxs-alarm.svg
bxs-bell.svg
bxs-bookmark.svg
bxs-calendar.svg
bxs-camera.svg
bxs-cloud.svg
bxs-cog.svg
bxs-envelope.svg
bxs-heart.svg
bxs-star.svg
```

## Sample filenames (logos)

```
bxl-99designs.svg
bxl-500px.svg
bxl-adobe.svg
bxl-airbnb.svg
bxl-algolia.svg
bxl-amazon.svg
bxl-android.svg
bxl-apple.svg
bxl-aws.svg
bxl-behance.svg
```

## Notes

- The upstream `atisawd/boxicons` default branch is the JS wrapper package; the SVG source lives on the `master` branch. Easy trap to fall into.
- Naming convention uses prefix rather than suffix: `bx-` (regular), `bxs-` (solid), `bxl-` (logos).
- Logos set is a useful brand-mark reference library in its own right.
- Visual character: 24x24 grid, 2px stroke on regular, heavier geometric shapes.
