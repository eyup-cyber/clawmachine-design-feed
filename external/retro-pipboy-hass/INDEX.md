# Pip-Boy Home Assistant Theme (retro-pipboy-hass)

**Upstream:** https://github.com/biofects/pipboy
**Demo:** ./images (screenshots)
**License:** MIT — see LICENSE

## What it looks like
Pip-Boy terminal aesthetic applied as a Home Assistant frontend theme. Green-on-black phosphor,
CRT scan lines, terminal typography. Self-contained YAML theme definitions + supporting CSS/card
overrides. More constrained surface than pip-terminal because it targets HA's Lovelace UI.

## What it offers
- ./themes/*.yaml — HA theme variable definitions (ready-to-port color tokens)
- ./www — supporting JS/CSS for card-mod overrides
- Readable color-token mapping: primary-color = green phosphor, warning = amber, background = near-black
- Screenshots at ./images

## Clawmachine fit
HIGH as a TOKEN SOURCE (not component source). The theme YAMLs contain a clean, named token map
for pip-boy green-phosphor + amber-on-black — map those into Clawmachine's design-token system
wholesale. Component surface is HA-specific and not directly reusable, but the token extraction
gives you the palette without the trademark baggage of pip-terminal's Fallout-branded assets.
