# LICENSE NOTE — Stripe design extraction

## Scope

Publicly-available design tokens, CSS, font references, and visual patterns from `stripe.com`, `docs.stripe.com`, `stripe.com/newsroom`, `stripe.com/payments`, and `stripe.com/billing` (Stripe, Inc.) captured for internal design research supporting the private Clawmachine project. Fetched 2026-04-21.

## Fair-use basis

- **Non-commercial, internal reference only.** No redistribution, no shipping. Nothing here enters a customer-facing surface.
- **Factual token extraction.** Extracted values (hex colors, radii, typography scale, motion curves) are functional facts not protected by copyright.
- **No Stripe assets redistributed.** The Söhne font — which is a proprietary Klim Type Foundry face licensed privately to Stripe — is NOT downloaded or embedded here. The `font-faces.txt` file cites Stripe's CDN URL for reference only; the recreation HTML references the same CDN URL at runtime and requires an appropriate license before being displayed to any third party. Before any production usage, Söhne would be replaced with a similarly-toned licensed or OFL face.
- **Public surface only.** All fetched URLs are publicly reachable without authentication, using standard HTTP.

## Source attribution

- Marketing site CSS: `b.stripecdn.com/mkt-ssr-statics/assets/_next/static/css/*.css`
- Docs site: `docs.stripe.com` — confirms the `#5469D4` / `#556CD6` indigo + `#0A2540` navy stack used in the dashboard family
- Payments dashboard HTML recreation uses only extracted color, spacing, and typography tokens populated with fabricated clawmachine-specific test data. No real Stripe customer data appears anywhere in this directory.

## Trademark

The Stripe wordmark remains Stripe, Inc. property. The SVG logo data-URI captured in `tokens/homepage-branding.json` is identification-only and never rendered into any shipped clawmachine artefact.

## Söhne specifically

Söhne is not to be shipped by any downstream project without a Klim license. This is a hard constraint. For clawmachine we would use an OFL face with similar neutral-humanist proportions (e.g. Inter, Satoshi, or IBM Plex Sans — all already inventoried in this workspace).
