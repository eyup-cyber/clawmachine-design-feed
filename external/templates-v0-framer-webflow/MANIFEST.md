# templates-v0-framer-webflow - Master Manifest

**Scrape date:** 2026-04-21
**Operator:** Regan (raygunelectronics@gmail.com)
**Use:** Clawmachine-internal fair-use template + component mining reference
**Redistribution:** Prohibited
**Credit:** Every designer is named in per-subdir `metadata.json`

## Subdirectories (each has its own INDEX.md + metadata.json + previews/)

| Subdir | Source | Items catalogued | Screenshots | Top source |
|---|---|---|---|---|
| `v0-dev/` | v0.app/templates | 40+ across 5 categories | 11 PNGs | Vercel AI SDK native |
| `framer-templates/` | framer.com/marketplace | 120+ slugs + 6 detail captures | 6 PNGs | Design-forward, compiled (no source) |
| `webflow-templates/` | webflow.com/templates | 14 admin-dashboard detail + 30+ adjacent | 3 PNGs | BRIX Templates (DevLink React export) |
| `notion-templates/` | notion.com/templates | 25 dashboard slugs | 0 (not applicable) | IA-only, not web UI |
| `figma-community-top/` | figma.com/community/ui-kits/dashboards | Top 43 kits by popularity | 0 (carousel URLs in JSON) | ByeWind + MUI + Iago Sousa |
| `vercel-templates/` | vercel.com/templates | 41 AI + 27 Next.js templates | 0 (use git clone) | MIT/Apache open-source |
| `design-to-code/` | Locofy/Builder/Plasmic/Supabase/Convex | 5 platforms | 0 | Supabase UI is only top-fit |

## Top 10 Clawmachine-stitch candidates (cross-subdir)

Ranked for immediate carry-forward into the Frankenstein build (priorities: dark-first dashboard, operator-ops density, agent platform, MCP/chat, OSS-licensable):

1. **v0: Dashboard - M.O.N.K.Y (joyco)** - visual template for the workstation/reseller-ops view. `v0-dev/previews/b7GDYVxuoGC-dashboard-monky.png`
2. **v0: Cyberpunk Dashboard / Tactical Ops** - SOC vocabulary, agent allocation, encrypted chat log. `v0-dev/previews/v9Hg1dBb5o3-cyberpunk-dashboard.png`
3. **v0: Network Traffic Analyzer** - real-time telemetry grammar for scout-bridge channels. `v0-dev/previews/4b4SzAt1CLV-network-traffic-analyzer.png`
4. **v0: Pulse - Incident Response Console** - P50/P95/P99 + incidents + deploys pattern. `v0-dev/previews/3hZwaLtyRbc-pulse-incident.png`
5. **v0: SalesOps Dashboard** - pipeline + leaderboard + KPI. Cleanest reseller analogue. `v0-dev/previews/9q2Mfgu6cDi-salesops-dashboard.png`
6. **Vercel Template: AI SDK Computer Use** - Claude Sonnet computer-use agent with Vercel Sandbox. `next.js/ai-sdk-computer-use`
7. **Vercel Template: AI Research Agent** - parallel-browsers via Stagehand + Browserbase. Ports straight into scout-bridge pattern. `next.js/ai-research-agent`
8. **Vercel Template: Tersa AI Workflow Canvas** - visual agent workflow. `next.js/tersa-ai-workflow-canvas`
9. **Webflow: Dashdark X (BRIX, FREE, DevLink)** - dark-mode Webflow-to-React via DevLink. `webflow.com/templates/html/dashdark-x-devlink-website-template`
10. **Supabase UI (MIT)** - auth + realtime + dropzone + infinite-query React primitives, MIT-licensed. `github.com/supabase-community/supabase-ui`

## Size status

- **Previews directory total:** ~5 MB (11 v0 + 6 framer + 3 webflow). Well under 2 GB cap.
- **Markdown / metadata:** ~200 KB.
- **Not persisted to disk:** Figma carousel images (URLs in metadata), Notion covers (IA-only value), Vercel template hero images (use git clone instead).

## How to re-use this corpus

1. **To fork a v0 template:** open the source_url from metadata, click "Open in v0", fork, download, inspect.
2. **To use a Vercel template:** `vercel clone <slug>` or visit the source_url + deploy button.
3. **To use a Webflow template:** visit `preview.webflow.com/preview/<slug>` to get the Designer link. Purchase required for production use.
4. **To use a Framer template:** each has a `framer.website` public preview. Purchase required for production use.
5. **To use a Figma kit:** visit `figma.com/community/file/<fileKey>` and "Duplicate".
6. **To use Supabase UI:** `npx create-next-app -e with-supabase` or git clone the community repo.

## Open gaps (not filled due to scope/budget)

- v0 JSX source: visible in each template's iframe but not persisted. Re-scrape the preview.vusercontent URLs if source-level analysis is needed.
- Figma file duplication: needs a logged-in Figma session; scrape-only yields preview images, not content.
- Notion page-cloning: needs a logged-in Notion session.
- Full-page screenshots: only the 1440x900 above-fold was captured for each v0/Framer/Webflow detail. Scroll-capture or full-page screenshotting would ~10x the disk footprint.

## Anti-goals honoured (per repo CLAUDE.md)

- **No liquid glass.** Apple iOS 26 + Liquid Glass Figma kits flagged as `visual-antithesis` in their metadata entries; not recommended for carry-forward.
- **No gen-AI art residue.** No Recraft/MJ/Dall-E screenshots captured.
- **No scaffolding.** This is one MANIFEST + per-subdir INDEX; no process docs, no roadmap, no session-X.md.
