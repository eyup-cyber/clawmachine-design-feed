# NES.css (retro-nes-css)

**Upstream:** https://github.com/nostalgic-css/NES.css
**Demo:** https://nostalgic-css.github.io/NES.css/ (also ./demo.html, ./docs/index.html)
**License:** MIT — see LICENSE

## What it looks like
8-bit / NES aesthetic. Chunky pixel borders (drawn via box-shadow), Press Start 2P font
(recommended separate install), primary palette in NES hardware colors (red #e76e55,
blue #209cee, green #92cc41, dark-grey), everything rendered at integer pixel scale.

## What it offers
- `.nes-btn` variants (primary, success, warning, error, disabled)
- `.nes-container` with `.is-rounded`, `.is-dark` modifiers
- Pixel-art form controls: radios, checkboxes, text inputs, textareas
- Icon sprites: `.nes-icon` (heart, star, close, trophy), `.nes-mario`, `.nes-ash`,
  `.nes-bcrikko`, `.nes-kirby`, `.nes-pokeball` — character art as CSS shadows
- Dialog: `.nes-dialog` + `.dialog-rounded`
- Built from SCSS in ./scss; CSS shipped as dist bundle (via npm) but source in repo
- ./assets has BlobWave cat and characters

## Clawmachine fit
Visual primitive for "game" nostalgia layer. NOT the lead aesthetic (operator rejected
gamification per project_visual_decisions) but the pixel-border technique and character
sprites are reference material for accent elements only. Press Start 2P font is standard
pixel-font reference.
