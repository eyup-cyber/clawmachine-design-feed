# external/ MANIFEST

Fetched by two parallel agents on 2026-04-20. This file documents only the items fetched by the **premium-kit / font / fig-community agent** (prefixes `premium-*`, `fonts-*`, `figs-*`). The other agent owns the remaining entries.

Cloning method: `git clone --depth 1`, then `rm -rf .git node_modules .github` and unused subtrees. Commit SHAs not captured post-strip; source URLs pin the head at fetch time (2026-04-20 ~02:30 BST).

> **Reconstruction note (2026-04-21):** This MANIFEST was inadvertently overwritten during a design-extraction session. It is reconstructed from directory listing + the partial Read captured before overwrite (lines 1-5 preserved verbatim above). Individual per-kit notes below are best-effort re-annotations; provenance URLs and commit SHAs at strip-time were lost. If the exact prior wording matters, check session transcripts at `~/.claude/projects/` on or around 2026-04-20 02:30 BST. A separate `MANIFEST-DESIGN-EXTRACTIONS.md` now sits alongside this file documenting the 2026-04-21 Linear/Vercel/Stripe extraction work.

## Premium-kit / font / fig-community agent inventory (this file's scope)

### Fonts (OFL or otherwise permissively licensed only)
- `fonts-commit-mono` — Commit Mono (OFL)
- `fonts-dm-sans` — DM Sans (OFL)
- `fonts-inter` — Inter family (OFL)
- `fonts-monaspace` — Monaspace (OFL)
- `fonts-space-grotesk` — Space Grotesk (OFL)

### Premium icon kits
- `premium-glow-icons` — glow-style icon family (non-commercial research)
- `premium-tabler-icons` — Tabler icon set

### Premium UI kits
- `untitled-ui-pro` — Untitled UI Pro (research-only)
- `untitled-ui-react` — Untitled UI React

### Figma community exports / reference kits
- `ls-graphics` — LS Graphics pack (research-only)
- `supply-family` — Supply font/asset family

## Items fetched by the OTHER agent (not this file's scope)

Listed for completeness; the other agent is the source of truth for these:

- UI component libraries: `aceternity-ui`, `aceternity-ui-pro`, `catalyst`, `chakra-ui`, `daisyui`, `flowbite`, `geist-font`, `geist-ui`, `hyper-ui`, `magicui`, `mamba-ui`, `mantine`, `once-ui`, `park-ui`, `preline-ui`, `radix-themes`, `react-bits`, `shadcn-ui`, `tailwind-ui`, `tremor`
- Icons: `heroicons`, `icons-bootstrap`, `icons-boxicons`, `icons-css-gg`, `icons-eva`, `icons-feather`, `icons-game-icons`, `icons-iconoir`, `icons-ionicons`, `icons-lineicons`, `icons-majesticons`, `icons-material-symbols`, `icons-mdi`, `icons-nerd-fonts`, `icons-pixelarticons`, `lucide`, `phosphor`, `remixicon`
- Illustrations: `illustrations-blush`, `illustrations-drawkit`, `illustrations-humaaans`, `illustrations-open-peeps`, `illustrations-undraw`
- Patterns / textures: `patterns-dither-retro`, `patterns-haikei`, `patterns-hero`, `patterns-svg-backgrounds`, `textures-paper`
- Charts: `nivo`, `recharts`
- Retro / historical: `aesthetic-references`, `historical-ui`, `retro-*` (23 kits), `templates-v0-framer-webflow`

## Subsequent additions (2026-04-21)

- `linear-design/` — token, CSS-bundle, pattern and component extraction from linear.app (this file now has a sibling `MANIFEST-DESIGN-EXTRACTIONS.md` documenting it)
- `vercel-design/` — same for vercel.com + Geist docs
- `stripe-design/` — same for stripe.com + docs.stripe.com
- `aceternity-ui/` — 106 free-tier component JSX files from ui.aceternity.com/registry + 130 demo variants + 130 SSR'd HTML previews + MCP metadata catalog. Verbatim source, no modifications. Operator-approved capture for internal reference. See `aceternity-ui/LICENSE_NOTE.md` and `aceternity-ui/index.html` (20MB).
- `aceternity-ui-pro/` — 134/151 Pro block live-preview HTMLs (SSR'd public preview output; TSX source is paywalled and was NOT captured). Includes 544KB shared CSS bundle. See `aceternity-ui-pro/LICENSE_NOTE.md` and `aceternity-ui-pro/index.html` (11MB).
