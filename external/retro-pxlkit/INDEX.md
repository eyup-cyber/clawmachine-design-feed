# Pxlkit (retro-pxlkit)

**Upstream:** https://github.com/Joangeldelarosa/pxlkit
**Demo:** ./example-page (Next.js app)
**License:** Split - MIT for code (see LICENSE-CODE), custom asset license with attribution requirement (see LICENSE-ASSETS), commercial tier available (see COMMERCIAL_LICENSE.md)

## What it looks like
Modern retro: pixel-art icons rendered crisp at 16/24/32/48px, NES-inspired color usage,
React/Next.js component library with 3D parallax effects. 200+ hand-drawn pixel-art icons
across 7 themed packs. The underlying components use Tailwind.

## What it offers
- Packages (in ./packages):
  - @pxlkit/core - core React primitives
  - @pxlkit/ui-kit - Button, Card, Input, Dialog, etc.
  - @pxlkit/voxel - 3D parallax pixel renderer
  - Icon packs (7): gamification, feedback, social, weather, ui, effects, parallax
- ./apps — full demo apps
- ./example-page — paste-and-go Next.js starter
- Validation script for icon consistency (validate-icons.js)

## Clawmachine fit
MEDIUM-HIGH. Pixel-art icon packs are substantial and hand-drawn (not SVG auto-generated),
which is exactly the kind of craft Clawmachine wants. Attribution requirement is fine for
internal/non-commercial. React components duplicate what neobrutalism-components provides
but with pixel styling — worth pulling the icon packs separately from the components.
Asset attribution must be preserved in any shipped build.
