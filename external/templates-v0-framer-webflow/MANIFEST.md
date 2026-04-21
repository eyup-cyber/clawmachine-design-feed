# templates-v0-framer-webflow - Master Manifest

**Scrape date:** 2026-04-21
**Operator:** Regan Cooney (regacooney@gmail.com)
**Use:** Clawmachine-internal fair-use template + component mining reference
**Redistribution:** Prohibited
**Credit:** Every designer is named in per-subdir `metadata.json` + visible footer on each HTML recreation

## Subdirectories (each has `previews/`, `recreated/`, `metadata.json`, `INDEX.md`, `LICENSE_NOTE.md`)

| Subdir | Source platform | Scraped previews | Recreated HTML |
|---|---|---|---|
| `v0-dev/` | v0.app/templates | 11 | 30 |
| `framer-templates/` | framer.com/marketplace | 10 | 10 |
| `webflow-templates/` | webflow.com/templates | 10 | 10 |
| `notion-templates/` | notion.com/templates | 10 | 10 |
| `figma-community-top/` | figma.com/community | 10 | 10 |
| `vercel-templates/` | vercel.com/templates | 10 | 10 |
| `design-to-code/` | Supabase/Convex/Builder/Plasmic/Locofy/Shadcn | 10 | 10 |
| `retool-bravo-bubble/` | retool.com/bubble.io/bravostudio.app | 11 | 10 |
| **total** | | **82** | **100** |

## Shared asset

- `_shared/dark-dashboard.css` — CSS primitives linked by all `recreated/*.html` files. Sidebar/topbar/KPI/table/chart/badge grammar in dark tokens + 4 theme variants (cyber / light / warm / matrix).
- `_shared/_gen.py` — generator script that authored all 100 HTML files. Regenerable; each HTML is a ~5-10 KB structural approximation (not source-code extraction).

## Verification summary

- 8 subfolders present, every folder has the five required artifacts.
- Total footprint: 18 MB (under 1 GB cap; largest subfolder 4.2 MB — under 150 MB cap).
- All 100 recreated HTML files link the shared stylesheet and carry a visible credit footer citing designer + source URL.
- Licence posture: UK fair-dealing for internal non-commercial research; per-subfolder LICENSE_NOTE.md documents the per-platform posture.

## Top 12 Clawmachine-stitch candidates (cross-subdir ranked)

Ranked for immediate carry-forward into the Frankenstein stitch (dark-first, operator-density, agent platform, MCP/chat, OSS-licensable). Recreations in `recreated/` are reference-grammar only — actual stitch goes through the operator's Swift + chromatic-schemes tokens, not via these CSS approximations.

1. **v0: Dashboard - M.O.N.K.Y** (joyco) — integrated chat + collapsible sidebar + reseller-fit internal tool. `v0-dev/previews/b7GDYVxuoGC-dashboard-monky.png`
2. **v0: Cyberpunk Dashboard / Tactical Ops** (emmartinzok) — SOC vocabulary, agent allocation, encrypted chat log. `v0-dev/previews/v9Hg1dBb5o3-cyberpunk-dashboard.png`
3. **v0: Network Traffic Analyzer** (heystu) — real-time telemetry grammar for scout-bridge channels. `v0-dev/previews/4b4SzAt1CLV-network-traffic-analyzer.png`
4. **v0: Pulse - Incident Response Console** (kerroudj) — P50/P95/P99 + incidents + deploys pattern. `v0-dev/previews/3hZwaLtyRbc-pulse-incident.png`
5. **v0: SalesOps Dashboard** (kerroudj) — pipeline + leaderboard + KPI. `v0-dev/previews/9q2Mfgu6cDi-salesops-dashboard.png`
6. **Vercel: AI SDK Computer Use** — Claude Sonnet computer-use agent with Vercel Sandbox. `vercel-templates/previews/vercel-ai-sdk-computer-use.png`
7. **Vercel: AI Research Agent** — parallel-browsers via Stagehand + Browserbase. `vercel-templates/previews/vercel-ai-research-agent.png`
8. **Vercel: Tersa AI Workflow Canvas** — visual agent workflow node-graph. `vercel-templates/previews/vercel-tersa-workflow.png`
9. **Webflow: Dashdark X (BRIX, FREE, DevLink)** — dark-mode Webflow-to-React via DevLink. `webflow-templates/previews/webflow-dashdark-x.png`
10. **Supabase UI (MIT)** — auth + realtime + dropzone + infinite-query React primitives, MIT-licensed. `design-to-code/previews/supabase-ui.png`
11. **Retool: KPI Dashboard** — cleanest KPI-grid reference + filterable data table. `retool-bravo-bubble/previews/retool-kpi-dashboard.png`
12. **Figma: Tesla Dashboard UI (Nami)** — industrial/operator-HUD aesthetic fit for Mesh page. `figma-community-top/previews/figma-tesla-dashboard.png`

## How to re-use this corpus

1. **To fork a v0 template:** open the source_url from metadata, click "Open in v0", fork, download.
2. **To use a Vercel template:** `vercel clone <slug>` or visit the source_url + deploy button.
3. **To use a Webflow template:** visit `preview.webflow.com/preview/<slug>` for the Designer link. Purchase required.
4. **To use a Framer template:** visit the `framer.website` preview, purchase required.
5. **To use a Figma kit:** visit `figma.com/community/file/<fileKey>` and "Duplicate".
6. **To use Supabase UI:** `npx create-next-app -e with-supabase` or copy from the community repo (MIT).
7. **To open a recreated HTML locally:** `open external/templates-v0-framer-webflow/<subdir>/recreated/<file>.html`.

## Recreations anti-claim

The 100 `recreated/*.html` files are authored structural approximations — NOT source extractions. They match the visible layout pattern (e.g. "4-column KPI strip + 2/3 chart + 1/3 side panel + full-width table") using generic dark-dashboard CSS. No proprietary component code has been copied. No designer's exact visual identity has been reproduced. Per-file footer credits the original designer + platform + source URL.

## Anti-goals honoured (per repo CLAUDE.md)

- **No liquid glass.** Apple iOS 26 + Liquid Glass Figma kits flagged as `visual-antithesis` in their metadata entries; NOT recommended for carry-forward.
- **No gen-AI art residue.** No Recraft/MJ/Dall-E screenshots captured.
- **No scaffolding.** Lean per-subdir INDEX + one MANIFEST. No roadmap, no session-X.md.
- **Reference, not ingest.** Per the repo CLAUDE.md, `external/` is reference material for the agents working on the feed, not for ingest into Claude Design. These recreations are for layout-pattern study only — the operator's chromatic-schemes + Swift tokens remain the ground-truth for any actual Clawmachine surface.
