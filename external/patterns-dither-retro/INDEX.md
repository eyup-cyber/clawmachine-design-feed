# patterns-dither-retro

**Count:** 30 SVG files (target: 30 — meets)
**Source:** hand-authored. No external scraping. Tileable dither / cross-hatch / halftone / Bayer-matrix / scanline patterns for retro Mac OS 9 and cyberpunk surfaces.
**Acquired:** authored locally. Every file is a small tileable SVG with `shape-rendering="crispEdges"` to preserve pixel-perfect rendering at any CSS scale.

## File list

1. `01-bayer-4x4.svg` — classic ordered 4x4 Bayer dither matrix.
2. `02-checker-2px.svg` — 2px checkerboard.
3. `03-dots-50pct.svg` — 50% dot fill.
4. `04-dots-25pct.svg` — 25% dot fill.
5. `05-dots-75pct.svg` — 75% dot fill.
6. `06-diagonal-lines.svg` — diagonal line hatching.
7. `07-cross-hatch.svg` — cross-hatch pattern.
8. `08-bayer-8x8.svg` — 8x8 Bayer matrix.
9. `09-halftone-dots.svg` — halftone dot pattern.
10. `10-horizontal-stripes.svg` — horizontal stripes.
11. `11-vertical-stripes.svg` — vertical stripes.
12. `12-mac-desktop.svg` — classic Mac desktop 50% grey dither.
13. `13-weave.svg` — basket-weave pattern.
14. `14-scan-lines.svg` — CRT scan lines.
15. `15-grid-dots.svg` — grid-aligned dots.
16. `16-brick.svg` — brick tile pattern.
17. `17-zigzag.svg` — zigzag line pattern.
18. `18-matrix-rain.svg` — Matrix-style rain slivers.
19. `19-noise-dense.svg` — dense monochrome noise.
20. `20-gradient-bayer.svg` — Bayer-dithered gradient.
21. `21-bayer-2x2.svg` — minimal 2x2 Bayer matrix.
22. `22-halftone-lines.svg` — varying-width horizontal lines (halftone gradient).
23. `23-cross-hatch-dense.svg` — dense cross-hatch, phosphor-green on dark.
24. `24-ordered-dither-stipple.svg` — ordered-dither stipple at 12% density.
25. `25-crt-scanline-rgb.svg` — RGB sub-pixel scanline strip.
26. `26-diagonal-hash-thick.svg` — thick diagonal hatching, paper on dark-cyan base.
27. `27-mac-os9-desktop.svg` — minimal 2x2 Mac OS 9 desktop dither tile.
28. `28-static-noise-mono.svg` — static-TV monochrome noise field.
29. `29-checker-phosphor.svg` — CRT-phosphor-green checker.
30. `30-bayer-16x16-gradient.svg` — 32x8 Bayer gradient strip (black-to-white dither ramp).

## Top 10 picks for Clawmachine

1. `12-mac-desktop.svg` — Mac OS 9 desktop tile; default page background for retro-Mac theme.
2. `27-mac-os9-desktop.svg` — ultra-minimal 2x2 variant for window-chrome fills.
3. `14-scan-lines.svg` — CRT scanline overlay; ship on cyberpunk / terminal surfaces.
4. `25-crt-scanline-rgb.svg` — RGB sub-pixel variant; heavier retro-monitor feel.
5. `23-cross-hatch-dense.svg` — phosphor-green hatching; inspector / debug panels.
6. `08-bayer-8x8.svg` — classic 8x8 ordered dither; transition / fade panels.
7. `29-checker-phosphor.svg` — CRT-green checker; agent-busy / thinking indicator.
8. `18-matrix-rain.svg` — Matrix-style vertical slivers; hero backdrops for hacker-mode.
9. `30-bayer-16x16-gradient.svg` — Bayer gradient ramp; use as progress-bar fill mask.
10. `20-gradient-bayer.svg` — gradient Bayer; dither-transition between panels.

## Rendering notes

All tiles use `shape-rendering="crispEdges"` (except `23-` which uses `geometricPrecision` for its anti-aliased stroke). Tile sizes range from 2x2 (mac-os9) to 32x32 (static-noise). Use as CSS `background-image` with `repeat`.
