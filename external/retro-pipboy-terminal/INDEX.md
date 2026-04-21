# Pip-Boy Terminal (retro-pipboy-terminal)

**Upstream:** https://github.com/CodyTolene/pip-terminal  (Pip-Boy.com)
**Demo:** ./src (Angular), ./public/images/pip-boy (screenshots + assets)
**License:** CC BY-NC 4.0 (non-commercial) + MIT (code) + MPL 2.0 (some modules) — see LICENSE.md, LICENSE_MIT.md, LICENSE_MPL.md
**Pruned:** ./public/images/fan-art and ./public/images/community removed (3.4M + 0.7M) — fan-submitted art, not framework material.

## What it looks like
Fallout Pip-Boy 3000 replica. Green monochrome CRT (amber variant also included), scan-line overlay,
CRT flicker, boot sequence animations, Monofonto font. THIS IS THE pip-boy/fallout terminal aesthetic
the brief asked for.

## What it offers
- Full Angular web app (not drop-in CSS) — requires build to extract styles cleanly
- CRT shader effects in SCSS
- Pip-Boy UI primitives: boot screen, menu navigation with selector arrow, boot log, stat panels,
  radio player, inventory grid, map view
- Audio assets (./public/sounds): terminal beeps, dial-tune, boot-sound (~132K)
- Fonts (./public/fonts): Monofonto and friends (1.7M)
- Pip-Boy screenshots at ./public/images/pip-boy (11M — reference imagery)

## Clawmachine fit
VERY HIGH for the "CRT monochrome terminal" mode. Non-commercial license fits brief.
Extract: the SCSS scanline/flicker/green-phosphor mixins, Monofonto font, boot-sequence pattern.
Do NOT ship the Fallout/Bethesda trademarks (Pip-Boy logo, Vault-Boy) in any exported product.
