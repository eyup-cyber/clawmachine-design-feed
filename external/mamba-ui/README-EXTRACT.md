# Mamba UI — README-EXTRACT

**Upstream**: https://github.com/Microwawe/mamba-ui
**Clone**: `git clone --depth 1` (shallow)
**Size on disk**: ~9.5 MB
**License**: MIT

## What this is

Mamba UI is an Angular-based gallery of 150+ Tailwind CSS components and templates. Despite being written as an Angular app, the deliverable is static Tailwind HTML markup (each component is a copy-paste snippet) — so the Angular scaffolding is irrelevant; only the Tailwind class chains matter. Good breadth-of-patterns reference at the "raw Tailwind markup" tier alongside Hyper UI.

Note: the request originally specified `mambaui-ts/mambaui` which doesn't exist; the canonical slug is `Microwawe/mamba-ui` (verified via search; Mamba UI's mambaui.com website references this repo).

Note: the README's claim that Mamba UI is "Tailwind + DaisyUI" is not accurate at the source level — we have DaisyUI separately at `external/daisyui/`. Mamba UI uses vanilla Tailwind.

## Key folders for reference

Angular app source under `src/app/`. Most of it is Angular boilerplate — only two subtrees matter:

| Path | What's in it |
|---|---|
| `src/app/components/` | **primary**: 30+ category dirs, each with Angular-wrapped Tailwind HTML — `article/`, `avatar/`, `banner/`, `blog/`, `breadcrumb/`, `button/`, `call-to-action/`, `card/`, `carousel/`, `contact/`, `error/`, `faq/`, `feature/`, `footer/`, `form/`, `gallery/`, `header/`, `hero/`, `input/`, `loading/`, `login/`, `modal/`, `news/`, `pagination/`, `pricing/`, `profile/`, `review/`, etc. Each dir holds `.component.html` files — the Tailwind markup lives inline. |
| `src/app/templates/` | **primary**: full-page templates — `business/`, `portfolio/`. |
| `src/app/core/`, `shared/`, `docs/` | Angular routing, layout, docs plumbing — not components. |
| `src/styles/`, `tailwind.config.js`, `postcss.config.js` | Tailwind config reference. |

## Boilerplate (skip)

- `src/{app.component.*, app.module.ts, app-routing.module.ts}`, `src/{environments, main.ts, main.server.ts, polyfills.ts, test.ts, index.html}` — Angular app scaffolding.
- `src/assets/`, all the favicons / android-chrome / apple-touch icons — site icons.
- `angular.json`, `browserconfig.xml`, `cypress*`, `e2e/`, `karma.conf.js`, `lighthouserc.js`, `ngsw-config.json`, `server.ts`, `stylelint.config.js`, `tsconfig*.json`, `package-lock.json` — tooling.

## Recommended entry points for Frankenstein stitch

1. **Raw-Tailwind markup**: open any `src/app/components/{card,hero,pricing,feature,footer}/*.component.html` and extract the HTML inside the Angular template (stripping `{{ }}` interpolations if present). This is the same tier as Hyper UI but with substantially different stylistic choices — good to cross-reference before committing to a card or hero pattern.
2. **Template structure**: `src/app/templates/business/` and `portfolio/` show how Mamba composes components into full pages. Relevant if we need a listing-preview or buyer-facing page layout.
3. **Breadth play vs Hyper UI**: Mamba has more inventory in `profile/`, `review/`, `login/`, `news/`; Hyper UI has more inventory in `application/` widgets (accordions, checkboxes, dropdowns, inputs). Use them as complements, not substitutes.
