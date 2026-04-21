# Pixelarticons — PRIORITY SET (retro 16x16 bitmap)

- **Source**: https://github.com/halfmage/pixelarticons
- **Site**: https://pixelarticons.com
- **Author**: Gerrit Halfmann
- **License**: MIT (see `LICENSE`)
- **Version fetched**: depth-1 clone, 2026-04-21
- **Icon count**: 800 SVGs (operator-flagged as "480" — upstream has grown since the ask)
- **Style**: 16x16 pixel-perfect bitmap, no anti-aliasing, no curves
- **Raw SVG path**: `svg/`
- **Grid**: 16x16 pixel (every rect is 1px)

## Contents

- `svg/` — 800 SVG files on strict 16x16 grid
- `LICENSE` — MIT
- `README.md` — upstream readme

## Consolidate notes

**This is the priority icon set for Clawmachine's retro Mac OS 9 + cyberpunk aesthetic.**

- 16x16 pixel grid matches the classic Mac OS chromatic icons era (pre-Aqua).
- All glyphs render crisp at 1x on modern screens — no blurring, no svg sub-pixel drift.
- Pairs naturally with bitmap fonts (Monaspace, Commit Mono on-pixel-grid) and with Css.gg's geometric primitives.
- Same author as Majesticons, so you can mix retro (Pixelarticons) for chrome/accent and modern stroke (Majesticons) for text-adjacent UI without visual whiplash.
- Each SVG uses `<path>` built from unit rects — zero dependency on stroke rendering. Safe to re-colorize with a token-driven paint layer.

## Usage recommendation for Clawmachine

- Primary retro chrome: window controls, dock-like affordances, file/folder glyphs.
- Use at native 16px OR integer-multiple zoom (32px, 48px, 64px). Non-integer scales destroy the pixel grid.
- Do not anti-alias. CSS: `image-rendering: pixelated;` if rasterizing.
