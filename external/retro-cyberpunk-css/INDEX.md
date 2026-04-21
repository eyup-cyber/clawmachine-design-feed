# cyberpunk-css (retro-cyberpunk-css)

**Upstream:** https://github.com/alddesign/cyberpunk-css
**Demo:** ./demo/ (index.html)
**License:** MIT — see LICENSE

## What it looks like
Cyberpunk 2077 in-game UI replica. Yellow (#fcee09) + cyan (#00f0ff) accents on black,
angular-clip-path buttons (chamfered corners), heavy glitch effects, Rajdhani + Blender Pro
suggested font stack (bundled subset in ./fonts).

## What it offers
- cyberpunk.css is the single-file framework
- Buttons with chamfered/notched corners via clip-path
- Glitch-text utilities (animated offset layers, not just typography)
- Panel frames with corner brackets
- Primary color signals: yellow = action, cyan = info, red = error, white = neutral
- HUD-style progress bars
- Minimal demo in ./demo

## Clawmachine fit
MEDIUM. Color palette is too aggressive for Clawmachine's palette decisions (yellow/cyan
conflicts with operator's 32+6 shortlist). The clip-path chamfer technique and corner-bracket
panels are reusable shape vocabulary. Glitch-text utilities are the strong carry candidate.
