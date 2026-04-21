# Nerd Fonts (icon glyph sheet only)

- **Source**: https://github.com/ryanoasis/nerd-fonts
- **Site**: https://nerdfonts.com
- **Author**: Ryan L McIntyre + upstream glyph sources
- **License**: per-source, see `LICENSE` and `license-audit.md`
- **Version fetched**: depth-1 clone, 2026-04-21 — **glyph sheet extracted, full repo discarded**
- **Glyph count**: thousands (aggregate of all source sets: Devicons, Font Awesome, Octicons, Powerline, Weather, Material, etc.)

## What was kept vs what was dropped

Upstream nerd-fonts repo is 8GB. Per brief ("just the icon glyph sheet") the following were EXTRACTED and the rest discarded:

- `src/glyphs/` (6.3MB) — master glyph source SVGs/TTFs that feed the patcher
- `src/svgs/` (880KB) — per-set SVG exports
- `css/` — cheatsheet CSS + codepoint mapping
- `glyphnames.json` — canonical name→codepoint map
- `10-nerd-font-symbols.conf` — fontconfig fallback snippet
- `LICENSE` + `license-audit.md` — per-source license breakdown
- `readme.md`

DISCARDED:

- `patched-fonts/` (5.5GB) — pre-patched TTF/OTF font binaries (regenerate via font-patcher if needed)
- `src/unpatched-fonts/` (1.1GB) — upstream font sources pre-patch
- `bin/`, `font-patcher`, `FontPatcher.zip`, Dockerfile, install scripts, all non-English readmes
- `images/` — repo marketing

## Consolidate notes

- Use `glyphnames.json` as the lookup: it maps human-readable names (`nf-fa-github`) to Unicode codepoints (`\uf09b`) for each sub-family.
- To render in an app: bundle a single patched Nerd Font (download from nerdfonts.com releases — not in this tree) and use the codepoints.
- The glyph SVGs in `src/glyphs/` are the raw sources, not meant for direct UI use. They're the reference sheet for the operator's brief.
- License is a patchwork: Nerd Fonts itself is MIT, but individual glyph sources carry their own licenses (MIT, Apache 2.0, SIL OFL, CC-BY). `license-audit.md` has the full breakdown per source.
