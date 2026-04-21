# figma-community-top — LICENSE & SOURCING NOTE

**Scrape date:** 2026-04-21
**Operator:** Regan Cooney (regacooney@gmail.com)

## Contents

- `recreated/` — 10 HTML component-gallery and dashboard approximations inspired by the top Figma Community dashboard kits.
- `metadata.json` — fileKey, slug, title, designer, price, duplicate-count, like-count per kit.

## Why no `previews/` directory

Figma Community previews are delivered as carousel-image URLs hosted on `s3-figma-hubfile-images-production.figma.com`. The URLs are captured in `metadata.json` but we have intentionally not persisted the binaries here — the value for research is the fileKey reference (to duplicate the original) plus the designer credit, not a 5-megabyte multi-panel carousel PNG per kit.

## Licence posture — per-kit

Each Figma Community file carries its own licence, typically:
- **Free personal+commercial use** (the default for most kits here)
- **No resale-as-template** (you can USE the design, you cannot repackage it as your own Figma template)

The `recreated/*.html` files in this directory are authored component galleries using generic dashboard/Material/shadcn grammar. They do NOT reproduce any specific designer's token system, colour palette, or custom illustration work. If you want the actual kit, duplicate it from `figma.com/community/file/<fileKey>`.

## Specific anti-goals

Per the Clawmachine consolidate repo CLAUDE.md — two kits in `metadata.json` are flagged as `visual-antithesis` (Apple iOS 26 Library + Liquid Glass — iOS 26). They appear in the ranked list for completeness but are explicitly NOT recommended for carry-forward into Clawmachine. The operator has settled that liquid-glass / frosted / translucent aesthetic is ruled out.

## Fair-use basis

UK fair-dealing for non-commercial research. Duplicate the source file for actual use. Named designers credited in `metadata.json` and in a visible footer on each HTML recreation.
