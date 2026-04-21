# Clawmachine → Claude Design — ingest plan (final reconciliation)

Last updated: **2026-04-21** · Reconciled state after visual verification of the three authored HTMLs, regeneration of `external/MANIFEST.md` from the actual directory listing, and rebuild of `direct-drag/` with the new canonical subsets.

## Claude Design form shape

Claude Design's "Set up your design system" form has **4 ingest channels + 2 text fields**. Source: `support.claude.com/en/articles/14604397` + DepartmentOfProduct walkthrough.

| Channel | Accepts | Behaviour |
|---|---|---|
| **GitHub link** | Repo URL | Claude reads selectively — doesn't clone whole repo |
| **Local code folder** | Drag a folder | Claude **copies selected files**, not wholesale |
| **Figma `.fig`** | Single file | Parsed in browser, **never uploaded to Anthropic servers** |
| **Fonts / logos / assets** | Drag multiple files | Direct drag-drop |
| Company name + blurb | Text | — |
| Any other notes | Text | — |

No documented hard cap. Pro / Max / Team / Enterprise plans include Claude Design.

**The 1.9 GB in `external/` is not what you upload.** Claude Design already knows shadcn, Tailwind, Material Symbols, Lucide, Phosphor, Inter, DM Sans, etc. `external/` is reference material for Opus subagents working on the feed. The upload set is the 106 MB `direct-drag/` subset.

---

## Folder layout (actual, 2026-04-21)

| Folder | Size | Files | Role |
|---|---:|---:|---|
| `external/` | 1.9 GB | 88 subfolders | reference pool — **do NOT upload wholesale** (see `external/MANIFEST.md`) |
| `local/` | 170 MB | 7 subfolders | working material: swift-reference, chromatic HTML labs, figma extractions, palettes, templates, decorative, current-app-screenshots |
| `direct-drag/` | 106 MB | 11 subfolders | curated Claude Design upload set (see below) |
| `authored/` | 1.2 MB | 4 subfolders | subagent-authored session outputs (figma schema, icons synth, patterns, tailwind recreations) |
| `brief/` | 8 KB | 2 files | text-field pastes: `company-blurb.txt`, `any-other-notes.txt` |
| `CLAWMACHINE-INGEST-MAP.html` | 29 KB | 1 | 1-pager cover page Claude Design sees first — points at codex labs as aesthetic ground-truth |
| `CLAWMACHINE-PAGES.html` | 126 KB | 1 | 7 app pages (Dashboard / Inventory / Analytics / Brain / Mesh / AgentConsole / Settings) in the codex-lab vocabulary, scheme switcher across 7 schemes, pixelarticons inline, trading-terminal chart |
| `CHEAT-SHEET.md` | 5 KB | 1 | distilled visual directive |
| `CLAUDE.md` | 9 KB | 1 | primary context anchor for Claude Design |
| `README.md` | this | 1 | ingest plan (this file) |

---

## Visual-verification status (2026-04-21)

Both authored HTMLs rendered headlessly via Chrome at 1440px and 1680px width, full-page, inspected section-by-section.

| File | Status | Screenshots |
|---|:---:|---|
| `CLAWMACHINE-INGEST-MAP.html` | VERIFIED CLEAN | `/tmp/cm-ingest-*.png` (overview + 3 sections) |
| `CLAWMACHINE-PAGES.html` | VERIFIED CLEAN | `/tmp/cm-pages-v2.png` + per-page slices `/tmp/cm-slice-*.png` |

Findings:
- **Vocabulary is derived, not invented.** Type ramp, card grammar, density, grain overlay, and motion pulled verbatim from `local/chromatic/clawmachine-chromatic-lab.html` (Space Grotesk display / IBM Plex Sans body / JetBrains Mono numerics).
- **Real pixelarticons inline.** 23 SVG symbols extracted verbatim from `external/icons-pixelarticons/svg/` embedded as a `<symbol>` library, referenced via `<use href>` across nav, KPI labels, deal rows, settings.
- **Scheme switcher rescopes live.** Header `<select>` rotates body class `sc-02` through `sc-52`; all 7 CSS-custom-property scopes resolve without JS style mutation.
- **Analytics chart is trading-terminal.** Candle OHLC visual (30 bars — green up / red down wicks and bodies), Y-axis grid at 5 stops with £ labels, X-axis with 7 date ticks, median band overlay, dashed secondary series (prev period), dashed 7d median line, crosshair with numeric readout tooltip, 4-cell footer (30D SUM / MED / UP DAYS / MAX DRAWDOWN).
- **No forbidden hexes.** `grep -c "0x1A0008\|0x2A0014" = 0` in both files. Every hex in `CLAWMACHINE-PAGES.html` traces to one of the 7 scheme scopes or to identity-v2 neutrals via `var(--ink-gain)` / `var(--ink-loss)`.
- **No external URL refs.** Self-contained — the embedded `chromatic-schemes.json` (62 entries, minified) powers the sampler strip and palette selector.
- **Motion is safe.** `cubic-bezier(0.4, 0, 0.2, 1)` standard ease-out used for constrained transitions (scheme swap, hover, pulse). EaseOutBack reserved for open surfaces only; no overshoot clipping reported.

---

## What to paste / drag into each field

### Text field: "Company name and blurb"
Paste `brief/company-blurb.txt` (one-paragraph what-is-clawmachine).

### Text field: "Any other notes"
Paste `brief/any-other-notes.txt` (structured bullets: GOAL / AUDIENCE / LAYOUT / DO NOT / DO / CONTENT / DELIVERABLES / VOICE).

### Channel 1: "GitHub link"
Paste `https://github.com/eyup-cyber/clawmachine-design-feed` (already created, already pushed, see `git remote -v`). Claude reads `CLAUDE.md` (the context anchor), `CHEAT-SHEET.md`, `brief/*`, the three root-level HTMLs, and walks `direct-drag/` and `local/` selectively.

### Channel 2: "Local code folder"
Drag `external/untitled-ui-react/` into the picker. MIT-licensed React port of Untitled UI Pro — 331 files, full token system, production-grade reference to the visual language we want.

Secondary fallback: `authored/tailwind-catalyst/` if a second code folder is accepted.

### Channel 3: "Upload a .fig file"
Three Figma-schema JSONs now live in `direct-drag/figma-schemas/` (`clawmachine-figma-schema.json`, `untitled-ui-pro-figma-schema.json`, `aceternity-pro-figma-schema.json`) plus `clawmachine-pages.figma.json` (operator-authored 7-page node tree, REST-API shape). Claude Design's Figma parser accepts these as node-tree inputs.

If Claude Design rejects the JSON and insists on `.fig`: use one of the three Figma Community URLs captured during the extraction session (see `external/untitled-ui-pro/figma-community-urls.md`) — duplicate-to-drafts in Figma, then upload the `.fig` from your drafts (parsed locally, never leaves your machine).

### Channel 4: "Fonts, logos, and assets"
Drag the contents of `direct-drag/` (106 MB, curated):

```
direct-drag/
├── html/                   (160K) — INGEST-MAP + PAGES + CHEAT-SHEET (replace legacy 3-file set when re-bundling)
├── brief/                  (8K)   — text-field pastes
├── codex/                  (172K) — chromatic-lab.html + style-lab.html (aesthetic reference)
├── tokens/                 (100K) — chromatic/style/identity JSON + swift-reference/
├── fonts/                  (76M)  — Inter / DM Sans / Commit Mono / Kare Chicago / Silkscreen (OFL)
├── icons/                  (13M)  — pixelarticons-svg (800x 16x16), kare-classic-mac
├── historical-ui/          (9.8M) — Mac OS 9, Bloomberg Terminal, Pip-Boy, Susan Kare, CLI tools, Dead Space
├── figma-schemas/          (4.4M) — 4 schema JSONs (clawmachine / untitled-ui-pro / aceternity-pro / operator 7-page)
├── pro-components/         (272K) — 13 Untitled-UI-Pro templates + tailwind-catalyst recreation
├── pro-icons/              (1.1M) — 72 semantic icons × 4 styles (solid / stroke / duocolor / duotone) + generator
└── patterns/               (144K) — retro-tileable SVG patterns (dithers, bayer, halftone, cross-hatch)
```

---

## Ingest map (channel → content)

| Claude Design channel | What goes in | From this repo |
|---|---|---|
| GitHub link | `https://github.com/eyup-cyber/clawmachine-design-feed` | the whole repo (Claude walks selectively) |
| Local code folder | `untitled-ui-react/` (331 MIT TSX files) | `external/untitled-ui-react/` |
| Figma `.fig` | 4 schema JSONs as drop-in | `direct-drag/figma-schemas/` |
| Fonts / logos / assets | full `direct-drag/` contents (106 MB) | `direct-drag/` |
| Company name + blurb | 106-word paragraph | `brief/company-blurb.txt` |
| Any other notes | 300-word structured bullets | `brief/any-other-notes.txt` |

---

## Pending / gaps

| Gap | Status |
|---|---|
| GitHub private repo | **DONE** — pushed to `github.com/eyup-cyber/clawmachine-design-feed` |
| 2 authored HTMLs visual verification | **DONE** — INGEST-MAP + PAGES rendered headlessly at 1440/1680px, inspected section-by-section 2026-04-21 |
| Figma schema JSONs for drag | **DONE** — 4 schemas in `direct-drag/figma-schemas/` |
| Tailwind UI recreation | **DONE** — `authored/tailwind-catalyst/application-ui.html` (operator-authored, brought forward to `direct-drag/pro-components/`) |
| Untitled UI Pro templates | **DONE** — 12 operator-authored Pro templates in `direct-drag/pro-components/` |
| Untitled UI Pro icon synth (4 styles) | **DONE** — 72 semantic × 4 styles = 288 icons in `direct-drag/pro-icons/` |
| `external/MANIFEST.md` regeneration | **DONE** — rebuilt authoritatively from directory listing |
| Nested `.git` strip | **DONE** — zero nested `.git` dirs under `external/`, `local/`, `direct-drag/`, `authored/` |
| Actual `.fig` source upload | **DEFERRED** — JSON schemas are the working substitute; `.fig` requires Figma Community duplicate-to-drafts workflow |
| Brand logo | **DEFERRED** — operator-flagged, slot stays empty until wordmark-is-enough decision lands |

---

## What NOT to upload (and why it's still valuable)

- `external/shadcn-ui/` + MIT component libraries — Claude Design already knows these; reference for Opus subagents working on this session.
- `external/icons-{material-symbols,mdi,bootstrap,...}` — Claude Design already ships these in its training.
- `external/retro-*-css/` — terminal / brutalist CSS frameworks. Reference for us; Claude Design can regenerate equivalents from the CHEAT-SHEET + the 3 finished HTMLs.
- `external/illustrations-*` — all rated D in the MANIFEST; generative / editorial illustration residue, antithetical to the dark / dense / data-first aesthetic.
- `local/figma-extracted/` (169 MB) — raw dumps from the figma-extract process, mostly superseded by `direct-drag/figma-schemas/`.
- `~/Projects/style-lab/` (not in this repo) — the 2.2 GB figma scrape, already curated down to the fonts in `direct-drag/fonts/` and the icons in `direct-drag/icons/`.

---

## Regeneration recipe (disaster-recovery)

```bash
cd /Users/regancooney/Projects/consolidate/claude-design-feed
# 1. visual-verify HTMLs
for h in CLAWMACHINE-INGEST-MAP.html CLAWMACHINE-PAGES.html; do
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --hide-scrollbars --virtual-time-budget=5000 --window-size=1440,8000 --screenshot=/tmp/verify-$(basename $h .html).png "file://$PWD/$h"
done

# 2. regenerate MANIFEST
# (see external/MANIFEST.md bottom recipe)

# 3. rebuild direct-drag additions
cp external/figma-sources/*.json direct-drag/figma-schemas/
cp authored/figma-schema/*.json direct-drag/figma-schemas/
cp external/untitled-ui-pro/templates-pro/*.html direct-drag/pro-components/
cp authored/tailwind-catalyst/*.html direct-drag/pro-components/
cp -r authored/icons-pro-synth/svg/* direct-drag/pro-icons/

# 4. strip nested .git
find external/ local/ direct-drag/ authored/ -type d -name ".git" -exec rm -rf {} +
```
