# Clawmachine — operator design brief

Primary source of operator directive for Claude Design. Read this to understand what the operator actually wants, in their own voice.

## Opening — operator voice

> Clawmachine is a macOS SwiftUI desktop app for second-hand tech-electronics arbitrage in the UK. I am one person running a fix-and-flip tech business — phones, laptops, console hardware, accessories — at a dense terminal for ten hours a day. The app scouts UK marketplaces for candidate listings, evaluates them against a live floor-price aggregate plus eBay sold comps, and I buy, fix, sell. That is the whole job.
>
> I have cycled through nine-plus prior iterations of this tool. The current shipped build is a visually dead grey box with mock rows. Months of iteration, months of regression caused by scaffolding — plan docs, roadmaps, session retros, doctrine files — ate the product. I cut eighty percent of that scaffolding on 2026-04-19. The app remains broken.
>
> I need this to work. Every pixel earns its keep. Display, not state. Do not narrate the architecture at me. Do not bleed developer voice into UI copy. Do not hand me a plaintext listing without context. A deal row that does not click through to its source is not a deal row. A button that does not work gets deleted, not left to rot. I am not a consumer and this is not a SaaS; I am the one user, writing this brief to you now, and I want a dense data terminal in an aesthetic I can actually stand to look at for ten hours.

## What survived the review

Features, screens, and flows that are keepable going forward:

- **Dashboard deal feed** — table shape keeps. Add images, vendor badge, floor price, eBay sold-median, ROI pill, clickthrough arrow to source listing. Drop `TARGET` column; resale default is eBay.
- **Dashboard KPI stat cards** — shape keeps. Per-page accent from active palette. Drop WIN RATE.
- **Inventory grid** — acquired-item grid with image, condition grade (MINT / EXCELLENT / GOOD / FAIR), target sell price, live comp.
- **Analytics trend** — counts, profit, ROI trend, worst-performers section (dismissed hidden by default, opt-in toggle).
- **Brain transcript + recommendations** — chat with the operator plus a live recommendations column. Internal `<think>` tokens never render.
- **Mesh machine cards + log** — three cards (MacBook / Studio / Pi), interleaved log stream, latency sparkline, bounded scroll.
- **Scout feed** — raw listing events streaming off the Pi scout.
- **Splash / loading treatment** — operator verbatim positive: "at least gives the singular instance of activity visually, even if it is a facade". Keep and extend.
- **Wordmark treatment** — lowercase `claw` and `machine` in two different colours. Exact hues open. Page-shift hypothesis worth testing (colour shift per active page).
- **Information-density patterns** from the Electron-era frontendclaw iteration: sparklines inside metric cards, source-performance gradient bars, trending-category pills with percent delta, today's-briefing panel. Visual idiom adoptable; their mascot and gamification skin rejected.

## What gets torched

- Gamification vocabulary in every form: WIN RATE card, achievements, streaks, XP, level-ups, badges, leaderboards.
- Title Case headings anywhere. CAPS or lowercase only.
- Gradients beyond a beveled edge.
- Translucency, blur, backdrop-filter, opacity-based fills. Apple liquid-glass aesthetic is the explicit antithesis.
- Generative-AI filler images. Static image boxes pasted in as decoration. Operator verbatim on prior iterations: "just paste random images in there which were ai slop, sometimes stylistically nice but had no cohesion whatsoever with the application. just static image boxes pasted in there. looked stupid as fuck."
- SF Symbols. Generic placeholder icons.
- Matter font. Fonts from the style-lab scrape folder.
- Developer-voice UI copy: `The user should...`, `In this view we...`, `no fake success here`, `the live session dropped. the app is retrying without switching to fake data`.
- Narration panels: `WHY THIS EXISTS`, `GOOD STATE`, `DON'T MOVE ON IF`. Seven-step setup wizards with in-joke step names.
- Float-in-empty-dark-field layouts. Infinite-scroll logs with chat bleeding in.
- Non-functional buttons. Placeholder action items.
- `TARGET PLATFORM` column on deal rows.
- Default-visible dismissed rows. Default-visible negative-profit rows.
- `unknown` platform in the legend. Greyed-out non-live sources.
- Selling to CeX. Selling to BS Exchange. (Buy-sources only.)
- Decluttr, Mazuma (dead UK vendors).

## Operator non-negotiables

Quoted or paraphrased verbatim from the operator record:

- Every pixel earns its keep.
- Display, not state.
- No directive bleed into UI text — address the user, not the agent.
- No contextless plaintext listings — deal rows have images, vendor badge, floor, sold-median, ROI pill, clickthrough.
- Deal rows click through to the original source listing URL.
- Every control works or is removed; no placeholders.
- Operator-authored palettes only — the 62 schemes in `chromatic-schemes.json`. No hand-rolled hex stacks.
- "Somewhere between 1 and 2 but not animation for the sake of animation" — on motion budget.
- Setup exists to remove burden, not narrate architecture. At most three steps.
- Role naming (brain / scout / app) as primary identity. Hardware names only in technical hardware-spec contexts.
- AgentConsole is a first-class nav page, not a chat overlay.
- Chat is not a system log — separate concerns, bound the scroll.

## The palette system

Source: `direct-drag/tokens/chromatic-schemes.json` — 62 operator-authored schemes from `clawmachine-codex/chromatic-lab.html`. Each entry carries `void` (page background), `p` (primary accent), `s` (secondary accent), and `pg.{dashboard, inventory, analytics, brain, mesh, onboarding, settings}` — a per-page accent baked into every scheme.

**Operator-shortlisted 38 palettes** (32 dark + 6 light):

`01 solar flare, 02 deep current, 04 terracotta grid, 06 kanji electric, 07 concrete bloom, 08 velvet terminal, 09 tekki shock, 10 burnt circuit, 11 arctic pulse, 12 chromatic forge, 14 ultraviolet haze, 15 electric bubblegum, 16 toxic line, 17 sunset boulevard, 18 plasma field, 19 viva vegas, 20 roller disco, 21 hong kong neon, 23 hey mr dj, 25 midnight dream, 26 neon citrus, 27 electric dreams, 28 neon jungle, 29 retro future, 30 cosmic violet, 33 sakura circuit, 35 cobalt rush, 36 firecracker, 37 synth wave, 38 alpine glow, 39 deep ocean, 40 desert storm, 46 coral reef, 51 aurora borealis, 52 rust oxide, 53 neon mint, 55 vapor trail, 57 jade emperor, 58 neon orchid.`

**Default scheme for new installs: #02 DEEP CURRENT** — dark oceanic, void `#060B10`, primary `#00E5A0`. All finished-page HTML examples render in this scheme.

**Selection model** — operator directive: "fuck it lets just ship all the pallettes as themes you can select during setup via dropdown, hover activates it for preview a la vscode / cursor / antigravity." Ship the shortlisted palettes as runtime-selectable themes. Selection in the setup wizard via dropdown. Hover triggers live preview of the whole app. Selection locks in. Changeable later in Settings — theme is not a setup-only decision. Light vs dark is inferred from the chosen scheme's `type` field, not a separate toggle.

**Per-page accent map** (default scheme #02, from the active scheme's `pg.*`):

- Dashboard -> `pg.dashboard` (`#00E5A0` in DEEP CURRENT).
- Inventory -> `pg.inventory`.
- Analytics -> `pg.analytics`.
- Brain -> `pg.brain`.
- Mesh -> `pg.mesh`.
- AgentConsole -> `pg.settings` (shares with Settings; may promote to its own `agentConsole` slot at implementation time).
- Settings -> `pg.settings`.

Each of the six UK vendor badges also carries its own accent from the active scheme — `ebay`, `cex`, `gumtree`, `facebook`, `shpock`, `preloved`, `wholesale-clearance`.

## Operator correction history

Ten specific mistakes prior iterations made, with the correction:

1. **Static AI-slop images pasted in as decoration.** The AppKit / liquid-glass era iteration did this repeatedly. Correction: no generative-image residue. Every image is a real product thumbnail tied to a real listing event.
2. **Title Case headings.** `Recent Deals`, `Win Rate`, `Target Platform`. Correction: ALL CAPS or lowercase only. Never Title Case anywhere.
3. **Gamification vocabulary.** `WIN RATE`, streaks, achievements, XP. Correction: strip entirely. This is a tool, not a game. Profit and ROI are the only scores.
4. **Developer voice in UI copy.** `The user should...`, `no fake success here`, `the live session dropped. the app is retrying without switching to fake data`. Correction: address the user, plainly. No meta-commentary about the app's own honesty.
5. **Plaintext deal rows with no images, broken buttons.** Current shipped dashboard does this. Correction: deal row carries thumbnail, vendor badge, floor price, eBay sold-median, ROI pill, clickthrough arrow. Buttons work or are removed.
6. **Seven-step setup wizards with in-joke step names and essay panels.** `brain / lobster / llama / pi / scout / proxy / first scan`, each with `WHY THIS EXISTS` / `GOOD STATE` / `DON'T MOVE ON IF`. Correction: at most three steps, plain language, the app does the work silently.
7. **`TARGET PLATFORM` column on deal rows.** The operator resells on eBay; restating it on every row is directive noise. Correction: default resale is eBay, drop the column entirely.
8. **Default-visible dismissed and negative-profit rows.** Noise without signal. Correction: hidden by default, opt-in toggle to view history.
9. **Mixed node naming.** `Studio.lan` / `clawmachine` / `raspberry-scout` as three conventions in one view. Correction: role (brain / scout / app) as primary identity everywhere; hardware names only in technical hardware-spec contexts.
10. **Chat bleeding into system logs.** Infinite-scroll mesh log with LLM chat lines interleaved. Correction: chat is not a system log. Separate concerns. Bound the scroll on both.

Additional anti-patterns to avoid, from the same correction record: float-in-empty-dark-field layouts (panels need bounded layouts), non-functional DETAILS / action buttons, `unknown` platform in the legend, the cartoon claw-machine-and-lobster mascot treated as final art (placeholder only; logo slot deferred), and any fontface from `~/Projects/style-lab/` that did not make the OFL shortlist.

## Fair use and non-commercial framing

This is internal tooling for a single UK-based operator running a fix-and-flip tech-electronics business. The application is not distributed publicly, is not sold or licensed to others, is not deployed to a team, and is not a SaaS. No third-party users. No commercial reseller relationship with any of the UK marketplaces the scout reads from. UK marketplace scraping ethics is a settled matter for the operator and is not re-opened in this brief.

The Claude Design ingest — fonts, icons, retro CSS references, aesthetic anchors, token JSON — draws from operator-authored artefacts plus OFL or MIT-licensed third-party reference material collated for internal design use. The handoff target is a single SwiftUI desktop build running on the operator's machines.
