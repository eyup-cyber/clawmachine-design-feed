# Catalyst UI Kit — provenance and license

## What's here

1. **`sourced/*.md`** — Catalyst public documentation pages at `https://catalyst.tailwindui.com/docs/*`, scraped on 2026-04-21 for personal / internal reference. One file per component (25 pages). The scraped docs include the full published component API, TSX usage examples as rendered in the public-facing doc site, and color references.
2. **`components/*.tsx`** — Clean-room Catalyst-aesthetic reimplementations of each documented component, written from the published API only (prop names, defaults, shape of returned markup), targeting the same exposed surface. They use Headless UI primitives that Catalyst itself uses, and Tailwind Labs neutral/zinc palette.
3. **`tokens.json`** — Design tokens inferred from the rendered markup on the public Catalyst docs site.

## License and intent

Catalyst UI Kit is a **paid** product from Tailwind Labs, sold under its own end-user license at <https://tailwindcss.com/plus/license>. **This folder does not distribute the paid Catalyst source files.** Only the public documentation pages (which Tailwind publishes under their public docs) were scraped, and the TSX components here are derivative reconstructions, not extractions from the paid package.

This workspace (Clawmachine / consolidate) is a single-operator internal macOS SwiftUI app for tech-electronics reselling research. The operator (Regan, UK) is the sole user. Outputs here are reference material for a non-commercial internal build.

If you (future operator or collaborator) decide to ship anything publicly that resembles Catalyst, purchase a Tailwind Plus license first. The scrape here is fair-use research/reference only; the reconstructions are yours to own or replace.

## Scrape date

2026-04-21 (Europe/UK)
