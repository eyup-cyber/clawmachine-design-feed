# Clawmachine → Claude Design — ingest plan (the real one)

Claude Design's "Set up your design system" form has **4 ingest channels + 2 text fields**. Source: `support.claude.com/en/articles/14604397` + DepartmentOfProduct walkthrough.

| Channel | Accepts | Behaviour |
|---|---|---|
| **GitHub link** | Repo URL | Claude reads selectively — doesn't clone whole repo |
| **Local code folder** | Drag a folder | Claude **copies selected files**, not wholesale |
| **Figma `.fig`** | Single file | Parsed in browser, **never uploaded to Anthropic servers** |
| **Fonts/logos/assets** | Drag multiple files | Direct drag-drop |
| Company name + blurb | Text | — |
| Any other notes | Text | — |

No documented hard cap. Pro/Max/Team/Enterprise plans include Claude Design.

**The 2.5GB this folder contains is not what you upload.** The bulk of `external/` is agent-reference gathered during this session — Claude Design already knows what shadcn, Tailwind, Material Symbols look like. Uploading it would be noise.

---

## What to paste / drag into each field

### "Company name and blurb"
Paste `brief/company-blurb.txt` (106 words).

### "Any other notes"
Paste `brief/any-other-notes.txt` (300 words, structured bullets).

### "GitHub link"
**(To be set up.)** The operator-authored artefacts — HTMLs, brief, CHEAT-SHEET, swift-reference, triage JSONs — total ~10MB. These should live in a small private GitHub repo so Claude can read the design tokens + finished-page examples as source code rather than as drag-upload. Create with:

```bash
cd /Users/regancooney/Projects/consolidate/claude-design-feed
git init
git add README.md CHEAT-SHEET.md \
  CLAWMACHINE-DESIGN-SYSTEM.html \
  CLAWMACHINE-DASHBOARD-38-VARIANTS.html \
  CLAWMACHINE-PAGES-BRAIN-MESH-AGENT-SETTINGS.html \
  brief/ \
  local/chromatic/ \
  local/swift-reference/ \
  local/layer-registry.json \
  direct-drag/
git commit -m "clawmachine design feed — authored artefacts"
gh repo create clawmachine-design-feed --private --source=. --push
```

Then paste the returned URL into Claude Design's "GitHub link" field.

### "Local code folder"
Drag `external/untitled-ui-pro/raw/untitled-ui-react/` into the picker. 297 MIT `.tsx` files, full token system, 36 demo stories, April-2025 open-sourced React port of Untitled UI Pro. Closest production-grade reference to the visual language we want.

If Claude Design accepts a second code folder, add `external/aceternity-ui/components/` (106 animated JSX components).

### "Upload a .fig file"
Blocked until the Untitled UI Pro gap-closer agent lands `external/untitled-ui-pro/untitled-ui-pro-figma-schema.json` **OR** a Figma Community duplicate URL. If the agent returns a URL, you manually duplicate-to-drafts in Figma and then upload the `.fig` from your drafts (parsed locally, never leaves your machine).

### "Fonts, logos and assets"
Drag the contents of **`direct-drag/`** (100 MB, curated). Structure:

```
direct-drag/
├── html/                         # the 3 finished-page HTML examples + CHEAT-SHEET
│   ├── CLAWMACHINE-DESIGN-SYSTEM.html        (120 KB — 3 pages + 62-deck + 20-style)
│   ├── CLAWMACHINE-DASHBOARD-38-VARIANTS.html (289 KB — Dashboard × 38 palettes)
│   ├── CLAWMACHINE-PAGES-BRAIN-MESH-AGENT-SETTINGS.html (79 KB — remaining 4 pages)
│   └── CHEAT-SHEET.md            (operator's visual directive distilled)
├── brief/                        # same text as the text-field pastes, handy to have
├── codex/                        # the two codex HTMLs that are the aesthetic reference
│   ├── clawmachine-chromatic-lab.html
│   └── clawmachine-style-lab.html
├── tokens/                       # the palette/style/identity JSON catalogues + Swift tokens
│   ├── chromatic-schemes.json    (62 palettes, source of truth)
│   ├── style-systems.json        (20 style systems)
│   ├── identity-systems.json     (identity foundation)
│   ├── layer-registry.json       (asset-layer taxonomy)
│   └── swift-reference/          (Colors / Typography / Spacing / Bevel / SidebarIcons + README)
├── fonts/                        # the 4 OFL font families we want rendered
│   ├── inter/                    (Inter family, OFL)
│   ├── dm-sans/                  (DM Sans + DM Serif, OFL)
│   ├── commit-mono/              (Commit Mono, OFL)
│   ├── kare-chicago/             (Susan Kare lineage bitmap display)
│   └── silkscreen/               (Google Silkscreen, OFL bitmap)
├── icons/
│   ├── pixelarticons-svg/        (800 retro 16×16 icons — PRIORITY match for our nav grammar)
│   └── kare-classic-mac/         (Classic Mac icon pack)
└── historical-ui/                # S-tier aesthetic reference (from the 20-target deep dive)
    ├── mac-os-9/                 (Finder / Apple Menu / Control Strip / Sherlock)
    ├── bloomberg-terminal/       (trading-terminal density)
    ├── pip-boy/                  (Fallout retro CRT)
    ├── susan-kare/               (original sketchbook + icon lineage)
    ├── cli-tools/                (htop / btop / lazygit / k9s — modern terminal density)
    └── dead-space/               (diegetic HUD)
```

This is the highest-signal-per-byte subset of the 2.5GB haul.

---

## What NOT to upload (and why it's still valuable)

- `external/shadcn-ui/` + other MIT component libraries — Claude Design already knows these; they're reference for OUR subagents during this session.
- `external/icons-{material-symbols,mdi,bootstrap,...}` — Claude Design already has icon sets in its training.
- `external/retro-*-css/` — terminal/brutalist CSS frameworks. Reference for us; Claude Design can regenerate equivalents from our CHEAT-SHEET.
- `external/historical-ui/<bulk>/` — only the S-tier subset is worth drag-upload; the rest is ours.
- `external/ls-graphics/previews/` — raw CDN mockup pulls; too generic.
- `~/Projects/style-lab/` — the 2.2GB figma scrape, already pruned to `local/` content-carrying subdirs.

These remain in place as reference for Opus subagents still running in this session.

---

## Still pending (blockers)

1. **Create the private GitHub repo** — requires `gh` CLI (authenticated as `eyup-cyber`) + operator approval to create under their account. Command above.
2. **Untitled UI Pro gap-closer** — in-flight agent producing `figma-schema.json` + `figma-community-urls.md` + 4800 synthesised icons + 10 more Pro templates. On land, drop the `.fig`-equivalent into the upload field OR use the community URL list.
3. **Tailwind UI + Catalyst** — still running. If it lands with useful recreations, add to `direct-drag/code-reference/` as a third code folder.
4. **Visual verification** of the 38-variant and 4-remaining-pages HTMLs — I've only eyeballed the main one. If a variant renders broken, swap to a better one before Claude Design ingests.

---

## The honest grade

At time of writing this README: **~70% adherence**. The haul + authored artefacts are substantial; the ingest plan is now real; the curated `direct-drag/` exists. Still short on: `.fig` source, GitHub repo push (requires operator approval), Tailwind UI gap, visual verification of two of three HTMLs, figma-extracted shell prune.
