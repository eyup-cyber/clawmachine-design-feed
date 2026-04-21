# cybercore-css (retro-cybercore-css)

**Upstream:** https://github.com/sebyx07/cybercore-css
**Demo:** ./cybercore-demo.html (+ ./demo/ + ./examples/)
**License:** MIT — see LICENSE

## What it looks like
Broader cyberpunk vocabulary: neon (magenta #ff00ff + cyan #00ffff on black), synthwave gradients,
animated scanlines, CRT flicker, hologram-shimmer text. Less Cyberpunk 2077-specific than alddesign/cyberpunk-css;
more "generic cyberpunk futurism" — runs toward Blade Runner / Vaporwave.

## What it offers
- Comprehensive component set: buttons, forms, cards, modals, tables, alerts, progress
- Animation utilities: .cc-glitch, .cc-flicker, .cc-scanlines, .cc-hologram, .cc-pulse-neon
- Multiple demo pages in ./demo (buttons, forms, typography, effects)
- Examples folder with full-page mockups
- Dark theme is default; no light variant

## Clawmachine fit
MEDIUM-HIGH. Larger surface area than alddesign/cyberpunk-css. Scanline + CRT-flicker utilities
are the primary carry candidates — those map to Clawmachine's "monitor terminal" aesthetic
and can be layered over the other retro kits (system.css, terminal.css) to age the look up.
Neon-magenta is NOT in operator's palette; use the effect utilities, skip the color defaults.
