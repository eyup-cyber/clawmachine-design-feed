# LICENSE NOTE — tailwind-ui kit

## What this folder is

A reference deposit for the **Tailwind UI** house style (tailwindui.com), assembled for a single internal non-commercial reference use inside a macOS SwiftUI app. The folder is composed of three distinct buckets, each under a distinct licensing basis:

### 1. `sourced-hyperui/` — MIT-licensed HyperUI deposit (bulk tier)

- **Source**: https://github.com/markmead/hyperui
- **License**: MIT (permissive; commercial and non-commercial use, modification, redistribution permitted with attribution)
- **Files**: 444 HTML files spanning 33 application categories + 22 marketing categories, plus LICENSE file
- **Attribution**: HyperUI by Mark Mead. Public MIT-licensed Tailwind component library modelled on Tailwind UI's taxonomy.
- **Use**: These are the actual MIT files from HyperUI, copied verbatim. They may be redistributed under MIT terms.

### 2. `application/`, `marketing/`, `ecommerce/` — bespoke clean-room reconstructions (80 files)

- **Source**: Original reconstructions produced in this session from knowledge of Tailwind Labs' public design system (published tailwindcss.com docs, public @headlessui/react repo, public @tailwindcss/forms repo, plus general Tailwind utility-class conventions).
- **License**: Clean-room — these files are independent works authored in this session. No code was extracted from the paid Tailwind UI package. No scraping of the authenticated Tailwind UI source occurred.
- **Aesthetic**: Matches the publicly-documented Tailwind Labs house style (indigo-600 primary, gray scale neutrals, rounded-md, shadow-xs, Inter font stack, focus-visible:outline-2 offset-2).
- **Component count**: 30 application + 30 marketing + 20 ecommerce = 80 files.
- **Use**: These files are for the single-user non-commercial reference that is the stated purpose of the claude-design-feed. Do not redistribute as "Tailwind UI components" — they are original work that follows the same public conventions.

### 3. `tokens.json` — inferred design tokens

- **Source**: Inferred from the public tailwindcss.com docs and the default Tailwind CSS config (open MIT). All values (colour scales, spacing, radius, shadow) are part of Tailwind CSS itself, which is MIT-licensed.
- **License**: MIT-aligned values; the composition is an analytical summary, not an extraction.

## What this folder is NOT

- **Not** a copy of the paid Tailwind UI package (no access was used, no files extracted from tailwindui.com authenticated area).
- **Not** a republication of Tailwind UI for redistribution or commercial use.
- **Not** an "official Tailwind UI" asset — Tailwind UI is a commercial product of Tailwind Labs, Inc. and is covered by their paid licence at https://tailwindui.com/license.

## Tailwind UI official licence

The Tailwind UI commercial licence (tailwindui.com/license) grants a single-developer personal-use licence per purchase. Any user seeking production-grade Tailwind UI components should purchase a licence directly from Tailwind Labs.

## Fair-use basis for this deposit

This folder exists as a reference feed inside a research / design workspace (consolidate/claude-design-feed). The intent is:

1. Aesthetic reference for the operator's single-user internal macOS SwiftUI app;
2. Structural reference (the HTML markup patterns, class conventions, layout geometries published across Tailwind docs, HyperUI, and Tailwind Labs' own open repos);
3. Token reference (inferred from published public docs and MIT-licensed Tailwind defaults).

No commercial redistribution. No upstream scraping of paid product. No misrepresentation as an official Tailwind UI deliverable.

## Attribution

- **Tailwind CSS** (MIT) — Adam Wathan et al., Tailwind Labs, Inc. https://tailwindcss.com
- **Tailwind UI** (commercial; used here only as aesthetic reference) — Tailwind Labs, Inc. https://tailwindui.com
- **Headless UI** (MIT) — Tailwind Labs, Inc. https://headlessui.com
- **HyperUI** (MIT) — Mark Mead. https://github.com/markmead/hyperui

## Provenance trail

Produced in session by Claude Code for Regan Cooney / consolidate workspace on 2026-04-21. Intended lifetime: reference-only, non-redistributable.
