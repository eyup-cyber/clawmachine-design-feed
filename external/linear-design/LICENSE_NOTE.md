# LICENSE NOTE — Linear design extraction

## Scope

This directory captures publicly-available design tokens, CSS, font references, and visual patterns from `linear.app` (Linear, Inc.) for internal design research supporting the private Clawmachine project. Fetched 2026-04-21.

## Fair-use basis

- **Non-commercial, internal reference only.** Files here are not distributed, not embedded in any shipped product, and not used to impersonate or imply affiliation with Linear.
- **Factual extraction of design tokens.** CSS values (hex colors, spacing scales, font stacks, easing curves) are not copyrightable under US/UK precedent — they are functional facts.
- **Technical inspection of public surface.** All content was fetched via standard HTTP from publicly-accessible URLs, using the same methods a browser would use.
- **No trademark usage claimed.** The Linear name and wordmark remain Linear, Inc.'s property. Recreations that appear here carry clawmachine content (issue titles, project names) — not Linear content — and are explicitly labeled "recreation".

## Source attribution

- Tokens: extracted from `static.linear.app/web/_next/static/css/*.css` and `linear.app/brand`.
- Fonts referenced (Inter Variable, Berkeley Mono) — **not redistributed**; only the original CDN URLs are cited for development-time fetching.
- Patterns (`patterns/issue-list.html`) are a visual recreation of the Linear issue-list pattern built from first principles using only the extracted token values, populated with clawmachine-specific content.

## Linear's own brand rules

Per `linear.app/brand`: assets are proprietary. Users must not alter Linear's graphics, imply affiliation, or combine them with other graphics without consent. This project does not display, embed, or redistribute any Linear-owned raster/vector assets. The SVG logo data-URI captured in `tokens/homepage-branding.json` is for identification of the brand only and is never rendered into any shipped clawmachine artefact.

## If Linear objects

Remove this directory. Nothing here enters the clawmachine build artefact; only abstracted token concepts flow into the stitch.
