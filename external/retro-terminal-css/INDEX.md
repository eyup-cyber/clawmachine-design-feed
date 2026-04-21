# terminal.css (retro-terminal-css)

**Upstream:** https://github.com/Gioni06/terminal.css
**Demo:** https://www.terminalcss.xyz/ (also ./demo.html)
**License:** MIT — see LICENSE
**Note:** Pruned ./builds and ./vendor (83M + 9M of Go compiler binaries) — site-builder residue, not styling material.

## What it looks like
Pure monospace, minimal ASCII-ish. White-on-black default (dark theme), optional light/sans variants.
Terminal prompt as `#` prefix on H5. Borderless tables, tight leading, dashed section rules.
The aesthetic is "shell output styled for the web" — not CRT, no scanlines.

## What it offers
- `.terminal-nav`, `.terminal-menu`, `.terminal-logo`, `.menu-item`
- `.terminal-prompt` (adds $-style prefix)
- `.terminal-card`, `.terminal-timeline`, `.terminal-alert` (primary, error)
- `.progress-bar` with `.progress-bar-filled` + `data-filled` label
- `.btn` (default, primary, error, ghost, block-level, btn-group)
- Forms: standard inputs, all HTML5 types
- Media component, blockquote with author, description-list
- Variables: --global-font-size, --font-color, --primary-color, --error-color, --block-background-color
- Built-in highlight.js theme that matches the framework

## Clawmachine fit
HIGH. This is the closest existing framework to the "terminal shell for an operator" vibe
Clawmachine needs. Use as primary chrome for the "machine is talking to you" text/log surfaces.
Combines cleanly with system.css dialogs as modals over terminal content.
