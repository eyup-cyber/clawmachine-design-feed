# retool-bravo-bubble — INDEX

Ranked for Clawmachine-stitch consideration. All three ecosystems share one property: they are **framework-locked** — you build inside Retool, Bubble, or Bravo, not in Swift. Carry-forward is pattern-level, not code-level.

## Top 10 ranked

1. **Retool — KPI Dashboard** (`retool-kpi-dashboard.png`) — clearest operator-ops KPI grammar. Marketing campaign metrics (Total Sales / Clicks / Impressions) + pie chart + filterable data table. Directly maps to Clawmachine Dashboard (Deal count / Revenue today / ROI / Cycle time + vendor-pie + deal-feed table). *recreated: `05-retool-kpi-dashboard`*
2. **Retool — Security Dashboard** (`retool-security-dashboard.png`) — SOC-style threat feed + incident trend + compliance matrix. Pattern maps onto Clawmachine's Mesh page (machine health) and scout-bridge alerts. *recreated: `04-retool-security-dash`*
3. **Retool — Custom CRM** (`retool-custom-crm.png`) — master-detail admin panel. Pattern maps onto Inventory detail view (left list of items → right detail panel with condition grade + comps + activity log). *recreated: `02-retool-custom-crm`*
4. **Retool — Analytics Dashboard** (`retool-analytics-dashboard.png`) — generic drag-drop dashboard. Useful as a reference for component density across the fold. *recreated: `01-retool-analytics`*
5. **Retool — REST API Admin Panel** (`retool-rest-api-admin.png`) — CRUD-over-REST grammar. If Clawmachine brain ever gets an HTTP layer, this is the admin pattern. *recreated: `06-retool-rest-admin`*
6. **Retool — Employee Directory** (`retool-employee-directory.png`) — search + edit grid. Low-priority for a solo operator, but the search-grid pattern is reusable. *recreated: `07-retool-employee-directory`*
7. **Retool — HR Analytics** (`retool-hr-analytics.png`) — chart-heavy layout; weak fit (Clawmachine has no HR). *recreated: `03-retool-hr-analytics`*
8. **Bubble — Dashboard Gallery** (`bubble-dashboard-gallery.png`) — useful only as a pattern-library reference: see which community templates get 50k+ installs (Ez Dashboard + OpenAI leads). Bubble itself is out-of-scope. *recreated: `08-bubble-dashboard-gallery`*
9. **Bubble — SaaS Gallery** (`bubble-saas-gallery.png`) — same — pattern reference only. *recreated: `09-bubble-saas-template`*
10. **Bravo Studio — Home** (`bravostudio-home.png`) — design-first, warm-palette marketing site. Clawmachine is macOS desktop, not mobile; Bravo's mobile-only focus means the tool is out-of-scope. Kept for completeness. *recreated: `10-bravo-design-to-native`*

## Carry-forward verdict

**Nothing here is code-level reusable** — all three platforms are framework-locked. The carry-forward is limited to:

- KPI-grid grammar (4-across, label-number-delta-sparkline) — generic enough that any dashboard gets it for free.
- Master-detail split for Inventory detail view.
- SOC threat-feed pattern for Mesh page.

None of this requires any of the three platforms' SDKs or runtimes. The Clawmachine Swift app can render the same patterns natively.
