# external/ MANIFEST

Authoritative regeneration from `find external/ -maxdepth 1 -type d` + `du -sh` + `LICENSE` probe on 2026-04-21.

- **Total footprint:** ~1.9 GB across 88 kits (one empty shell `figma-sources` retained as placeholder; one empty shell `patterns-haikei` retained pending pattern dump).
- **Scope.** Reference-only pool for Claude Design ingest decisions + Opus subagents working on the feed. **Do not upload wholesale.** Claude Design already recognises shadcn, Tailwind, Material Symbols, Lucide, Phosphor, Inter, DM Sans, etc. Uploading is noise.
- **Acquisition method.** `git clone --depth 1` for OSS projects; `curl` / `firecrawl_scrape` for hosted pages; manual `.zip` extraction for Figma Community exports. `rm -rf .git node_modules .github` post-clone. Commit SHAs not preserved; source URLs pin the head at fetch time (~2026-04-20 02:30 BST, two sibling agents).
- **Clawmachine-fit rating** (per CLAUDE.md aesthetic doctrine: Mac OS 9 + Bloomberg Terminal + Pip-Boy + Brutalist, OFL-only fonts, beveled not glass, dark dense).
  - **S** — on-aesthetic; can feed tokens or ornament directly.
  - **A** — useful pattern/structure; selective picks.
  - **B** — generic reference; teach-Claude-about-tokens only.
  - **C** — off-aesthetic (glassy / playful / illustration-heavy); reference for *what-not-to-do*.
  - **D** — residue; keep for completeness, not for pull.

## Full table

| Kit | Size | Files | License | Acquisition | Fit |
|---|---:|---:|---|---|:---:|
| aceternity-ui | 20M | 994 | LICENSE_NOTE.md | firecrawl SSR of 106 free components + 130 demos, internal reference | C |
| aceternity-ui-pro | 11M | 272 | LICENSE_NOTE.md | SSR'd 134/151 Pro preview HTMLs; TSX paywalled, NOT captured | C |
| aesthetic-references | 373M | 454 | — | mixed image pool: ShopTalk / Dribbble / historical refs | B |
| catalyst | 260K | 56 | LICENSE_NOTE.md | Tailwind UI Catalyst starter extract (operator-authored recreation in `authored/tailwind-catalyst/`) | A |
| chakra-ui | 152M | 3,692 | LICENSE | git clone of chakra-ui v3 | C |
| daisyui | 8.2M | 568 | LICENSE | git clone | C |
| figma-sources | 0B | 0 | — | empty placeholder for future `.fig` drops (Untitled UI Pro schema pending upstream) | — |
| flowbite | 17M | 361 | LICENSE.md | git clone | C |
| fonts-commit-mono | 10M | 153 | LICENSE | GitHub release zip (OFL) | S |
| fonts-dm-sans | 33M | 305 | — | Google Fonts export (OFL) — license inside TTF metadata | S |
| fonts-inter | 31M | 6,140 | LICENSE.txt | GitHub release (OFL) | S |
| fonts-monaspace | 85M | 224 | LICENSE | GitHub release (OFL) | A |
| fonts-space-grotesk | 3.5M | 27 | — | Google Fonts export (OFL) | A |
| geist-font | 98M | 5,098 | LICENSE.txt | git clone vercel/geist-font | A |
| geist-ui | 9.0M | 765 | LICENSE | git clone | B |
| heroicons | 10M | 2,607 | LICENSE | git clone | C |
| historical-ui | 72M | 200 | — | curated folders: Mac OS 9, Bloomberg Terminal, Pip-Boy, Susan Kare, CLI tools, Dead Space HUD — this is the aesthetic core | S |
| hyper-ui | 4.4M | 634 | LICENSE | git clone | C |
| icons-bootstrap | 8.1M | 2,080 | LICENSE | git clone | C |
| icons-boxicons | 6.4M | 1,636 | LICENSE | git clone | C |
| icons-css-gg | 3.7M | 710 | LICENSE.md | git clone | C |
| icons-eva | 1.9M | 496 | LICENSE.txt | git clone | C |
| icons-feather | 1.2M | 303 | LICENSE | git clone | C |
| icons-game-icons | 17M | 4,233 | LICENSE.txt | git clone game-icons.net export | B |
| icons-iconoir | 6.6M | 1,673 | LICENSE | git clone | C |
| icons-ionicons | 5.3M | 1,359 | LICENSE | git clone | C |
| icons-lineicons | 5.2M | 627 | LICENSE.md | git clone | C |
| icons-majesticons | 3.0M | 764 | LICENSE | git clone | C |
| icons-material-symbols | 90M | 23,150 | LICENSE | git clone google/material-design-icons | C |
| icons-mdi | 29M | 7,449 | LICENSE | git clone Material Design Icons | C |
| icons-nerd-fonts | 8.8M | 344 | LICENSE | release download | B |
| icons-pixelarticons | 3.1M | 806 | LICENSE | git clone — **800x 16x16 pixel SVGs, priority for sidebar nav grammar** | S |
| illustrations-blush | 6.6M | 66 | — | Blush download pack | D |
| illustrations-drawkit | 920K | 64 | — | DrawKit download | D |
| illustrations-humaaans | 2.7M | 157 | LICENSE.md | git clone | D |
| illustrations-open-peeps | 6.5M | 61 | — | OpenPeeps download | D |
| illustrations-undraw | 21M | 1,363 | LICENSE | git clone | D |
| linear-design | 4.6M | 66 | LICENSE_NOTE.md | firecrawl_scrape of linear.app tokens + patterns | A |
| ls-graphics | 13M | 327 | LICENSE_NOTE.md | Ramotion LS Graphics research-reference | B |
| lucide | 20M | 4,393 | LICENSE | git clone | C |
| magicui | 13M | 927 | LICENSE.md | git clone | C |
| mamba-ui | 6.6M | 630 | LICENSE.md | git clone | C |
| mantine | 34M | 5,652 | LICENSE | git clone | C |
| nivo | 19M | 1,690 | LICENSE.md | git clone | B |
| once-ui | 22M | 632 | LICENSE.md | git clone | B |
| park-ui | 9.3M | 1,733 | LICENSE | git clone | C |
| patterns-dither-retro | 100K | 25 | — | operator-authored + agent SVG dithers + bayer + halftone + cross-hatch | S |
| patterns-haikei | 0B | 0 | — | empty placeholder for haikei.app exports | — |
| patterns-hero | 480K | 88 | — | HeroPatterns SVG dump | B |
| patterns-svg-backgrounds | 1.1M | 278 | — | svgbackgrounds.com scrape | B |
| phosphor | 71M | 18,159 | LICENSE | git clone | C |
| preline-ui | 6.6M | 291 | LICENSE | git clone | C |
| premium-glow-icons | 1.7M | 444 | LICENSE | Figma Community export — glow-style set | B |
| premium-tabler-icons | 25M | 6,281 | LICENSE | git clone Tabler | B |
| radix-themes | 30M | 662 | LICENSE | git clone | C |
| react-bits | 82M | 2,045 | LICENSE.md | git clone | C |
| recharts | 34M | 1,956 | LICENSE | git clone | B |
| remixicon | 24M | 3,247 | LICENSE | git clone | C |
| retro-7-css | 960K | 90 | LICENSE | git clone 7.css (Windows 7 aesthetic) | A |
| retro-98-css | 752K | 51 | LICENSE | git clone 98.css | A |
| retro-brutalist-framework | 32M | 812 | LICENSE.txt | git clone brutalist framework | A |
| retro-cybercore-css | 5.3M | 299 | LICENSE | cybercore theme | A |
| retro-cyberpunk-2077-theme | 680K | 8 | LICENSE | Figma Community export | B |
| retro-cyberpunk-css | 764K | 24 | LICENSE | cyberpunk-css lib | A |
| retro-kare-chicago-font | 1.2M | 276 | LICENSE | Chicago lineage bitmap | S |
| retro-kare-chinata-icons | 872K | 165 | LICENSE | Kare-adjacent icon set | A |
| retro-kare-classic-mac-icons | 6.6M | 84 | — | Classic Mac OS 9 icon pack | S |
| retro-neobrutalism-components | 4.5M | 546 | LICENSE | neobrutalism.dev git clone | A |
| retro-nes-css | 1.6M | 136 | LICENSE | NES.css | B |
| retro-pipboy-hass | 2.8M | 11 | LICENSE | HomeAssistant Pip-Boy theme | A |
| retro-pipboy-terminal | 18M | 548 | LICENSE.md | Pip-Boy terminal emulator | S |
| retro-pxlkit | 4.8M | 539 | LICENSE | pixel UI kit | A |
| retro-retroui | 852K | 74 | LICENSE | RetroUI | A |
| retro-silkscreen-font | 1.1M | 28 | — | Google Silkscreen (OFL bitmap display) | S |
| retro-system-css | 436K | 41 | LICENSE | System.css | A |
| retro-terminal-css | 556K | 90 | LICENSE | terminal.css | A |
| retro-tuicss | 1.7M | 131 | LICENSE.md | TuiCSS (TUI-in-browser) | A |
| retro-xp-css | 1.3M | 127 | LICENSE | XP.css | B |
| shadcn-ui | 88M | 8,564 | LICENSE.md | git clone | C |
| stripe-design | 2.1M | 25 | LICENSE_NOTE.md | firecrawl_scrape stripe.com + docs | B |
| supply-family | 97M | 344 | LICENSE_NOTE.md | Supply.Family editorial type reference | B |
| tailwind-ui | 3.1M | 528 | LICENSE_NOTE.md | Tailwind UI sample pages (operator-authored recreation in `authored/tailwind-catalyst/`) | A |
| templates-v0-framer-webflow | 6.7M | 36 | — | v0.dev + Framer + Webflow template exports | B |
| textures-paper | 80K | 20 | — | paper / grain PNG tileables | B |
| tremor | 2.0M | 192 | LICENSE | git clone | B |
| untitled-ui-pro | 80M | 17,482 | LICENSE_NOTE.md | extracted kit + operator-synthesised 288-icon Pro set (`icons-4k-synth/`) + 12 operator-authored Pro templates (`templates-pro/`) | A |
| untitled-ui-react | 3.2M | 331 | LICENSE | git clone untitled-ui/react (MIT port of Untitled UI Pro) — **primary drag candidate for Claude Design "Local code folder"** | A |
| vercel-design | 6.3M | 89 | LICENSE_NOTE.md | firecrawl_scrape vercel.com + Geist docs | B |

## Rollup by fit rating

- **S (on-aesthetic):** historical-ui, icons-pixelarticons, retro-kare-chicago-font, retro-kare-classic-mac-icons, retro-silkscreen-font, retro-pipboy-terminal, patterns-dither-retro, fonts-commit-mono, fonts-dm-sans, fonts-inter — the carry-forward set.
- **A (selective pick):** catalyst, fonts-monaspace, fonts-space-grotesk, geist-font, linear-design, retro-7-css, retro-98-css, retro-brutalist-framework, retro-cybercore-css, retro-cyberpunk-css, retro-kare-chinata-icons, retro-neobrutalism-components, retro-pipboy-hass, retro-pxlkit, retro-retroui, retro-system-css, retro-terminal-css, retro-tuicss, tailwind-ui, untitled-ui-pro, untitled-ui-react.
- **B (generic ref):** aesthetic-references, geist-ui, icons-game-icons, icons-nerd-fonts, ls-graphics, nivo, once-ui, patterns-hero, patterns-svg-backgrounds, premium-glow-icons, premium-tabler-icons, recharts, retro-cyberpunk-2077-theme, retro-nes-css, retro-xp-css, stripe-design, supply-family, templates-v0-framer-webflow, textures-paper, tremor, vercel-design.
- **C (off-aesthetic):** aceternity-ui, aceternity-ui-pro, chakra-ui, daisyui, flowbite, heroicons, hyper-ui, and the bulk icon sets (bootstrap/boxicons/css-gg/eva/feather/iconoir/ionicons/lineicons/majesticons/material-symbols/mdi/lucide/phosphor/remixicon), magicui, mamba-ui, mantine, park-ui, preline-ui, radix-themes, react-bits, shadcn-ui.
- **D (residue, don't pull):** illustrations-blush, illustrations-drawkit, illustrations-humaaans, illustrations-open-peeps, illustrations-undraw.

## Companion file

`MANIFEST-DESIGN-EXTRACTIONS.md` sits alongside this file and documents the 2026-04-21 Linear / Vercel / Stripe / Aceternity extraction work in more detail. That file is authoritative for those four kits.

## Regeneration recipe

```bash
cd /Users/regancooney/Projects/consolidate/claude-design-feed
for d in external/*/; do
  cnt=$(find "$d" -type f | wc -l | tr -d ' ')
  lic=""
  for lf in LICENSE LICENSE.txt LICENSE.md LICENSE_NOTE.md; do
    [ -f "${d}${lf}" ] && { lic="$lf"; break; }
  done
  name=$(basename "$d")
  sz=$(du -sh "$d" | awk '{print $1}')
  printf '| %s | %s | %s | %s |\n' "$name" "$sz" "$cnt" "$lic"
done
```

Last regenerated: 2026-04-21.
