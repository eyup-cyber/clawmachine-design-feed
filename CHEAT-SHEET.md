# Clawmachine — design directives (tl;dr for Claude Design)

One-pager distilling every operator-enforced constraint. Lower in the feed there are 120k+ of HTML, 37k SVGs, 20+ retro/brutalist CSS frameworks, 7 component libraries, 10+ font families, and the `.triage/*.json` palette catalogue. Read this first.

## Who this is for

Solo UK fix-and-flip tech-electronics reseller. Desktop-only macOS SwiftUI app. Internal tooling. Ten-hour days at one dense terminal. Not consumer-facing. Not a team tool. Not a SaaS.

## The aesthetic (composite — get all three)

1. **Retro Mac OS 9 / System 7** — beveled chrome, Chicago/Silkscreen bitmap type, platinum 3D edges, outlined 16×16 icons (clean 1.5–2px stroke, not pixel-jagged).
2. **Cyberpunk HUD** — saturated accent-on-dark, scanline-adjacent density, terminal readouts.
3. **Brutalist web** — thick borders, honest corners, tabular numerics, no ornament, ALL-CAPS and lowercase only (never Title Case).

Think Bloomberg Terminal + Pro Tools + Fallout Pip-Boy + Susan Kare Chicago + Neobrutalism.dev — rendered in operator-authored palettes (see `.triage/chromatic-schemes.json`).

## Absolute do-nots

- No translucency / blur / backdrop-filter / opacity-based fills. (Apple liquid-glass is explicitly ruled out.)
- No gradients beyond a beveled edge (highlight top-left, shadow bottom-right — solid colours, not gradients).
- No SF Symbols. Sidebar nav uses **Lucide Regular** (clean outlined, 1.5–2px stroke) at 16×16. Device thumbnails use hand-authored outlined silhouettes at 24–44px, 2px stroke. Pixelarticons are reference-pool only, never in active UI (operator flagged them as jagged/ugly).
- No Title Case anywhere — only ALL CAPS labels or lowercase.
- No gamification: no WIN RATE, achievements, streaks, leaderboards, XP, badges, level-ups.
- No developer-voice UI copy ("The user should…", "In this view we…"). Plain English, direct labels.
- No AI-generated illustration filler. No generative-image residue.
- No "TARGET PLATFORM" column on deal rows. Default resale is eBay — don't make the user click it every row.
- No default-visible dismissed or negative-profit rows.
- No Matter font. No fonts from the style-lab scrape folder.
- No Decluttr, Mazuma (dead UK vendors). No sell-to-CeX, no sell-to-BS-Exchange (CeX + BSE are buy-sources and floor-aggregate inputs ONLY; never sell-targets).

## Do

- Dark, dense, data-first foundation. Per-scheme accent ramps per page (see `.triage/chromatic-schemes.json` → `pg.*` per scheme).
- Beveled borders: highlight top-left, shadow bottom-right (see `swift-reference/Bevel.swift`).
- Satoshi for display, JetBrains Mono for all numerics/data, IBM Plex Sans body.
- Corner radius ≤ 4px everywhere.
- Spacing from `{4, 8, 12, 16, 24, 32}` only.
- Curve-and-bounce motion: `cubic-bezier(0.34, 1.56, 0.64, 1)` — easeOutBack. Transitions ≤ 300ms. Ambient loops ≤ 2s.
- Deal rows are a CSS-grid with fixed columns: device thumbnail (44px) · vendor chip (120px) · title (1fr) · BUY £ (96px, floor-aggregate + "· N SRC" sub-label) · SELL £ (96px, eBay sold-median) · ROI pill (72px) · ↗ clickthrough (32px). Column headers "BUY" / "SELL" in plain English — never "FLOOR" / "EBAY MED". No "DEV" column text label.
- Six UK vendor badges: `ebay, cex, gumtree, facebook, shpock, preloved, wholesale-clearance`. Each gets a distinct accent from the active scheme's `pg.*`.

## The 7 pages

1. **Dashboard** — live deal feed + KPI stat cards + status strip.
2. **Inventory** — acquired-item grid with image, condition grade (MINT/EXCELLENT/GOOD/FAIR), target sell price, live comp.
3. **Analytics** — counts, profit, ROI trend, worst-performers (hidden dismissed section). Chart is trading-terminal density — candles, grid, ticks, numeric labels, crosshair.
4. **Brain** — chat transcript with operator + live recommendations column. No `<think>` tags ever visible.
5. **Mesh** — 3 machine cards (MacBook / Studio / Pi) + interleaved log stream + latency sparkline.
6. **AgentConsole** — tool list + call-trace viewer.
7. **Settings** — appearance (62-palette selector), channels (BlueBubbles/Studio/Pi config), brain model config.

All 7 pages are rendered in `CLAWMACHINE-PAGES.html` — same vocabulary as the codex labs at `local/chromatic/clawmachine-chromatic-lab.html` and `local/chromatic/clawmachine-style-lab.html`. Scheme switcher in the header rescopes across 7 schemes (02/07/18/25/38/46/52). The 1-pager cover for Claude Design ingest is `CLAWMACHINE-INGEST-MAP.html`.

## The palette catalogue

62 operator-authored schemes in `.triage/chromatic-schemes.json`. Operator shortlist of 38 most-preferred: `01,02,04,06,07,08,09,10,11,12,14,15,16,17,18,19,20,21,23,25,26,27,28,29,30,33,35,36,37,38,39,40,46,51,52,53,55,57,58`.

Each scheme provides: `void` (page bg), `p` (primary accent), `s` (secondary), `pg.{dashboard,inventory,analytics,brain,mesh,onboarding,settings}` (per-page accent).

Default scheme for new installs: **#02 DEEP CURRENT** — dark oceanic, void `#060B10`, primary `#00E5A0`. All the finished-page HTML examples use this scheme.

## Reality check

The current shipped app is visually dead — grey-box shell with mock rows. We're building its replacement. The `local/current-app-screenshots/` folder (if populated by the screenshot agent) shows the "before" — do NOT match that; match the HTML examples.

## Handoff expectation

When we hit "Send to Claude Code" from Claude Design, the spec should arrive as SwiftUI-ready structure (views + components + tokens). The app is Swift 6.3, Foundation + SwiftUI only, no AppKit, no SF Symbols.
