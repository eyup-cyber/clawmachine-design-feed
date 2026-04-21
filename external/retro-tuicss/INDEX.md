# TuiCSS (retro-tuicss)

**Upstream:** https://github.com/vinibiavatti1/TuiCss
**Demo:** https://github.com/vinibiavatti1/TuiCss (see ./examples/)
**License:** MIT — see LICENSE.md

## What it looks like
MS-DOS TUI / Norton Commander aesthetic. ASCII-block UI (`█ ╔═╗ ║ ╚═╝`), 16-color CGA palette,
VGA 8x16 raster font, hard edges, no anti-aliasing. Title bars done with `░ ▒ ▓` fills.
Truer "BIOS terminal" feel than terminal.css.

## What it offers
- Grid-based screens: `.tui-screen`, `.tui-panel`, `.tui-window`
- Menu bars: `.tui-menubar`, `.tui-menu`
- Form controls: buttons, checkboxes, radios, selects, inputs — all ASCII-rendered
- Progress bars, tab navigation, status bars
- Tree view, list view
- Full CGA color utility classes: `.blue`, `.red`, `.yellow`, `.cyan`, `.green` as foreground AND background
- Examples folder: 15+ screen mockups (calculator, file-manager, login, setup, etc.)
- dist/tuicss.min.css is the single bundle

## Clawmachine fit
VERY HIGH. This is the BIOS-terminal aesthetic the brief asked for (standalone BIOS.css doesn't exist).
Best candidate for "inspector panel" / "setup screen" / error-diagnostics layout.
Pairs naturally with Chicago/Silkscreen fonts where a more DOS look is wanted.
