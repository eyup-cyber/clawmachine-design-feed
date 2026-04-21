# Aceternity UI (Free Tier) — License & Attribution

## Source

All component source pulled from **ui.aceternity.com** public registry endpoints:
- `https://ui.aceternity.com/registry/{slug}.json` — the official shadcn-compatible component registry used by the `npx shadcn@latest add @aceternity/{slug}` CLI.
- `https://ui.aceternity.com/live-preview/{slug}` — fully SSR'd HTML output.

These endpoints are publicly accessible and unauthenticated for free-tier components.

## Original author

**Manu Arora** (`hi@manuarora.in`, `@mannupaaji`) and Aceternity Labs LLC.

Website: <https://ui.aceternity.com>
Twitter: <https://twitter.com/mannupaaji>

## License

Aceternity UI free-tier components are published as **MIT**-style copy-paste components intended for reuse. From the official site: "Copy-paste beautiful UI components built with React, Next.js, Tailwind CSS, and Framer Motion. 200+ free components, blocks, and templates." No EULA applied to individual free components at time of capture (2026-04-21).

Formal license page: <https://ui.aceternity.com/licence>

## Intended use in this repository

**Reference-only for internal (non-commercial) use.** Captured on 2026-04-21 as a design-library input for Claude Design to evaluate when stitching the Clawmachine UI. Clawmachine is a single-user, non-commercial, personal tool. No republishing, no redistribution as a product, no claiming authorship.

When a component is *adopted* into Clawmachine, attribution to Manu Arora / Aceternity Labs must be preserved in the copied source as a comment.

## Fair-use / Research rationale

- Registry endpoints are public and designed for programmatic consumption (that's literally what `shadcn` does).
- Live-preview endpoints return public HTML SSR'd for every visitor.
- No auth bypass, no paywall circumvention for free tier.
- Pro tier (`/pro` blocks) source is auth-gated — we captured only the public live-preview HTML, NOT the JSX source. See `../aceternity-ui-pro/LICENSE_NOTE.md`.

## Contents

| Path | Content | Count |
|------|---------|-------|
| `components/*.tsx` | Verbatim JSX source from registry | 106 files (103 single-file + 3 multi-file dirs) |
| `demos/*-demo.tsx` or `demos/*-demo/` | Demo/usage examples (component + example wrapper) | 130 demo variants |
| `demos-html/*.html` | SSR'd standalone HTML with absolute CDN URLs | 130 files |
| `raw/registry/*.json` | Original registry JSON with full metadata + content field | 106 files |
| `raw/metadata/*.json` | Rich MCP metadata (description, tags, scores, compatibility) | 106 files + index |
| `raw/categories/*.json` | Category groupings (17 categories) | 17 files |
| `raw/demos/*.json` | Demo registry JSON | 130 files |
| `raw/live-previews/*.html` | Raw SSR'd HTML from ui.aceternity.com | 130 files |
| `index.html` | Browsable gallery with category filter | 1 file |

## Dependencies (for any component adopted)

Most components require:
- `react`, `next`
- `tailwindcss`
- `motion` (formerly `framer-motion`)
- `clsx`, `tailwind-merge`, `lucide-react`
- `@/lib/utils` with a `cn` helper (tailwind-merge + clsx)

Some also need: `three`, `@react-three/fiber`, `@react-three/drei`, `cobe`, `qss`.
