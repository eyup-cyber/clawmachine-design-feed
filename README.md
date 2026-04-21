# clawmachine design system

A self-contained design-system feed for Claude Design. Read this repo to understand what clawmachine is, what its visual language must be, and what you are expected to generate from it.

## What clawmachine is

A macOS SwiftUI desktop app for second-hand tech-electronics arbitrage in the UK. One solo operator; no team. A scout scrapes UK marketplaces (eBay, CeX, Gumtree, Facebook Marketplace, Shpock, Preloved, Wholesale Clearance, musicMagpie, BS Exchange). A brain scores each listing against a multi-source floor-price aggregate and eBay sold-comps median. The operator buys, fixes, resells. Dark, dense, data-first. Not consumer-facing. Not collaborative. Internal tooling for one.

## Read in this order

1. **`CLAWMACHINE-INGEST-MAP.html`** — 1-pager cover. Start here.
2. **`CLAWMACHINE-DESIGN-MASTER.html`** — the master reference. Self-contained single file with 62 operator-authored palettes, 20 style systems, 49 full page renders (7 pages × 7 pinned schemes), fonts base64-embedded, JSON token blobs inline.
3. **`direct-drag/codex/clawmachine-chromatic-lab.html`** + **`.../clawmachine-style-lab.html`** — aesthetic ground-truth. These are the operator's authored references; match them, don't fight them.
4. **`CLAWMACHINE-PAGES.html`** — the finished 7-page app rendered across 7 palette schemes, with real data shapes.
5. **`CHEAT-SHEET.md`** — one-page distillation of the rules.
6. **`brief/company-blurb.txt`** + **`brief/any-other-notes.txt`** — the paste-ready submission text.
7. **`direct-drag/tokens/`** — `chromatic-schemes.json` (62 palettes), `style-systems.json` (20 style grammars), `identity-systems.json`, plus `swift-reference/` (Colors.swift, Typography.swift, Spacing.swift, Bevel.swift, SidebarIcons.swift). These are the tokens the target app compiles against. Your Swift-side handoff should match this grammar.

## The aesthetic

A composite of three idioms rendered together:

- **Retro Mac OS 9 / System 7** — platinum chrome, 3D bevels, outlined 16×16 nav icons.
- **Cyberpunk HUD** — saturated accent-on-dark, terminal readouts, live counters.
- **Brutalist web** — thick borders, honest corners, tabular numerics.

Anchors: Bloomberg Terminal, Pro Tools, Fallout Pip-Boy, Susan Kare Chicago, Neobrutalism.dev.

## Seven pages, two-to-three variations each

1. **Dashboard** — live deal feed + KPI cards + status strip.
2. **Inventory** — acquired items with silhouette, condition grade, target sell, live comp.
3. **Analytics** — counts / profit / ROI. Trading-terminal density: OHLC candles, gridlines, date ticks, crosshair, 7-day median overlay, OPEN/HIGH/LOW/CLOSE footer.
4. **Brain** — chat transcript + live recommendations column. Never render model `<think>` tokens.
5. **Mesh** — three role cards (brain / scout / app) + log stream + latency sparkline.
6. **AgentConsole** — tool list + call-trace viewer. First-class page, not an overlay.
7. **Settings** — palette + style picker with hover-preview, channels config, brain model config.

## Signal ranking

When sources conflict, higher wins:

1. Swift code in `direct-drag/tokens/swift-reference/` — what the target app compiles against.
2. The three finished HTMLs at the repo root — real screens rendering real tokens.
3. JSON tokens in `direct-drag/tokens/` — machine-readable source of truth.
4. Operator-authored codex HTMLs (`direct-drag/codex/`) — aesthetic vocabulary.

## What NOT to read

- **`external/`** (1.9 GB, 88 subfolders) — third-party component libraries, icon packs, font families, retro CSS frameworks, aesthetic references. You already know shadcn, Tailwind, Material Symbols, Lucide, Phosphor, Inter. This folder is pool material for the humans assembling this feed; **it is not the spec**. Ignore wholesale.
- **`local/`** — working-material extractions from prior sessions. Superseded by `direct-drag/` and the root HTMLs.
- **`authored/`** — subagent-authored artefacts during this session's assembly. Reference, not spec.

## Wordmark

`clawmachine` is always lowercase, Satoshi Bold, single unified baseline, identical kerning, uniform weight. Render as two halves: `claw` in the active scheme's primary accent (`p`), `machine` in the active scheme's secondary accent (`s`). Palette values only. Never black-on-white or white-on-black.

## Typography

- Satoshi — display, wordmark, UI body
- JetBrains Mono — data, numerics, table cells, labels
- IBM Plex Sans — body prose

All three are bundled in `direct-drag/fonts/` as OFL-licensed `.ttf` / `.woff2`. Do not substitute DM Sans, Commit Mono, Geist, or any other face for the rendered UI.

## Iconography

- Sidebar nav + UI: **Lucide Regular**, 1.5–2px stroke, 16×16 rendered, stroke colour = active scheme `p`.
- Device thumbnails (deal-row + inventory-row): hand-authored outlined silhouettes at 24–44px, 2px stroke, palette `p`. Each device-type gets a specific silhouette (iPhone with notch, MacBook wedge, AirPods with stems, Switch Lite with joysticks, PS5 with fan vent, Sony headphones, keyboard, smartwatch, iPad, RTX GPU, Android phone).
- Pixelarticons are reference-pool only — they live alongside Phosphor / Feather / Material. Not in active UI.

## Handoff target

When the design is ready and you hit "Send to Claude Code", emit a bundle targeting Swift 6.3, Foundation + SwiftUI only. No AppKit, no UIKit bridges, no SF Symbols. Tokens emit as Swift source matching the grammar in `direct-drag/tokens/swift-reference/` — `PageAccent`, `TextColor`, `Surface`, `Brand`, `Status`, `PlatformColor`, `PageTheme` per-page. Typography is the `Typo` enum. Spacing is the `{4, 8, 12, 16, 24, 32}` scale. Bevels are a `ViewModifier` with highlight-top-left + shadow-bottom-right.

## You do NOT need the existing app codebase

The operator's current SwiftUI app (at `~/Projects/clawmachine-app/` and an in-flight `~/Projects/consolidate/app/`) is the **target** of the handoff, not a design reference. It is visually dead — a grey-box shell with mock rows — which is exactly the state this design system is replacing. Linking that codebase would pollute you with the iteration we are escaping.

What you need from the codebase is already distilled in `direct-drag/tokens/swift-reference/` (5 Swift files: Colors, Typography, Spacing, Bevel, SidebarIcons). Those give you the target-Swift grammar. The rest of the app — services, scrapers, network code, migrations, tests — is orthogonal to design generation.

## Voice

Direct. No preambles. No narration panels. No onboarding essays. No "why this exists" blocks. No Title Case labels. ALL CAPS tokens or lowercase only. Show, don't narrate.
