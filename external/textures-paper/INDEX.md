# textures-paper

**Count:** 20 SVG + 5 PNG = 25 overlay files (target: 15 SVG + curled PNGs — meets)
**Source:** all hand-authored; no external scraping. Small, tileable, CC0.
**Acquired:** authored locally. SVGs use SVG filters (`feTurbulence`, `feColorMatrix`) to synthesise grain; PNGs use per-pixel random noise rendered via Pillow.

## File list

SVG:
1. `01-paper-grain-fine.svg` — fine turbulence grain, cream base.
2. `02-paper-grain-coarse.svg` — coarse turbulence, higher frequency.
3. `03-paper-noise-cream.svg` — soft noise, cream palette.
4. `04-paper-kraft.svg` — kraft-brown warm grain.
5. `05-paper-vellum.svg` — low-contrast translucent feel.
6. `06-paper-aged.svg` — mottled aged-paper overlay.
7. `07-paper-washi.svg` — fibrous washi-paper style.
8. `08-paper-parchment.svg` — warm parchment tone.
9. `09-paper-newsprint.svg` — cool newsprint grey.
10. `10-paper-cardboard.svg` — corrugated cardboard hint.
11. `11-paper-rice.svg` — rice-paper speckle.
12. `12-paper-stained.svg` — stained / blotched overlay.
13. `13-paper-linen.svg` — linen-weave grain.
14. `14-paper-grunge.svg` — distressed grunge overlay.
15. `15-paper-rough.svg` — rough-cut paper texture.
16. `16-paper-smooth.svg` — smooth high-quality paper.
17. `17-paper-handmade.svg` — handmade paper flecks.
18. `18-paper-sepia.svg` — sepia-tone aged.
19. `19-paper-graph.svg` — graph-paper with grain.
20. `20-paper-dotted.svg` — dot-noise overlay.

PNG (authored via Pillow):
- `png-01-warm-paper-grain.png` — 512x512 warm cream grain, fully opaque-alpha.
- `png-02-cool-paper-grain.png` — 512x512 cool cream grain.
- `png-03-kraft-coarse.png` — 512x512 coarse kraft-brown grain.
- `png-04-fine-dot-noise.png` — 512x512 transparent PNG of sparse dark dots, multiply-blend overlay.
- `png-05-screen-grain-overlay.png` — 512x512 transparent PNG of screen-grain specks for film-grain mode.

## Top 10 picks for Clawmachine

1. `01-paper-grain-fine.svg` — default page-background overlay for document-style surfaces.
2. `08-paper-parchment.svg` — evaluator reports, price-history panels.
3. `png-04-fine-dot-noise.png` — film-grain overlay on dark theme hero.
4. `10-paper-cardboard.svg` — warehouse / pallet-buy list backgrounds.
5. `14-paper-grunge.svg` — retro-cyberpunk panel backing.
6. `png-02-cool-paper-grain.png` — light-theme default grain at 8% opacity.
7. `19-paper-graph.svg` — schematic / workbench surfaces (pairs with Hero `010-graph-paper.svg`).
8. `13-paper-linen.svg` — onboarding hero texture.
9. `png-05-screen-grain-overlay.png` — animated retro-monitor surfaces.
10. `12-paper-stained.svg` — annotation / margin surfaces for notes views.

## Usage

Multiply-blend over any background colour. SVG overlays scale cleanly; PNG overlays tile at 512x512 seamlessly.
