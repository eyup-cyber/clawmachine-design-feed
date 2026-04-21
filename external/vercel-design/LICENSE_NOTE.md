# LICENSE NOTE — Vercel / Geist design extraction

## Scope

Publicly-available design tokens, CSS, font references, component spec pages from `vercel.com`, `vercel.com/geist`, and `vercel.com/design` (Vercel, Inc.) captured for internal design research supporting the private Clawmachine project. Fetched 2026-04-21.

## Fair-use basis

- **Non-commercial, internal reference.** No redistribution, no shipping in any product.
- **Geist is mostly open.** Vercel publishes the [Geist design system](https://vercel.com/geist) and maintains open-source packages (`vercel/geist-font`, `vercel/geist-ui`, `vercel/examples`) under permissive licenses.
- **Factual token extraction.** Color scales, typography scales, border-radius values, animation curves are functional facts, not copyrightable expression.
- **Geist typeface is OFL.** The [Geist font](https://github.com/vercel/geist-font) ships under SIL Open Font License 1.1 — permissive, including commercial redistribution, with restriction on selling the font alone.

## Source attribution

- Tokens extracted from `vercel.com/vc-ap-vercel-marketing/_next/static/immutable/chunks/*.css` (production bundles) and `vercel.com/geist/*` docs.
- Geist font files referenced at their production CDN URLs; canonical source is the OFL-licensed `vercel/geist-font` GitHub repo, already cloned elsewhere in this workspace.
- Deployment-dashboard HTML recreation uses only extracted token values + clawmachine-specific content.

## Trademark

The Vercel wordmark, triangle mark, and "Geist" name remain Vercel, Inc. property. No use of those marks is implied by this extraction.
