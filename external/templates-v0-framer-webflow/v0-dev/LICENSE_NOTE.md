# v0-dev — LICENSE & SOURCING NOTE

**Scrape date:** 2026-04-21
**Operator:** Regan Cooney (regacooney@gmail.com) — UK reseller, internal non-commercial use
**Purpose:** Clawmachine internal research reference — template-ecosystem mining

## What is in this directory

- `previews/` — 11 PNG screenshots of v0.app public template pages captured via firecrawl (1440x900 viewport above-fold). Each preview is linked to a named designer and source URL in `metadata.json`.
- `recreated/` — 30 authored HTML structural approximations. These are NOT the original v0-generated JSX source — they are hand-authored dashboards written by the research agent based on what is visible in each preview image. Every file carries a visible credit footer linking back to the original designer + source URL.
- `gallery-index.json` + `gallery-pages/` — raw JSON scrape output from the v0.app/templates listing pages.
- `metadata.json` — per-template catalogue: designer handle, designer profile URL, source URL, views, forks, last-updated, visual tags.
- `INDEX.md` — top-10 ranked by Clawmachine-fit.

## Licence posture — authored HTML

The `recreated/*.html` files are original work authored for this research capture. They do not contain any copied code from v0.app. Visual layout patterns (sidebar + topbar + KPI grid + data table) are a generic dashboard form that is not copyrightable in itself. Specific designer flourishes (exact colour choices, custom typography, custom illustrations, proprietary icon sets) have not been reproduced.

Each recreation sits at the structural-fidelity level: "this layout has a 4-column KPI strip, a 2/3 + 1/3 chart-plus-side-panel, and a full-width activity table below." Nothing at that level of abstraction is proprietary to any individual designer.

## Licence posture — captured previews

Previews are 1440x900 screenshots of publicly accessible v0.app/templates pages. Each PNG is credited to a named designer in `metadata.json`. Retention is for **internal research reference only**; not for redistribution, not for commercial reuse, not for display in any Clawmachine product.

## Anti-claims

- This directory is NOT a v0.app export.
- This directory is NOT licensed for redistribution.
- No preview image here should be embedded in any shipping Clawmachine surface.
- The HTML recreations are for layout-pattern study only — if any visual idea is carried into the Clawmachine product, it goes through the operator's palette/token system, not via this directory's CSS.

## Fair-use basis

UK fair-dealing for non-commercial research. Operator is the sole viewer. No derivative product, no distribution, no public-facing reuse.

## If a designer asks

Contact Regan (regacooney@gmail.com). The corresponding preview PNG and recreated HTML will be removed on request.
