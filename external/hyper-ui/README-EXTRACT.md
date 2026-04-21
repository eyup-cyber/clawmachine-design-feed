# Hyper UI — README-EXTRACT

**Upstream**: https://github.com/markmead/hyperui
**Clone**: `git clone --depth 1` (shallow)
**Size on disk**: ~5.3 MB (smallest of the seven)
**License**: MIT

## What this is

Mark Mead's "free open-source Tailwind CSS components" — an Astro-driven gallery of raw Tailwind HTML blocks. No React, no framework dependencies: each component is static Tailwind markup in an MDX file. Reference for "what does the base-layer Tailwind pattern look like for this widget" without the abstraction layers Mantine/Chakra add.

## Key folders for reference

Astro site — the useful part is `src/content/collection/`.

| Path | What's in it |
|---|---|
| `src/content/collection/application/` | **primary (app UI)**: `accordions.mdx`, `badges.mdx`, `breadcrumbs.mdx`, `button-groups.mdx`, `checkboxes.mdx`, `details-list.mdx`, `dividers.mdx`, `dropdown.mdx`, `empty-states.mdx`, `file-uploaders.mdx`, `filters.mdx`, `grids.mdx`, `inputs.mdx`, `loaders.mdx`, `media.mdx`, `modals.mdx`, `pagination.mdx`, `progress-bars.mdx`, `quantity-inputs.mdx`, `radio-groups.mdx` … |
| `src/content/collection/marketing/` | **primary (marketing UI)**: `announcements.mdx`, `banners.mdx`, `blog-cards.mdx`, `buttons.mdx`, `cards.mdx`, `carts.mdx`, `contact-forms.mdx`, `ctas.mdx`, `empty-content.mdx`, `faqs.mdx`, `feature-grids.mdx`, `footers.mdx`, `headers.mdx`, `logo-clouds.mdx`, `newsletter-signup.mdx`, `polls.mdx`, `pricing.mdx`, `product-cards.mdx`, `product-collections.mdx`, `sections.mdx` … |
| `src/content/collection/neobrutalism/` | neobrutalist variants — visually adjacent to our retro palette direction. |
| `src/content/blog/` | blog posts accompanying components. |
| `src/components/` | Astro site components (not library components — don't confuse). |
| `src/styles/` | Astro site styling. |

Each `.mdx` in `collection/` contains multiple Tailwind HTML snippets inline, each annotated with a `<Preview>` wrapper. To extract raw markup, strip the MDX wrappers.

## Boilerplate (skip)

- `src/{layouts,pages,assets,tests,types,utils}/`, `content.config.ts`, `consts.ts` — Astro plumbing.
- `astro.config.js`, `eslint.config.js`, `playwright.config.js`, `wrangler.jsonc`, `worker-configuration.d.ts`, `pnpm-*.yaml`, `tsconfig.json`, `public/` — site tooling.
- `CONTRIBUTING.md`, `README.md`.

## Recommended entry points for Frankenstein stitch

1. **Raw Tailwind patterns**: open `src/content/collection/application/inputs.mdx` or `modals.mdx` — you see the literal class-chain for that widget, uncluttered by React abstractions. Good floor for a Swift-UI-via-webview where we're emitting static HTML.
2. **Neobrutalism collection**: `src/content/collection/neobrutalism/` — closest visual register to the high-contrast retro themes in the palette shortlist.
3. **Marketing vs application split**: Hyper UI separates them cleanly — useful when our evaluator-engine UI needs to borrow app-shell primitives but our buyer-facing listing preview needs marketing polish.
