# Preline UI — README-EXTRACT

**Upstream**: https://github.com/htmlstreamofficial/preline
**Clone**: `git clone --depth 1` (shallow)
**Size on disk**: ~7.7 MB
**License**: **MIT + Preline UI Fair Use dual license** — see `LICENSE_NOTE.md` (this is NOT pure MIT).

## What this is

Preline UI is the open-source Preline component kit: prebuilt Tailwind components with vanilla-JS + HTMX interactivity plugins. Unlike Hyper UI (static markup only), Preline ships actual interactive plugins (accordion, carousel, combobox, datepicker, dropdown, modal/overlay, range-slider, tabs, tooltip, tree-view, etc.) written as vanilla-JS classes you bundle into a Tailwind/HTMX site.

## Key folders for reference

| Path | What's in it |
|---|---|
| `src/plugins/` | **primary**: vanilla-JS interactivity plugins, one dir per plugin: `accordion/`, `carousel/`, `collapse/`, `combobox/`, `copy-markup/`, `datatable/`, `datepicker/`, `dropdown/`, `file-upload/`, `input-number/`, `layout-splitter/`, `overlay/`, `pin-input/`, `range-slider/`, `remove-element/`, `scroll-nav/`, `scrollspy/`, `select/`, `stepper/`, `strong-password/`, `tabs/`, `textarea-auto-height/`, `theme-switch/`, `toggle-count/`, `toggle-password/`, `tooltip/`, `tree-view/`, plus `accessibility-manager/` and `base-plugin/`. Each plugin has index.ts, helpers, interfaces, types. |
| `src/helpers/` | shared JS helpers across plugins. |
| `src/utils/` | utility functions. |
| `src/auto/` | auto-initialisation bootstrap. |
| `src/globals.ts`, `constants.ts`, `interfaces.ts`, `index.ts` | public entry + types. |
| `templates/` | full-page templates: `agency/`, `ai-chat/`, `cms/`, `coffee-shop/`, `personal/` (Tailwind + HTMX HTML pages). |
| `dist/` | prebuilt bundles (skip if reading source). |
| `css/`, `variants.css` | Tailwind variant CSS fragments. |
| `skills/` | LLM prompt-skill bundles — interesting side artefact. |

## Boilerplate (skip)

- `dist/` if you want source-of-truth (it's the compiled output of `src/`).
- `scripts/`, `webpack.config*.js`, `tsconfig*.json`, `prettier.config.js`, `dts-config.js`, `package-lock.json`.
- `preline.d.ts`, `preline.js`, `index.d.ts`, `index.js` at repo root — these are the bundle exports.

## Recommended entry points for Frankenstein stitch

1. **Interactive-plugin reference**: `src/plugins/combobox/`, `src/plugins/overlay/`, `src/plugins/datepicker/` are the right reads if we end up wiring vanilla-JS interactions into a Swift webview (no React runtime required). This is the lightest-weight interactivity pattern of the seven kits.
2. **AI-chat template**: `templates/ai-chat/` — direct UI reference for the chat surface we know clawmachine needs.
3. **Preline's `skills/` dir**: unusual inclusion — LLM prompt skills shipped alongside a UI kit. Worth a pass.
