# patterns-haikei

**Count:** 40 SVG files (target: 40 — meets)
**Source:** hand-authored, inspired by haikei.app output taxonomies (blobs, waves, layered peaks, stairs, topography, mesh).
**Acquired:** authored from scratch — no scraping. Palette drawn from Clawmachine visual decisions (dark bases, warm orange / amber accents, cool cyan / violet accents).

## Taxonomy

- `blob-01.svg` through `blob-08.svg` — soft organic blobs, 1440x900, layered accents on dark base.
- `wave-01.svg` through `wave-08.svg` — layered sine-wave bands, closed to bottom edge.
- `peaks-01.svg` through `peaks-08.svg` — layered jagged peaks, mountain-silhouette style.
- `stairs-01.svg` through `stairs-06.svg` — stepped rectangle stacks.
- `topo-01.svg` through `topo-05.svg` — topographic ellipse contour rings.
- `mesh-01.svg` through `mesh-05.svg` — gaussian-blur mesh-gradient approximations via overlapping circles.

## Top 10 picks for Clawmachine

1. `blob-01.svg` — hero section background for landing / onboarding surface.
2. `wave-04.svg` — chat-view header banner; motion feel without animation cost.
3. `peaks-05.svg` — evaluator workspace header; horizon feel matches "fix-and-flip workbench".
4. `stairs-03.svg` — progress / step indicators or empty sidebars.
5. `topo-02.svg` — full-page page-background texture; low opacity overlay.
6. `mesh-01.svg` — splash / login full-bleed background; soft gradient depth.
7. `blob-06.svg` — modal / dialog backdrop for confirmation screens.
8. `wave-07.svg` — channel-list footer separator.
9. `peaks-02.svg` — alternative hero for dark-theme variants.
10. `mesh-04.svg` — advisor / consult pane background.

## Rendering notes

- All 1440x900 viewBox; use `preserveAspectRatio="none"` (already set) or override to taste for corner cropping.
- Mesh variants embed a Gaussian blur filter — may be heavy on low-end GPUs; rasterise to PNG if needed.
- Colour palette is Clawmachine-aligned; recolour via SVG `fill` replacement if theme shifts.
