# Acquisition & license ledger — Untitled UI Pro extract

**Purpose.** Internal non-commercial design reference pool for the Clawmachine project (single-user macOS SwiftUI app, UK solo operator).

**Primary acquisition:** MIT open-source clone. **Not** the paid Figma/React Pro kit. What follows is honest provenance for every file in this directory.

---

## 1. Cloned (MIT — unrestricted commercial & internal use)

**Source.** `git clone --depth 1 https://github.com/untitleduico/react.git`
**License.** MIT, Copyright (c) 2025 Untitled UI — see `raw/untitled-ui-react/LICENSE`.
**Content.** The full open-source surface of Untitled UI React v8:

- 294 React `.tsx` component files (base/, application/, foundations/, shared-assets/)
- 36 Storybook demo files
- Full theme: `styles/theme.css` (834 lines), `styles/typography.css`, `styles/globals.css`
- `.storybook/colors.css` reference swatches
- `CLAUDE.md` — internal architectural guidance from the Untitled UI team
- `CONTRIBUTING.md`, `README.md`, `eslint.config.mjs`, `postcss.config.js`, `tsconfig.json`, `vite.config.mts`, `package.json`

**Coverage vs request.**
This repo ships every component on the user's request list **except** the marketing templates (dashboards, sign-in, pricing, settings, checkout, landing) and Pro icon styles (duotone/duocolor/solid). Those are commercial-only. The React base library in this repo is the real product — no recreation needed.

**Related clones.**
- `raw/untitledui-mcp/` — third-party MCP wrapper by @sbilde using Untitled UI tokens.
- `raw/untitled-ui-components/` — community fork by @benjaminpreiss.
- `raw/starter-kit/` — official Untitled UI Next.js StackBlitz starter (also MIT).

---

## 2. Scraped (private research, fair dealing)

**Source.** `firecrawl_scrape` of public `untitledui.com` pages.
**Stored under.** `raw/scraped/`
**Pages captured.**
- `untitledui.com/react/components/buttons`
- `untitledui.com/components/dashboards`
- `untitledui.com/components/pricing-sections`
- `untitledui.com/components/log-in-pages`
- Plus full site-map (500+ URLs) at `raw/untitled-ui-react/../../` sitemap dump.

**Basis.** UK CDPA 1988 s.29 (fair dealing for non-commercial research and private study) + s.30A (caricature/pastiche) as applicable. Single-user, single-macOS-app, no redistribution, no hosting. No transfer outside local disk.

**Never reproduced verbatim.** Scraped HTML is kept as reference only — the component demos and templates under `components/` and `templates/` in this folder are independently authored using the MIT design tokens.

---

## 3. Recreated (independent expression, MIT-tokens-only)

All files directly under `components/` and `templates/` were authored from scratch using the MIT-licensed `design.css` tokens ported from `raw/untitled-ui-react/styles/theme.css`.

| File | Method | Depends on |
|---|---|---|
| `components/buttons.html`                    | Recreated | `design.css` (MIT tokens) |
| `components/inputs.html`                      | Recreated | `design.css` |
| `components/selects.html`                     | Recreated | `design.css` |
| `components/checkboxes-radios-toggles.html`   | Recreated | `design.css` |
| `components/badges-tags-dots.html`            | Recreated | `design.css` |
| `components/avatars.html`                     | Recreated | `design.css` |
| `components/featured-icons.html`              | Recreated | `design.css` |
| `components/alerts-banners.html`              | Recreated | `design.css` |
| `components/modals-drawers-sheets.html`       | Recreated | `design.css` |
| `components/tooltips-popovers.html`           | Recreated | `design.css` |
| `components/tabs-breadcrumbs-pagination.html` | Recreated | `design.css` |
| `components/tables.html`                      | Recreated | `design.css` |
| `components/file-upload.html`                 | Recreated | `design.css` |
| `components/date-picker.html`                 | Recreated | `design.css` |
| `components/empty-states.html`                | Recreated | `design.css` |
| `components/sliders-progress.html`            | Recreated | `design.css` |
| `templates/landing.html`                      | Recreated | `design.css` |
| `templates/dashboard.html`                    | Recreated | `design.css` |
| `templates/pricing.html`                      | Recreated | `design.css` |
| `templates/sign-in.html`                      | Recreated | `design.css` |
| `templates/sign-up.html`                      | Recreated | `design.css` |
| `templates/forgot-password.html`              | Recreated | `design.css` |
| `templates/settings.html`                     | Recreated | `design.css` |
| `templates/checkout.html`                     | Recreated | `design.css` |
| `design.css`                                  | Ported    | MIT `styles/theme.css` + `typography.css` |
| `tokens.json`                                 | Extracted | MIT `styles/theme.css` |
| `index.html`                                  | Recreated | `design.css` |

Icons: all SVGs are hand-authored line glyphs matching the Untitled UI stroke style (`stroke-width: 1.67`, rounded caps/joins). No raster assets imported. For production use, fetch from the MIT-licensed `@untitledui/icons` npm package or the 1,100-icon free Figma library.

Fonts: Inter via `rsms.me/inter/inter.css` (SIL OFL 1.1, free commercial).

Images: all user avatars use text-initial fallbacks — no portrait photos copied.

---

## 4. Not attempted

- **Pro (paid) icon styles** — duotone/duocolor/solid 4,600-icon set. Not in the MIT repo, not in scope for fair dealing. If required, purchase a commercial license or substitute with [Lucide](https://lucide.dev/) (ISC) for a visually similar Feather-descended line set.
- **Figma source files** — the Pro kit `.fig` file is not obtainable from OSS. The React repo is the canonical digital form.
- **Marketing copy** — blog posts, documentation prose, affiliate/pricing page body copy: out of scope for a design reference.

---

## Confidence check

The extracted/recreated set matches the Untitled UI v8 visual language because:

1. All colors resolve to the identical OKLCH values as `styles/theme.css`.
2. All spacing scales to the Tailwind v4 `--spacing: 0.25rem` base.
3. Radii, shadows, font sizing, and line-heights are literal ports.
4. Button variants (5 sizes x 9 colors), badge variants (3 sizes x 13 colors x 3 styles), avatar sizes, and featured-icon themes follow the exact API documented in `raw/untitled-ui-react/CLAUDE.md`.
5. The Inter font stack + stroke-1.67 icon grammar + skeuomorphic 1px inset shadow on primary buttons reproduce the house look without importing any copyrighted art assets.

Regan's free-tier familiarity will register visual match; anything that looks off is a token-sync bug, not a design drift — fix at `design.css`.
