# retool-bravo-bubble — LICENSE & SOURCING NOTE

**Scrape date:** 2026-04-21
**Operator:** Regan Cooney (regacooney@gmail.com)

## Contents

- `previews/` — 11 PNG screenshots of retool.com/templates detail pages (7), bubble.io/templates gallery pages (3), and bravostudio.app home (1). All captured via firecrawl at 1440x900 viewport.
- `recreated/` — 10 HTML structural approximations covering Retool (analytics, CRM, HR, security, KPI, REST admin, employee directory), Bubble (dashboard gallery, SaaS gallery), and Bravo Studio (home/templates landing).
- `metadata.json` — per-template catalogue.
- `INDEX.md` — top-ranked picks.

## Licence posture — upstream

- **Retool templates** — "Try this in Retool" clones into your Retool workspace. Free to adopt; customisation and deploy fall under your Retool plan's terms. Underlying template is not owned by you until cloned.
- **Bubble templates** — Free or paid, per creator. Free templates are copy-paste into your Bubble project; paid templates carry a single-project licence per purchase.
- **Bravo Studio** — Figma-to-native conversion platform. Templates are marketing examples; actual conversion is done inside the Bravo app with your own Figma source.

## Licence posture — recreated HTML

The `recreated/*.html` files are authored approximations of the documented layouts (Retool's PostgreSQL-backed admin panels, Bubble's free-tier dashboard gallery, Bravo Studio's design-first landing grammar). They do NOT reproduce any Retool component code, any Bubble page source, or any Bravo export. They sit at the structural-pattern layer only.

## Fair-use basis

UK fair-dealing for non-commercial research. Each recreation carries a visible footer crediting the platform (retool.com / bubble.io / bravostudio.app) and linking back to the specific source page. On request from any named creator, the corresponding recreation will be removed.

## Named-creator credits

All Retool templates are authored by the Retool team (`retool.com/templates`). Bubble dashboard gallery items are by community creators — names are visible in each template's detail page (out of scope for this scrape, but every HTML recreation shows the gallery rather than claiming individual authorship). Bravo Studio content is Bravo-authored marketing.
