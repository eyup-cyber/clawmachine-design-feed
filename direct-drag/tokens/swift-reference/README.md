# Swift design tokens — reference only

These five files are the **canonical source** for Clawmachine's design tokens. They are SwiftUI but the values (hexes, spacing scale, font stack, bevel pattern, icon bitmap grammar) translate 1:1 to web.

Do NOT treat this as the implementation target. The web-side design system is in `CLAWMACHINE-DESIGN-SYSTEM.html` + `CLAWMACHINE-DASHBOARD-38-VARIANTS.html` + `CLAWMACHINE-PAGES-BRAIN-MESH-AGENT-SETTINGS.html` at the feed root. These five files are to confirm the tokens you see embedded there are the real, shipped app tokens — not invented.

## Files

- `Colors.swift` — `PageAccent`, `TextColor`, `Surface`, `Brand`, `Status`, `PlatformColor`, `PageTheme` (7 themes). Every hex also in `.triage/chromatic-schemes.json`.
- `Typography.swift` — font families + size scale.
- `Spacing.swift` — `{4, 8, 12, 16, 24, 32}` only.
- `Bevel.swift` — beveled border grammar (highlight top-left, shadow bottom-right). No blur, no translucency.
- `SidebarIcons.swift` — 16×16 `UInt16` bitmap masks for the 7 nav icons. Same grammar used in the HTML files' pixel-icon render.

## Page→accent map (per scheme #02 DEEP CURRENT in the HTML examples)

| Page | Accent |
|---|---|
| Dashboard | `#00E5A0` |
| Inventory | `pg.inventory` from active scheme |
| Analytics | `pg.analytics` from active scheme |
| Brain | `pg.brain` from active scheme |
| Mesh | `pg.mesh` from active scheme |
| AgentConsole | `pg.settings` (shares accent with Settings) |
| Settings | `pg.settings` from active scheme |

## What to generate against these

- **Buttons** — beveled (highlight top-left, shadow bottom-right), 4px radius max, solid fills only, label in lowercase or ALL CAPS never Title Case.
- **Inputs** — inset beveled (shadow top-left, highlight bottom-right = reverse of button), same radius, solid bg.
- **Cards** — beveled panel, 4px radius, solid fill, inset shadow optional for recessed areas.
- **Tables** — row-striped with panel/panelAlt fills, sticky headers in ALL CAPS, tabular numerics in JetBrains Mono.
- **Icons** — 16×16 bitmap grammar (see SidebarIcons.swift) for nav. Hand-authored SVG for everything else. Never SF Symbols.
