#!/usr/bin/env python3
"""Generate structural HTML recreations across all 8 template-ecosystem subfolders.

Each HTML is a 200-300 line structural approximation based on visible preview images.
All files link ../_shared/dark-dashboard.css for consistent tokens.
These are authored approximations, NOT scraped source code.
"""

import os
import json
from pathlib import Path

ROOT = Path("/Users/regancooney/Projects/consolidate/claude-design-feed/external/templates-v0-framer-webflow")

# --- helpers for fragment composition ---

def head(title, theme="", extra_css=""):
    body_class = f"theme-{theme}" if theme else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../../_shared/dark-dashboard.css">
<style>{extra_css}</style>
</head>
<body class="{body_class}">
"""

def foot():
    return """</body>
</html>
"""

def sidebar(brand, items, active_idx=0):
    nav_html = f'<div class="brand"><div class="brand-mark"></div><div class="brand-name">{brand}</div></div>\n<nav class="nav">\n'
    for i, (group, sub) in enumerate(items):
        if sub is None:
            # single nav-item at top level
            cls = "nav-item active" if i == active_idx else "nav-item"
            nav_html += f'  <div class="{cls}"><span class="nav-icon"></span>{group}</div>\n'
        else:
            nav_html += f'  <div class="nav-group-label">{group}</div>\n'
            for j, name in enumerate(sub):
                cls = "nav-item active" if (i, j) == active_idx else "nav-item"
                nav_html += f'  <div class="{cls}"><span class="nav-icon"></span>{name}</div>\n'
    nav_html += "</nav>\n"
    return f'<aside class="sidebar">\n{nav_html}</aside>\n'

def topbar(title, user="Regan C."):
    return f"""<div class="topbar">
  <div class="row" style="gap:16px"><div class="h2">{title}</div></div>
  <div class="row" style="gap:12px">
    <div class="search"><input class="input" placeholder="Search...\"></div>
    <button class="btn btn-sm">+ New</button>
    <div class="avatar">{user[0]}</div>
  </div>
</div>
"""

def kpi(label, value, delta=None, direction="up", spark_bars=14):
    direction_cls = {"up":"", "down":"down", "flat":"flat"}.get(direction, "")
    delta_html = f'<div class="kpi-delta {direction_cls}">{delta}</div>' if delta else ""
    bars = "".join(
        f'<span style="height:{20 + (i * 37) % 70}%"></span>'
        for i in range(spark_bars)
    )
    return f"""<div class="kpi">
  <div class="kpi-label">{label}</div>
  <div class="kpi-value num">{value}</div>
  {delta_html}
  <div class="kpi-spark">{bars}</div>
</div>
"""

def bar_chart(n=24, seed=1):
    bars = "".join(
        f'<span style="height:{15 + (i * 53 + seed * 17) % 80}%"></span>'
        for i in range(n)
    )
    return f'<div class="chart"><div class="chart-bars">{bars}</div></div>'

def line_chart(seed=1):
    # Simple deterministic polyline
    pts = []
    for i in range(20):
        x = i * (100 / 19)
        y = 50 + 30 * ((i * 31 + seed) % 7 - 3) / 6
        pts.append(f"{x:.1f},{y:.1f}")
    d = "M " + " L ".join(pts)
    area = f"M 0,100 L {pts[0]} L " + " L ".join(pts[1:]) + f" L 100,100 Z"
    return f"""<div class="chart chart-line">
  <svg viewBox="0 0 100 100" preserveAspectRatio="none">
    <defs><linearGradient id="g{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="currentColor" stop-opacity="0.35"/><stop offset="100%" stop-color="currentColor" stop-opacity="0"/></linearGradient></defs>
    <path d="{area}" fill="url(#g{seed})" stroke="none" style="color:var(--accent)"/>
    <path d="{d}" fill="none" stroke="var(--accent)" stroke-width="1.2" vector-effect="non-scaling-stroke"/>
  </svg>
</div>"""

def donut():
    return '<div class="chart-donut"></div>'

def pie():
    return '<div class="chart-pie"></div>'

def table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = ""
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        body += f"<tr>{tds}</tr>"
    return f'<table class="table"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>'

def list_rows(items):
    html = '<div class="list">'
    for avatar, name, meta, badge in items:
        html += f'''<div class="list-row">
  <div class="avatar">{avatar}</div>
  <div class="col" style="gap:2px;flex:1"><div>{name}</div><div class="muted" style="font-size:11px">{meta}</div></div>
  {badge}
</div>'''
    html += "</div>"
    return html

def credit(designer, source_url, platform):
    return f'''<div style="position:fixed;bottom:8px;right:8px;font-size:10px;color:var(--muted-2);background:var(--bg-1);padding:4px 8px;border-radius:4px;border:1px solid var(--line);font-family:var(--mono)">Recreation - inspired by {designer} ({platform}) - <a href="{source_url}" target="_blank" style="color:var(--muted-2)">source</a></div>'''

# =====================================================================
# V0-DEV — 30 dashboard recreations
# =====================================================================

V0_RECREATIONS = [
    # (filename, title, theme, designer, source, config)
    ("01-monky-internal-tool", "M.O.N.K.Y — Internal Tool", "", "joyco", "https://v0.app/templates/b7GDYVxuoGC", "internal-tool"),
    ("02-cyberpunk-tactical-ops", "TACTICAL OPS — Command Center", "cyber", "emmartinzok", "https://v0.app/templates/v9Hg1dBb5o3", "cyberpunk-soc"),
    ("03-financial-dashboard", "Accounts — Transactions Overview", "", "kokonut", "https://v0.app/templates/DuidKNEmCKf", "financial"),
    ("04-shadcn-dashboard", "Documents — Review Queue", "", "estebansuarez", "https://v0.app/templates/Pf7lw1nypu5", "shadcn-datatable"),
    ("05-pulse-incident-response", "Pulse — Incident Response Console", "", "kerroudj", "https://v0.app/templates/3hZwaLtyRbc", "incident-response"),
    ("06-network-traffic-analyzer", "Network Traffic Analyzer", "cyber", "heystu", "https://v0.app/templates/4b4SzAt1CLV", "nta"),
    ("07-nexus-work-mgmt", "Nexus — Work Management", "", "rajoninternet", "https://v0.app/templates/ALfQrxyrJ8b", "work-mgmt"),
    ("08-salesops-dashboard", "SalesOps — Pipeline & Leaderboard", "", "kerroudj", "https://v0.app/templates/9q2Mfgu6cDi", "salesops"),
    ("09-compute-agents", "COMPUTE — Platform for AI Agents", "", "kerroudj", "https://v0.app/templates/Auw4otwlr20", "agents"),
    ("10-analytics-overview", "Analytics — Revenue & Cohorts", "", "generic", "https://v0.app/templates", "analytics"),
    ("11-crm-contacts", "CRM — Contacts & Deals", "", "generic", "https://v0.app/templates", "crm"),
    ("12-project-kanban", "Projects — Kanban Board", "", "generic", "https://v0.app/templates", "kanban"),
    ("13-orders-ecommerce", "Orders — E-commerce Ops", "", "generic", "https://v0.app/templates", "orders"),
    ("14-inventory-stock", "Inventory — Stock Management", "", "generic", "https://v0.app/templates", "inventory"),
    ("15-support-tickets", "Support — Helpdesk Queue", "", "generic", "https://v0.app/templates", "support"),
    ("16-users-access", "Users — Access & Roles", "", "generic", "https://v0.app/templates", "users"),
    ("17-logs-observability", "Observability — Service Logs", "matrix", "generic", "https://v0.app/templates", "logs"),
    ("18-billing-subscriptions", "Billing — Subscriptions", "", "generic", "https://v0.app/templates", "billing"),
    ("19-ai-chat-workbench", "AI Workbench — Chat & Tools", "", "generic", "https://v0.app/templates", "ai-chat"),
    ("20-deploy-infra", "Infra — Deploys & Regions", "", "generic", "https://v0.app/templates", "infra"),
    ("21-kpi-executive", "KPI — Executive Summary", "", "generic", "https://v0.app/templates", "kpi"),
    ("22-finance-treasury", "Finance — Treasury", "", "generic", "https://v0.app/templates", "treasury"),
    ("23-marketing-campaigns", "Marketing — Campaigns", "", "generic", "https://v0.app/templates", "marketing"),
    ("24-hr-people", "HR — People & Orgchart", "", "generic", "https://v0.app/templates", "hr"),
    ("25-research-papers", "Research — Paper Library", "", "generic", "https://v0.app/templates", "research"),
    ("26-iot-fleet", "IoT — Fleet Monitoring", "", "generic", "https://v0.app/templates", "iot"),
    ("27-social-monitor", "Social Monitor — Mentions", "", "generic", "https://v0.app/templates", "social"),
    ("28-legal-contracts", "Legal — Contracts", "", "generic", "https://v0.app/templates", "legal"),
    ("29-content-cms", "Content — CMS Entries", "", "generic", "https://v0.app/templates", "cms"),
    ("30-warehouse-ops", "Warehouse — Pick & Pack", "", "generic", "https://v0.app/templates", "warehouse"),
]

def build_v0_dashboard(fname, title, theme, designer, source, kind):
    """Build a structural dashboard approximation matching v0-style patterns."""
    nav_items_default = [
        ("General", ["Overview", "Analytics", "Projects", "Tasks", "Settings"]),
        ("Team", ["Members", "Activity", "Invites"]),
    ]
    # Customise sidebar per kind
    nav_map = {
        "cyberpunk-soc": [("Command Center", ["Dashboard", "Agent Network", "Operations", "Intelligence", "Systems"]),
                          ("Comms", ["Encrypted Chat", "Mission Log"])],
        "nta": [("NTA Core", ["Monitor", "Packets", "Traffic Origins", "Heatmap"]),
                ("Detect", ["Rules", "Alerts", "Playback"]),
                ("System", ["Exports", "Settings"])],
        "incident-response": [("Pulse", ["Overview", "Incidents", "Deploys", "SLO"]),
                              ("Signals", ["Alerts", "Runbooks"])],
        "financial": [("Accounts", ["Overview", "Transactions", "Savings", "Cards"]),
                      ("Reports", ["Monthly", "Tax"])],
        "crm": [("Sales", ["Pipeline", "Contacts", "Deals", "Activities"]),
                ("Ops", ["Reports", "Settings"])],
        "kanban": [("Workspace", ["Board", "Timeline", "Calendar", "Files"]),
                   ("Team", ["Members"])],
        "orders": [("Store", ["Orders", "Products", "Customers", "Discounts"]),
                   ("Ops", ["Reports", "Settings"])],
        "inventory": [("Stock", ["Items", "Locations", "Receiving", "Transfers"]),
                      ("Reports", ["Valuation", "Aging"])],
        "support": [("Inbox", ["Open", "Pending", "Resolved", "Spam"]),
                    ("Manage", ["Macros", "Teams"])],
        "users": [("IAM", ["Users", "Roles", "Permissions", "Sessions"]),
                  ("Audit", ["Log"])],
        "logs": [("Services", ["All", "web-01", "api-02", "worker-03"]),
                 ("Queries", ["Saved", "Alerts"])],
        "billing": [("Billing", ["Subscriptions", "Invoices", "Plans", "Coupons"]),
                    ("Customers", ["Accounts"])],
        "ai-chat": [("Workbench", ["Chat", "Tools", "Prompts", "Traces"]),
                    ("Models", ["Library"])],
        "infra": [("Infra", ["Overview", "Regions", "Deploys", "Incidents"]),
                  ("Secrets", ["Keys"])],
        "kpi": [("Executive", ["KPIs", "Goals", "OKRs"]),
                ("Detail", ["Revenue", "CS"])],
        "treasury": [("Treasury", ["Positions", "Liquidity", "FX", "Investments"]),
                     ("Risk", ["Exposure"])],
        "marketing": [("Campaigns", ["Active", "Draft", "Completed"]),
                      ("Analytics", ["Attribution", "Channels"])],
        "hr": [("People", ["Directory", "Orgchart", "Leave", "Reviews"]),
                ("Pay", ["Payroll"])],
        "research": [("Library", ["All", "Read", "Unread", "Annotations"]),
                     ("Tags", ["ML", "Bio", "Physics"])],
        "iot": [("Fleet", ["Map", "Devices", "Alerts", "Health"]),
                ("Firmware", ["Rollouts"])],
        "social": [("Monitor", ["Mentions", "Sentiment", "Influencers"]),
                   ("Response", ["Queue"])],
        "legal": [("Contracts", ["Active", "Review", "Archived", "Clauses"]),
                  ("Parties", ["Counterparties"])],
        "cms": [("Content", ["Posts", "Pages", "Media", "Categories"]),
                ("Settings", ["Authors"])],
        "warehouse": [("Operations", ["Pick", "Pack", "Receive", "Ship"]),
                      ("Inventory", ["Bins", "SKUs"])],
        "salesops": [("Sales", ["Pipeline", "Leaderboard", "Forecast"]),
                     ("Team", ["Reps", "Regions"])],
        "agents": [("Agents", ["Runs", "Tools", "Integrations"]),
                   ("Infra", ["Sandboxes", "Logs"])],
        "work-mgmt": [("Work", ["Dashboard", "Projects", "Tasks", "Team"]),
                      ("Settings", ["Workspace"])],
        "shadcn-datatable": [("Library", ["Documents", "Templates", "Trash"]),
                             ("Team", ["Reviewers"])],
        "analytics": [("Reports", ["Overview", "Revenue", "Cohorts", "Retention"]),
                      ("Segments", ["Custom"])],
        "internal-tool": [("Workstation", ["Dashboard", "Chat", "Repairs", "Inventory", "Orders"]),
                          ("Admin", ["Users", "Settings"])],
    }
    items = nav_map.get(kind, nav_items_default)

    # Build content per kind
    content = ""
    if kind == "internal-tool":
        content = f"""<div class="grid grid-4">
  {kpi("Active repairs", "247", "+12 this week")}
  {kpi("In queue", "18", "-3 vs yesterday", "down")}
  {kpi("Avg cycle time", "2.4 d", "-0.3 d")}
  {kpi("Revenue today", "£4,128", "+8%")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr; gap:16px">
  <div class="card">
    <div class="card-hd"><div class="card-title">Active workstreams</div><div class="row" style="gap:8px"><button class="btn btn-sm">Filter</button><button class="btn btn-sm btn-primary">+ Task</button></div></div>
    {table(["Ticket","Device","Assignee","Status","Cycle"], [
      ["CM-2041","iPhone 13 screen","Regan",'<span class="badge badge-good"><span class="dot"></span>In progress</span>',"1.2 d"],
      ["CM-2040","MacBook Air 2020 — battery","Aria",'<span class="badge badge-warn"><span class="dot"></span>Parts wait</span>',"3.1 d"],
      ["CM-2039","iPad Pro 11 — glass","Regan",'<span class="badge badge-good"><span class="dot"></span>In progress</span>',"0.4 d"],
      ["CM-2038","Galaxy S23 — charging","Kai",'<span class="badge"><span class="dot"></span>Queued</span>',"0.0 d"],
      ["CM-2037","Pixel 7 — water damage","Aria",'<span class="badge badge-bad"><span class="dot"></span>Blocked</span>',"4.8 d"],
      ["CM-2036","Switch OLED — joystick","Regan",'<span class="badge badge-good"><span class="dot"></span>QA</span>',"1.8 d"],
    ])}
  </div>
  <div class="card">
    <div class="card-hd"><div class="card-title">Team chat</div><span class="badge">3 online</span></div>
    <div class="list" style="font-size:13px">
      <div><span class="avatar" style="display:inline-flex;margin-right:8px;vertical-align:middle">A</span><b>Aria</b> &middot; parts for CM-2040 arrive Tue</div>
      <div><span class="avatar" style="background:linear-gradient(135deg,var(--teal),var(--accent));display:inline-flex;margin-right:8px;vertical-align:middle">K</span><b>Kai</b> &middot; re-soldering 3 boards before lunch</div>
      <div><span class="avatar" style="background:linear-gradient(135deg,var(--pink),var(--purple));display:inline-flex;margin-right:8px;vertical-align:middle">M</span><b>Mara</b> &middot; Vinted batch listed, 42 items</div>
      <div class="muted">Regan is typing...</div>
    </div>
    <div class="mt-4" style="display:flex;gap:8px"><input class="input" style="flex:1" placeholder="Message team..."><button class="btn btn-primary btn-sm">Send</button></div>
  </div>
</div>"""
    elif kind == "cyberpunk-soc":
        content = f"""<div class="grid grid-4">
  {kpi("AGENTS ACTIVE", "14/18")}
  {kpi("MISSIONS", "247", "+3 today")}
  {kpi("SUCCESS", "94.2%", "+0.8pt")}
  {kpi("THREATS", "3", "+1", "down")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card">
    <div class="card-hd"><div class="card-title mono">[ AGENT NETWORK ]</div><span class="badge badge-good mono">OPERATIONAL</span></div>
    {table(["CALLSIGN","REGION","LINK","ALLOC","STATE"], [
      ["VEX-7","EMEA/UK-SE","82ms",'82%','<span class="badge badge-good mono"><span class="dot"></span>ACTIVE</span>'],
      ["CRUX-2","AMER/US-E","139ms",'41%','<span class="badge badge-good mono"><span class="dot"></span>ACTIVE</span>'],
      ["NOVA-3","EMEA/DE-C","94ms",'67%','<span class="badge badge-warn mono"><span class="dot"></span>STANDBY</span>'],
      ["HALO-9","APAC/SG","209ms",'12%','<span class="badge mono"><span class="dot"></span>IDLE</span>'],
      ["DRIFT-5","AMER/US-W","158ms",'0%','<span class="badge badge-bad mono"><span class="dot"></span>OFFLINE</span>'],
      ["ORBIT-1","EMEA/UK-N","71ms",'91%','<span class="badge badge-good mono"><span class="dot"></span>ACTIVE</span>'],
    ])}
  </div>
  <div class="card">
    <div class="card-hd"><div class="card-title mono">[ ENCRYPTED CHAT ]</div><span class="badge badge-good mono">E2E</span></div>
    <div class="list mono" style="font-size:12px">
      <div class="muted">[04:21:07] CRUX-2 &gt; target engaged, payload deployed</div>
      <div>[04:21:14] CC &gt; confirm receipt, hold position</div>
      <div class="muted">[04:22:08] VEX-7 &gt; perimeter clear, 0 hostiles</div>
      <div>[04:23:02] CC &gt; advance to phase 2</div>
      <div class="muted">[04:25:41] ORBIT-1 &gt; extraction complete</div>
    </div>
  </div>
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title mono">[ MISSION ACTIVITY — 24H ]</div></div>{bar_chart(48, 7)}</div>
  <div class="card"><div class="card-hd"><div class="card-title mono">[ RISK DISTRIBUTION ]</div></div><div class="row" style="gap:20px">{donut()}<div class="col" style="gap:8px;font-size:12px" class="mono"><div><span class="dot" style="color:var(--accent)"></span> LOW &middot; 42%</div><div><span class="dot" style="color:var(--purple)"></span> MED &middot; 30%</div><div><span class="dot" style="color:var(--teal)"></span> HIGH &middot; 16%</div><div><span class="dot" style="color:var(--amber)"></span> CRIT &middot; 12%</div></div></div></div>
</div>"""
    elif kind == "incident-response":
        content = f"""<div class="grid grid-4">
  {kpi("P50 latency", "128ms", "+2ms")}
  {kpi("P95 latency", "412ms", "-18ms", "up")}
  {kpi("P99 latency", "1.28s", "+240ms", "down")}
  {kpi("Uptime 30d", "99.94%", "+0.02pt")}
</div>
<div class="grid grid-2">
  <div class="card">
    <div class="card-hd"><div class="card-title">Live incidents</div><span class="badge badge-bad"><span class="dot"></span>2 active</span></div>
    {table(["ID","Service","Severity","Duration","Owner"], [
      ["INC-412","api-gateway",'<span class="badge badge-bad">P1</span>',"00:14:22","Regan"],
      ["INC-411","worker-dispatch",'<span class="badge badge-warn">P2</span>',"00:47:02","Kai"],
      ["INC-410","redis-01",'<span class="badge badge-good">Resolved</span>',"01:22:00","Aria"],
    ])}
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">Deploy velocity</div></div>{bar_chart(28, 5)}</div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Response time distribution</div></div>{line_chart(2)}</div>"""
    elif kind == "nta":
        content = f"""<div class="grid grid-4">
  {kpi("Packets/s", "82.1K", "+12%")}
  {kpi("Bandwidth", "940 Mbps", "+3%")}
  {kpi("Connections", "12,847")}
  {kpi("Alerts", "7", "+2", "down")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card">
    <div class="card-hd"><div class="card-title mono">PACKET STREAM</div><div class="row"><span class="badge mono">TCP</span><span class="badge mono">UDP</span><span class="badge mono">ICMP</span></div></div>
    {table(["TIME","SRC","DST","PROTO","SIZE"], [
      ["04:21.142","10.0.1.42:443","198.51.100.8:51224","TCP","1428"],
      ["04:21.142","10.0.1.42:443","198.51.100.8:51224","TCP","1428"],
      ["04:21.143","10.0.1.88:53","192.0.2.22:51118","UDP","94"],
      ["04:21.144","10.0.1.42:443","203.0.113.9:62441","TCP","1428"],
      ["04:21.148","10.0.1.118:22","45.33.11.4:45001","TCP","392"],
      ["04:21.149","10.0.1.42:443","198.51.100.8:51224","TCP","224"],
      ["04:21.151","10.0.1.88:80","172.16.0.4:50112","TCP","1428"],
    ])}
  </div>
  <div class="card"><div class="card-hd"><div class="card-title mono">24H HEATMAP</div></div>
    <div style="display:grid;grid-template-columns:repeat(24,1fr);gap:2px;height:180px">""" + "".join(f'<div style="background:rgba(61,124,255,{((i*13+7)%100)/100});border-radius:1px"></div>' for i in range(24*7)) + """</div>
  </div>
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title mono">THREAT RULES</div></div>
    <div class="list"><div class="list-row"><span class="dot" style="color:var(--bad)"></span><span>Port scan from 45.33.11.4</span><span class="badge badge-bad mono">TRIGGERED</span></div>
    <div class="list-row"><span class="dot" style="color:var(--warn)"></span><span>Repeat conn to 198.51.100.8</span><span class="badge badge-warn mono">WATCH</span></div>
    <div class="list-row"><span class="dot" style="color:var(--good)"></span><span>DDoS pattern — upstream</span><span class="badge badge-good mono">CLEAR</span></div>
    <div class="list-row"><span class="dot" style="color:var(--good)"></span><span>Suspicious UDP flood</span><span class="badge badge-good mono">CLEAR</span></div></div>
  </div>
  <div class="card"><div class="card-hd"><div class="card-title mono">REPLAY CONTROLS</div></div>
    <div class="row" style="gap:8px"><button class="btn btn-sm mono">&lt;&lt;</button><button class="btn btn-sm mono">&gt;</button><button class="btn btn-sm mono">&gt;&gt;</button>
    <span class="mono muted">0.25x | 1x | 2x | 4x | 8x</span></div>
    <div class="mt-4 mono" style="font-size:12px">Buffer: 00:14:22 / 01:00:00</div>
    <div class="progress mt-2"><div class="progress-bar" style="width:23%"></div></div>
  </div>
</div>"""
    elif kind == "financial":
        content = f"""<div class="grid grid-4">
  {kpi("Balance", "£24,812", "+£1,204")}
  {kpi("Income 30d", "£8,421", "+12%")}
  {kpi("Spend 30d", "£3,298", "+4%", "down")}
  {kpi("Savings rate", "61%", "+3pt")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card">
    <div class="card-hd"><div class="card-title">Transactions</div><div class="row"><span class="badge">All</span><span class="badge">Income</span><span class="badge">Expense</span></div></div>
    {table(["Date","Merchant","Category","Amount","Account"], [
      ["Apr 20","musicMagpie","Sales","+£42.18","Business"],
      ["Apr 20","Vinted UK","Sales","+£18.00","Business"],
      ["Apr 19","Royal Mail","Shipping","-£12.80","Business"],
      ["Apr 19","CeX","Sales","+£124.00","Business"],
      ["Apr 18","iFixit","Parts","-£38.20","Business"],
      ["Apr 17","BS Exchange","Stock","-£420.00","Business"],
      ["Apr 16","eBay","Sales","+£88.40","Business"],
    ])}
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">Savings goals</div></div>
    <div class="col" style="gap:14px">
      <div><div class="row between"><span>New soldering station</span><span class="num">£320 / £480</span></div><div class="progress mt-2"><div class="progress-bar" style="width:66%"></div></div></div>
      <div><div class="row between"><span>Business emergency fund</span><span class="num">£4,200 / £6,000</span></div><div class="progress mt-2"><div class="progress-bar" style="width:70%"></div></div></div>
      <div><div class="row between"><span>Studio upgrade</span><span class="num">£1,880 / £5,000</span></div><div class="progress mt-2"><div class="progress-bar" style="width:37%"></div></div></div>
    </div>
  </div>
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Monthly flow</div></div>{bar_chart(12, 3)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Category breakdown</div></div><div class="row" style="gap:24px">{donut()}<div class="col" style="gap:6px;font-size:12px"><div><span class="dot" style="color:var(--accent)"></span> Parts &middot; 42%</div><div><span class="dot" style="color:var(--purple)"></span> Stock &middot; 30%</div><div><span class="dot" style="color:var(--teal)"></span> Shipping &middot; 16%</div><div><span class="dot" style="color:var(--amber)"></span> Other &middot; 12%</div></div></div></div>
</div>"""
    elif kind == "shadcn-datatable":
        content = f"""<div class="card">
  <div class="card-hd">
    <div class="card-title">Documents</div>
    <div class="row" style="gap:8px">
      <button class="btn btn-sm">Customise columns</button>
      <button class="btn btn-sm btn-primary">+ Section</button>
    </div>
  </div>
  {table(["Drag","Header","Section","Status","Target","Limit","Reviewer"], [
    ["::",  "Cover page",          "Cover",        '<span class="badge badge-good">In process</span>', "18", "5", '<span class="avatar" style="display:inline-flex;width:24px;height:24px">R</span>'],
    ["::",  "Table of contents",   "TOC",          '<span class="badge badge-good">In process</span>', "29", "24",'<span class="avatar" style="display:inline-flex;width:24px;height:24px">A</span>'],
    ["::",  "Executive summary",   "Summary",      '<span class="badge">Done</span>', "10","13",'<span class="avatar" style="display:inline-flex;width:24px;height:24px">K</span>'],
    ["::",  "Technical approach",  "Technical",    '<span class="badge">Done</span>', "27","23",'<span class="avatar" style="display:inline-flex;width:24px;height:24px">M</span>'],
    ["::",  "Design",              "Design",       '<span class="badge badge-warn">In review</span>',"2", "16",'<span class="avatar" style="display:inline-flex;width:24px;height:24px">R</span>'],
    ["::",  "Capabilities",        "Features",     '<span class="badge badge-warn">In review</span>',"20","8",'<span class="avatar" style="display:inline-flex;width:24px;height:24px">A</span>'],
    ["::",  "Integration w/ APIs", "Integration",  '<span class="badge">Done</span>',  "25","21",'<span class="avatar" style="display:inline-flex;width:24px;height:24px">K</span>'],
    ["::",  "Innovation",          "Features",     '<span class="badge badge-good">In process</span>', "12","9",'<span class="avatar" style="display:inline-flex;width:24px;height:24px">M</span>'],
  ])}
  <div class="row between mt-4 muted" style="font-size:12px">
    <span>0 of 8 row(s) selected</span>
    <div class="row" style="gap:12px"><span>Rows per page 10</span><span>Page 1 of 3</span></div>
  </div>
</div>"""
    elif kind == "salesops":
        content = f"""<div class="grid grid-4">
  {kpi("Pipeline value", "£412K", "+£18K")}
  {kpi("Closed won", "£48K", "+22%")}
  {kpi("Win rate", "34%", "+2pt")}
  {kpi("Avg cycle", "18d", "-2d", "up")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Pipeline by stage</div></div>
    <div class="col" style="gap:10px">
      <div class="row between"><span>Qualify</span><span class="num">£112K &middot; 42 deals</span></div><div class="progress"><div class="progress-bar" style="width:92%"></div></div>
      <div class="row between"><span>Demo</span><span class="num">£84K &middot; 28 deals</span></div><div class="progress"><div class="progress-bar" style="width:68%"></div></div>
      <div class="row between"><span>Proposal</span><span class="num">£61K &middot; 14 deals</span></div><div class="progress"><div class="progress-bar" style="width:51%"></div></div>
      <div class="row between"><span>Negotiate</span><span class="num">£42K &middot; 9 deals</span></div><div class="progress"><div class="progress-bar" style="width:35%"></div></div>
      <div class="row between"><span>Closed won</span><span class="num">£48K &middot; 11 deals</span></div><div class="progress"><div class="progress-bar" style="width:40%;background:var(--good)"></div></div>
    </div>
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">Top performers</div></div>
    """ + list_rows([
      ("R","Regan C.","£92K closed",'<span class="badge badge-good">+18%</span>'),
      ("A","Aria P.","£74K closed",'<span class="badge badge-good">+11%</span>'),
      ("K","Kai J.","£51K closed",'<span class="badge">+4%</span>'),
      ("M","Mara S.","£38K closed",'<span class="badge badge-bad">-2%</span>'),
      ("T","Theo R.","£21K closed",'<span class="badge">+0%</span>'),
    ]) + """
  </div>
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Monthly bookings</div></div>""" + bar_chart(12, 4) + """</div>
  <div class="card"><div class="card-hd"><div class="card-title">Forecast trend</div></div>""" + line_chart(3) + """</div>
</div>"""
    elif kind == "agents":
        content = f"""<div class="grid grid-3">
  {kpi("Agents active", "24")}
  {kpi("Runs/min", "1,842", "+6%")}
  {kpi("Cost today", "$48.12", "+$3")}
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Integrations</div></div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">""" + "".join(f'<div class="card" style="padding:14px;text-align:center;background:var(--bg-2)"><div style="width:32px;height:32px;background:var(--accent);border-radius:8px;margin:0 auto 8px;opacity:0.3"></div><div style="font-size:12px">{name}</div></div>' for name in ["Slack","Gmail","Linear","Notion","GitHub","Stripe","Postgres","Discord"]) + """</div>
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">SDK Example</div></div>
    <pre class="mono" style="background:var(--bg);padding:16px;border-radius:8px;font-size:11px;overflow:auto;color:var(--fg)">import {{ Agent }} from "compute";

const agent = new Agent({{
  model: "claude-opus-4.7",
  tools: [slack, linear, github],
  memory: "persistent",
}});

const result = await agent.run(
  "Triage the three oldest open issues"
);
</pre>
  </div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Region status</div></div>
""" + table(["Region","Agents","Runs/min","P95","Status"], [
  ["us-east-1","8","642","184ms",'<span class="badge badge-good"><span class="dot"></span>healthy</span>'],
  ["us-west-2","6","418","210ms",'<span class="badge badge-good"><span class="dot"></span>healthy</span>'],
  ["eu-west-1","7","521","141ms",'<span class="badge badge-good"><span class="dot"></span>healthy</span>'],
  ["ap-south-1","3","261","312ms",'<span class="badge badge-warn"><span class="dot"></span>degraded</span>'],
]) + """</div>"""
    elif kind == "work-mgmt":
        content = f"""<div class="hero" style="background:linear-gradient(135deg,var(--bg-1),var(--bg-2));border:1px solid var(--line);border-radius:12px;padding:48px 32px;text-align:center;margin-bottom:16px">
  <div class="h1" style="font-size:36px">Work, unified.</div>
  <div class="muted mt-2">Projects, tasks, docs, and dashboards — in one operator-first workspace.</div>
  <div class="row" style="gap:8px;justify-content:center;margin-top:20px"><button class="btn btn-primary">Start free</button><button class="btn">See demo</button></div>
</div>
<div class="grid grid-4">
  {kpi("Active projects", "27")}
  {kpi("Tasks in flight", "184")}
  {kpi("Team members", "14")}
  {kpi("On-time rate", "92%")}
</div>
<div class="card">
  <div class="card-hd"><div class="card-title">Project overview</div></div>
""" + table(["Project","Owner","Progress","Due","Status"], [
  ["Site redesign","Regan",'<div class="progress" style="width:80px"><div class="progress-bar" style="width:64%"></div></div>',"Apr 28",'<span class="badge badge-good">On track</span>'],
  ["Data platform v2","Aria",'<div class="progress" style="width:80px"><div class="progress-bar" style="width:82%"></div></div>',"May 02",'<span class="badge badge-good">On track</span>'],
  ["Retro campaign","Kai",'<div class="progress" style="width:80px"><div class="progress-bar" style="width:34%"></div></div>',"May 12",'<span class="badge badge-warn">At risk</span>'],
  ["Partner portal","Mara",'<div class="progress" style="width:80px"><div class="progress-bar" style="width:21%"></div></div>',"Jun 08",'<span class="badge">Planning</span>'],
]) + """</div>
<div class="grid grid-3">
  <div class="card" style="padding:28px"><div class="h2">Feature-rich</div><div class="muted mt-2">Dashboards, kanban, timeline, automation, and docs — switch without context loss.</div></div>
  <div class="card" style="padding:28px"><div class="h2">Flexible</div><div class="muted mt-2">Every view is configurable. Make it yours.</div></div>
  <div class="card" style="padding:28px"><div class="h2">Fast</div><div class="muted mt-2">Local-first with realtime sync. Works offline.</div></div>
</div>"""
    elif kind == "analytics":
        content = f"""<div class="grid grid-4">
  {kpi("MAU", "412K", "+4.2%")}
  {kpi("Revenue", "$84.2K", "+12.1%")}
  {kpi("Conversion", "3.8%", "+0.4pt")}
  {kpi("Churn", "1.4%", "-0.2pt", "up")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Revenue trend</div></div>{line_chart(5)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Traffic sources</div></div>
    <div class="row" style="gap:20px">{donut()}<div class="col" style="gap:6px;font-size:12px"><div><span class="dot" style="color:var(--accent)"></span> Direct 42%</div><div><span class="dot" style="color:var(--purple)"></span> Search 28%</div><div><span class="dot" style="color:var(--teal)"></span> Social 18%</div><div><span class="dot" style="color:var(--amber)"></span> Referral 12%</div></div></div>
  </div>
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Cohort retention</div></div>
    <div style="display:grid;grid-template-columns:repeat(12,1fr);gap:2px">""" + "".join(f'<div style="aspect-ratio:1;background:rgba(61,124,255,{max(0.1,(100-i*7)/100)});border-radius:2px"></div>' for i in range(12*6)) + """</div>
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">Top pages</div></div>""" + table(["Path","Views","Δ"], [["/","48.2K","+4%"],["/pricing","21.4K","+12%"],["/docs","18.8K","-2%"],["/blog","14.1K","+18%"],["/signup","9.2K","+1%"]]) + """
  </div>
</div>"""
    elif kind == "crm":
        content = f"""<div class="grid grid-4">
  {kpi("Contacts", "12,418", "+241")}
  {kpi("Open deals", "188", "+14")}
  {kpi("Won MTD", "£48K", "+12%")}
  {kpi("Lost MTD", "£18K", "+4%", "down")}
</div>
<div class="card"><div class="card-hd"><div class="card-title">All contacts</div><button class="btn btn-sm btn-primary">+ Contact</button></div>
""" + table(["Name","Company","Stage","Value","Owner","Last touch"], [
  ["Sarah Kim","Meridian Labs",'<span class="badge badge-good">Demo</span>',"£18,400","Regan","2h ago"],
  ["David Chen","Apex Industries",'<span class="badge badge-warn">Proposal</span>',"£42,200","Aria","1d ago"],
  ["Priya N.","Northbound Co",'<span class="badge">Qualify</span>',"£8,400","Kai","3d ago"],
  ["Oliver Reed","Ironbark Ltd",'<span class="badge badge-good">Negotiate</span>',"£120,000","Regan","5h ago"],
  ["Mei Lin","Summit Health",'<span class="badge">Qualify</span>',"£14,800","Mara","1w ago"],
  ["Jonas B.","Harbor Print",'<span class="badge badge-warn">Proposal</span>',"£6,200","Aria","2d ago"],
  ["Ana Silva","Crestview",'<span class="badge">Qualify</span>',"£21,000","Kai","4h ago"],
  ["Ben Aldridge","Loom Media",'<span class="badge badge-good">Demo</span>',"£48,100","Regan","1d ago"],
]) + """</div>"""
    elif kind == "kanban":
        content = """<div class="grid grid-4">
  <div class="card"><div class="card-hd"><div class="card-title">Backlog <span class="badge">12</span></div></div>
    <div class="col" style="gap:8px">
""" + "".join(f'<div class="card" style="padding:12px;background:var(--bg-2)"><div style="font-size:12px;color:var(--muted)">CM-{200+i}</div><div class="mt-2">Task title for card {i+1}</div><div class="row mt-2" style="gap:6px"><span class="badge badge-accent">frontend</span><span class="avatar" style="width:20px;height:20px;font-size:9px">R</span></div></div>' for i in range(4)) + """
    </div>
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">In progress <span class="badge">6</span></div></div>
    <div class="col" style="gap:8px">
""" + "".join(f'<div class="card" style="padding:12px;background:var(--bg-2);border-left:3px solid var(--accent)"><div style="font-size:12px;color:var(--muted)">CM-{210+i}</div><div class="mt-2">Ticket {i+5}</div><div class="row mt-2" style="gap:6px"><span class="badge badge-accent">backend</span><span class="avatar" style="width:20px;height:20px;font-size:9px">A</span></div></div>' for i in range(3)) + """
    </div>
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">Review <span class="badge">3</span></div></div>
    <div class="col" style="gap:8px">
""" + "".join(f'<div class="card" style="padding:12px;background:var(--bg-2);border-left:3px solid var(--warn)"><div style="font-size:12px;color:var(--muted)">CM-{220+i}</div><div class="mt-2">In review {i+8}</div></div>' for i in range(2)) + """
    </div>
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">Done <span class="badge badge-good">18</span></div></div>
    <div class="col" style="gap:8px">
""" + "".join(f'<div class="card" style="padding:12px;background:var(--bg-2);border-left:3px solid var(--good);opacity:0.7"><div style="font-size:12px;color:var(--muted)">CM-{230+i}</div><div class="mt-2">Shipped {i+10}</div></div>' for i in range(3)) + """
    </div>
  </div>
</div>"""
    else:
        # Generic dashboard template
        content = f"""<div class="grid grid-4">
  {kpi("Metric A", "1,284", "+12%")}
  {kpi("Metric B", "£48.2K", "+£3K")}
  {kpi("Metric C", "94.2%", "+0.8pt")}
  {kpi("Metric D", "2.4s", "-0.3s", "up")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Overview</div></div>{bar_chart(28, 9)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Breakdown</div></div>{pie()}</div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Recent activity</div></div>
""" + table(["Item","Owner","Status","Date"], [
  [f"Entry {i+1}", ["Regan","Aria","Kai","Mara"][i%4], ['<span class="badge badge-good">Active</span>','<span class="badge badge-warn">Pending</span>','<span class="badge badge-bad">Blocked</span>','<span class="badge">New</span>'][i%4], f"Apr {20-i}"]
  for i in range(6)
]) + """</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Trend</div></div>""" + line_chart(6) + """</div>
  <div class="card"><div class="card-hd"><div class="card-title">Heatmap 7d</div></div>
    <div style="display:grid;grid-template-columns:repeat(24,1fr);gap:2px;height:120px">""" + "".join(f'<div style="background:rgba(61,124,255,{((i*11+3)%100)/100});border-radius:1px"></div>' for i in range(24*4)) + """</div>
  </div>
</div>"""

    html = head(title, theme)
    html += '<div class="app">\n'
    html += sidebar("CLAWMACHINE", items, (0, 0))
    html += '<div class="main">\n'
    html += topbar(title)
    html += f'<div class="content">\n{content}\n</div>\n'
    html += '</div></div>\n'
    html += credit(designer, source, "v0.app")
    html += foot()
    return html


def write_v0():
    dest = ROOT / "v0-dev" / "recreated"
    dest.mkdir(parents=True, exist_ok=True)
    for fname, title, theme, designer, source, kind in V0_RECREATIONS:
        html = build_v0_dashboard(fname, title, theme, designer, source, kind)
        (dest / f"{fname}.html").write_text(html)
    print(f"Wrote {len(V0_RECREATIONS)} v0-dev recreations")


# =====================================================================
# FRAMER TEMPLATES — 10 recreations
# =====================================================================

FRAMER_RECREATIONS = [
    ("01-dash-saas-landing", "Dash — SaaS Landing", "Yadwinder Singh", "https://www.framer.com/marketplace/templates/dash/", "saas-landing"),
    ("02-dashcraft-agency", "Dashcraft — Creative Agency", "Emily Clarke", "https://www.framer.com/marketplace/templates/dashcraft/", "agency"),
    ("03-dashsynt-clean-saas", "DashSynt — Advanced SaaS", "Asad Synt", "https://www.framer.com/marketplace/templates/dashsynt/", "saas-clean"),
    ("04-dashbar-portfolio", "Dashbar — Personal Site", "Masbobz Works", "https://www.framer.com/marketplace/templates/dashbar/", "portfolio-sidebar"),
    ("05-aegis-ai-saas", "Aegis — AI & SaaS", "Dan W", "https://www.framer.com/marketplace/templates/aegis/", "ai-saas"),
    ("06-dashfolio-n2", "Dashfolio N2 — Portfolio", "Dashfolio Studio", "https://www.framer.com/marketplace/templates/dashfolio-n2/", "portfolio"),
    ("07-dashboard-productivity", "DashX — Productivity App", "Framer Creator", "https://www.framer.com/marketplace/templates/", "productivity"),
    ("08-studio-portfolio", "Studio — Dark Portfolio", "Framer Creator", "https://www.framer.com/marketplace/templates/", "studio-dark"),
    ("09-fintech-landing", "Vault — Fintech Landing", "Framer Creator", "https://www.framer.com/marketplace/templates/", "fintech"),
    ("10-agency-dark", "Mono — Agency Dark", "Framer Creator", "https://www.framer.com/marketplace/templates/", "mono-dark"),
]

def build_framer_landing(title, designer, source, kind):
    """Framer templates are marketing sites. Build landing-page approximations."""
    nav = """<nav style="position:sticky;top:0;z-index:10;background:rgba(10,10,11,0.85);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);padding:16px 48px;display:flex;align-items:center;justify-content:space-between">
  <div class="row" style="gap:10px"><div class="brand-mark"></div><div class="brand-name">""" + title.split('—')[0].strip() + """</div></div>
  <div class="row" style="gap:32px;font-size:14px">
    <a style="color:var(--muted)">Features</a><a style="color:var(--muted)">Pricing</a><a style="color:var(--muted)">Templates</a><a style="color:var(--muted)">Docs</a>
  </div>
  <div class="row" style="gap:8px"><button class="btn btn-sm btn-ghost">Sign in</button><button class="btn btn-sm btn-primary">Get started</button></div>
</nav>"""

    # hero variants
    if kind == "saas-landing":
        hero = """<section style="padding:120px 48px 80px;text-align:center;background:radial-gradient(ellipse at top,rgba(61,124,255,0.18),transparent 60%)">
  <span class="badge" style="margin-bottom:24px">New — v2.4 released</span>
  <h1 style="font-size:72px;font-weight:600;letter-spacing:-0.03em;line-height:1.05;max-width:900px;margin:0 auto">The dashboard<br><span style="background:linear-gradient(90deg,var(--accent),var(--purple));-webkit-background-clip:text;background-clip:text;color:transparent">teams actually ship with.</span></h1>
  <p class="muted" style="font-size:18px;max-width:560px;margin:24px auto">Launch an operator-grade surface in minutes. No config, no sprawl. 12 pages, every breakpoint.</p>
  <div class="row" style="gap:12px;justify-content:center;margin-top:32px"><button class="btn btn-primary" style="padding:14px 28px;font-size:15px">Start free trial</button><button class="btn" style="padding:14px 28px;font-size:15px">Watch demo (2:18)</button></div>
  <div style="max-width:1100px;margin:64px auto 0;aspect-ratio:16/9;background:linear-gradient(135deg,var(--bg-1),var(--bg-2));border:1px solid var(--line);border-radius:16px;position:relative;overflow:hidden">
    <div style="position:absolute;inset:24px;background:var(--bg);border-radius:8px;display:grid;grid-template-columns:200px 1fr">
      <div style="background:var(--bg-1);border-right:1px solid var(--line)"></div>
      <div style="padding:24px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;grid-template-rows:auto 1fr"><div style="background:var(--bg-2);border-radius:6px;height:80px"></div><div style="background:var(--bg-2);border-radius:6px;height:80px"></div><div style="background:var(--bg-2);border-radius:6px;height:80px"></div><div style="background:var(--bg-2);border-radius:6px;grid-column:span 2"></div><div style="background:var(--bg-2);border-radius:6px"></div></div>
    </div>
  </div>
</section>"""
    elif kind == "agency":
        hero = """<section style="padding:120px 48px 80px;text-align:center">
  <h1 style="font-size:96px;font-weight:500;letter-spacing:-0.04em;line-height:0.95">We build<br><i style="font-family:serif;font-weight:400">digital presence.</i></h1>
  <p class="muted" style="font-size:18px;max-width:520px;margin:32px auto">Creative studio crafting brand systems, websites, and products for modern teams.</p>
  <button class="btn btn-primary" style="padding:14px 36px;margin-top:24px">Start a project →</button>
</section>
<section style="padding:48px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px">
""" + "".join(f'<div style="aspect-ratio:4/3;background:linear-gradient(135deg,{["var(--accent)","var(--purple)","var(--teal)","var(--amber)","var(--pink)","var(--bad)"][i%6]},var(--bg-2));border-radius:16px;position:relative;overflow:hidden"><div style="position:absolute;bottom:16px;left:16px;color:white;font-size:13px">Project {i+1:02d} — Case study</div></div>' for i in range(6)) + """
</section>"""
    elif kind == "saas-clean":
        hero = """<section style="padding:100px 48px;text-align:center;border-bottom:1px solid var(--line)">
  <h1 style="font-size:64px;font-weight:500;letter-spacing:-0.03em;line-height:1.1">Minimal by design.<br>Powerful under the hood.</h1>
  <p class="muted" style="font-size:17px;max-width:520px;margin:24px auto">A 3-page SaaS template for teams that hate clutter.</p>
  <button class="btn btn-primary" style="margin-top:24px">View demo</button>
</section>
<section style="padding:80px 48px;display:grid;grid-template-columns:repeat(3,1fr);gap:32px;max-width:1100px;margin:0 auto">
""" + "".join(f'<div><div style="font-size:48px;font-weight:500;letter-spacing:-0.02em">0{i+1}</div><div class="h2 mt-2">{name}</div><div class="muted mt-2">{desc}</div></div>' for i, (name, desc) in enumerate([("Clean components","No gloss, no glass. Just the geometry teams build with."),("System-first","Typography, spacing, colour — locked to a grid that scales."),("Ship fast","Three pages, every breakpoint. Deploy Monday, iterate all week.")])) + """
</section>"""
    elif kind == "portfolio-sidebar":
        hero = """<div style="display:grid;grid-template-columns:280px 1fr;min-height:100vh">
  <aside style="background:var(--bg-1);border-right:1px solid var(--line);padding:32px 24px;display:flex;flex-direction:column;gap:24px">
    <div class="brand"><div class="brand-mark"></div><div class="brand-name">Dashbar</div></div>
    <div class="col" style="gap:6px">
      <div class="muted" style="font-size:11px;text-transform:uppercase">Portfolio</div>
      <a class="nav-item active">Home</a><a class="nav-item">Work</a><a class="nav-item">About</a><a class="nav-item">Journal</a><a class="nav-item">Contact</a>
    </div>
    <div style="margin-top:auto">
      <div class="muted" style="font-size:11px;text-transform:uppercase;margin-bottom:8px">Connect</div>
      <div class="col" style="gap:4px;font-size:13px"><a class="muted">X / Twitter</a><a class="muted">Dribbble</a><a class="muted">LinkedIn</a></div>
    </div>
  </aside>
  <main style="padding:80px 64px">
    <div class="muted" style="font-size:13px">Designer &middot; UK &middot; Available from May</div>
    <h1 style="font-size:72px;font-weight:500;letter-spacing:-0.03em;margin-top:24px;line-height:1.05">Portfolio of<br><i style="font-family:serif">considered design.</i></h1>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:64px">""" + "".join(f'<div style="aspect-ratio:4/3;background:var(--bg-2);border:1px solid var(--line);border-radius:12px;padding:24px;display:flex;flex-direction:column;justify-content:flex-end"><div class="muted" style="font-size:12px">2025 &middot; Brand</div><div class="h2 mt-2">Project Title {i+1}</div></div>' for i in range(4)) + """</div>
  </main>
</div>"""
    elif kind == "ai-saas":
        hero = """<section style="padding:120px 48px 80px;text-align:center;background:radial-gradient(ellipse at top,rgba(167,139,250,0.18),transparent 60%)">
  <span class="badge badge-accent" style="margin-bottom:24px">AEGIS — AI infrastructure</span>
  <h1 style="font-size:72px;font-weight:500;letter-spacing:-0.03em;line-height:1.05;max-width:880px;margin:0 auto">Deploy AI agents<br>without the<br><span style="background:linear-gradient(90deg,var(--purple),var(--pink));-webkit-background-clip:text;background-clip:text;color:transparent">plumbing.</span></h1>
  <p class="muted" style="font-size:18px;max-width:560px;margin:24px auto">Prompts, tools, memory, and deploys — unified. Ship an agent in under an hour.</p>
  <div class="row" style="gap:12px;justify-content:center;margin-top:32px"><button class="btn btn-primary">Start building</button><button class="btn">Read docs</button></div>
</section>
<section style="padding:80px 48px;background:var(--bg-1);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:32px">
""" + "".join(f'<div><div style="color:var(--purple);font-size:24px;font-weight:500">{v}</div><div class="muted mt-2">{l}</div></div>' for v,l in [("1.2M+","Agent runs/day"),("48ms","Median latency"),("99.99%","SLA uptime"),("200+","Integrations"),]) + """
  </div>
</section>"""
    elif kind == "portfolio":
        hero = """<section style="padding:80px 48px;text-align:center">
  <div class="muted" style="font-size:13px;letter-spacing:0.1em;text-transform:uppercase">Portfolio 2026</div>
  <h1 style="font-size:120px;font-weight:500;letter-spacing:-0.04em;line-height:0.95;margin-top:16px">Selected<br><i style="font-family:serif;font-weight:400">works.</i></h1>
</section>
<section style="padding:48px;display:grid;grid-template-columns:repeat(12,1fr);gap:12px">
""" + "".join(f'<div style="grid-column:span {[6,6,4,4,4,8,4][i]};aspect-ratio:{["16/10","16/10","1","1","1","21/9","3/4"][i]};background:linear-gradient(135deg,{["var(--accent)","var(--purple)","var(--teal)","var(--amber)","var(--pink)","var(--bad)","var(--good)"][i]},var(--bg-2));border-radius:16px"></div>' for i in range(7)) + """
</section>"""
    elif kind == "productivity":
        hero = """<section style="padding:96px 48px 64px;text-align:center">
  <h1 style="font-size:68px;font-weight:500;letter-spacing:-0.03em;line-height:1.05">Your workday,<br>structured.</h1>
  <p class="muted mt-4" style="font-size:17px;max-width:480px;margin:24px auto">A productivity suite for teams that plan, execute, and review — in one place.</p>
  <button class="btn btn-primary" style="margin-top:24px">Try it free</button>
</section>
<section style="max-width:1200px;margin:64px auto;padding:0 48px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
""" + "".join(f'<div class="card" style="padding:32px"><div style="width:40px;height:40px;background:var(--accent);opacity:0.2;border-radius:10px;margin-bottom:16px"></div><div class="h2">{t}</div><div class="muted mt-2">{d}</div></div>' for t,d in [("Tasks","Kanban, list, and calendar — synced."),("Docs","Blocks, embeds, and @mentions."),("Review","Weekly and quarterly cycles built in.")]) + """
</section>"""
    elif kind == "studio-dark":
        hero = """<section style="padding:160px 48px 80px;text-align:left;max-width:1200px;margin:0 auto">
  <div class="muted" style="font-size:12px;letter-spacing:0.15em;text-transform:uppercase">Independent studio &middot; Est. 2019</div>
  <h1 style="font-size:128px;font-weight:500;letter-spacing:-0.04em;line-height:0.95;margin-top:24px">Brand<br>systems,<br><i style="font-family:serif;font-weight:400;color:var(--muted)">built to last.</i></h1>
  <div class="row" style="gap:16px;margin-top:48px"><button class="btn btn-primary">Start a project</button><button class="btn btn-ghost">View work →</button></div>
</section>
<section style="padding:96px 48px;border-top:1px solid var(--line)">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(2,1fr);gap:24px">
""" + "".join(f'<div style="aspect-ratio:4/3;background:var(--bg-1);border:1px solid var(--line);border-radius:16px;padding:32px;display:flex;flex-direction:column;justify-content:space-between"><div class="muted">0{i+1}</div><div><div class="h2">Case {i+1}</div><div class="muted mt-2">Brand system, 2025</div></div></div>' for i in range(4)) + """
  </div>
</section>"""
    elif kind == "fintech":
        hero = """<section style="padding:120px 48px 80px;text-align:center">
  <span class="badge badge-accent">Vault — FCA-regulated</span>
  <h1 style="font-size:72px;font-weight:500;letter-spacing:-0.03em;line-height:1.05;max-width:880px;margin:32px auto 0">The business account<br>that respects your time.</h1>
  <p class="muted mt-4" style="font-size:17px;max-width:520px;margin:24px auto">Multi-currency, instant payouts, no monthly fee. For UK-incorporated teams.</p>
  <button class="btn btn-primary" style="margin-top:24px">Open an account</button>
</section>
<section style="padding:48px;max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
""" + "".join(f'<div class="card" style="padding:32px"><div class="h2">{t}</div><div class="muted mt-2">{d}</div></div>' for t,d in [("Multi-currency","Hold GBP, EUR, USD in one account."),("Instant payouts","SEPA Instant, Faster Payments, SWIFT."),("API-first","Full API coverage and webhooks.")]) + """
</section>"""
    else:  # mono-dark
        hero = """<section style="padding:120px 48px;text-align:left;max-width:1200px;margin:0 auto">
  <h1 style="font-size:128px;font-weight:500;letter-spacing:-0.04em;line-height:0.9">Mono.<br><i style="font-family:serif;font-weight:400">A studio.</i></h1>
  <p class="muted mt-4" style="font-size:18px;max-width:480px;margin-top:32px">We design things for people who already know what they want.</p>
</section>
<section style="padding:64px 48px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;font-family:var(--mono);font-size:12px;color:var(--muted)">
    <div>SERVICES<br><br>Brand<br>Product<br>Web<br>Identity</div>
    <div>CLIENTS<br><br>2025<br>— Ashpine<br>— Redway<br>— Ironbark<br>— Northcliffe</div>
    <div>AWARDS<br><br>Type 2025<br>Awwwards SOTY<br>CSS Design Awards<br>The FWA</div>
    <div>CONTACT<br><br>hello@mono.studio<br>+44 20 ...<br>London + NYC</div>
  </div>
</section>"""

    html = head(title)
    html += nav + hero
    if kind != "portfolio-sidebar":
        # common feature section
        html += """<section style="padding:80px 48px;border-top:1px solid var(--line)">
  <div style="max-width:1100px;margin:0 auto">
    <div class="muted" style="font-size:13px;letter-spacing:0.08em;text-transform:uppercase">Features</div>
    <h2 style="font-size:48px;font-weight:500;letter-spacing:-0.02em;margin-top:8px">Built for teams that ship.</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:48px">
""" + "".join(f'<div class="card" style="padding:28px"><div style="width:36px;height:36px;background:linear-gradient(135deg,var(--accent),var(--purple));border-radius:8px;margin-bottom:16px"></div><div class="h2">{t}</div><div class="muted mt-2">{d}</div></div>' for t,d in [("A11y","WCAG 2.1 AA across all pages."),("Animations","60fps, reduced-motion aware."),("SEO","OpenGraph, JSON-LD, sitemap."),("Analytics","Umami/Plausible-ready."),("Components","40+ reusable sections."),("Visual Breakpoints","Desktop, tablet, mobile.")]) + """
    </div>
  </div>
</section>
<footer style="padding:48px;text-align:center;border-top:1px solid var(--line);color:var(--muted);font-size:13px">
  &copy; 2026 """ + title.split('—')[0].strip() + """ — recreated for research
</footer>"""
    html += credit(designer, source, "Framer Marketplace")
    html += foot()
    return html


def write_framer():
    dest = ROOT / "framer-templates" / "recreated"
    dest.mkdir(parents=True, exist_ok=True)
    for fname, title, designer, source, kind in FRAMER_RECREATIONS:
        (dest / f"{fname}.html").write_text(build_framer_landing(title, designer, source, kind))
    print(f"Wrote {len(FRAMER_RECREATIONS)} framer recreations")


# =====================================================================
# WEBFLOW TEMPLATES — 10 recreations
# =====================================================================

WEBFLOW_RECREATIONS = [
    ("01-dashdark-x", "Dashdark X — Dark Admin", "BRIX Templates", "https://webflow.com/templates/html/dashdark-x-devlink-website-template", "admin-dark"),
    ("02-dashflow-x", "Dashflow X — SaaS Admin", "BRIX Templates", "https://webflow.com/templates", "saas-admin"),
    ("03-dashkit", "Dashkit — Startup Admin", "BRIX Templates", "https://webflow.com/templates", "startup-admin"),
    ("04-dark-dasher", "Dark Dasher — Creative Admin", "BRIX Templates", "https://webflow.com/templates", "creative-admin"),
    ("05-finanza", "Finanza — Financial Dashboard", "Webflow Creator", "https://webflow.com/templates", "finance-admin"),
    ("06-analytiq", "Analytiq — Analytics Admin", "Webflow Creator", "https://webflow.com/templates", "analytics-admin"),
    ("07-commerce-admin", "Commerce Admin", "Webflow Creator", "https://webflow.com/templates", "commerce-admin"),
    ("08-crm-control", "CRM Control — Sales Admin", "Webflow Creator", "https://webflow.com/templates", "crm-admin"),
    ("09-project-orbit", "Project Orbit — PM Admin", "Webflow Creator", "https://webflow.com/templates", "pm-admin"),
    ("10-support-cloud", "Support Cloud — Help Admin", "Webflow Creator", "https://webflow.com/templates", "support-admin"),
]

def build_webflow_admin(title, designer, source, kind):
    """Webflow admin templates — dark admin UI approximations."""
    sidebar_items = [
        ("Main", ["Dashboard", "Analytics", "Reports"]),
        ("Manage", ["Customers", "Products", "Orders", "Inventory"]),
        ("Account", ["Settings", "Team", "Billing"]),
    ]

    if kind == "finance-admin":
        content = f"""<div class="grid grid-4">
  {kpi("Total balance", "£248,412", "+£12.8K")}
  {kpi("Income MTD", "£42.1K", "+18%")}
  {kpi("Spend MTD", "£14.8K", "+4%", "down")}
  {kpi("Net MTD", "£27.3K", "+22%")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Revenue vs spend</div><div class="row" style="gap:6px"><span class="badge">7d</span><span class="badge badge-accent">30d</span><span class="badge">90d</span><span class="badge">1y</span></div></div>{line_chart(7)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Account mix</div></div><div class="row" style="gap:16px">{donut()}<div class="col" style="gap:6px;font-size:12px"><div><span class="dot" style="color:var(--accent)"></span>Main 48%</div><div><span class="dot" style="color:var(--purple)"></span>Savings 28%</div><div><span class="dot" style="color:var(--teal)"></span>FX 16%</div><div><span class="dot" style="color:var(--amber)"></span>Reserve 8%</div></div></div></div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Recent transactions</div></div>
""" + table(["Date","Merchant","Category","Account","Amount"], [
  ["Apr 20","Stripe payout","Revenue","Main","+£4,210.82"],
  ["Apr 20","AWS","Infrastructure","Main","-£412.04"],
  ["Apr 19","Payroll","Payroll","Main","-£18,422.00"],
  ["Apr 19","Client — Meridian","Revenue","Main","+£12,000.00"],
  ["Apr 18","Notion Labs","SaaS","Main","-£412.00"],
]) + "</div>"
    elif kind == "commerce-admin":
        content = f"""<div class="grid grid-4">
  {kpi("Orders", "1,284", "+48")}
  {kpi("Revenue", "£48.2K", "+12%")}
  {kpi("AOV", "£37.60", "+4%")}
  {kpi("Cart abandonment", "68%", "-2pt", "up")}
</div>
<div class="card"><div class="card-hd"><div class="card-title">Recent orders</div><button class="btn btn-sm btn-primary">+ Order</button></div>
""" + table(["Order","Customer","Items","Total","Status","Placed"], [
  ["#4821","S. Kim","3","£84.20",'<span class="badge badge-good">Fulfilled</span>',"2h ago"],
  ["#4820","D. Chen","1","£42.00",'<span class="badge badge-warn">Processing</span>',"3h ago"],
  ["#4819","P. Nair","2","£68.40",'<span class="badge badge-good">Fulfilled</span>',"5h ago"],
  ["#4818","O. Reed","5","£124.00",'<span class="badge badge-warn">Processing</span>',"6h ago"],
  ["#4817","M. Lin","1","£18.00",'<span class="badge badge-bad">Refunded</span>',"8h ago"],
  ["#4816","J. Brandt","2","£52.40",'<span class="badge badge-good">Fulfilled</span>',"1d ago"],
]) + """</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Sales — last 30d</div></div>""" + bar_chart(30, 2) + """</div>
  <div class="card"><div class="card-hd"><div class="card-title">Top products</div></div>
""" + list_rows([
  ("P1","Soldering station Pro","128 sold",'<span class="badge badge-good">+18%</span>'),
  ("P2","USB microscope","84 sold",'<span class="badge badge-good">+12%</span>'),
  ("P3","Tweezer set","62 sold",'<span class="badge">+4%</span>'),
  ("P4","Heat gun","48 sold",'<span class="badge badge-bad">-2%</span>'),
]) + "</div></div>"
    elif kind == "crm-admin":
        content = f"""<div class="grid grid-4">
  {kpi("Leads", "412", "+28")}
  {kpi("Open deals", "88", "+4")}
  {kpi("Revenue this quarter", "£124K", "+£18K")}
  {kpi("Win rate", "34%", "+2pt")}
</div>
<div class="card"><div class="card-hd"><div class="card-title">Deal pipeline</div><button class="btn btn-sm btn-primary">+ Deal</button></div>
""" + table(["Deal","Contact","Stage","Value","Close date","Owner"], [
  ["Meridian renewal","S. Kim",'<span class="badge badge-good">Negotiate</span>',"£42,200","Apr 30","Regan"],
  ["Apex onboarding","D. Chen",'<span class="badge">Qualify</span>',"£12,000","May 08","Aria"],
  ["Northbound expansion","P. Nair",'<span class="badge badge-warn">Proposal</span>',"£28,400","May 02","Kai"],
  ["Ironbark Q2","O. Reed",'<span class="badge badge-good">Demo</span>',"£84,200","May 22","Regan"],
]) + "</div>"
    else:
        content = f"""<div class="grid grid-4">
  {kpi("Active users", "12,412", "+4%")}
  {kpi("Sessions", "84,218", "+8%")}
  {kpi("Avg duration", "4m 18s", "+12s")}
  {kpi("Bounce rate", "42%", "-2pt", "up")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Sessions — last 30d</div></div>{line_chart(8)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Devices</div></div>{donut()}</div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Recent activity</div></div>
""" + table(["Time","User","Action","Page","Duration"], [
  ["04:21","sarah@meridian","Viewed","/pricing","2:18"],
  ["04:19","david@apex","Signed up","/signup","0:48"],
  ["04:12","priya@north","Viewed","/docs","5:42"],
  ["04:08","oliver@ironbark","Exported","/reports","1:22"],
  ["04:01","mei@summit","Viewed","/","0:28"],
]) + "</div>"

    html = head(title)
    html += '<div class="app">\n' + sidebar(title.split('—')[0].strip(), sidebar_items, (0, 0)) + '<div class="main">\n'
    html += topbar(title)
    html += f'<div class="content">\n{content}\n</div>\n'
    html += '</div></div>\n'
    html += credit(designer, source, "Webflow Templates")
    html += foot()
    return html


def write_webflow():
    dest = ROOT / "webflow-templates" / "recreated"
    dest.mkdir(parents=True, exist_ok=True)
    for fname, title, designer, source, kind in WEBFLOW_RECREATIONS:
        (dest / f"{fname}.html").write_text(build_webflow_admin(title, designer, source, kind))
    print(f"Wrote {len(WEBFLOW_RECREATIONS)} webflow recreations")


# =====================================================================
# NOTION TEMPLATES — 10 recreations (HTML approximations of Notion IA)
# =====================================================================

NOTION_RECREATIONS = [
    ("01-jobs-dashboard", "Jobs Dashboard", "Notion Community", "https://notion.so/templates/jobs-dashboard"),
    ("02-task-management", "Task Management Dashboard", "Emmanuel Ogwuma", "https://notion.so/templates/task-management-dashboard-141"),
    ("03-life-dashboard", "Life Dashboard", "MuchelleB", "https://notion.so/templates/life-dashboard"),
    ("04-2026-life-planner", "2026 Life Planner", "Notion Community", "https://notion.so/templates/life-planner-dashboard"),
    ("05-digital-seller", "Digital Product Seller OS", "Notion Community", "https://notion.so/templates/digital-product-seller-dashboard"),
    ("06-content-hq", "Content & Social Media HQ", "Notion Community", "https://notion.so/templates/content-social-media-hq"),
    ("07-applicant-tracker", "Applicant Tracker w/ Automations", "Notion", "https://notion.so/templates/applicant-tracker-with-automations"),
    ("08-3d-printing-mgmt", "3D Printing Management", "Notion Community", "https://notion.so/templates/advanced-3d-printing-management-system"),
    ("09-grant-tracking", "Grant Tracking System", "Lavender E", "https://notion.so/templates/grant-tracking-management-system"),
    ("10-execution-os", "Execution OS", "Notion Community", "https://notion.so/templates/execution-os"),
]

NOTION_CSS = """
.notion { background: #1f1f1f; color: #e2e2e0; font-family: -apple-system, Inter, sans-serif; padding: 64px 96px; min-height: 100vh; max-width: 960px; margin: 0 auto; }
.notion-hero { font-size: 40px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 8px; display: flex; gap: 12px; align-items: center; }
.notion-emoji { font-size: 44px; }
.notion-description { color: #9b9b9b; margin-bottom: 32px; }
.notion-h2 { font-size: 24px; font-weight: 600; margin: 48px 0 12px; display: flex; gap: 8px; align-items: center; }
.notion-h3 { font-size: 18px; font-weight: 600; margin: 24px 0 8px; }
.notion-callout { display: flex; gap: 12px; background: #2d2d2d; border-radius: 6px; padding: 16px; margin: 16px 0; }
.notion-callout-icon { font-size: 20px; }
.notion-cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 16px 0; }
.notion-col { background: #2a2a2a; border-radius: 6px; padding: 14px 16px; }
.notion-col-title { color: #9b9b9b; font-size: 13px; margin-bottom: 6px; }
.notion-table { width: 100%; border-collapse: collapse; margin: 16px 0; border: 1px solid #333; }
.notion-table th, .notion-table td { border: 1px solid #333; padding: 10px 14px; text-align: left; font-size: 14px; }
.notion-table th { background: #2a2a2a; color: #9b9b9b; font-weight: 500; font-size: 12px; }
.notion-tag { background: rgba(200, 100, 50, 0.2); color: #e07848; border-radius: 4px; padding: 1px 8px; font-size: 12px; }
.notion-tag-blue { background: rgba(68, 131, 237, 0.2); color: #6a96de; }
.notion-tag-green { background: rgba(76, 175, 80, 0.2); color: #77aa7a; }
.notion-tag-purple { background: rgba(168, 127, 203, 0.2); color: #a87fcb; }
.notion-check { color: #6bb562; margin-right: 8px; }
.notion-gallery { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 16px 0; }
.notion-card { background: #2a2a2a; border: 1px solid #333; border-radius: 6px; padding: 14px; }
.notion-card-cover { background: linear-gradient(135deg, #4a5568, #2d3748); height: 80px; border-radius: 4px; margin-bottom: 10px; }
.notion-p { margin: 8px 0; }
.notion-divider { border-top: 1px solid #333; margin: 32px 0; }
.notion-toggle { cursor: pointer; background: #262626; border-radius: 4px; padding: 8px 12px; margin: 4px 0; }
"""

def build_notion(title, designer, source, idx):
    hero_emojis = ["[target]", "[chart]", "[sparkle]", "[calendar]", "[package]", "[note]", "[people]", "[print]", "[money]", "[check]"]
    emoji = hero_emojis[idx % len(hero_emojis)]

    body = f"""<div class="notion">
  <div class="notion-hero"><span class="notion-emoji">{emoji}</span>{title}</div>
  <div class="notion-description">A Notion workspace template — recreated as HTML for research. Original by {designer}.</div>

  <div class="notion-callout"><div class="notion-callout-icon">[i]</div><div><b>How to use.</b> Duplicate this template to your workspace. Customise the databases for your own workflows. Every block here is optional — keep what works, delete the rest.</div></div>

  <div class="notion-cols">
    <div class="notion-col"><div class="notion-col-title">Owner</div><div>Regan C.</div></div>
    <div class="notion-col"><div class="notion-col-title">Last updated</div><div>Apr 21, 2026</div></div>
    <div class="notion-col"><div class="notion-col-title">Status</div><div><span class="notion-tag notion-tag-green">Active</span></div></div>
    <div class="notion-col"><div class="notion-col-title">Template</div><div>v2.4</div></div>
  </div>

  <div class="notion-h2">[pin] Overview</div>
  <div class="notion-p">This dashboard centralises the operational flows for {title.lower()}. Every database below is linked — changing a property in one reflects everywhere else.</div>

  <div class="notion-h2">[sparkle] Key databases</div>
  <table class="notion-table">
    <thead><tr><th>Database</th><th>Purpose</th><th>Items</th><th>Last edit</th></tr></thead>
    <tbody>
      <tr><td>Items</td><td>Primary records</td><td>248</td><td>Today</td></tr>
      <tr><td>Status</td><td>Workflow states</td><td>6</td><td>Apr 12</td></tr>
      <tr><td>People</td><td>Contacts & assignees</td><td>14</td><td>Apr 18</td></tr>
      <tr><td>Notes</td><td>Linked docs</td><td>42</td><td>Today</td></tr>
      <tr><td>Archive</td><td>Closed items</td><td>1,284</td><td>Apr 20</td></tr>
    </tbody>
  </table>

  <div class="notion-h2">[table] Active items</div>
  <table class="notion-table">
    <thead><tr><th>Name</th><th>Status</th><th>Owner</th><th>Priority</th><th>Due</th></tr></thead>
    <tbody>
      <tr><td>First entry for {title.split(' ')[0].lower()} flow</td><td><span class="notion-tag notion-tag-green">In progress</span></td><td>Regan</td><td><span class="notion-tag">High</span></td><td>Apr 25</td></tr>
      <tr><td>Second tracked item with longer name</td><td><span class="notion-tag notion-tag-blue">Queued</span></td><td>Aria</td><td><span class="notion-tag notion-tag-purple">Med</span></td><td>Apr 28</td></tr>
      <tr><td>Third item requiring review</td><td><span class="notion-tag">To do</span></td><td>Kai</td><td><span class="notion-tag">High</span></td><td>Apr 30</td></tr>
      <tr><td>Fourth item — awaiting approval</td><td><span class="notion-tag notion-tag-green">In progress</span></td><td>Mara</td><td><span class="notion-tag notion-tag-purple">Low</span></td><td>May 02</td></tr>
      <tr><td>Fifth item — blocked on dependency</td><td><span class="notion-tag">Blocked</span></td><td>Regan</td><td><span class="notion-tag">High</span></td><td>May 05</td></tr>
      <tr><td>Sixth entry — new this week</td><td><span class="notion-tag notion-tag-blue">Queued</span></td><td>Aria</td><td><span class="notion-tag notion-tag-purple">Med</span></td><td>May 08</td></tr>
    </tbody>
  </table>

  <div class="notion-h2">[gallery] Gallery view</div>
  <div class="notion-gallery">
""" + "".join(f'<div class="notion-card"><div class="notion-card-cover"></div><b>Item {i+1}</b><div style="color:#9b9b9b;font-size:12px;margin-top:4px">Short description of card {i+1}</div></div>' for i in range(8)) + f"""
  </div>

  <div class="notion-h2">[check] Weekly checklist</div>
  <div class="notion-p"><span class="notion-check">✓</span>Review items due this week</div>
  <div class="notion-p"><span class="notion-check">✓</span>Triage new entries</div>
  <div class="notion-p"><span class="notion-check">✓</span>Archive completed items older than 30 days</div>
  <div class="notion-p" style="color:#9b9b9b">☐ Send weekly summary to team</div>
  <div class="notion-p" style="color:#9b9b9b">☐ Plan next week&rsquo;s priorities</div>
  <div class="notion-p" style="color:#9b9b9b">☐ 1:1 with direct reports</div>

  <div class="notion-h2">[toggle] Linked pages</div>
  <div class="notion-toggle">▸ Getting started guide</div>
  <div class="notion-toggle">▸ Automations reference</div>
  <div class="notion-toggle">▸ Weekly review template</div>
  <div class="notion-toggle">▸ Quarterly planning template</div>

  <div class="notion-divider"></div>
  <div style="color:#5a5a5a;font-size:12px">Template recreated for research. Original by {designer}. Source: <a href="{source}" style="color:#5a5a5a">{source}</a></div>
</div>
"""
    html = head(title, extra_css=NOTION_CSS)
    html += body
    html += foot()
    return html


def write_notion():
    dest = ROOT / "notion-templates" / "recreated"
    dest.mkdir(parents=True, exist_ok=True)
    for i, (fname, title, designer, source) in enumerate(NOTION_RECREATIONS):
        (dest / f"{fname}.html").write_text(build_notion(title, designer, source, i))
    print(f"Wrote {len(NOTION_RECREATIONS)} notion recreations")


# =====================================================================
# VERCEL TEMPLATES — 10 recreations (open-source style previews)
# =====================================================================

VERCEL_RECREATIONS = [
    ("01-ai-sdk-computer-use", "AI SDK Computer Use", "Vercel", "https://vercel.com/templates/next.js/ai-sdk-computer-use", "computer-use"),
    ("02-ai-research-agent", "AI Research Agent", "Vercel", "https://vercel.com/templates/next.js/ai-research-agent", "research-agent"),
    ("03-tersa-workflow", "Tersa — AI Workflow Canvas", "Vercel", "https://vercel.com/templates/next.js/tersa-ai-workflow-canvas", "workflow-canvas"),
    ("04-chatbot", "Vercel Chatbot", "Vercel", "https://vercel.com/templates/next.js/chatbot", "chatbot"),
    ("05-coding-agent", "Coding Agent Platform", "Vercel", "https://vercel.com/templates/next.js/coding-agent-platform", "coding-agent"),
    ("06-platforms-starter", "Platforms Starter Kit", "Vercel", "https://vercel.com/templates/next.js/platforms-starter-kit", "platforms"),
    ("07-commerce", "Next.js Commerce", "Vercel", "https://vercel.com/templates/next.js/nextjs-commerce", "commerce"),
    ("08-liveblocks-starter", "Liveblocks Starter", "Vercel", "https://vercel.com/templates/next.js/liveblocks-starter-kit", "liveblocks"),
    ("09-mcp-starter", "MCP Next.js Starter", "Vercel", "https://vercel.com/templates/next.js/model-context-protocol-mcp-with-next-js", "mcp"),
    ("10-subscription-starter", "Stripe Subscription Starter", "Vercel", "https://vercel.com/templates/next.js/subscription-starter", "subscription"),
]

def build_vercel(title, designer, source, kind):
    if kind == "computer-use":
        content = """<div class="grid" style="grid-template-columns: 320px 1fr; gap:16px;height:100%">
  <div class="card" style="display:flex;flex-direction:column">
    <div class="card-hd"><div class="card-title">Session</div><span class="badge badge-good">Claude Sonnet 4.7</span></div>
    <div class="col" style="gap:12px;flex:1">
      <div><div class="muted" style="font-size:12px">Task</div><div>Find the cheapest flight from LON to NYC in the next 30 days</div></div>
      <div><div class="muted" style="font-size:12px">Sandbox</div><div class="mono" style="font-size:12px">vs-sandbox-18f2a9</div></div>
      <div><div class="muted" style="font-size:12px">Status</div><div><span class="badge badge-good"><span class="dot"></span>Running — step 14/32</span></div></div>
    </div>
    <div class="card-hd mt-4"><div class="card-title" style="font-size:13px">Steps</div></div>
    <div class="list" style="font-size:12px">
      <div class="list-row"><span class="dot" style="color:var(--good)"></span>Take screenshot</div>
      <div class="list-row"><span class="dot" style="color:var(--good)"></span>Open browser</div>
      <div class="list-row"><span class="dot" style="color:var(--good)"></span>Navigate to skyscanner.net</div>
      <div class="list-row"><span class="dot" style="color:var(--good)"></span>Fill origin LON</div>
      <div class="list-row"><span class="dot" style="color:var(--accent)"></span>Fill destination NYC <span class="badge badge-accent" style="margin-left:auto">current</span></div>
      <div class="list-row muted"><span class="dot"></span>Select dates</div>
      <div class="list-row muted"><span class="dot"></span>Review results</div>
    </div>
  </div>
  <div class="card" style="padding:0;overflow:hidden">
    <div style="background:#2a2a2d;padding:10px;display:flex;gap:6px;align-items:center;border-bottom:1px solid var(--line)">
      <div style="width:10px;height:10px;border-radius:50%;background:#ff5f56"></div>
      <div style="width:10px;height:10px;border-radius:50%;background:#ffbd2e"></div>
      <div style="width:10px;height:10px;border-radius:50%;background:#27c93f"></div>
      <div style="flex:1;text-align:center;font-size:12px;color:var(--muted)">skyscanner.net</div>
    </div>
    <div style="padding:40px;color:var(--muted);text-align:center;height:520px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--bg-2),var(--bg-3))">
      <div><div style="font-size:48px;margin-bottom:12px">⊡</div><div>Sandbox browser preview</div><div class="mono" style="font-size:11px;margin-top:8px">1280 × 800 viewport</div></div>
    </div>
  </div>
</div>"""
    elif kind == "research-agent":
        content = """<div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:16px">
  <div class="card"><div class="card-hd"><div class="card-title">Browser 1 — arxiv.org</div><span class="badge badge-good">active</span></div><div style="background:var(--bg-2);padding:20px;min-height:280px;border-radius:8px;font-family:var(--mono);font-size:11px;color:var(--muted);white-space:pre-wrap">Reading: Llemma — an open language model for mathematics (2310.10631)...

abstract: We present Llemma, a large language model for mathematics...

extracting citations...
[32/148] parsed</div></div>
  <div class="card"><div class="card-hd"><div class="card-title">Browser 2 — semanticscholar.org</div><span class="badge badge-good">active</span></div><div style="background:var(--bg-2);padding:20px;min-height:280px;border-radius:8px;font-family:var(--mono);font-size:11px;color:var(--muted);white-space:pre-wrap">Querying: "open-source math LLMs 2024"...

found 241 results.
ranked by citation count.
fetching top 20 abstracts...
[12/20]</div></div>
  <div class="card"><div class="card-hd"><div class="card-title">Browser 3 — huggingface.co</div><span class="badge badge-warn">slow</span></div><div style="background:var(--bg-2);padding:20px;min-height:280px;border-radius:8px;font-family:var(--mono);font-size:11px;color:var(--muted);white-space:pre-wrap">Reading: meta-math/MetaMath model card...

extracting benchmark scores...
GSM8K: 82.3%
MATH: 26.6%

waiting for page load... (retry 1/3)</div></div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Synthesis — live</div><span class="badge badge-accent">Claude Sonnet 4.7</span></div>
<div style="background:var(--bg-2);padding:20px;border-radius:8px;font-size:13px;line-height:1.6">
  <b>Open-source math LLMs — current SOTA (as of today):</b><br><br>
  Based on 3 concurrent browser sessions across arxiv, Semantic Scholar, and HF Hub:
  <ol style="margin-left:24px;margin-top:8px">
    <li><b>Llemma-34B</b> (EleutherAI, Oct 2023) — 51.5% MATH, 83.3% GSM8K. Strongest open checkpoint for proof-generation workloads.</li>
    <li><b>MetaMath-70B</b> (MIT + UCL) — 82.3% GSM8K but weaker on MATH (26.6%). Optimised for word problems.</li>
    <li><b>MAmmoTH-70B</b> (Waterloo) — Tool-augmented; 58.8% MATH with calculator access...</li>
  </ol>
  <span style="color:var(--muted)">[cursor blinking]</span>
</div></div>"""
    elif kind == "workflow-canvas":
        content = """<div class="card" style="padding:0;overflow:hidden">
  <div class="card-hd" style="padding:20px"><div class="card-title">Workflow — content pipeline</div><div class="row" style="gap:8px"><button class="btn btn-sm">Save</button><button class="btn btn-sm btn-primary">Run</button></div></div>
  <div style="background:var(--bg-2);height:540px;position:relative;border-top:1px solid var(--line);background-image:radial-gradient(circle,var(--line-2) 1px,transparent 1px);background-size:24px 24px">
""" + "".join(f'''<div style="position:absolute;left:{x}px;top:{y}px;background:var(--bg-1);border:2px solid {c};border-radius:10px;padding:12px 16px;min-width:180px">
  <div class="muted" style="font-size:10px;text-transform:uppercase">{t}</div>
  <div style="font-weight:500;margin-top:4px">{n}</div>
</div>''' for x,y,c,t,n in [(40,40,'var(--accent)','trigger','Webhook incoming'),(320,40,'var(--purple)','llm','Claude Sonnet'),(620,40,'var(--teal)','tool','Google Search'),(320,180,'var(--amber)','llm','Summarise'),(620,180,'var(--pink)','tool','Notion DB'),(320,320,'var(--good)','output','Slack #research'),(620,320,'var(--good)','output','Email digest')]) + """
  </div>
</div>"""
    elif kind == "chatbot":
        content = """<div style="max-width:760px;margin:0 auto;display:flex;flex-direction:column;height:calc(100vh - 96px)">
  <div style="flex:1;overflow:auto;display:flex;flex-direction:column;gap:16px;padding:16px">
    <div class="card" style="padding:16px"><div class="row" style="gap:8px;margin-bottom:4px"><span class="avatar" style="background:var(--accent)">R</span><b>You</b></div><div>What's the best way to ship a macOS app that uses Metal for rendering?</div></div>
    <div class="card" style="padding:16px"><div class="row" style="gap:8px;margin-bottom:4px"><span class="avatar" style="background:linear-gradient(135deg,var(--purple),var(--pink))">A</span><b>Assistant</b></div>
    <div>For shipping a macOS app with Metal, here are the essentials:
      <ol style="margin-left:20px;margin-top:8px;font-size:13px">
        <li>Use <code style="background:var(--bg-2);padding:1px 4px;border-radius:3px">MTLDevice</code> for GPU access</li>
        <li>Enable Metal in Xcode capabilities</li>
        <li>Target macOS 12+ for modern Metal features</li>
        <li>Sign with Developer ID and notarise via altool</li>
      </ol>
      <div class="muted" style="font-size:11px;margin-top:12px">References: Apple Metal docs, WWDC 2023</div>
    </div></div>
    <div class="card" style="padding:16px"><div class="row" style="gap:8px;margin-bottom:4px"><span class="avatar" style="background:var(--accent)">R</span><b>You</b></div><div>What about GPU-family detection for broader device support?</div></div>
  </div>
  <div style="padding:16px;border-top:1px solid var(--line)"><div class="row" style="gap:8px;background:var(--bg-1);border:1px solid var(--line);border-radius:12px;padding:12px"><input class="input" style="flex:1;background:transparent;border:0" placeholder="Send a message..."><button class="btn btn-sm btn-primary">Send</button></div></div>
</div>"""
    else:
        content = f"""<div class="grid grid-4">
  {kpi("Deployments", "428", "+12")}
  {kpi("Avg build time", "42s", "-4s", "up")}
  {kpi("Edge requests/day", "2.1M", "+8%")}
  {kpi("Errors 24h", "12", "-4", "up")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Deployments — last 30d</div></div>{bar_chart(30, 8)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Framework mix</div></div>{donut()}</div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Recent deployments</div><button class="btn btn-sm btn-primary">Deploy</button></div>
{table(["Commit","Branch","Environment","Duration","Status"], [
  ["feat: add /api/agents","main","Production","42s",'<span class="badge badge-good">Ready</span>'],
  ["fix: type error","feat/settings","Preview","38s",'<span class="badge badge-good">Ready</span>'],
  ["refactor: extract useAuth","main","Production","52s",'<span class="badge badge-good">Ready</span>'],
  ["wip: billing","feat/billing","Preview","—",'<span class="badge badge-warn"><span class="dot"></span>Building</span>'],
])}
</div>"""

    items = [("Platform", ["Dashboard", "Deployments", "Functions", "Analytics"]),
             ("Team", ["Members", "Tokens", "Webhooks"])]

    html = head(title)
    html += '<div class="app">\n' + sidebar("Vercel", items, (0, 0)) + '<div class="main">\n'
    html += topbar(title)
    html += f'<div class="content">\n{content}\n</div>\n'
    html += '</div></div>\n'
    html += credit(designer, source, "vercel.com/templates")
    html += foot()
    return html


def write_vercel():
    dest = ROOT / "vercel-templates" / "recreated"
    dest.mkdir(parents=True, exist_ok=True)
    for fname, title, designer, source, kind in VERCEL_RECREATIONS:
        (dest / f"{fname}.html").write_text(build_vercel(title, designer, source, kind))
    print(f"Wrote {len(VERCEL_RECREATIONS)} vercel recreations")


# =====================================================================
# FIGMA COMMUNITY TOP — 10 recreations
# =====================================================================

FIGMA_RECREATIONS = [
    ("01-material-ui", "Material UI for Figma", "MUI", "https://www.figma.com/community/file/912837788133317724", "material"),
    ("02-untitled-ui", "Untitled UI v2.0", "Jordan Hughes", "https://www.figma.com/community/file/1020079203222518115", "untitled"),
    ("03-byewind-dashboard", "Dashboard UI Kit (ByeWind)", "ByeWind", "https://www.figma.com/community/file/1210542873091115123", "byewind"),
    ("04-charts-59", "59 Charts UI Components", "Iago Sousa", "https://www.figma.com/community/file/1136725187967938411", "charts"),
    ("05-snow-dashboard", "Snow Dashboard UI Kit", "ByeWind", "https://www.figma.com/community/file/1168811417705255214", "snow"),
    ("06-metrix-saas", "Metrix SaaS Dashboard", "Usman Ndako", "https://www.figma.com/community/file/1149477096761797772", "metrix"),
    ("07-myna-ui", "Myna UI (Tailwind+Shadcn+Radix)", "Praveen Juge", "https://www.figma.com/community/file/1340017605248937608", "myna"),
    ("08-tesla-dashboard", "Tesla Dashboard UI", "Nami", "https://www.figma.com/community/file/1382192547846546595", "tesla"),
    ("09-maglo-financial", "Maglo Financial Web UI", "UIHut", "https://www.figma.com/community/file/1496029882992276524", "maglo"),
    ("10-ai-agent-chat", "UI Kit for AI Agent Chat", "Armando Qose", "https://www.figma.com/community/file/1496647384826493443", "agent-chat"),
]

def build_figma(title, designer, source, kind):
    """Figma-kit approximations — visual component-library previews."""
    if kind == "charts":
        content = """<div class="grid grid-4">""" + "".join(f'<div class="card"><div class="card-hd"><div class="card-title">Chart {i+1}</div></div>{c}</div>' for i,c in enumerate([bar_chart(12,1),line_chart(2),donut(),pie(),bar_chart(18,3),line_chart(4),donut(),pie(),bar_chart(8,5),line_chart(6),donut(),bar_chart(24,7)])) + """</div>"""
    elif kind in ("material", "untitled", "myna"):
        content = """<div class="grid grid-3">
""" + "".join(f'''<div class="card"><div class="card-hd"><div class="card-title">{t}</div></div>{ex}</div>''' for t,ex in [
    ("Buttons", '<div class="col" style="gap:8px"><div class="row" style="gap:8px"><button class="btn btn-primary">Primary</button><button class="btn">Secondary</button><button class="btn btn-ghost">Ghost</button></div><div class="row" style="gap:8px"><button class="btn btn-sm btn-primary">SM Primary</button><button class="btn btn-sm">SM</button></div></div>'),
    ("Inputs", '<div class="col" style="gap:8px"><input class="input" placeholder="Placeholder"><div class="search"><input class="input" placeholder="Search..."></div><div class="row" style="gap:8px"><input class="input" placeholder="First"><input class="input" placeholder="Last"></div></div>'),
    ("Badges", '<div class="row" style="gap:6px;flex-wrap:wrap"><span class="badge">Default</span><span class="badge badge-good">Good</span><span class="badge badge-warn">Warn</span><span class="badge badge-bad">Bad</span><span class="badge badge-accent">Accent</span></div>'),
    ("Avatars", '<div class="row" style="gap:8px"><span class="avatar">R</span><span class="avatar" style="background:linear-gradient(135deg,var(--teal),var(--accent))">A</span><span class="avatar" style="background:linear-gradient(135deg,var(--pink),var(--purple))">K</span><span class="avatar" style="background:linear-gradient(135deg,var(--amber),var(--warn))">M</span></div>'),
    ("Progress", '<div class="col" style="gap:12px"><div class="progress"><div class="progress-bar" style="width:32%"></div></div><div class="progress"><div class="progress-bar" style="width:64%;background:var(--good)"></div></div><div class="progress"><div class="progress-bar" style="width:88%;background:var(--warn)"></div></div></div>'),
    ("Cards", '<div class="card" style="padding:14px;background:var(--bg-2)"><div class="card-title">Card title</div><div class="muted mt-2" style="font-size:12px">Supporting text for the card.</div><div class="row mt-4" style="gap:6px"><button class="btn btn-sm">Action</button></div></div>'),
    ("Tabs", '<div class="row" style="gap:0;border-bottom:1px solid var(--line)"><div style="padding:8px 12px;border-bottom:2px solid var(--accent)">Active</div><div style="padding:8px 12px;color:var(--muted)">Tab 2</div><div style="padding:8px 12px;color:var(--muted)">Tab 3</div></div>'),
    ("Alert", '<div class="card" style="padding:12px;background:rgba(61,124,255,0.1);border-color:var(--accent)"><div class="row" style="gap:8px"><span class="dot" style="color:var(--accent)"></span><b>Info</b></div><div class="muted mt-2" style="font-size:12px">This is an info-level alert message.</div></div>'),
    ("Table", table(["Name","Status","Role"], [["Regan",'<span class="badge badge-good">Active</span>',"Admin"],["Aria",'<span class="badge">Invited</span>',"Member"]])),
]) + """</div>"""
    else:  # byewind, metrix, snow, maglo, tesla, agent-chat
        if kind == "tesla":
            content = """<div class="card" style="padding:40px;text-align:center;background:linear-gradient(180deg,var(--bg-2),var(--bg));border-radius:24px">
  <div class="muted mono" style="font-size:11px;letter-spacing:0.1em">SENTINEL ACTIVE &middot; RANGE 312 mi</div>
  <div style="font-size:120px;font-weight:300;letter-spacing:-0.04em;margin:16px 0">68°</div>
  <div class="row" style="justify-content:center;gap:48px;margin-top:32px;font-family:var(--mono);font-size:13px">
    <div><div class="muted" style="font-size:11px">SPEED</div><div style="font-size:24px">0 mph</div></div>
    <div><div class="muted" style="font-size:11px">BATTERY</div><div style="font-size:24px">84%</div></div>
    <div><div class="muted" style="font-size:11px">RANGE</div><div style="font-size:24px">312 mi</div></div>
    <div><div class="muted" style="font-size:11px">ETA</div><div style="font-size:24px">—</div></div>
  </div>
</div>
<div class="grid grid-3 mt-4">
  <div class="card"><div class="card-hd"><div class="card-title mono">CLIMATE</div></div><div class="mono" style="font-size:24px;text-align:center;padding:24px">21°C</div></div>
  <div class="card"><div class="card-hd"><div class="card-title mono">MEDIA</div></div><div style="padding:12px"><div class="h2">Now playing</div><div class="muted mt-2" style="font-size:12px">Radiohead — Everything In Its Right Place</div></div></div>
  <div class="card"><div class="card-hd"><div class="card-title mono">NAVIGATION</div></div><div style="padding:12px"><div>Home</div><div class="muted" style="font-size:12px">18 min &middot; 12 mi</div></div></div>
</div>"""
        elif kind == "agent-chat":
            content = """<div class="grid" style="grid-template-columns: 260px 1fr; gap:16px">
  <div class="card">
    <div class="card-hd"><div class="card-title">Conversations</div><button class="btn btn-sm btn-primary">+</button></div>
    <div class="list">
      <div class="list-row"><div class="avatar">A</div><div class="col" style="gap:2px;flex:1"><b style="font-size:13px">Agent 1</b><span class="muted" style="font-size:11px">Research task</span></div></div>
      <div class="list-row" style="background:var(--bg-2);border-radius:6px;padding:6px 8px"><div class="avatar">A</div><div class="col" style="gap:2px;flex:1"><b style="font-size:13px">Agent 2</b><span class="muted" style="font-size:11px">Code review</span></div><span class="dot" style="color:var(--accent)"></span></div>
      <div class="list-row"><div class="avatar">A</div><div class="col" style="gap:2px;flex:1"><b style="font-size:13px">Agent 3</b><span class="muted" style="font-size:11px">Email triage</span></div></div>
    </div>
  </div>
  <div class="card" style="display:flex;flex-direction:column;min-height:640px">
    <div class="card-hd"><div class="card-title">Agent 2 — Code review</div><span class="badge badge-good">Claude Sonnet 4.7</span></div>
    <div style="flex:1;display:flex;flex-direction:column;gap:12px;padding:12px">
      <div class="row" style="gap:8px"><span class="avatar">R</span><div class="card" style="background:var(--bg-2);padding:12px;max-width:70%">Review the PR — add tests and check for security issues.</div></div>
      <div class="row" style="gap:8px"><span class="avatar" style="background:linear-gradient(135deg,var(--purple),var(--pink))">A</span><div class="card" style="background:var(--bg-1);border:1px solid var(--accent);padding:12px;max-width:70%">Running security scan... Found 2 issues:<br>1. Missing rate-limit on /api/login<br>2. Sensitive fields in log output<br><br>Generating tests now...</div></div>
      <div class="row" style="gap:8px"><span class="avatar" style="background:linear-gradient(135deg,var(--purple),var(--pink))">A</span><div class="card" style="background:var(--bg-1);padding:12px;max-width:70%"><div style="font-family:var(--mono);font-size:11px;background:var(--bg-2);padding:10px;border-radius:4px">// tests/login.test.ts<br>test('rate-limit', async ()=&gt;{<br>  for(let i=0;i&lt;20;i++) await login();<br>  expect(lastStatus).toBe(429);<br>});</div></div></div>
    </div>
    <div class="row" style="gap:8px;padding:12px;border-top:1px solid var(--line)"><input class="input" style="flex:1" placeholder="Message agent..."><button class="btn btn-primary">Send</button></div>
  </div>
</div>"""
        else:  # dashboard-style (byewind, metrix, snow, maglo)
            content = f"""<div class="grid grid-4">
  {kpi("Revenue", "$84.2K", "+12%")}
  {kpi("Customers", "12,412", "+4%")}
  {kpi("Orders", "1,248", "+8%")}
  {kpi("Conversion", "3.8%", "+0.4pt")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Revenue by month</div></div>{bar_chart(12, 4)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Sales by region</div></div>{donut()}</div>
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Traffic — last 7d</div></div>{line_chart(9)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Goals</div></div>
    <div class="col" style="gap:14px">
      <div><div class="row between"><span>Monthly revenue</span><span class="num">$84K / $100K</span></div><div class="progress mt-2"><div class="progress-bar" style="width:84%"></div></div></div>
      <div><div class="row between"><span>New customers</span><span class="num">412 / 500</span></div><div class="progress mt-2"><div class="progress-bar" style="width:82%;background:var(--good)"></div></div></div>
      <div><div class="row between"><span>NPS</span><span class="num">58 / 70</span></div><div class="progress mt-2"><div class="progress-bar" style="width:82%;background:var(--warn)"></div></div></div>
    </div>
  </div>
</div>"""

    items = [("Kit", ["Components", "Tokens", "Charts", "Icons"]),
             ("Pages", ["Dashboard", "Settings"])]

    html = head(title)
    html += '<div class="app">\n' + sidebar(designer, items, (0, 0)) + '<div class="main">\n'
    html += topbar(title)
    html += f'<div class="content">\n{content}\n</div>\n'
    html += '</div></div>\n'
    html += credit(designer, source, "figma.com/community")
    html += foot()
    return html


def write_figma():
    dest = ROOT / "figma-community-top" / "recreated"
    dest.mkdir(parents=True, exist_ok=True)
    for fname, title, designer, source, kind in FIGMA_RECREATIONS:
        (dest / f"{fname}.html").write_text(build_figma(title, designer, source, kind))
    print(f"Wrote {len(FIGMA_RECREATIONS)} figma recreations")


# =====================================================================
# DESIGN-TO-CODE — 10 recreations
# =====================================================================

D2C_RECREATIONS = [
    ("01-supabase-ui-auth", "Supabase UI — Auth Flow", "Supabase", "https://supabase.com/ui", "auth"),
    ("02-supabase-ui-realtime", "Supabase UI — Realtime Chat", "Supabase", "https://supabase.com/ui", "realtime"),
    ("03-supabase-ui-dropzone", "Supabase UI — File Upload Dropzone", "Supabase", "https://supabase.com/ui", "dropzone"),
    ("04-convex-fullstack", "Convex — Fullstack Template", "Convex", "https://www.convex.dev/templates", "convex-fullstack"),
    ("05-convex-chat", "Convex — Realtime Chat", "Convex", "https://www.convex.dev/templates", "convex-chat"),
    ("06-builderio-example", "Builder.io — Landing CMS Example", "Builder.io", "https://www.builder.io/examples", "builder"),
    ("07-plasmic-example", "Plasmic — Visual Builder Output", "Plasmic", "https://www.plasmic.app/examples", "plasmic"),
    ("08-locofy-figma-port", "Locofy — Figma to React Port", "Locofy", "https://www.locofy.ai/templates", "locofy"),
    ("09-shadcn-d2c-template", "Shadcn — Dashboard Template", "shadcn", "https://ui.shadcn.com/examples/dashboard", "shadcn"),
    ("10-radix-themes-dashboard", "Radix Themes — Dashboard", "Radix UI", "https://www.radix-ui.com/themes/docs/overview/getting-started", "radix"),
]

def build_d2c(title, designer, source, kind):
    if kind == "auth":
        content = """<div style="max-width:420px;margin:48px auto">
  <div class="card" style="padding:32px">
    <div class="h1" style="font-size:24px;text-align:center">Welcome back</div>
    <div class="muted mt-2" style="text-align:center">Sign in to continue</div>
    <form class="col mt-4" style="gap:12px">
      <div class="row" style="gap:8px"><button class="btn" style="flex:1">GitHub</button><button class="btn" style="flex:1">Google</button></div>
      <div class="row" style="gap:12px;color:var(--muted);font-size:12px;margin:8px 0"><div style="flex:1;border-top:1px solid var(--line)"></div>or<div style="flex:1;border-top:1px solid var(--line)"></div></div>
      <input class="input" type="email" placeholder="you@example.com">
      <div><input class="input" type="password" placeholder="Password" style="width:100%"><div class="row between mt-2"><span class="muted" style="font-size:11px;display:flex;gap:6px;align-items:center">Strength: <div style="width:100px;height:4px;background:var(--bg-3);border-radius:2px;overflow:hidden"><div style="width:80%;height:100%;background:var(--good)"></div></div>Strong</span><a class="muted" style="font-size:11px">zxcvbn</a></div></div>
      <button type="submit" class="btn btn-primary">Sign in</button>
    </form>
    <div class="muted mt-4" style="text-align:center;font-size:12px">New here? <a style="color:var(--accent)">Create account</a></div>
  </div>
</div>"""
    elif kind == "realtime":
        content = """<div class="card" style="max-width:680px;margin:32px auto;display:flex;flex-direction:column;height:540px">
  <div class="card-hd"><div class="card-title">#clawmachine</div><div class="row" style="gap:6px"><span class="dot" style="color:var(--good)"></span><span class="muted" style="font-size:12px">4 online</span></div></div>
  <div style="flex:1;overflow:auto;padding:12px;display:flex;flex-direction:column;gap:8px">
    <div class="row" style="gap:8px;align-items:flex-start"><span class="avatar">A</span><div><div class="row" style="gap:8px"><b style="font-size:13px">Aria</b><span class="muted" style="font-size:11px">04:21</span></div><div style="font-size:13px">parts for CM-2040 arrived, starting on it now</div></div></div>
    <div class="row" style="gap:8px;align-items:flex-start"><span class="avatar" style="background:linear-gradient(135deg,var(--teal),var(--accent))">K</span><div><div class="row" style="gap:8px"><b style="font-size:13px">Kai</b><span class="muted" style="font-size:11px">04:23</span></div><div style="font-size:13px">heads up — iFixit order delayed, eta thursday</div></div></div>
    <div class="row" style="gap:8px;align-items:flex-start"><span class="avatar">R</span><div><div class="row" style="gap:8px"><b style="font-size:13px">Regan</b><span class="muted" style="font-size:11px">04:24</span></div><div style="font-size:13px">ack, rescheduling repairs</div></div></div>
    <div class="muted" style="font-size:11px;text-align:center;margin:8px 0">Aria is typing...</div>
  </div>
  <div class="row" style="gap:8px;padding:12px;border-top:1px solid var(--line)"><input class="input" style="flex:1" placeholder="Message #clawmachine..."><button class="btn btn-primary">Send</button></div>
</div>"""
    elif kind == "dropzone":
        content = """<div style="max-width:560px;margin:64px auto">
  <div class="card" style="padding:48px;border:2px dashed var(--line);text-align:center;background:var(--bg-1)">
    <div style="font-size:48px;color:var(--muted-2);margin-bottom:16px">[upload]</div>
    <div class="h2">Drag files here</div>
    <div class="muted mt-2">or click to browse</div>
    <div class="muted mt-4" style="font-size:12px">PNG, JPG, WEBP up to 10MB</div>
    <button class="btn btn-primary" style="margin-top:24px">Select files</button>
  </div>
  <div class="card mt-4"><div class="card-hd"><div class="card-title">Uploaded</div><span class="badge">3 files</span></div>
    <div class="list">
      <div class="list-row"><span style="width:32px;height:32px;background:var(--bg-3);border-radius:4px"></div><div class="col" style="gap:2px;flex:1"><div>repair-before.jpg</div><div class="progress" style="margin-top:2px"><div class="progress-bar" style="width:100%;background:var(--good)"></div></div></div><span class="badge badge-good">Done</span></div>
      <div class="list-row"><span style="width:32px;height:32px;background:var(--bg-3);border-radius:4px"></div><div class="col" style="gap:2px;flex:1"><div>board-detail.png</div><div class="progress" style="margin-top:2px"><div class="progress-bar" style="width:68%"></div></div></div><span class="badge badge-accent">68%</span></div>
      <div class="list-row"><span style="width:32px;height:32px;background:var(--bg-3);border-radius:4px"></div><div class="col" style="gap:2px;flex:1"><div>IMG_4032.jpg</div><div class="progress" style="margin-top:2px"><div class="progress-bar" style="width:12%"></div></div></div><span class="badge">Queued</span></div>
    </div>
  </div>
</div>"""
    elif kind in ("convex-fullstack", "convex-chat"):
        content = f"""<div class="grid grid-3">
  {kpi("Documents", "12,418")}
  {kpi("Active sessions", "128")}
  {kpi("Functions/min", "842")}
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Real-time log</div></div>
    <div class="mono" style="font-size:11px;background:var(--bg);padding:12px;border-radius:6px;height:220px;overflow:auto">
      <div class="muted">[04:21:02.142] query:getUser user_42</div>
      <div class="muted">[04:21:02.148] mutation:sendMessage</div>
      <div style="color:var(--good)">[04:21:02.158] mutation:sendMessage OK 16ms</div>
      <div class="muted">[04:21:02.201] query:listMessages</div>
      <div style="color:var(--good)">[04:21:02.204] query:listMessages OK 3ms</div>
      <div class="muted">[04:21:02.301] action:generateReply</div>
      <div style="color:var(--accent)">[04:21:02.302] action:generateReply running (Claude Sonnet)</div>
      <div style="color:var(--good)">[04:21:03.814] action:generateReply OK 1512ms</div>
    </div>
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">Schema</div></div>
    <pre class="mono" style="background:var(--bg);padding:12px;border-radius:6px;font-size:11px;overflow:auto">export default defineSchema({{
  users: defineTable({{
    name: v.string(),
    email: v.string(),
    clerkId: v.string(),
  }}).index("by_clerkId", ["clerkId"]),

  messages: defineTable({{
    body: v.string(),
    userId: v.id("users"),
    conversationId: v.id("conversations"),
  }}).index("by_conversation", ["conversationId"]),

  conversations: defineTable({{
    title: v.string(),
    ownerId: v.id("users"),
  }}),
}});</pre>
  </div>
</div>"""
    elif kind in ("shadcn", "radix"):
        content = f"""<div class="grid grid-4">
  {kpi("Total revenue", "$45,231.89", "+20.1% from last month")}
  {kpi("Subscriptions", "+2,350", "+180.1% from last month")}
  {kpi("Sales", "+12,234", "+19% from last month")}
  {kpi("Active now", "+573", "+201 since last hour")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Overview</div></div>{bar_chart(12, 3)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Recent sales</div><span class="muted" style="font-size:12px">265 this month</span></div>
""" + list_rows([
  ("O","Olivia Martin","olivia.martin@email.com","<span class='num'>+$1,999.00</span>"),
  ("J","Jackson Lee","jackson.lee@email.com","<span class='num'>+$39.00</span>"),
  ("I","Isabella Nguyen","isabella.nguyen@email.com","<span class='num'>+$299.00</span>"),
  ("W","William Kim","will@email.com","<span class='num'>+$99.00</span>"),
  ("S","Sofia Davis","sofia.davis@email.com","<span class='num'>+$39.00</span>"),
]) + "</div></div>"
    else:  # builder, plasmic, locofy
        content = """<div class="card" style="padding:0;overflow:hidden">
  <div class="row between" style="padding:14px 20px;border-bottom:1px solid var(--line);background:var(--bg-1)">
    <div class="row" style="gap:12px"><div class="brand-mark"></div><div><b>""" + designer + """</b><div class="muted" style="font-size:11px">Visual editor</div></div></div>
    <div class="row" style="gap:8px"><button class="btn btn-sm">Preview</button><button class="btn btn-sm btn-primary">Publish</button></div>
  </div>
  <div style="display:grid;grid-template-columns:240px 1fr 280px;min-height:560px">
    <aside style="background:var(--bg-1);border-right:1px solid var(--line);padding:16px">
      <div class="muted" style="font-size:11px;text-transform:uppercase">Components</div>
      <div class="col" style="gap:4px;margin-top:8px"><div class="nav-item active">Section</div><div class="nav-item">Heading</div><div class="nav-item">Text</div><div class="nav-item">Image</div><div class="nav-item">Button</div><div class="nav-item">Form</div><div class="nav-item">Grid</div><div class="nav-item">Stack</div></div>
    </aside>
    <main style="padding:24px;background:var(--bg-2);overflow:auto"><div class="card" style="padding:64px 32px;text-align:center;background:linear-gradient(135deg,var(--bg-1),var(--bg))"><div class="h1" style="font-size:48px">Your headline here</div><div class="muted mt-4" style="font-size:17px;max-width:440px;margin:16px auto">Drag components from the left to customise this page. Every element is editable inline.</div><button class="btn btn-primary mt-4">Call to action</button></div>
      <div class="grid grid-3 mt-4">""" + "".join(f'<div class="card" style="padding:20px"><div style="width:32px;height:32px;background:var(--accent);opacity:0.2;border-radius:8px;margin-bottom:12px"></div><div class="h2">Feature {i+1}</div><div class="muted mt-2" style="font-size:12px">Supporting text for this feature.</div></div>' for i in range(3)) + """</div>
    </main>
    <aside style="background:var(--bg-1);border-left:1px solid var(--line);padding:16px">
      <div class="muted" style="font-size:11px;text-transform:uppercase">Properties</div>
      <div class="col" style="gap:10px;margin-top:10px;font-size:12px">
        <div><div class="muted" style="margin-bottom:4px">Padding</div><input class="input" value="64px 32px" style="width:100%"></div>
        <div><div class="muted" style="margin-bottom:4px">Background</div><input class="input" value="linear-gradient(...)" style="width:100%"></div>
        <div><div class="muted" style="margin-bottom:4px">Heading</div><input class="input" value="Your headline here" style="width:100%"></div>
        <div><div class="muted" style="margin-bottom:4px">Align</div><div class="row" style="gap:4px"><button class="btn btn-sm">Left</button><button class="btn btn-sm btn-primary">Center</button><button class="btn btn-sm">Right</button></div></div>
      </div>
    </aside>
  </div>
</div>"""

    items = [("Platform", ["Projects", "Models", "API", "Settings"])]

    html = head(title)
    html += '<div class="app">\n' + sidebar(designer, items, (0, 0)) + '<div class="main">\n'
    html += topbar(title)
    html += f'<div class="content">\n{content}\n</div>\n'
    html += '</div></div>\n'
    html += credit(designer, source, "design-to-code")
    html += foot()
    return html


def write_d2c():
    dest = ROOT / "design-to-code" / "recreated"
    dest.mkdir(parents=True, exist_ok=True)
    for fname, title, designer, source, kind in D2C_RECREATIONS:
        (dest / f"{fname}.html").write_text(build_d2c(title, designer, source, kind))
    print(f"Wrote {len(D2C_RECREATIONS)} d2c recreations")


# =====================================================================
# RETOOL/BRAVO/BUBBLE — 10 recreations
# =====================================================================

RBB_RECREATIONS = [
    ("01-retool-analytics", "Retool — Analytics Dashboard", "Retool", "https://retool.com/templates/analytics-dashboard", "retool-analytics"),
    ("02-retool-custom-crm", "Retool — Custom CRM", "Retool", "https://retool.com/templates/custom-crm", "retool-crm"),
    ("03-retool-hr-analytics", "Retool — HR Analytics", "Retool", "https://retool.com/templates/hr-analytics-dashboard", "retool-hr"),
    ("04-retool-security-dash", "Retool — Security Dashboard", "Retool", "https://retool.com/templates/security-dashboard", "retool-security"),
    ("05-retool-kpi-dashboard", "Retool — KPI Dashboard", "Retool", "https://retool.com/templates/kpi-dashboard", "retool-kpi"),
    ("06-retool-rest-admin", "Retool — REST API Admin Panel", "Retool", "https://retool.com/templates/rest-api-admin-panel", "retool-admin"),
    ("07-retool-employee-directory", "Retool — Employee Directory", "Retool", "https://retool.com/templates/employee-directory", "retool-directory"),
    ("08-bubble-dashboard-gallery", "Bubble — Dashboard Gallery", "Bubble Community", "https://bubble.io/templates/dashboard", "bubble-dashboard"),
    ("09-bubble-saas-template", "Bubble — SaaS Template", "Bubble Community", "https://bubble.io/templates/saas", "bubble-saas"),
    ("10-bravo-design-to-native", "Bravo Studio — Figma to Native", "Bravo Studio", "https://www.bravostudio.app", "bravo-home"),
]

def build_rbb(title, designer, source, kind):
    if kind.startswith("retool-"):
        if kind == "retool-analytics":
            content = f"""<div class="grid grid-4">
  {kpi("Total Sales", "35,031", "+12%")}
  {kpi("Clicks", "5,211", "+8%")}
  {kpi("Impressions", "85,234", "+4%")}
  {kpi("CTR", "6.12%", "+0.3pt")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Monthly Revenue</div></div>{line_chart(7)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Campaign Revenue</div></div><div class="row" style="gap:20px">{pie()}<div class="col" style="gap:8px;font-size:12px"><div><span class="dot" style="color:var(--accent)"></span> Summer Sale &middot; 42.9%</div><div><span class="dot" style="color:var(--purple)"></span> Back to School &middot; 42.9%</div><div><span class="dot" style="color:var(--teal)"></span> Holiday Sale &middot; 14.3%</div></div></div></div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Campaigns</div><div class="row" style="gap:8px"><button class="btn btn-sm">View Details</button><button class="btn btn-sm">Export Data</button></div></div>
{table(["Id","Campaign Name","Campaign Owner","Start Date","End Date","Budget","Impressions"], [
  ["001","Summer Sale","Regan C.","May 01","Jun 30","£12,000","42,188"],
  ["002","Back to School","Aria P.","Aug 15","Sep 30","£8,000","28,441"],
  ["003","Holiday Sale","Kai J.","Nov 20","Dec 24","£18,000","14,605"],
  ["004","Spring Refresh","Mara S.","Mar 01","Apr 15","£6,000","9,842"],
  ["005","Flash Friday","Regan C.","Apr 19","Apr 19","£2,000","3,221"],
])}
</div>"""
        elif kind == "retool-crm":
            content = f"""<div class="grid grid-4">
  {kpi("Contacts", "2,418")}
  {kpi("Active Deals", "84")}
  {kpi("Revenue Q2", "£184K")}
  {kpi("Win rate", "42%")}
</div>
<div class="grid" style="grid-template-columns: 280px 1fr; gap:16px">
  <div class="card">
    <div class="card-hd"><div class="card-title">Contacts</div><button class="btn btn-sm btn-primary">+</button></div>
    <div class="list">
""" + "".join(f'<div class="list-row"><div class="avatar">{n[0]}</div><div class="col" style="gap:2px;flex:1"><b style="font-size:13px">{n}</b><span class="muted" style="font-size:11px">{c}</span></div></div>' for n,c in [("Sarah Kim","Meridian Labs"),("David Chen","Apex Industries"),("Priya Nair","Northbound Co"),("Oliver Reed","Ironbark Ltd"),("Mei Lin","Summit Health")]) + """
    </div>
  </div>
  <div class="card">
    <div class="card-hd"><div class="card-title">Sarah Kim — Meridian Labs</div><div class="row" style="gap:6px"><button class="btn btn-sm">Edit</button><button class="btn btn-sm btn-primary">Log activity</button></div></div>
    <div class="grid grid-2" style="gap:12px">
      <div><div class="muted" style="font-size:11px">Email</div><div>sarah@meridianlabs.co</div></div>
      <div><div class="muted" style="font-size:11px">Phone</div><div>+44 20 7946 0018</div></div>
      <div><div class="muted" style="font-size:11px">Stage</div><div><span class="badge badge-good">Negotiate</span></div></div>
      <div><div class="muted" style="font-size:11px">Deal value</div><div class="num">£42,200</div></div>
      <div><div class="muted" style="font-size:11px">Owner</div><div>Regan C.</div></div>
      <div><div class="muted" style="font-size:11px">Last contact</div><div>2 hours ago</div></div>
    </div>
    <div class="h2 mt-4">Activity</div>
    <div class="list mt-2"><div class="list-row"><span class="dot" style="color:var(--accent)"></span><div class="col" style="gap:2px;flex:1"><div>Proposal sent</div><span class="muted" style="font-size:11px">2h ago by Regan</span></div></div>
      <div class="list-row"><span class="dot" style="color:var(--accent)"></span><div class="col" style="gap:2px;flex:1"><div>Demo call — 45 min</div><span class="muted" style="font-size:11px">yesterday by Aria</span></div></div>
      <div class="list-row"><span class="dot" style="color:var(--accent)"></span><div class="col" style="gap:2px;flex:1"><div>Email thread opened</div><span class="muted" style="font-size:11px">3d ago</span></div></div>
    </div>
  </div>
</div>"""
        elif kind == "retool-hr":
            content = f"""<div class="grid grid-4">
  {kpi("Employees", "247", "+4 new")}
  {kpi("Retention", "94%", "+2pt")}
  {kpi("Open roles", "18", "+3")}
  {kpi("Avg tenure", "3.2 yr")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Headcount by department</div></div>{bar_chart(8, 2)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Gender balance</div></div><div class="row" style="gap:20px">{donut()}<div class="col" style="gap:6px;font-size:12px"><div><span class="dot" style="color:var(--accent)"></span> Women 48%</div><div><span class="dot" style="color:var(--purple)"></span> Men 47%</div><div><span class="dot" style="color:var(--teal)"></span> Non-binary 3%</div><div><span class="dot" style="color:var(--amber)"></span> Undisclosed 2%</div></div></div></div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Employees</div></div>
{table(["Name","Dept","Role","Tenure","Manager"], [
  ["Regan C.","Ops","Founder","5 yr","—"],
  ["Aria P.","Engineering","Senior SE","2.3 yr","Regan"],
  ["Kai J.","Engineering","SE","1.1 yr","Aria"],
  ["Mara S.","Ops","Analyst","2.8 yr","Regan"],
  ["Theo R.","Sales","AE","0.8 yr","Regan"],
])}
</div>"""
        elif kind == "retool-security":
            content = f"""<div class="grid grid-4">
  {kpi("Active threats", "3", "+1", "down")}
  {kpi("Incidents 30d", "18", "-4", "up")}
  {kpi("SOC coverage", "99.2%", "+0.3pt")}
  {kpi("MTTR", "14 min", "-2 min", "up")}
</div>
<div class="grid grid-2">
  <div class="card"><div class="card-hd"><div class="card-title">Threat feed</div></div>
{table(["Severity","Source","Category","Time"], [
  ['<span class="badge badge-bad">CRITICAL</span>',"45.33.11.4","Port scan","04:21"],
  ['<span class="badge badge-warn">HIGH</span>',"198.51.100.8","Repeat conn","04:18"],
  ['<span class="badge badge-warn">HIGH</span>',"203.0.113.9","Suspicious UA","04:12"],
  ['<span class="badge">MED</span>',"internal-worker-03","Process anomaly","04:08"],
  ['<span class="badge">LOW</span>',"email.mail01","Policy violation","03:44"],
])}
  </div>
  <div class="card"><div class="card-hd"><div class="card-title">Incident trend</div></div>{bar_chart(30, 6)}</div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Compliance matrix</div></div>
<div class="grid grid-4">
  <div class="kpi"><div class="kpi-label">SOC 2 Type II</div><div class="kpi-value" style="color:var(--good);font-size:20px">Passed</div><div class="kpi-delta">renewed 2025-Q4</div></div>
  <div class="kpi"><div class="kpi-label">ISO 27001</div><div class="kpi-value" style="color:var(--good);font-size:20px">Passed</div><div class="kpi-delta">renewed 2025-Q3</div></div>
  <div class="kpi"><div class="kpi-label">GDPR</div><div class="kpi-value" style="color:var(--good);font-size:20px">Compliant</div></div>
  <div class="kpi"><div class="kpi-label">HIPAA</div><div class="kpi-value" style="color:var(--warn);font-size:20px">In progress</div><div class="kpi-delta down">Q3 target</div></div>
</div>
</div>"""
        else:  # retool-kpi, retool-admin, retool-directory
            content = f"""<div class="grid grid-4">
  {kpi("Users", "12,418", "+4%")}
  {kpi("Revenue", "£84.2K", "+12%")}
  {kpi("Sessions", "82K", "+8%")}
  {kpi("Churn", "1.4%", "-0.2pt", "up")}
</div>
<div class="grid" style="grid-template-columns: 2fr 1fr">
  <div class="card"><div class="card-hd"><div class="card-title">Trend</div></div>{line_chart(11)}</div>
  <div class="card"><div class="card-hd"><div class="card-title">Breakdown</div></div>{pie()}</div>
</div>
<div class="card"><div class="card-hd"><div class="card-title">Table — detail records</div><button class="btn btn-sm btn-primary">+ Record</button></div>
{table(["ID","Customer","Email","Plan","Status","Created"], [
  ["001","Sarah Kim","sarah@meridian.co","Pro",'<span class="badge badge-good">Active</span>',"Apr 21"],
  ["002","David Chen","david@apex.io","Team",'<span class="badge badge-good">Active</span>',"Apr 20"],
  ["003","Priya Nair","priya@north.co","Free",'<span class="badge">Trialing</span>',"Apr 19"],
  ["004","Oliver Reed","oliver@ironbark.co","Enterprise",'<span class="badge badge-good">Active</span>',"Apr 18"],
  ["005","Mei Lin","mei@summit.health","Pro",'<span class="badge badge-bad">Cancelled</span>',"Apr 17"],
  ["006","Jonas B.","jonas@harborprint.co","Team",'<span class="badge badge-good">Active</span>',"Apr 16"],
])}
</div>"""

        items = [("App", ["Dashboard","Queries","Components","Settings"]),
                 ("Resources", ["Postgres","REST","Slack","GitHub"])]
        html = head(title)
        html += '<div class="app">\n' + sidebar("Retool", items, (0, 0)) + '<div class="main">\n'
        html += topbar(title)
        html += f'<div class="content">\n{content}\n</div>\n'
        html += '</div></div>\n'
        html += credit(designer, source, "retool.com")
        html += foot()
        return html

    elif kind.startswith("bubble-"):
        # Bubble gallery
        templates = [
            ("Ez Dashboard + OpenAI","Free","58.5K","4.0"),
            ("Responsive Webapp Template","Free","11.9K","4.0"),
            ("Analytics Dashboard","Free","8.6K","4.0"),
            ("AI SAAS Starter Kit","Free","7.9K","3.8"),
            ("Base Dashboard","Free","4.2K","4.1"),
            ("Charts / Analytics","Free","2.9K","4.3"),
            ("Soft UI Dashboard","Free","2.7K","4.7"),
            ("CodeFree Dashboard","Free","2.0K","4.3"),
            ("Vision Dashboard","Free","1.9K","4.3"),
            ("Purity UI Dashboard","Free","1.3K","—"),
            ("Material UI Dashboard","Free","1.1K","4.0"),
            ("Simple User Management","Free","784","5.0"),
        ]
        content = """<section style="background:linear-gradient(180deg,var(--bg-1),var(--bg));padding:48px 24px;text-align:center;border-radius:16px;border:1px solid var(--line);margin-bottom:24px">
  <div class="h1" style="font-size:34px">Build no-code apps faster with Dashboard templates</div>
  <div class="muted mt-2" style="max-width:520px;margin:8px auto">Ready-made apps and templates created by the Bubble community.</div>
  <div class="row" style="gap:8px;justify-content:center;margin-top:16px"><input class="input" style="width:380px" placeholder="Search..."><button class="btn btn-primary">Search</button></div>
</section>
<div class="grid" style="grid-template-columns:200px 1fr;gap:24px">
  <aside>
    <div class="muted" style="font-size:11px;text-transform:uppercase;margin-bottom:8px">Category</div>
    <div class="col" style="gap:4px;font-size:13px">
""" + "".join(f'<div style="padding:6px 10px;border-radius:4px;{"background:var(--bg-2)" if i==0 else ""}">{c}</div>' for i,c in enumerate(["Dashboard","AI","Blog","Booking","Chat","CRM","Finance","Marketplace","Portfolio","SaaS","Social"])) + """
    </div>
  </aside>
  <div>
    <div class="row between" style="margin-bottom:12px"><div class="muted" style="font-size:12px">Showing 12 of 124 templates</div><select class="input" style="width:200px"><option>Sort: Most installed</option></select></div>
    <div class="grid grid-4" style="gap:16px">
""" + "".join(f'<div class="card" style="padding:0;overflow:hidden"><div style="aspect-ratio:16/9;background:linear-gradient(135deg,{["var(--accent)","var(--purple)","var(--teal)","var(--amber)","var(--pink)","var(--good)","var(--warn)","var(--bad)"][i%8]},var(--bg-2))"></div><div style="padding:12px"><div style="font-weight:500;font-size:13px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</div><div class="muted" style="font-size:11px">{price} &middot; DASHBOARD</div><div class="row between mt-2" style="font-size:11px"><span class="muted">{dl} installs</span><span class="muted">{rating} ★</span></div></div></div>' for i,(name,price,dl,rating) in enumerate(templates)) + """
    </div>
  </div>
</div>"""
        html = head(title)
        html += '<div style="padding:24px;max-width:1280px;margin:0 auto">\n'
        html += """<nav style="display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid var(--line);margin-bottom:24px"><div class="row"><div class="brand-mark" style="background:#0051ff"></div><b>Bubble</b></div><div class="row" style="gap:16px;font-size:14px"><a class="muted">Marketplace</a><a>Templates</a><a class="muted">Plugins</a></div><div class="row" style="gap:8px"><button class="btn btn-sm btn-ghost">Log in</button><button class="btn btn-sm btn-primary">Get started</button></div></nav>\n"""
        html += content + "\n</div>\n"
        html += credit(designer, source, "bubble.io")
        html += foot()
        return html

    else:  # bravo-home
        content = """<nav style="display:flex;justify-content:space-between;padding:16px 48px;border-bottom:1px solid var(--line);margin-bottom:64px"><div class="row"><div class="brand-mark" style="background:linear-gradient(135deg,#ff6b6b,#ffa500)"></div><b>Bravo Studio</b></div><div class="row" style="gap:24px;font-size:14px"><a class="muted">Features</a><a class="muted">Pricing</a><a class="muted">Showcase</a><a class="muted">Academy</a></div><div class="row" style="gap:8px"><button class="btn btn-sm btn-ghost">Log in</button><button class="btn btn-sm btn-primary">Start building</button></div></nav>
<section style="text-align:center;padding:0 48px 64px">
  <div class="h1" style="font-size:64px;font-weight:500;letter-spacing:-0.03em">Your Dream App,<br>Your Design, No Limits.</div>
  <div class="muted mt-4" style="font-size:17px;max-width:480px;margin:24px auto">Convert your Figma designs into real iOS and Android apps without coding.</div>
  <div class="row" style="gap:8px;justify-content:center;margin-top:24px"><button class="btn btn-primary" style="padding:14px 28px">Start for free</button><button class="btn" style="padding:14px 28px">Explore #MadeWithBravo</button></div>
</section>
<section style="padding:32px 48px;max-width:1100px;margin:0 auto">
  <div class="row between" style="margin-bottom:24px"><h2 class="h2" style="font-size:28px">Two ways to build</h2></div>
  <div class="grid grid-2" style="gap:16px">
    <div class="card" style="padding:32px"><div class="h2">Bravo Studio</div><div class="muted mt-2">Build visually. Ship fast.</div><div class="col mt-4" style="gap:6px;font-size:13px"><div>✓ Figma to native iOS & Android</div><div>✓ Update directly from design</div><div>✓ No setup required</div><div>✓ No-code / low-code workflow</div></div><button class="btn btn-primary mt-4">Start building for free</button></div>
    <div class="card" style="padding:32px"><div class="h2">Bravo-To-Go</div><div class="muted mt-2">Start with code. Build with AI.</div><div class="col mt-4" style="gap:6px;font-size:13px"><div>✓ React Native app in 1–2 days</div><div>✓ Full code ownership</div><div>✓ Backend, auth, and infra ready</div><div>✓ Use Claude, OpenAI, Cursor, or Gemini</div></div><button class="btn mt-4">Explore Bravo-To-Go</button></div>
  </div>
</section>
<section style="padding:64px 48px;max-width:1100px;margin:0 auto">
  <h2 class="h2" style="font-size:28px;margin-bottom:24px">Templates</h2>
  <div class="grid grid-4" style="gap:12px">
""" + "".join(f'<div class="card" style="padding:14px;text-align:center"><div style="aspect-ratio:3/4;background:linear-gradient(135deg,{["var(--accent)","var(--purple)","var(--teal)","var(--amber)","var(--pink)","var(--good)","var(--warn)","var(--bad)"][i%8]},var(--bg-2));border-radius:8px;margin-bottom:10px"></div><div style="font-weight:500">{n}</div></div>' for i,n in enumerate(["Mindfulness","Fitness","CRM","Restaurant","Event","Personal Trainer","Recipe","School"])) + """
  </div>
</section>
<section style="padding:48px;text-align:center;background:var(--bg-1);border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin:48px 0 0">
  <div class="h2" style="font-size:24px">Ready to Turn Your Figma Designs into Real Apps?</div>
  <button class="btn btn-primary mt-4">Start for Free</button>
</section>"""
        html = head(title)
        html += content
        html += credit(designer, source, "bravostudio.app")
        html += foot()
        return html


def write_rbb():
    dest = ROOT / "retool-bravo-bubble" / "recreated"
    dest.mkdir(parents=True, exist_ok=True)
    for fname, title, designer, source, kind in RBB_RECREATIONS:
        (dest / f"{fname}.html").write_text(build_rbb(title, designer, source, kind))
    print(f"Wrote {len(RBB_RECREATIONS)} retool-bravo-bubble recreations")


# --- run all ---
if __name__ == "__main__":
    write_v0()
    write_framer()
    write_webflow()
    write_notion()
    write_vercel()
    write_figma()
    write_d2c()
    write_rbb()
    print("\nAll recreations generated.")
