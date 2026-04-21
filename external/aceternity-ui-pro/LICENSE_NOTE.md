# Aceternity UI Pro — License & Attribution

## Source

All content captured from **ui.aceternity.com** public URLs:
- `https://ui.aceternity.com/blocks/{category}/{slug}` — public catalog page (no auth).
- `https://ui.aceternity.com/live-preview/{slug}` — SSR'd fully-rendered HTML (no auth).

**Not captured**: `https://ui.aceternity.com/registry/{slug}.json` for Pro slugs — these return 401 Unauthorized. Pro tier source code is paywalled ($149 / lifetime at the Pricing page) and we respected that boundary. Only the publicly-rendered HTML output was captured.

## Original author

**Manu Arora** (`hi@manuarora.in`, `@mannupaaji`) and Aceternity Labs LLC.
Website: <https://ui.aceternity.com/pro>

## License

Aceternity UI Pro blocks require a lifetime-access purchase: <https://ui.aceternity.com/pricing>

The HTML+CSS captured here is the public preview output. It is the same content any visitor sees loading the live-preview page in a browser. No auth token was used, no paywall was bypassed, no source code was exfiltrated.

## Intended use in this repository

**Reference-only.** Used as visual input for Claude Design to study layouts, spacing, motion patterns, and color treatments when stitching Clawmachine's UI. Clawmachine is a single-user, non-commercial, personal tool.

Any Pro block adopted into Clawmachine must be reimplemented from scratch based on the captured rendered HTML — the source JSX is not in this repo because we don't have it. That's acceptable: we have enough visual information to rebuild equivalent components without direct copying.

If a Pro block ends up being load-bearing for Clawmachine, the proper path is to purchase Pro ($149 lifetime) for that user, or rewrite cleanly.

## Contents

| Path | Content | Count |
|------|---------|-------|
| `demos/*.html` | Rewritten HTML (paths absolute to ui.aceternity.com CDN) | 134 files |
| `raw/live-previews/*.html` | Raw SSR'd HTML from ui.aceternity.com | 134 files |
| `raw/css/*.css` | Global CSS bundles referenced by all previews | 2 files (544 KB + 16 KB) |
| `index.html` | Browsable gallery with category filter | 1 file |

The 17 missing blocks (151 catalogued, 134 captured) returned 404 on `/live-preview/` — likely simpler static backgrounds/cards that don't have a live-preview route. They exist only as iframe-embedded snippets on the parent blocks page.

## Categories captured

- hero-sections (20)
- feature-sections (17)
- illustrations (18)
- testimonials (7)
- pricing-sections (6)
- bento-grids (5)
- navbars (7)
- footers (4)
- contact-sections (3)
- cta-sections (5)
- blog-sections (3), blog-content-sections (2)
- faqs (4)
- login-and-signup-sections (6)
- logo-clouds (5)
- shaders (3)
- sidebars (3)
- stats-sections (4)
- team-sections (4)
- text-animations (4)
- backgrounds (partial)

## How to view

Open `index.html` in a browser. The demo HTMLs reference the original ui.aceternity.com CDN for CSS/JS/images, so internet access is required to see the blocks render with full animations. The raw HTML structure itself is in `raw/live-previews/`.
