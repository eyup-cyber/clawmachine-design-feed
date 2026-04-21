# Clawmachine Aesthetic References — Manifest

Internal non-commercial fair-use aesthetic-reference mining for the Clawmachine design stitch. All images remain the property of their creators; do not redistribute externally. Credits are recorded per-bucket in each `INDEX.md`.

## Aesthetic target

Dense, dark, data-first, retro-tech, terminal-adjacent, brutalist-edge. Not flat SaaS. Not Apple liquid-glass. Not gradient-heavy. Not liquid-glass / frosted / blurred — that aesthetic is actively ruled out per project doctrine.

## Buckets

| bucket | images | disk | scope |
| --- | --- | --- | --- |
| `retro-mac/` | 53 | 8.5M | Mac OS 9 / System 7 / Classic Finder, Amiga Workbench, BeOS/Haiku, Windows 9x/NT/XP, Apple Lisa, NewDeal, OS/2 — all canonical pre-Aqua desktop chrome |
| `terminal-bloomberg/` | 60 | 102M | Bloomberg Terminal / Thomson Reuters concepts, trading-terminal multi-pane dashboards, TradingView multi-chart layouts, IBKR TWS, crypto exchanges rendered terminal-adjacent |
| `cyberpunk-hud/` | 67 | 65M | Cyberpunk 2077 in-game HUDs + concepts, sci-fi dashboards, cyber-HUD motifs, Orca / Splunk / Datadog / Kibana dark dashboards, Watchtower terminal CLI |
| `brutalist-dense/` | 59 | 63M | Neo-brutalist dashboards, brutalist portfolio/web reference, Windows 95 / 9x grey-chrome dialogs as brutalist ancestor, Swiss vs brutalism comparisons |
| `pip-boy-fallout/` | 46 | 18M | Fallout Pip-Boy 3000 / 4000 CSS recreations, Vault-Tec terminal themes, in-game Fallout 4 Pip-Boy screens, Vault Boy glyph set, Apollo/Gemini mission-control consoles as analogue |
| `reseller-arbitrage/` | 64 | 45M | eBay Seller Hub, Amazon Seller Central, CamelCamelCamel + Keepa price history charts, Tactical Arbitrage, SellerApp, SparkShipping, Vendoo, warehouse + inventory Dribbble, reseller spreadsheets |
| `scraper-monitor/` | 50 | 22M | Octoparse / ParseHub / Firecrawl / Oxylabs / BrightData scraper consoles, Grafana + Prometheus monitoring dashboards, SilentArc submarine tactical dashboard, IDE dark themes as tooling reference |
| `dense-admin/` | 46 | 50M | Dark data-grid + table UI, admin/SaaS dashboards at high data density, Muzli / AdminLTE / Colorlib / BootstrapDash / shadcn dark dashboards, command-center installations as spatial analogue |

**Total images: 445** (well past the 240 minimum). **Disk: ~370MB** (under the 1.5GB ceiling).

## Sources mined

- **Dribbble** — primary: tag search + shot pages (`/tags/trading-terminal`, `/tags/neobrutalism`, `/search/bloomberg-terminal`, etc.).
- **Behance** — project-gallery images (90s UX Interface, Retro User Interface, 80s Retro Interfaces, Macintosh UI Elements, Report Analytics Admin).
- **Interface In Game** + **Game UI Database** — Cyberpunk 2077 canonical HUD captures.
- **ToastyTech GUIs + Guidebook Gallery + Wikipedia / Wikimedia** — canonical classic-OS screenshots (System 7, Mac OS 9, Win 9x, Lisa, Amiga, BeOS, NextStep traces).
- **Nexus Mods + Reddit + DeviantArt + Codemotion + Bethesda** — Pip-Boy recreations and canonical game HUDs.
- **Stok.ly / LitCommerce / Multiorders / SnapToList / 3DSellers / SellerApp / Amalytix / SalesBacker / Amazon Sell / Porter Metrics / Daasity / Peel** — reseller/arbitrage reference.
- **Firecrawl / Oxylabs / Octoparse / ParseHub / BrightData / ScrapingBee / Scrapingdog / Wiser / PriceShape / FrigginYeah / Decodo** — scraper/price-tracker UI reference.
- **Grafana Labs / Prometheus / Datadog / Splunk / Kibana / Orca Security / GreyNoise / Dash0 / Percona** — monitoring/observability dashboards.
- **TradingView + IBKR + TradesViz + CrossTrade + Strike.money + FXOpen + AltcoinTrading** — trading-terminal dense layouts.
- **Muzli / AdminLTE / Colorlib / BootstrapDash / MUI / Nuxt Charts / shadcn / Koala UI** — admin/dashboard pattern libraries.
- **Mission-control / command-center photography** — NASA Apollo/Gemini consoles (Ars Technica, NBC, Chron, phys.org, Evans Federal, DasNet, US Army CERDEC, Applied Global).

## Method

1. `firecrawl_search` with `sources: [{type: images}]` targeting each bucket's taxonomy scoped to the right site.
2. URL lists authored per-bucket (`/tmp/urls_<bucket>*.txt`) with `name|image_url|source_page|caption` schema so captions + credits travel with the file name.
3. `curl` download via `/tmp/download_image.sh` with Mac UA, Dribbble URL cleanup (drop `?resize` params when cheap), 5KB minimum size + `file --mime-type` validation. Non-image or <5KB hits discarded automatically.
4. Per-bucket `INDEX.md` built by `/tmp/make_indexes.sh` — awk lookup against the URL lists, stable file→source→caption row.
5. This manifest regenerated from filesystem truth (`ls | grep -iE '\.(jpg|jpeg|png|webp|gif|svg|bmp)$'`).

## Known exclusions

- **Godly.website** — firecrawl_search returned zero image results for this site, likely due to JS-rendered gallery. Skipped; substituted with direct brutalist Dribbble shots + Webflow brutalism article + brutalistwebsites.com gallery.
- **Mobbin** — returned results are CDN-signed opaque URLs whose signatures expire; downloading them directly often 403s. The few that fetched are in `terminal-bloomberg/` under Mobbin captions.
- **pttrns / UI Garage / screenlane / dark.ai** — minimal public image surface via search; not substantively added in this pass. The direct-vendor screenshots (Splunk, Datadog, Orca, Grafana, Octoparse, Amazon Seller Central) cover the same aesthetic territory at higher resolution and cleaner provenance.
- **Liquid-glass / Apple frosted-translucent** — explicitly excluded per project doctrine.
- **Generic stock-art synthwave neon-grid clip-art** — filtered out; kept only actual UI / HUD reference, not decoration backgrounds.

## Legal

Fair-use research reference only. Every image is mirrored from its original source; each bucket's `INDEX.md` carries the source URL per file. Do not redistribute. If the Frankenstein build ships elements that quote these references, designer credit should travel with the final piece; these references must not appear in any marketing surface.
