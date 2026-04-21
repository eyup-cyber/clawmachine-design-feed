# system.css (retro-system-css)

**Upstream:** https://github.com/sakofchit/system.css
**Demo:** https://sakofchit.github.io/system.css/ (also ./demo.html, ./docs/index.html.ejs)
**License:** MIT (c) 2022 Sakun Acharige — see LICENSE

## What it looks like
Apple System OS / Classic Mac (System 6-7) aesthetic. Pixel-perfect 1-bit UI. Chicago + Geneva typography
(bundled). Square-edged windows with thin 1px borders, patterned title bars, scalloped menu bar, drop-shadow
on top-most chrome. Monochrome; dither patterns for fill states. No gradients, no anti-aliasing in chrome.

## What it offers
- Window chrome: `.window`, `.title-bar`, `.modeless-dialog`, `.standard-dialog`
- Controls: `.btn` (default, primary, disabled), radio, checkbox, select, field-row
- Menu bar + dropdown: `.menu-bar`, `.menu` with nested `details`
- Dialog icons: note, caution, stop (64x64 pixel-art PNGs in ./icon)
- Fonts: Chicago-12.woff, Geneva-9.woff, ChicagoFLF.ttf, FindersKeepers.ttf (./fonts)
- style.css is the single-file import; docs/docs.css holds demo-specific layout only.

## Clawmachine fit
Primary retro-mac layer. Window chrome + dialog modals for "operator console" feel.
Chicago-12 bitmap font is the canonical Kare-era typeface.
