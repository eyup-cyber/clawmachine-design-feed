# external/ MANIFEST

Fetched by two parallel agents on 2026-04-20. This file documents only the items fetched by the **premium-kit / font / fig-community agent** (prefixes `premium-*`, `fonts-*`, `figs-*`). The other agent owns the remaining entries.

Cloning method: `git clone --depth 1`, then `rm -rf .git node_modules .github` and unused subtrees. Commit SHAs not captured post-strip; source URLs pin the head at fetch time (2026-04-20 ~02:30 BST).

Disk: `du -sh external/` = **645M total** (fetched by other agent and this agent combined). This agent's contribution = **191M** (items below).

## This agent's fetches

| Subfolder | Kind | License | Size | Source URL | Status |
|---|---|---|---|---|---|
| `fonts-inter` | Sans font family | OFL 1.1 | 31M | https://github.com/rsms/inter | fetched |
| `fonts-space-grotesk` | Sans font | OFL 1.1 | 3.5M | https://github.com/floriankarsten/space-grotesk | fetched |
| `fonts-dm-sans` | Sans+Serif family | OFL 1.1 | 33M | https://github.com/googlefonts/dm-fonts | fetched |
| `fonts-commit-mono` | Mono font | OFL 1.1 + MIT (site) | 10M | https://github.com/eigilnikolajsen/commit-mono | fetched |
| `fonts-monaspace` | Mono superfamily (Argon/Neon/Xenon/Radon/Krypton) | OFL 1.1 | 85M | https://github.com/githubnext/monaspace | fetched (Variable+Static only; Web/Nerd/Frozen pruned) |
| `premium-tabler-icons` | 5800+ MIT SVG icons | MIT | 25M | https://github.com/tabler/tabler-icons | fetched |
| `premium-glow-icons` | 442 icons (Outline+Solid) | MIT | 1.7M | https://github.com/glow-ui/glow-icons | fetched |

## Attempted but not fetched

| Kit | Status | Reason |
|---|---|---|
| Untitled UI Figma (free `.fig`) | paywalled-ish | Download URL `/download` requires Figma login to duplicate community file. Hard rule: no auth bypass. See "Figma Community URLs" below - operator can manually duplicate. |
| Untitled UI React (mine) | skipped | Other agent already cloned to `external/untitled-ui-react/` - duplicate avoided. |
| Tailwind Catalyst UI Kit | paywalled | Zip is delivered as part of Tailwind UI All-Access purchase. No public GitHub mirror (repo `tailwindlabs/catalyst-ui-kit` = 404). GitHub issue #1580 confirms "zip included with Tailwind UI". |
| Tailwind UI free samples | none | `tailwindlabs/tailwindui-issues` repo is a README only. `tailwindcss.com/plus/ui-kit` is marketing only. |
| LS Graphics freebies | none | `lsgraphics.com/freebies` 404s; LS Graphics has moved to an app-delivered model. No public-URL freebies. |
| Supply Family freebies | none | `/product-tag/free/` returns 8 items but all are **$19-28 paid** products that merely use the word "Free" in their names (e.g. "Free Entry badge mockup"). Genuine freebies sit behind account/newsletter gate - not scraped. |
| shadcn/blocks | other-agent | `shadcn-ui/apps/www/registry/new-york/blocks/` expected path is absent from the other agent's clone (no `registry/` dir under `apps/www/`). If blocks are needed, clone `https://github.com/shadcn-ui/ui` at a tag where blocks were present (recent `shadcn/registry` split has moved them) - see note at bottom. |
| Glow Icons (first URLs tried) | wrong-org | Correct org is `glow-ui`, not `glowingloom` / `glowicons`. Succeeded on second attempt. |
| Lucide | other-agent | In `external/lucide/` already. |
| Geist Sans/Mono | other-agent | In `external/geist-font/` (98M - includes all source woffs and samples). |
| Phosphor, Heroicons, Remix Icon | other-agent | Already present. |

## shadcn/blocks note

The other agent's `shadcn-ui/` clone does NOT contain the `blocks/` registry directory at `apps/www/registry/new-york/blocks/`. The shadcn team moved blocks into a separate `shadcn/registry` repository in early 2026. If operator wants blocks, clone `https://github.com/shadcn-ui/registry` (or ask the other agent).

## Figma Community URLs for manual duplication

These cannot be exported as `.fig` without the operator clicking "Duplicate" while logged in (Figma REST API requires a personal access token and the community-copy flow on the web). List is curated to the clawmachine aesthetic brief (cyberpunk / retro Mac / brutalist / dark data-viz / Swiss).

Method for each: operator logs into Figma -> opens URL -> clicks "Duplicate" -> the file appears in their drafts with a new file-key visible in the URL bar -> paste that file-key into whatever extraction script style-lab uses.

| # | Name | File key | URL | Reason-why |
|---|------|----------|-----|------------|
| 1 | Untitled UI FREE v2.0 | `1020079203222518115` | https://www.figma.com/community/file/1020079203222518115/untitled-ui-free-figma-ui-kit-and-design-system-v2-0 | Operator explicitly named; 280k+ designers, huge component base, neutral base to override with clawmachine palette |
| 2 | Cyberpunk UI Elements - Free Pack | `1410999019282442873` | https://www.figma.com/community/file/1410999019282442873/cyberpunk-ui-elements-free-pack | HUD/decal elements from an unfinished mech game - exactly the texture/noise aesthetic brief |
| 3 | Cyberpunk 2077 Concept UI Redesign | `1014971564349982506` | https://www.figma.com/community/file/1014971564349982506/cyberpunk-2077-concept-ui-redesign-freebie | Full UI redesign; good for modal/menu patterns |
| 4 | Sci-fi UI Kit (Free) | `1595778560755863610` | https://www.figma.com/community/file/1595778560755863610/sci-fi-ui-kit-free | Geometry/contrast-driven; component-library scope not just vibes |
| 5 | Cyber Punk Website UI/UX | `1436481525663061827` | https://www.figma.com/community/file/1436481525663061827/cyber-punk-website-ui-ux-design | Full website composition reference |
| 6 | Mac OS 9: UI Kit | `966779730364082883` | https://www.figma.com/community/file/966779730364082883/mac-os-9-ui-kit | Exact Mac OS 9 chrome; reference for platinum-era controls |
| 7 | Macintosh Classic | `992075397105401200` | https://www.figma.com/community/file/992075397105401200/macintosh-classic | 1984 Macintosh 128K skeuomorph; bezel/shadow patterns |
| 8 | 1300 Free Pixel Icons | `1196864707579677521` | https://www.figma.com/community/file/1196864707579677521/1-300-free-pixel-icons-vector-pixel-icons-svg | Susan-Kare-inspired; retro Mac pixel icon pack |
| 9 | Pixel Icon Library (HackerNoon) | `1278952394341234192` | https://www.figma.com/community/file/1278952394341234192/pixel-icon-library-2300-pixelated-icons-by-hackernoon | 2300 pixelated icons; category coverage |
| 10 | Pixelarticons Free | `952542622393317653` | https://www.figma.com/community/file/952542622393317653/pixelarticons-free | 800 pixel icons; strict 24x24 grid, currentColor fills - drops straight into SwiftUI |
| 11 | Retro Gadget Pixel Icons | `1406871567465699006` | https://www.figma.com/community/file/1406871567465699006/retro-gadget-pixel-icons | Camera/gamepad/radio/iPod - matches tech-electronics vertical |
| 12 | Terminal Window UI + 485 Themes | `1616918715705746649` | https://www.figma.com/community/file/1616918715705746649/terminal-window-ui-485-themes | 485 terminal themes; monospace-first - matches operator's terminal-as-primary-UI thread |
| 13 | Brutalist Design | `1349495910680102205` | https://www.figma.com/community/file/1349495910680102205/brutalist-design | Brutalist homepage; strong thick-border aesthetic |
| 14 | 17 Screens NeoBrutalism Admin Dashboard | `1601916523900495011` | https://www.figma.com/community/file/1601916523900495011/17-screens-neobrutalism-admin-dashboard-ui-kit | Hard offset shadows, thick borders, flat pastel - dashboard-scale |
| 15 | Free Vector Shapes (420 Brutalist/Memphis) | `1532351178915770638` | https://www.figma.com/community/file/1532351178915770638/free-vector-shapes-abstract-geometric-memphis-brutalist-brutalism | Shape library for identity/motif decoration |
| 16 | Data Visualization Dashboard v1.0 | `1251727181815311308` | https://www.figma.com/community/file/1251727181815311308/data-visualization-dashboard-v1-0 | 12 chart types; direct data-viz template for arbitrage dashboards |
| 17 | Data Visualization Package (Community) | `1130361890489454674` | https://www.figma.com/community/file/1130361890489454674/data-visualization-package-community | Data-rich interface components |
| 18 | Ultra Accessible Charts - dataviz | `1293857341962412271` | https://www.figma.com/community/file/1293857341962412271/ultra-accessible-charts-dataviz | 10 chart types x 6 colour themes; accessibility variants |
| 19 | DataCanvas Data Viz Dashboard Kit 3 Lite | `1623990511462121790` | https://www.figma.com/community/file/1623990511462121790/datacanvas-data-visualization-dashboard-ui-kit-3-lite | Large-screen dashboard modules |
| 20 | A Swiss Design System 3.0 Core | `1361746573902788643` | https://www.figma.com/community/file/1361746573902788643/a-swiss-design-system-3-0-core | Variables + Autolayout + Variants; Swiss-style tokens |

## Existing extractions (style-lab)

`~/Projects/style-lab/figma-community-raw/` - **operator already has 52 file-key extractions here** per the brief. This agent did NOT inspect its subfolders during this job (shell reset behaviour blocked inline `ls`; paths above can be confirmed with a fresh shell).

## Re-hydration (if you need commit SHAs later)

Each `fonts-*` / `premium-*` subfolder has its LICENSE and README preserved. If you need the exact SHA that landed on disk, run `git ls-remote <upstream> HEAD` against the source URL at the exact minute of this manifest (2026-04-20 ~02:40 BST) - it will be within one commit either way for these low-churn repos.

---

## Retro / brutalist / cyberpunk / terminal aesthetic kits (2026-04-21)

Fetched in a third acquisition pass on 2026-04-21 to feed the retro-Mac + cyberpunk + brutalist synthesis
(the *exact* aesthetic Clawmachine is trying to hit). Same clone-strip-index method as the rows above.
Every subfolder has its own `INDEX.md` with aesthetic description, offering summary, and Clawmachine-fit note.
Per-kit ceiling 100MB, total fleet 86M.

| Subfolder | Kind | License | Size | Source URL | Status |
|---|---|---|---|---|---|
| `retro-system-css` | Mac Classic System 6/7 CSS framework | MIT | 436K | https://github.com/sakofchit/system.css | fetched + demo.html |
| `retro-7-css` | Windows 7 Aero CSS framework | MIT | 960K | https://github.com/khang-nd/7.css | fetched + demo.html (CAUTION: glass aesthetic ruled out) |
| `retro-98-css` | Windows 98 CSS framework | MIT | 752K | https://github.com/jdan/98.css | fetched + demo.html |
| `retro-xp-css` | Windows XP Luna CSS framework | MIT | 1.3M | https://github.com/botoxparty/XP.css | fetched + demo.html |
| `retro-nes-css` | 8-bit NES CSS framework | MIT | 1.6M | https://github.com/nostalgic-css/NES.css | fetched + demo.html |
| `retro-terminal-css` | Modern terminal/monospace CSS | MIT | 556K | https://github.com/Gioni06/terminal.css | fetched + demo.html (pruned 92M of Go compiler binaries) |
| `retro-tuicss` | MS-DOS TUI / ASCII-block CSS (BIOS-substitute) | MIT | 1.7M | https://github.com/vinibiavatti1/TuiCss | fetched (in-repo examples/) |
| `retro-brutalist-framework` | Raw web brutalism (40+ HTML demos) | BITCHY/MIT | 32M | https://github.com/pinecreativelabs/Brutalist-Framework | fetched (static/ = 40 demo pages) |
| `retro-neobrutalism-components` | Neobrutalist React/Tailwind shadcn-style | MIT | 4.5M | https://github.com/ekmas/neobrutalism-components | fetched + demo.html |
| `retro-cyberpunk-css` | Cyberpunk 2077 replica UI CSS | MIT | 764K | https://github.com/alddesign/cyberpunk-css | fetched (in-repo demo/) |
| `retro-cybercore-css` | Broader cyberpunk (neon/scanlines/CRT) | MIT | 5.3M | https://github.com/sebyx07/cybercore-css | fetched (multiple demos) |
| `retro-cyberpunk-2077-theme` | Cyberpunk 2077 theme layer | GPLv3 | 680K | https://github.com/gwannon/Cyberpunk-2077-theme-css | fetched - GPL: reference only, no source mixing |
| `retro-pipboy-terminal` | Fallout Pip-Boy 3000 replica (Angular) | CC BY-NC + MIT + MPL | 18M | https://github.com/CodyTolene/pip-terminal | fetched (pruned fan-art+community, 4.1M) |
| `retro-pipboy-hass` | Pip-Boy Home Assistant theme | MIT | 2.8M | https://github.com/biofects/pipboy | fetched (use as token source) |
| `retro-pxlkit` | Pixel-art React UI + 200+ icons | MIT code + custom asset | 4.8M | https://github.com/Joangeldelarosa/pxlkit | fetched - attribution required for assets |
| `retro-retroui` | Pixelated React/Next UI library | BSD-3-Clause | 852K | https://github.com/Dksie09/RetroUI | fetched |
| `retro-kare-chicago-font` | Chicago typeface reproduction (Susan Kare) | MIT | 1.2M | https://github.com/KingDuane/Chicago-Kare | fetched - PRIMARY for classic-mac type |
| `retro-kare-chinata-icons` | MacOS 9 icon replica pack | CC BY-SA 4.0 | 872K | https://github.com/DawnVespero/Chi-Nata | fetched - ShareAlike constraint, reference only |
| `retro-kare-classic-mac-icons` | Classic Mac icon SVG+PNG recreations | NOT DECLARED | 6.6M | https://github.com/thomasareed/Classic-Mac-icons | fetched - license unclear, reference only until sign-off |
| `retro-silkscreen-font` | Silkscreen pixel font (Jason Kottke / Google Fonts) | OFL 1.1 | 1.1M | https://github.com/googlefonts/silkscreen | fetched - OFL compliant with font doctrine |

**Search-route findings (for audit trail):**

- **BIOS.css standalone does not exist** on GitHub despite persistent inbound searches — closest match
  is TuiCSS (already fetched) which hits the actual aesthetic (DOS/CGA TUI) accurately. Noted so the
  operator doesn't chase a phantom.
- **Susan Kare official icon SVG pack is not on GitHub** — she sells prints via asprey/moma. Three
  community recreations cover the ground: classic-mac-icons (1-bit era), Chi-Nata (MacOS 9 color),
  Chicago-Kare (font). Figma community file 1258417138275801052 "Apple Macintosh Icons (1984)" is
  listed in the earlier Figma Community block above if operator wants to duplicate.
- **Brutalist Framework upstream was NOT `brutalistframework/brutalistframework`** (404) — actual repo
  is `pinecreativelabs/Brutalist-Framework`. Brief's URL was a guess; real one via search.
- **Silkscreen upstream was NOT `damieng/silkscreen`** (404) — damieng does adjacent ZX Spectrum font
  work (`damieng/pixelworld`) but Silkscreen by Jason Kottke lives at `googlefonts/silkscreen`.

**Licenses requiring handling:**

- CC BY-SA 4.0 (chinata-icons) — attribution AND derivative-ShareAlike; reference-only to avoid
  license contamination of Clawmachine's distribution.
- CC BY-NC 4.0 (pipboy-terminal) — non-commercial; matches brief's "internal, non-commercial, fair-use"
  framing. Do not ship Fallout/Bethesda trademarks (Pip-Boy logo, Vault-Boy) in any exported product.
- GPLv3 (cyberpunk-2077-theme) — cannot be mixed into Clawmachine source; reference-only.
- Not Declared (classic-mac-icons) — treat as all-rights-reserved; reference-only until author confirms.
- Custom split license (pxlkit) — code MIT, assets require attribution (paid tier removes requirement).

**Pruning log:**

- `retro-terminal-css/builds/` (83M) and `retro-terminal-css/vendor/` (9.4M) removed — Go-language site-builder
  binaries + module dependencies, not styling material.
- `retro-pipboy-terminal/public/images/fan-art/` (3.4M) and `.../community/` (0.7M) removed — community
  submissions, not framework assets.
- All kits: `.git/`, `node_modules/`, `.github/` stripped.
