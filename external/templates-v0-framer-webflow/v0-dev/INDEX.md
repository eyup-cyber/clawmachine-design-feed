# v0.dev (v0.app) Community - Component & Template Mining

**Source:** https://v0.app/templates (formerly v0.dev/community)
**Scraped:** 2026-04-21
**Scope:** dashboards, components, design-systems, layouts, agents + community-root
**License:** Fair-use research reference. Every designer credited in `metadata.json`. Do NOT redistribute.

Vercel's v0 gallery is the highest-fit corpus for Clawmachine: GPT-generated Next.js + Tailwind + Shadcn dashboards, many dark-first and data-dense. JSX source is typically visible in the detail preview via `preview-<slug>.vusercontent.net` URLs (captured in per-item metadata when observable).

## Top 10 Clawmachine-fit picks (ranked)

Ranked by density + dark-theme fidelity + reuse value for the reseller/electronics/SOC-style interactivity the Clawmachine stitch wants:

1. **Dashboard - M.O.N.K.Y** (`b7GDYVxuoGC`) - JOYCO-made internal tool. Collapsible sidebar, dark-by-default, custom iconography, integrated chat, multi-view layout. Closest visual analogue to the "workstation / reseller ops" feel on the Clawmachine wishlist. `previews/b7GDYVxuoGC-dashboard-monky.png`. 10.5K views / 1.2K forks. Author: joyco.
2. **Cyberpunk dashboard design / Tactical Ops** (`v9Hg1dBb5o3`) - Full SOC console vocabulary: agent allocation, mission activity overview, encrypted chat log, collapsible sidebar. Straight-line carry-forward for the agentic/telemetry panes. `previews/v9Hg1dBb5o3-cyberpunk-dashboard.png`. 14.6K / 627. Author: emmartinzok.
3. **Network Traffic Analyzer** (`4b4SzAt1CLV`) - Real-time packet stream, protocol filters, world map, bandwidth meters, threat detection, heatmap. Ready-made visual grammar for scout-bridge / channel telemetry dashboards. Full feature-spec in metadata. `previews/4b4SzAt1CLV-network-traffic-analyzer.png`. 179 / 68. Author: heystu.
4. **Pulse - Engineering Metrics & Incident Response Console** (`3hZwaLtyRbc`) - Active incidents list (critical/high/medium), service latency P50/P95/P99 bar, request volume area chart, deployment counters. Direct pattern for build/deploy status surfacing. `previews/3hZwaLtyRbc-pulse-incident.png`. 84 / 40. Author: kerroudj.
5. **SalesOps Dashboard** (`9q2Mfgu6cDi`) - KPI cards + pipeline stages + deal status + top-performer leaderboard. Near-perfect skeleton for the "sold/stock/sourced" Clawmachine operator view. `previews/9q2Mfgu6cDi-salesops-dashboard.png`. 300 / 118. Author: kerroudj.
6. **Financial Dashboard** (`DuidKNEmCKf`) - Multi-account cards + transaction list + progress-toward-goal cards. Transactional density pattern. `previews/DuidKNEmCKf-financial-dashboard.png`. 27.7K / 594. Author: kokonut.
7. **Shadcn Dashboard** (`Pf7lw1nypu5`) - The canonical Shadcn + Recharts + TanStack Table + DnD Kit reference dashboard. Drag-reorder data table, section editing, reviewer assignment. Use as Shadcn baseline before restyling. `previews/Pf7lw1nypu5-shadcn-dashboard.png`. 3.5K / 446. Author: estebansuarez.
8. **INTERFACE** (`XhGK3naSZPB`) - Dark minimal + GSAP + Solari/Split-Flap header, SVG text animations. Take as motion / identity inspiration not dashboard pattern. `previews/XhGK3naSZPB-interface.png`. 2.4K / 663. Author: webrenew.
9. **Nexus Work Management Platform** (`ALfQrxyrJ8b`) - Feature-complete SaaS landing-page DNA with inline mini-dashboards (CPU/memory/storage). Useful for public-facing Clawmachine marketing page if ever needed. `previews/ALfQrxyrJ8b-nexus-work-mgmt.png`. 1.9K / 307. Author: rajoninternet.
10. **COMPUTE - Platform to Build & Ship AI Agents** (`Auw4otwlr20`) - Integrations grid (GitHub/Slack/S3/Stripe/Snowflake/etc), agent orchestration copy, global-region grid, TS SDK code block. Direct template for the Clawmachine agent channels surface. `previews/Auw4otwlr20-compute-agents.png`. 693 / 180. Author: kerroudj.

## Captured screenshot inventory (`previews/`)

| File | Template id | Views / Forks |
|---|---|---|
| `b7GDYVxuoGC-dashboard-monky.png` | b7GDYVxuoGC | 10500/1200 |
| `v9Hg1dBb5o3-cyberpunk-dashboard.png` | v9Hg1dBb5o3 | 14600/627 |
| `DuidKNEmCKf-financial-dashboard.png` | DuidKNEmCKf | 27700/594 |
| `Pf7lw1nypu5-shadcn-dashboard.png` | Pf7lw1nypu5 | 3500/446 |
| `3hZwaLtyRbc-pulse-incident.png` | 3hZwaLtyRbc | 84/40 |
| `4b4SzAt1CLV-network-traffic-analyzer.png` | 4b4SzAt1CLV | 179/68 |
| `ALfQrxyrJ8b-nexus-work-mgmt.png` | ALfQrxyrJ8b | 1900/307 |
| `9q2Mfgu6cDi-salesops-dashboard.png` | 9q2Mfgu6cDi | 300/118 |
| `6rnQUvOhgnB-katachi.png` | 6rnQUvOhgnB | 3000/680 |
| `XhGK3naSZPB-interface.png` | XhGK3naSZPB | 2400/663 |
| `Auw4otwlr20-compute-agents.png` | Auw4otwlr20 | 693/180 |

## Category gallery index JSON

See `gallery-index.json` for the full 40+ template catalogue across: dashboards, components, design-systems, layouts, agents, featured. Each row captures id, title, category, metric views, metric forks, URL, and visual tags.

## Notes

- v0 component source (JSX) is often accessible via each template's `preview-<slug>.vusercontent.net` iframe; only the rendered markdown was captured - retrieve source at fork time.
- Each template page has an `Open in v0` link and most have an `Open Original` deploy URL; both persisted in the markdown sidecar.
- Full markdown dumps of the five category index pages (`dashboards`, `components`, `design-systems`, `layouts`, `agents`) are preserved inside the scrape-cache; for repeat use, re-scrape via `firecrawl_scrape` with `onlyMainContent: false`.
