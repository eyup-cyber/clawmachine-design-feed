# 7.css (retro-7-css)

**Upstream:** https://github.com/khang-nd/7.css
**Demo:** https://khang-nd.github.io/7.css/ (also ./demo.html)
**License:** MIT — see LICENSE

## What it looks like
Windows 7 Aero aesthetic. Glossy pill buttons, glass title-bars (translucent/blur),
rounded-corner windows, gradient-filled scrollbars, Segoe UI typography.

## What it offers
- Same class system as 98.css/XP.css (`.window`, `.title-bar`, `.button`, `field-row`, `progress`)
- Aero glass: `.glass` modifier for translucent title chrome
- Taskbar component, start menu, balloon tooltips
- Themes: light + dark via .theme-dark
- Build: ./gui (source) -> docs/ (rendered demo, same as 98/XP/system pattern)

## Clawmachine fit
CAUTION: operator has ruled out liquid glass aesthetic (feedback_visual_antithesis_liquid_glass).
Ship as reference only for window-chrome geometry; do NOT carry Aero glass/blur into final.
The `.window` + `.title-bar` structure is still useful as a skeleton.
