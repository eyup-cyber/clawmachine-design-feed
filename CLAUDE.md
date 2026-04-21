# Clawmachine — Claude Design context

Primary context file for Claude Design ingest. Read this first; it links the rest of the feed in the right order.

## Status of this brief

The HTML files, palettes, style systems, and tokens in this feed are **the closest approximation the operator has reached so far** — not dogma. Nine-plus prior iterations failed in specific, documented ways (see the Do-Not list below); those failure modes are hard constraints. Everything else is a starting point you are expected to **surpass**. If you see a structure, spacing, rhythm, motion, or composition that could more faithfully realise the operator's stated vision (dark, dense, data-first, retro-Mac-OS-9 + cyberpunk-HUD + brutalist composite, every pixel earns its keep, display not state), take it further. Don't mimic the finished HTMLs — out-execute them.

The oceanic resource pool (62 palettes, 20 style systems, 10 identity rows, 1,400+ inline SVG icons, 157 historical UI references, 445 aesthetic references, 184 LS Graphics assets, 1,362 unDraw + Humaaans + Open Peeps illustrations, 40 tileable patterns, 288 authored pro-icons, Untitled UI Pro + Tailwind UI + Catalyst + Aceternity Pro component primitives) exists so you have breadth, not so you must use everything. Pick what serves the vision. Reject what doesn't.

**Do-Not list (recurrence guards): follow dogmatically.**
**Aesthetic direction (positive spec): use as floor, build higher.**

## What Clawmachine is

Clawmachine is a macOS SwiftUI desktop application for second-hand tech-electronics arbitrage in the UK. A scout scrapes UK marketplaces for candidate listings, a brain evaluates each candidate against a live floor-price aggregate plus eBay sold comps, and the operator buys, fixes, and resells. Dark, dense, data-first. Not consumer-facing. Not a team tool. Not SaaS. Internal tooling for one operator running a fix-and-flip tech business.

## Who the operator is

Regan — solo UK reseller, ten-hour days at a single dense terminal. Fix-and-flip tech electronics (phones, laptops, console hardware, accessories). Desktop-only workflow. Has cycled through nine-plus prior iterations of this tool; current shipped build is visually dead — grey-box shell with mock rows. The directive is: every pixel earns its keep; display not state; no placeholders, no narration, no gamification. Treat every iteration that bled developer voice into the UI as a regression to avoid.

## Read these first, in this order

1. `CLAWMACHINE-INGEST-MAP.html` — **the 1-pager cover page**. Read this first. Points you at the codex labs as aesthetic ground-truth and at the finished 7-page example. All navigation elsewhere starts here.
2. `local/chromatic/clawmachine-chromatic-lab.html` — **canonical aesthetic reference**. 62 complete colour systems the operator authored. Density, card grammar, type ramp, motion — this is the vocabulary to derive from, not compete with.
3. `local/chromatic/clawmachine-style-lab.html` — **canonical aesthetic reference**. 20 radically different UI style systems rendered as real components. Reference for component grammar.
4. `CLAWMACHINE-PAGES.html` — the 7 app pages (Dashboard / Inventory / Analytics / Brain / Mesh / AgentConsole / Settings) rendered in the codex-lab vocabulary, scheme switcher across 7 palettes (02/07/18/25/38/46/52), pixelarticons inline, trading-terminal Analytics chart.
5. `CHEAT-SHEET.md` — the distilled directive. Compact operator doctrine.
6. `brief/any-other-notes.txt` — operator directive as structured bullets (GOAL / AUDIENCE / LAYOUT / DO NOT / DO / CONTENT / DELIVERABLES / VOICE).
7. `brief/company-blurb.txt` — one-paragraph what-is-clawmachine (the company-blurb field paste).
8. `.triage/chromatic-schemes.json` — 62 operator-authored palettes, source of truth. Each entry carries `void`, `p`, `s`, and `pg.{dashboard,inventory,analytics,brain,mesh,onboarding,settings}`.

Everything else in the repo is reference, token confirmation, or asset pool. These seven are the canon.

## Primary signal ranking

When sources conflict, higher wins:

1. **Swift code** in `local/swift-reference/` and `direct-drag/tokens/swift-reference/` (`Colors.swift`, `Typography.swift`, `Spacing.swift`, `Bevel.swift`, `SidebarIcons.swift`). This is what the app actually compiles against.
2. **Finished-page HTML** at the feed root — the three files above. They render the tokens into real screens with real data shapes.
3. **Token JSON** in `direct-drag/tokens/` — `chromatic-schemes.json`, `style-systems.json`, `identity-systems.json`, `layer-registry.json`.
4. **`.fig` source** — blocked at time of writing; add when available.

Prefer code over token JSON. Prefer finished HTML over isolated component examples. Never infer intent from the `external/` reference libraries — they are training-equivalent noise for Claude Design.

## Aesthetic doctrine

Composite of three idioms — ship all three in the same frame:

1. **Retro Mac OS 9 / System 7** — beveled chrome, platinum 3D edges, 16x16 pixel icons, Chicago/Silkscreen bitmap display type for wordmarks and ornament.
2. **Cyberpunk HUD** — saturated accent-on-dark, scanline-adjacent density, terminal-style readouts, live counters and tickers.
3. **Brutalist web** — thick borders, honest corners, tabular numerics, no ornament for its own sake.

Reference anchors: Bloomberg Terminal, Pro Tools, Fallout Pip-Boy, Susan Kare Chicago, Neobrutalism.dev — rendered in operator-authored palettes.

**Hard rules:**

- No translucency, blur, backdrop-filter, or opacity-based fills. Apple liquid-glass is explicitly the antithesis.
- Corner radius at most 4px everywhere.
- Spacing from `{4, 8, 12, 16, 24, 32}` only.
- Beveled borders: highlight top-left, shadow bottom-right. Solid colours, not gradients. Inputs reverse the bevel (shadow top-left, highlight bottom-right) to read as inset.
- Satoshi (bold, lowercase) for the wordmark and display. JetBrains Mono for every numeric, table cell, and data readout. IBM Plex Sans for body prose.
- Labels are ALL CAPS or lowercase. Never Title Case.
- Motion is curve-and-bounce: `cubic-bezier(0.34, 1.56, 0.64, 1)` (easeOutBack). Transitions at most 300ms. Ambient loops at most 2s. Animation carries signal (scanning pulse, live counter, log tick) — decoration without signal is out.

## Do not

- Translucency, blur, backdrop-filter, glass, frost.
- Gradients beyond a beveled edge.
- SF Symbols.
- Title Case anywhere.
- Gamification vocabulary: WIN RATE, streaks, achievements, leaderboards, XP, badges, level-ups.
- Developer-voice UI copy (`The user should...`, `In this view we...`, `no fake success here`). Address the user, plainly.
- AI-generated illustration filler. Generative-image residue from prior iterations.
- `TARGET PLATFORM` column on deal rows. Resale default is eBay; do not make the user click it each row.
- Default-visible dismissed rows. Default-visible negative-profit rows.
- Matter font. Any font from `~/Projects/style-lab/` that did not make the OFL shortlist.
- Selling to CeX. Selling to BS Exchange. Both are buy-sources only, floor-aggregate inputs; never sell-targets.
- Dead UK vendors: Decluttr, Mazuma — do not reference.
- Contextless plaintext listings. Deal rows without images. Buttons that do nothing.
- Narration panels, hero empty states, onboarding essays, `WHY THIS EXISTS` copy blocks.
- Hero mascots, cartoon claws, logo in places a wordmark suffices (logo slot is deferred).

## Do

- Dark, dense, data-first foundation. Per-scheme accent ramps per page — the active scheme's `pg.dashboard`, `pg.inventory`, `pg.analytics`, `pg.brain`, `pg.mesh`, `pg.onboarding`, `pg.settings` each drive one page.
- Beveled borders, thick honest corners, tabular numerics.
- Satoshi + JetBrains Mono + IBM Plex Sans. Nothing else.
- 16x16 pixel bitmap icons for the sidebar nav (see `SidebarIcons.swift`). Hand-authored SVG elsewhere.
- Deal rows with image, vendor badge, floor price, eBay-sold-median, ROI pill, clickthrough arrow to source listing.
- Inventory rows with image, condition grade, acquired price, live comp price.
- Six UK vendor badges — each with a distinct accent from the active scheme: `ebay`, `cex`, `gumtree`, `facebook`, `shpock`, `preloved`, `wholesale-clearance`.
- Splash / loading treatment as the one sanctioned moment of activity visualisation (operator-endorsed).
- Two or three variations per page for review. Prefer finished screens over style-guide pages.
- Plain-English direct labels. No preambles.

## Seven-page app structure

1. **Dashboard** — live deal feed (table of source listings), KPI stat cards without win-rate, status strip across the top.
2. **Inventory** — acquired-item grid with image, condition grade (MINT / EXCELLENT / GOOD / FAIR), target sell price, live comp.
3. **Analytics** — counts, profit, ROI trend, worst-performers section with dismissed rows hidden by default (opt-in toggle).
4. **Brain** — chat transcript with the operator plus live recommendations column. Model `<think>` tags never render.
5. **Mesh** — three machine cards (MacBook / Studio / Pi), interleaved log stream, latency sparkline.
6. **AgentConsole** — tool list, call-trace viewer. First-class nav page, not a chat overlay.
7. **Settings** — appearance (62-palette selector with hover-preview), channels config (BlueBubbles / Studio / Pi), brain model config.

Finished-page examples for all seven are in `CLAWMACHINE-PAGES.html` at the feed root. The 1-pager ingest cover is `CLAWMACHINE-INGEST-MAP.html`.

## Data shapes

- **Deal row** (Dashboard): thumbnail image, vendor badge (one of the six), floor-aggregate price, eBay sold-median, ROI pill (color-coded), clickthrough arrow to the original source listing URL. No TARGET column. No BUY button unless it is wired.
- **Inventory row**: thumbnail image, item label, condition grade, acquired price (GBP), live comp price (GBP), delta pill.
- **KPI stat card**: label ALL CAPS, big number in JetBrains Mono, small delta or sparkline underneath. No win-rate card. No streaks.
- **Analytics trend**: counts and profit over time, ROI curve, worst-performers table (dismissed hidden by default).
- **Brain transcript**: operator message + response, recommendations column alongside, no internal reasoning tokens ever visible.
- **Mesh log line**: timestamp, node role (brain / scout / app), event, latency. Machine-name (Studio / Pi / MacBook) allowed in hardware-spec cards only.
- **Scout feed**: raw listing events as they stream off the Pi scout.

Node naming convention: role (brain / scout / app) everywhere as primary identity. Hardware names (MacBook / Mac Studio / Raspberry Pi) appear only in technical hardware-spec and SSH-diagnostic contexts.

## UK vendor scope

Tech electronics only. Clothing, books, software — out.

- `ebay` — source listings, sold-comps aggregate, sell venue. Primary.
- `cex` — buy-source only. Never a sell-target. Floor-aggregate input.
- `gumtree` — source listings.
- `facebook` — Facebook Marketplace source listings (UK).
- `shpock` — source listings.
- `preloved` — source listings.
- `wholesale-clearance` — pallet-buy source.
- `musicmagpie` — live, source/comp input.
- `bs-exchange` (`webse.co.uk`) — buy-side only.

Dead or out-of-scope: Decluttr, Mazuma — do not surface as badges or sell-targets.

Console hardware in; console games out.

## Repository layout

- **Feed root** — `CLAWMACHINE-INGEST-MAP.html` (the 1-pager cover), `CLAWMACHINE-PAGES.html` (the 7-page finished example), `CHEAT-SHEET.md`, this file, `README.md`. The ingest canon.
- **`brief/`** — `company-blurb.txt` (Claude Design "Company name and blurb" paste), `any-other-notes.txt` (Claude Design "Any other notes" paste). Short, operator-voice, authoritative.
- **`direct-drag/`** — the curated asset subset for the Claude Design "Fonts, logos and assets" drag field. Contains `html/` (the three finished HTMLs), `brief/`, `codex/` (chromatic-lab + style-lab HTML reference), `tokens/` (JSON + Swift), `fonts/` (OFL families), `icons/` (pixelarticons + Kare classic Mac), `historical-ui/` (Mac OS 9, Bloomberg Terminal, Pip-Boy, Susan Kare, CLI tools, Dead Space HUD reference).
- **`local/`** — working material. `swift-reference/` carries the canonical Swift token files. `chromatic/` carries the codex HTML labs. `figma-extracted/`, `palettes/`, `decorative/`, `templates/` are extraction workspaces; `current-app-screenshots/` shows the grey-box before-state (do not match).
- **`external/`** — 2+ GB of third-party component libraries, icon packs, font families, retro CSS frameworks, aesthetic references. Claude Design already knows shadcn, Tailwind, Material Symbols, Lucide, Phosphor, and similar — this directory is reference material for the Opus subagents working on the feed, not for ingest. Ignore wholesale.
- **`authored/`** — subagent output during this session (figma schema probes, Tailwind+Catalyst recreations, pro-icon synthesis, pattern extraction). Treat as draft, not spec.

## Handoff to Claude Code

When a design is ready, the handoff bundle targets Swift 6.3, Foundation and SwiftUI only. No AppKit. No SF Symbols. No UIKit bridges. Tokens arrive as Swift source matching the grammar in `local/swift-reference/` — `PageAccent`, `TextColor`, `Surface`, `Brand`, `Status`, `PlatformColor`, `PageTheme` per-page. Typography is `Typo` enum with Satoshi + JetBrains Mono + IBM Plex Sans. Spacing is the `{4, 8, 12, 16, 24, 32}` scale. Bevel is the highlight-TL + shadow-BR modifier. Icons are `UInt16` bitmap masks at 16x16 or hand-authored SVG.

Prefer Claude-Code handoff bundles over design-only deliverables. Two or three variations per page is the deliverable unit.
