#!/usr/bin/env python3
"""
Build three Figma-REST-shaped JSON documents from Clawmachine source
material. Output:

    clawmachine-figma-schema.json   — 7 canvases (pages)
    untitled-ui-pro-figma-schema.json — 20 canvases (pages)
    aceternity-pro-figma-schema.json  — 20 canvases (category aggregation)

All three files match the shape of the Figma REST API `GET /files/:key`
response: figma.com/developers/api#get-file-endpoint .
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

ROOT = Path("/Users/regancooney/Projects/consolidate")
FEED = ROOT / "claude-design-feed"
OUT  = FEED / "external" / "figma-sources"
OUT.mkdir(parents=True, exist_ok=True)

SCHEMES = json.loads((ROOT / ".triage" / "chromatic-schemes.json").read_text())
STYLES  = json.loads((ROOT / ".triage" / "style-systems.json").read_text())

SCHEME_02 = next(s for s in SCHEMES if s["n"] == 2)  # DEEP CURRENT

ACE_DEMOS_DIR = FEED / "external" / "aceternity-ui-pro" / "demos"
UNTITLED_TEMPLATES = FEED / "external" / "untitled-ui-pro" / "templates"
UNTITLED_TEMPLATES_PRO = FEED / "external" / "untitled-ui-pro" / "templates-pro"


# ---------- colour helpers ----------------------------------------------

def hex_to_rgba(h: str, a: float = 1.0) -> dict[str, float]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r = int(h[0:2], 16) / 255.0
    g = int(h[2:4], 16) / 255.0
    b = int(h[4:6], 16) / 255.0
    return {"r": round(r, 4), "g": round(g, 4), "b": round(b, 4), "a": round(a, 4)}


def solid_fill(h: str, a: float = 1.0) -> dict[str, Any]:
    return {
        "blendMode": "NORMAL",
        "type": "SOLID",
        "color": hex_to_rgba(h, a),
    }


# ---------- node helpers ------------------------------------------------

def frame(
    node_id: str,
    name: str,
    x: float,
    y: float,
    w: float,
    h: float,
    *,
    fill: str | None = None,
    stroke: str | None = None,
    children: list[dict[str, Any]] | None = None,
    layout_mode: str = "NONE",
    padding: int = 0,
    item_spacing: int = 0,
    corner_radius: int = 0,
) -> dict[str, Any]:
    node: dict[str, Any] = {
        "id": node_id,
        "name": name,
        "type": "FRAME",
        "scrollBehavior": "SCROLLS",
        "blendMode": "PASS_THROUGH",
        "absoluteBoundingBox": {"x": x, "y": y, "width": w, "height": h},
        "absoluteRenderBounds": {"x": x, "y": y, "width": w, "height": h},
        "constraints": {"vertical": "TOP", "horizontal": "LEFT"},
        "clipsContent": True,
        "background": [solid_fill(fill)] if fill else [],
        "fills": [solid_fill(fill)] if fill else [],
        "strokes": [solid_fill(stroke)] if stroke else [],
        "strokeWeight": 1 if stroke else 0,
        "strokeAlign": "INSIDE",
        "backgroundColor": hex_to_rgba(fill) if fill else hex_to_rgba("#000000", 0),
        "effects": [],
        "cornerRadius": corner_radius,
        "layoutMode": layout_mode,
        "primaryAxisSizingMode": "FIXED",
        "counterAxisSizingMode": "FIXED",
        "primaryAxisAlignItems": "MIN",
        "counterAxisAlignItems": "MIN",
        "paddingLeft": padding,
        "paddingRight": padding,
        "paddingTop": padding,
        "paddingBottom": padding,
        "itemSpacing": item_spacing,
        "children": children or [],
    }
    return node


def text_node(
    node_id: str,
    name: str,
    x: float,
    y: float,
    w: float,
    h: float,
    characters: str,
    *,
    font_family: str = "IBM Plex Sans",
    font_weight: int = 400,
    font_size: int = 14,
    line_height_px: float = 20,
    letter_spacing: float = 0,
    fill: str = "#EDEDF0",
    text_case: str = "ORIGINAL",
    text_align_horizontal: str = "LEFT",
) -> dict[str, Any]:
    return {
        "id": node_id,
        "name": name,
        "type": "TEXT",
        "scrollBehavior": "SCROLLS",
        "blendMode": "PASS_THROUGH",
        "absoluteBoundingBox": {"x": x, "y": y, "width": w, "height": h},
        "absoluteRenderBounds": {"x": x, "y": y, "width": w, "height": h},
        "constraints": {"vertical": "TOP", "horizontal": "LEFT"},
        "fills": [solid_fill(fill)],
        "strokes": [],
        "strokeWeight": 0,
        "strokeAlign": "OUTSIDE",
        "effects": [],
        "characters": characters,
        "style": {
            "fontFamily": font_family,
            "fontPostScriptName": f"{font_family.replace(' ', '')}-{ 'Bold' if font_weight >= 700 else 'Regular' }",
            "fontWeight": font_weight,
            "fontSize": font_size,
            "textAlignHorizontal": text_align_horizontal,
            "textAlignVertical": "TOP",
            "letterSpacing": letter_spacing,
            "lineHeightPx": line_height_px,
            "lineHeightPercent": 100,
            "lineHeightUnit": "PIXELS",
            "textCase": text_case,
        },
        "layoutVersion": 4,
        "characterStyleOverrides": [],
        "styleOverrideTable": {},
        "lineTypes": ["NONE"],
        "lineIndentations": [0],
    }


def rect(
    node_id: str,
    name: str,
    x: float,
    y: float,
    w: float,
    h: float,
    *,
    fill: str | None = None,
    stroke: str | None = None,
    corner_radius: int = 0,
) -> dict[str, Any]:
    return {
        "id": node_id,
        "name": name,
        "type": "RECTANGLE",
        "scrollBehavior": "SCROLLS",
        "blendMode": "PASS_THROUGH",
        "absoluteBoundingBox": {"x": x, "y": y, "width": w, "height": h},
        "absoluteRenderBounds": {"x": x, "y": y, "width": w, "height": h},
        "constraints": {"vertical": "TOP", "horizontal": "LEFT"},
        "fills": [solid_fill(fill)] if fill else [],
        "strokes": [solid_fill(stroke)] if stroke else [],
        "strokeWeight": 1 if stroke else 0,
        "strokeAlign": "INSIDE",
        "effects": [],
        "cornerRadius": corner_radius,
    }


def canvas(
    node_id: str,
    name: str,
    bg_hex: str,
    children: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "id": node_id,
        "name": name,
        "type": "CANVAS",
        "scrollBehavior": "SCROLLS",
        "children": children,
        "backgroundColor": hex_to_rgba(bg_hex),
        "prototypeStartNodeID": None,
        "flowStartingPoints": [],
        "prototypeDevice": {
            "type": "NONE",
            "rotation": "NONE",
        },
    }


# ---------- clawmachine pages ------------------------------------------

def clawmachine_sidebar(canvas_idx: int, page_accent: str, active_page: str) -> dict[str, Any]:
    """208-px nav sidebar replicating CLAWMACHINE-DESIGN-SYSTEM.html."""
    items = [
        ("DASHBOARD",    SCHEME_02["pg"]["dashboard"]),
        ("INVENTORY",    SCHEME_02["pg"]["inventory"]),
        ("ANALYTICS",    SCHEME_02["pg"]["analytics"]),
        ("BRAIN",        SCHEME_02["pg"]["brain"]),
        ("MESH",         SCHEME_02["pg"]["mesh"]),
        ("AGENTCONSOLE", SCHEME_02["pg"]["onboarding"]),  # onb accent reused
        ("SETTINGS",     SCHEME_02["pg"]["settings"]),
    ]

    brand = text_node(
        f"{canvas_idx}:100", "wordmark",
        8, 24, 192, 26,
        "clawmachine",
        font_family="Satoshi", font_weight=700, font_size=22,
        line_height_px=26, letter_spacing=-0.44,
        fill="#EDEDF0", text_case="LOWER",
    )

    nav_children = []
    for i, (label, accent) in enumerate(items):
        is_active = label == active_page
        row_y = 72 + i * 36
        row_fill = "#0F1822" if is_active else None
        row_stroke = "#1F3145" if is_active else None
        row = frame(
            f"{canvas_idx}:{200 + i}",
            f"nav-{label.lower()}",
            8, row_y, 192, 32,
            fill=row_fill, stroke=row_stroke,
            layout_mode="HORIZONTAL", padding=12, item_spacing=12,
            children=[
                rect(f"{canvas_idx}:{300 + i}", f"bullet-{label.lower()}",
                     16, row_y + 13, 6, 6,
                     fill=accent if is_active else "#48485A"),
                text_node(
                    f"{canvas_idx}:{400 + i}", f"label-{label.lower()}",
                    40, row_y + 8, 120, 16,
                    label,
                    font_family="JetBrains Mono", font_weight=500, font_size=11,
                    line_height_px=16, letter_spacing=1.32,
                    fill="#EDEDF0" if is_active else "#9898AD",
                    text_case="UPPER",
                ),
            ],
        )
        nav_children.append(row)

    sidebar = frame(
        f"{canvas_idx}:50", "sidebar",
        0, 0, 208, 960,
        fill="#0A1118", stroke="#1F3145",
        children=[brand, *nav_children],
    )
    return sidebar


def clawmachine_topbar(canvas_idx: int, title: str, page_accent: str) -> dict[str, Any]:
    title_node = text_node(
        f"{canvas_idx}:510", "page-title",
        24, 20, 400, 24,
        title,
        font_family="Satoshi", font_weight=700, font_size=18,
        line_height_px=24, letter_spacing=2.52,
        fill=page_accent, text_case="UPPER",
    )
    status_live = frame(
        f"{canvas_idx}:520", "status-pill-live",
        900, 18, 90, 26,
        fill="#0A1118", stroke="#1F3145",
        layout_mode="HORIZONTAL", padding=8, item_spacing=8,
        children=[
            rect(f"{canvas_idx}:521", "dot", 912, 28, 6, 6, fill=page_accent),
            text_node(
                f"{canvas_idx}:522", "label",
                924, 22, 60, 16,
                "LIVE",
                font_family="JetBrains Mono", font_weight=500, font_size=10,
                line_height_px=16, letter_spacing=1.2,
                fill="#9898AD", text_case="UPPER",
            ),
        ],
    )
    clock = text_node(
        f"{canvas_idx}:530", "clock",
        1000, 22, 200, 16,
        "00:00:00 / LON",
        font_family="JetBrains Mono", font_weight=500, font_size=10,
        line_height_px=16, letter_spacing=1.2,
        fill="#9898AD", text_case="UPPER",
    )

    return frame(
        f"{canvas_idx}:500", "topbar",
        208, 0, 1232, 64,
        fill="#060B10", stroke="#1F3145",
        children=[title_node, status_live, clock],
    )


def clawmachine_kpi_grid(canvas_idx: int, y: int, labels_values: list[tuple[str, str, str, str]]) -> list[dict[str, Any]]:
    """labels_values items: (label, value, delta, delta_class: gain|loss|neutral)"""
    nodes: list[dict[str, Any]] = []
    for i, (label, value, delta, klass) in enumerate(labels_values):
        x = 232 + i * 300
        card_fill = "#0A1118"
        delta_col = "#00E5A0" if klass == "gain" else "#FF4057" if klass == "loss" else "#9898AD"
        card = frame(
            f"{canvas_idx}:{600 + i}",
            f"kpi-{i}",
            x, y, 284, 120,
            fill=card_fill, stroke="#1F3145",
            children=[
                text_node(f"{canvas_idx}:{610 + i}", "label",
                          x + 16, y + 16, 252, 14,
                          label,
                          font_family="JetBrains Mono", font_weight=500, font_size=10,
                          line_height_px=14, letter_spacing=1.4,
                          fill="#8A8AA8", text_case="UPPER"),
                text_node(f"{canvas_idx}:{620 + i}", "value",
                          x + 16, y + 40, 252, 28,
                          value,
                          font_family="JetBrains Mono", font_weight=700, font_size=22,
                          line_height_px=28, letter_spacing=0,
                          fill="#EDEDF0"),
                text_node(f"{canvas_idx}:{630 + i}", "delta",
                          x + 16, y + 80, 252, 14,
                          delta,
                          font_family="JetBrains Mono", font_weight=500, font_size=10,
                          line_height_px=14, letter_spacing=0,
                          fill=delta_col),
            ],
        )
        nodes.append(card)
    return nodes


def clawmachine_panel(
    canvas_idx: int,
    slot: int,
    x: int, y: int, w: int, h: int,
    title: str,
    aux: str,
    body_rows: list[str],
) -> dict[str, Any]:
    head = frame(
        f"{canvas_idx}:{700 + slot * 50}",
        "panel-head",
        x, y, w, 40,
        fill="#0A1118", stroke="#1F3145",
        layout_mode="HORIZONTAL", padding=16, item_spacing=16,
        children=[
            text_node(
                f"{canvas_idx}:{701 + slot * 50}", "title",
                x + 16, y + 12, w - 180, 16,
                title,
                font_family="Satoshi", font_weight=700, font_size=12,
                line_height_px=16, letter_spacing=2.16,
                fill="#EDEDF0", text_case="UPPER",
            ),
            text_node(
                f"{canvas_idx}:{702 + slot * 50}", "aux",
                x + w - 160, y + 14, 144, 14,
                aux,
                font_family="JetBrains Mono", font_weight=500, font_size=10,
                line_height_px=14, letter_spacing=1.2,
                fill="#8A8AA8", text_case="UPPER",
                text_align_horizontal="RIGHT",
            ),
        ],
    )
    row_nodes: list[dict[str, Any]] = []
    for ri, txt in enumerate(body_rows):
        row_y = y + 40 + ri * 36
        row_fill = "#0A1118" if ri % 2 == 1 else "#060B10"
        row = frame(
            f"{canvas_idx}:{710 + slot * 50 + ri}",
            f"row-{ri}",
            x, row_y, w, 36,
            fill=row_fill, stroke="#1F3145",
            children=[
                text_node(
                    f"{canvas_idx}:{720 + slot * 50 + ri}",
                    f"row-{ri}-text",
                    x + 16, row_y + 11, w - 32, 14,
                    txt,
                    font_family="JetBrains Mono", font_weight=500, font_size=12,
                    line_height_px=14, letter_spacing=0,
                    fill="#D6D6E8",
                ),
            ],
        )
        row_nodes.append(row)

    outer = frame(
        f"{canvas_idx}:{700 + slot * 50 - 1}",
        f"panel-{slot}",
        x, y, w, h,
        fill="#060B10", stroke="#1F3145",
        children=[head, *row_nodes],
    )
    return outer


def clawmachine_page_canvas(
    idx: int,
    page_name: str,
    active: str,
    accent_hex: str,
    kpis: list[tuple[str, str, str, str]],
    panels: list[tuple[str, str, list[str]]],
) -> dict[str, Any]:
    canvas_id = f"{idx}:0"
    children: list[dict[str, Any]] = []
    children.append(clawmachine_sidebar(idx, accent_hex, active))
    children.append(clawmachine_topbar(idx, page_name, accent_hex))
    children.extend(clawmachine_kpi_grid(idx, 96, kpis))

    # two-panel body grid
    panel_y = 240
    for slot_i, (title, aux, rows) in enumerate(panels):
        col = slot_i % 2
        row = slot_i // 2
        px = 232 + col * 608
        py = panel_y + row * 280
        children.append(
            clawmachine_panel(idx, slot_i, px, py, 584, 260, title, aux, rows)
        )

    # Root FRAME for the page body
    root = frame(
        f"{idx}:1",
        f"{page_name.lower()}-root",
        0, 0, 1440, 960,
        fill="#060B10", stroke="#1F3145",
        children=children,
    )

    return canvas(canvas_id, page_name, "#060B10", [root])


def build_clawmachine_document() -> dict[str, Any]:
    pg = SCHEME_02["pg"]
    pages: list[dict[str, Any]] = []

    pages.append(clawmachine_page_canvas(
        1, "Dashboard", "DASHBOARD", pg["dashboard"],
        kpis=[
            ("PROFIT MTD",      "£3,482.10",  "+12.4% vs L30",     "gain"),
            ("ACTIVE LOTS",     "38",          "7 fresh today",     "neutral"),
            ("WIN RATE",        "71.3%",       "+4.1pp week",       "gain"),
            ("EXPOSURE",        "£1,204.00",   "within ceiling",    "neutral"),
        ],
        panels=[
            ("LIVE DEAL FEED", "15 MIN WINDOW",
             ["GUMTREE • iPhone 13 Pro 128 GB / Excellent / £340",
              "FACEBOOK • MacBook Pro 14 M1 / Good / £720",
              "SHPOCK • iPad 10 WiFi / Mint / £180",
              "CEX • Nintendo Switch OLED / Good / £195",
              "PRELOVED • Dyson V11 / Fair / £148"]),
            ("QUEUE / NEXT ACTIONS", "4 WAITING",
             ["MESSAGE SELLER → 32 Hillside Rd / poll in 40 min",
              "PAYOUT CONFIRM → deposit £120 pending",
              "LISTING LIVE → eBay 'MBP 14 M1' / 3 views",
              "COURIER ETA → DPD tomorrow 09:30"]),
            ("TODAY'S P&L CURVE", "ROLLING 24 H",
             ["09:00 → +£42.00",
              "11:00 → +£118.00",
              "14:00 → +£210.00",
              "17:00 → +£312.00"]),
            ("AGENT STATUS", "3 AGENTS LIVE",
             ["SCOUT → Pi01 / 12 queries/min",
              "EVAL → Studio / gemma-4 27B",
              "COURIER-TRACK → LocalMac / idle"]),
        ],
    ))

    pages.append(clawmachine_page_canvas(
        2, "Inventory", "INVENTORY", pg["inventory"],
        kpis=[
            ("OPEN SKUs",     "61",         "48 listable",    "neutral"),
            ("BUY AVG",       "£132.40",    "-3% week",       "gain"),
            ("FLIP DAYS AVG", "7.1",        "target <10",     "gain"),
            ("SELL PRICE SUM","£12,480",    "forecast Q",     "neutral"),
        ],
        panels=[
            ("DEVICES IN STOCK", "61 LOTS",
             ["IPHONE 13 PRO 128 / MINT / £310 → list",
              "MBP 14 M1 / GOOD / £680 → photo queue",
              "NINTENDO SWITCH OLED / GOOD / £168 → listed",
              "IPAD 10 WIFI / MINT / £160 → courier",
              "DYSON V11 / FAIR / £118 → parts strip"]),
            ("REFURB WORKLIST", "12 OPEN",
             ["REPLACE BATTERY → iPhone 12 × 3",
              "DEEP CLEAN → Dyson V11",
              "SCREEN POLISH → MBP 14 × 2",
              "FIRMWARE RESET → Switch OLED"]),
            ("SOURCE MIX", "LAST 30 DAYS",
             ["GUMTREE → 42%",
              "FACEBOOK → 28%",
              "SHPOCK → 12%",
              "PRELOVED → 10%",
              "CEX BUY-IN → 8%"]),
            ("LISTING HEALTH", "REAL-TIME",
             ["EBAY → 14 active / 3 watching",
              "VINTED UK → 6 active / 1 offer",
              "GUMTREE RELIST → 2 stale",
              "FB MARKETPLACE → 8 active"]),
        ],
    ))

    pages.append(clawmachine_page_canvas(
        3, "Analytics", "ANALYTICS", pg["analytics"],
        kpis=[
            ("PIPELINE VALUE", "£8,940",    "ROI 41%",       "gain"),
            ("AVG MARGIN",     "32.1%",     "+1.8 pp month", "gain"),
            ("DEAD STOCK",     "3",         "aged >45 d",    "loss"),
            ("SEARCH HITS",    "1,204",     "feed 15 m",     "neutral"),
        ],
        panels=[
            ("PROFIT BY CATEGORY", "L30D",
             ["PHONES → £1,840 / 42%",
              "LAPTOPS → £1,210 / 28%",
              "CONSOLES → £612 / 14%",
              "TABLETS → £418 / 10%",
              "OTHER → £260 / 6%"]),
            ("CONDITION YIELDS", "L30D",
             ["MINT → 61% gross margin",
              "EXCELLENT → 44%",
              "GOOD → 31%",
              "FAIR → 18% (refurb uplift)"]),
            ("BUY→SELL TIME HISTOGRAM", "DAYS",
             ["0-3 → 12 lots",
              "4-7 → 24 lots",
              "8-14 → 18 lots",
              "15-30 → 6 lots",
              "31+ → 3 lots"]),
            ("SOURCE-LEVEL ROI", "PER CHANNEL",
             ["GUMTREE → 38%",
              "FACEBOOK → 29%",
              "SHPOCK → 22%",
              "PRELOVED → 19%"]),
        ],
    ))

    pages.append(clawmachine_page_canvas(
        4, "Brain", "BRAIN", pg["brain"],
        kpis=[
            ("MODELS LOADED", "3",          "Studio+Pi",     "neutral"),
            ("TOKENS/S",      "128",        "gemma-4 27B",   "gain"),
            ("MEM USE",       "184 GB/512", "headroom 64%",  "gain"),
            ("KL DRIFT",      "<0.1",       "abliteration",  "neutral"),
        ],
        panels=[
            ("ACTIVE MODELS", "VLLM-MLX",
             ["GEMMA-4-27B-HERETICAL → Studio GPU-0",
              "QWEN-14B-JACKRONG-V2 → Studio GPU-1",
              "CS2764-QWEN-BACKUP → idle-hot",
              "EMBED-BGE-M3 → Pi / RAM"]),
            ("PROMPT PACKS", "VERSIONED",
             ["EVAL-DEAL-V3 → 124 shots / stable",
              "COND-GRADE-V2 → 86 shots / drift-check OK",
              "LOT-SPLIT-V1 → 34 shots / beta",
              "SELLER-MSG-V4 → 212 shots / prod"]),
            ("CAPTURED MEMORIES", "SUPERMEMORY",
             ["regan.cooney @ UK fix-flip reseller",
              "scheme-02 deep-current accepted 2026-04-21",
              "pro-license untitledui v8 paywalled",
              "clawmachine_mission: frankenstein stitch"]),
            ("INFERENCE QUEUE", "BACKPRESSURE",
             ["COMING IN → 14 / 20 slots",
              "IN-FLIGHT → 4",
              "COMPLETED L10M → 812",
              "FAILED L10M → 3 / retried"]),
        ],
    ))

    pages.append(clawmachine_page_canvas(
        5, "Mesh", "MESH", pg["mesh"],
        kpis=[
            ("NODES ONLINE", "4/4",     "all green",    "gain"),
            ("CHANNELS",     "18",      "WA+BB+Disc",   "neutral"),
            ("LATENCY AVG",  "184 ms",  "Pi→Studio",    "neutral"),
            ("MSG Q DEPTH",  "12",      "no lag",       "gain"),
        ],
        panels=[
            ("MESH NODES", "LIVE TOPOLOGY",
             ["STUDIO-01 @ 100.103.16.45:18789 → primary inference",
              "PI-SCOUT @ 100.108.234.18:3847 → browser + decodo",
              "MBP-CORE @ localhost:3000 → orchestrator",
              "BACKUP-SSD @ /Volumes/ext → assets cache"]),
            ("MESSAGE CHANNELS", "OPENCLAW BRIDGES",
             ["BLUEBUBBLES → iMessage / up",
              "WHATSAPP → web client / up",
              "DISCORD BOT → 3 guilds / up",
              "SIGNAL → linked / up",
              "TELEGRAM → linked / up"]),
            ("ROUTE MAP", "HOP BREAKDOWN",
             ["SELLER-REPLY → Bridge → Scout → Eval → Queue",
              "DEAL-ALERT → Scout → Eval → Dashboard",
              "COURIER-UPDATE → Bridge → Mesh → Inventory",
              "INVENTORY-SYNC → Studio → Dashboard / 5 min"]),
            ("DECODO TIER", "PROXY LAYER",
             ["DEDICATED ISP → 3 UK static / unlimited",
              "RESIDENTIAL → exhausted / retired",
              "MOBILE → exhausted / retired",
              "DATACENTER → fallback only"]),
        ],
    ))

    pages.append(clawmachine_page_canvas(
        6, "AgentConsole", "AGENTCONSOLE", pg["onboarding"],
        kpis=[
            ("AGENTS",       "6",          "3 active",    "neutral"),
            ("TOOL CALLS",   "482 / hr",   "rolling",     "gain"),
            ("COST MTD",     "£41.20",     "self-host",   "gain"),
            ("ESCALATIONS",  "2 open",     "need op",     "loss"),
        ],
        panels=[
            ("ACTIVE AGENTS", "LOOP STATE",
             ["SCOUT → scraping gumtree / loop 3s",
              "EVAL → grading 4 lots / batch",
              "MESSAGE → composing 2 seller replies",
              "COURIER-TRACK → idle / next poll 15m",
              "FINANCE → reconciling / nightly",
              "META-OBSERVER → auditing / on-demand"]),
            ("TOOL CATALOG", "MCP-BASED",
             ["FIRECRAWL → search + scrape",
              "DECODO → proxy rotate",
              "PLAYWRIGHT → browser",
              "BLUEBUBBLES → iMessage send",
              "SUPERMEMORY → recall + write"]),
            ("AGENT CHAT LOG", "LAST 10 TURNS",
             ["SCOUT → eval: new lot 'iPhone 13 Pro' £340",
              "EVAL → scout: COND=EXCELLENT, target £460, margin 35%",
              "MESSAGE → seller: 'hi, can we do £310?'",
              "SELLER → message: 'ok, collection?'",
              "COURIER-TRACK → message: booked DPD tomorrow 09:30"]),
            ("ESCALATION QUEUE", "OPERATOR REQ",
             ["LOT 'MBP 14 M1 £720' → exceeds ceiling / need op approve",
              "SELLER 32 Hillside Rd → address ambiguity / verify"]),
        ],
    ))

    pages.append(clawmachine_page_canvas(
        7, "Settings", "SETTINGS", pg["settings"],
        kpis=[
            ("BUDGET MTD",     "£1,204 / £1,500", "80% spent",    "neutral"),
            ("MAX PER LOT",    "£600",            "guard-rail",   "neutral"),
            ("GEOFENCE",       "40 mi LND",       "collection",   "neutral"),
            ("PRIVACY",        "local-only",      "no-cloud-LLM", "gain"),
        ],
        panels=[
            ("ACCOUNT", "REGAN COONEY",
             ["email → regacooney@gmail.com",
              "phone → +44 7*** *** ***",
              "address → UK SW19",
              "vendor-status → LIVE musicMagpie, webse.co.uk"]),
            ("RULES ENGINE", "THRESHOLDS",
             ["min margin → 22%",
              "max ceiling per lot → £600",
              "auto-offer step → -£15",
              "refurb budget cap → £40"]),
            ("KEYS & VAULTS", "MACOS KEYCHAIN",
             ["decodo-* → live",
              "augment-session-auth → live",
              "openai-token → unset",
              "anthropic-token → unset (offline)"]),
            ("SCHEME SELECTION", "62 PALETTES AVAILABLE",
             ["ACTIVE → #02 DEEP CURRENT",
              "SHORTLIST → 32+6 dark / 5+3 light",
              "LOGO → deferred",
              "MOTION → easeOutBack 260ms"]),
        ],
    ))

    # Reference components block
    components = {
        "1:100": {
            "key": "cm-wordmark",
            "name": "wordmark",
            "description": "clawmachine — Satoshi 700, lowercase, scheme-primary accent on 'machine' token.",
            "documentationLinks": [],
            "remote": False,
        },
        "1:200": {
            "key": "cm-nav-row",
            "name": "nav-row",
            "description": "Sidebar nav row, JetBrains Mono 11 / 1.32 tracking, inset bevel on active.",
            "documentationLinks": [],
            "remote": False,
        },
        "1:500": {
            "key": "cm-topbar",
            "name": "topbar",
            "description": "Per-page topbar — Satoshi title in page-accent + mono status pills.",
            "documentationLinks": [],
            "remote": False,
        },
        "1:600": {
            "key": "cm-kpi",
            "name": "kpi-card",
            "description": "120-px dense card: mono label, 22-px mono value, delta in gain/loss token.",
            "documentationLinks": [],
            "remote": False,
        },
        "1:700": {
            "key": "cm-panel",
            "name": "panel",
            "description": "Panel with 40-px head, zebra rows, inset bevel highlight.",
            "documentationLinks": [],
            "remote": False,
        },
    }

    component_sets: dict[str, Any] = {}

    # Styles — 62 palette colours + style-system fills
    styles: dict[str, dict[str, Any]] = {}
    for s in SCHEMES:
        key = f"scheme-{s['n']:02d}-{re.sub(r'[^a-z]+', '-', s['name'].lower()).strip('-')}"
        styles[f"S:{s['n']}:primary"] = {
            "key": f"{key}-primary",
            "name": f"schemes/{s['n']:02d}-{s['name']}/primary",
            "styleType": "FILL",
            "description": f"{s['type']} / void {s['void']} / primary {s['p']}",
            "remote": False,
        }
        styles[f"S:{s['n']}:secondary"] = {
            "key": f"{key}-secondary",
            "name": f"schemes/{s['n']:02d}-{s['name']}/secondary",
            "styleType": "FILL",
            "description": f"{s['type']} / secondary {s['s']}",
            "remote": False,
        }
        styles[f"S:{s['n']}:void"] = {
            "key": f"{key}-void",
            "name": f"schemes/{s['n']:02d}-{s['name']}/void",
            "styleType": "FILL",
            "description": f"{s['type']} / void {s['void']}",
            "remote": False,
        }

    # 20 style systems as text styles
    for sys in STYLES:
        sys_id = f"T:{sys['n']}"
        styles[sys_id] = {
            "key": f"style-system-{sys['n']:02d}-{sys['id']}",
            "name": f"style-systems/{sys['n']:02d}-{sys['name']}",
            "styleType": "TEXT",
            "description": sys["variables"].get("desc", ""),
            "remote": False,
        }

    document = {
        "id": "0:0",
        "name": "Document",
        "type": "DOCUMENT",
        "children": pages,
    }

    return {
        "name": "clawmachine — design system",
        "role": "owner",
        "lastModified": "2026-04-21T00:00:00Z",
        "editorType": "figma",
        "thumbnailUrl": None,
        "version": "1",
        "document": document,
        "components": components,
        "componentSets": component_sets,
        "schemaVersion": 0,
        "styles": styles,
        "mainFileKey": "clawmachine-synth-2026-04-21",
        "linkAccess": "view",
    }


# ---------- generic template canvas ------------------------------------

def generic_template_canvas(
    idx: int,
    page_name: str,
    hero_copy: str,
    body_sections: list[tuple[str, str, list[str]]],
    bg: str = "#FFFFFF",
    fg: str = "#101014",
    accent: str = "#101014",
    width: int = 1440,
    height: int = 960,
) -> dict[str, Any]:
    """Generic canvas used by Untitled UI Pro + Aceternity Pro schemas."""
    body_fill = bg
    text_fill = fg

    nav = frame(
        f"{idx}:100", "nav",
        0, 0, width, 72,
        fill=body_fill, stroke="#E2E2E8",
        children=[
            text_node(f"{idx}:101", "brand",
                      32, 24, 200, 24,
                      page_name.split("/", 1)[0],
                      font_family="Satoshi", font_weight=700, font_size=18,
                      line_height_px=24, letter_spacing=-0.36,
                      fill=text_fill),
            text_node(f"{idx}:102", "link-1",
                      width - 420, 26, 80, 20,
                      "Product",
                      font_family="Inter", font_weight=500, font_size=14,
                      line_height_px=20, letter_spacing=0,
                      fill=text_fill),
            text_node(f"{idx}:103", "link-2",
                      width - 320, 26, 80, 20,
                      "Solutions",
                      font_family="Inter", font_weight=500, font_size=14,
                      line_height_px=20, letter_spacing=0,
                      fill=text_fill),
            text_node(f"{idx}:104", "link-3",
                      width - 220, 26, 80, 20,
                      "Pricing",
                      font_family="Inter", font_weight=500, font_size=14,
                      line_height_px=20, letter_spacing=0,
                      fill=text_fill),
            text_node(f"{idx}:105", "cta",
                      width - 120, 26, 80, 20,
                      "Sign in",
                      font_family="Inter", font_weight=600, font_size=14,
                      line_height_px=20, letter_spacing=0,
                      fill=accent),
        ],
    )

    hero = frame(
        f"{idx}:200", "hero",
        0, 72, width, 420,
        fill=body_fill,
        children=[
            text_node(f"{idx}:201", "eyebrow",
                      120, 128, 400, 20,
                      page_name.upper(),
                      font_family="JetBrains Mono", font_weight=500, font_size=12,
                      line_height_px=20, letter_spacing=1.44,
                      fill=accent, text_case="UPPER"),
            text_node(f"{idx}:202", "hero-title",
                      120, 160, width - 240, 80,
                      hero_copy,
                      font_family="Satoshi", font_weight=700, font_size=56,
                      line_height_px=64, letter_spacing=-1.12,
                      fill=text_fill),
            text_node(f"{idx}:203", "hero-sub",
                      120, 252, width - 240, 60,
                      f"{page_name} — Clawmachine internal substitute for the paywalled Pro .fig. "
                      "Rendered locally by the Claude Design anchor.",
                      font_family="Inter", font_weight=400, font_size=18,
                      line_height_px=28, letter_spacing=0,
                      fill="#5E5E72"),
            rect(f"{idx}:204", "cta-primary",
                 120, 332, 160, 48,
                 fill=accent, corner_radius=4),
            text_node(f"{idx}:205", "cta-primary-text",
                      120, 344, 160, 24,
                      "Get started",
                      font_family="Inter", font_weight=600, font_size=14,
                      line_height_px=24, letter_spacing=0,
                      fill=bg, text_align_horizontal="CENTER"),
            rect(f"{idx}:206", "cta-ghost",
                 296, 332, 160, 48,
                 stroke="#32323F", corner_radius=4),
            text_node(f"{idx}:207", "cta-ghost-text",
                      296, 344, 160, 24,
                      "Docs",
                      font_family="Inter", font_weight=600, font_size=14,
                      line_height_px=24, letter_spacing=0,
                      fill=text_fill, text_align_horizontal="CENTER"),
        ],
    )

    # body sections
    sections: list[dict[str, Any]] = []
    section_y = 492
    for si, (title, subtitle, items) in enumerate(body_sections):
        sec = frame(
            f"{idx}:{300 + si * 50}",
            f"section-{si}",
            120, section_y + si * 260, width - 240, 240,
            fill=body_fill, stroke="#E2E2E8",
            children=[
                text_node(f"{idx}:{301 + si * 50}", "title",
                          24, 24, width - 288, 28,
                          title,
                          font_family="Satoshi", font_weight=700, font_size=22,
                          line_height_px=28, letter_spacing=-0.44,
                          fill=text_fill),
                text_node(f"{idx}:{302 + si * 50}", "subtitle",
                          24, 56, width - 288, 20,
                          subtitle,
                          font_family="Inter", font_weight=400, font_size=14,
                          line_height_px=20, letter_spacing=0,
                          fill="#5E5E72"),
                *[
                    text_node(
                        f"{idx}:{310 + si * 50 + ii}",
                        f"item-{ii}",
                        24 + ii * 260, 104, 236, 60,
                        item,
                        font_family="Inter", font_weight=500, font_size=14,
                        line_height_px=20, letter_spacing=0,
                        fill=text_fill,
                    )
                    for ii, item in enumerate(items[:4])
                ],
            ],
        )
        sections.append(sec)

    root = frame(
        f"{idx}:1", f"{page_name.lower().replace(' ', '-')}-root",
        0, 0, width, max(height, section_y + len(body_sections) * 260 + 120),
        fill=body_fill,
        children=[nav, hero, *sections],
    )

    return canvas(f"{idx}:0", page_name, bg, [root])


# ---------- untitled ui pro --------------------------------------------

UNTITLED_PAGES: list[tuple[str, str, list[tuple[str, str, list[str]]]]] = [
    ("Landing",       "Ship polished product pages without the Pro paywall.",
     [("Above the fold",   "Hero slab + CTA + trust row",  ["Hero", "CTA primary", "CTA ghost", "Logo cloud"]),
      ("Feature grid",     "Four-up benefit cards",         ["Speed", "Scale", "Safety", "Stability"]),
      ("Pricing cut-in",   "Inline pricing teaser",         ["Starter", "Pro", "Team", "Enterprise"])]),
    ("Dashboard",     "Dense KPI tile layout.",
     [("Overview",         "Four tiles + chart",            ["Revenue", "Users", "Orders", "Churn"]),
      ("Activity",         "Table of recent events",         ["Login", "Export", "Purchase", "Refund"]),
      ("Widgets",          "Mix of metric cards",            ["LTV", "ARPU", "CAC", "DAU/MAU"])]),
    ("Pricing",       "Three-tier pricing with compare.",
     [("Tiers",             "Starter / Pro / Team",          ["£0/mo", "£29/mo", "£99/mo", "Custom"]),
      ("Feature matrix",     "Checks vs crosses",             ["Users", "Integrations", "Support", "SLA"]),
      ("FAQ",                "Accordion block",               ["Billing", "Refunds", "Cancel", "Upgrades"])]),
    ("Checkout",      "Two-step Stripe-style checkout.",
     [("Details",           "Name / email / card",           ["Name", "Email", "Card", "ZIP"]),
      ("Summary",           "Order summary card",            ["Product", "Qty", "Total", "Tax"]),
      ("Confirm",           "Final CTA + trust",             ["Pay", "Secure", "Refund", "Support"])]),
    ("Settings",      "App preferences canvas.",
     [("Profile",           "Avatar + name + email",         ["Name", "Email", "Avatar", "Timezone"]),
      ("Security",          "Password, 2FA, sessions",       ["Password", "2FA", "Sessions", "API keys"]),
      ("Billing",           "Invoice history + card",        ["Card", "Invoice", "Plan", "Usage"])]),
    ("Sign in",       "Email + social sign in.",
     [("Form",              "Email + password",              ["Email", "Password", "Remember", "Forgot"]),
      ("Social",            "Google / Apple / SSO",           ["Google", "Apple", "SSO", "Magic link"]),
      ("Legal",             "Tiny legal block",               ["ToS", "Privacy", "Cookies", "DPA"])]),
    ("Sign up",       "Onboarding-friendly sign up.",
     [("Form",              "Email + password + role",        ["Name", "Email", "Password", "Role"]),
      ("Plan",              "Choose plan",                    ["Free", "Pro", "Team", "Enterprise"]),
      ("Invite",            "Invite teammates",                ["Email 1", "Email 2", "Email 3", "Skip"])]),
    ("Forgot password","Single-field reset form.",
     [("Form",              "Email input",                    ["Email", "Submit", "Back", "Help"]),
      ("Check inbox",       "Confirmation screen",             ["Inbox", "Spam", "Resend", "Support"]),
      ("Reset",             "New password form",               ["Password", "Confirm", "Submit", "Login"])]),
    ("About",         "Company story page.",
     [("Hero",              "Mission statement",              ["Mission", "Vision", "Values", "Team"]),
      ("Timeline",          "Milestones by year",              ["2021", "2022", "2023", "2024"]),
      ("Team",              "Founder + hires",                 ["CEO", "CTO", "Design", "Eng"])]),
    ("Blog Index",    "Magazine-style index.",
     [("Featured",          "Top post",                       ["Title", "Hero img", "Lead", "Author"]),
      ("Recent",            "4-up grid",                      ["Post 1", "Post 2", "Post 3", "Post 4"]),
      ("Categories",        "Tag filters",                    ["Product", "Engineering", "Design", "Company"])]),
    ("Case Study",    "Deep-dive customer story.",
     [("Summary",           "Problem / solution / result",    ["Problem", "Solution", "Result", "Metric"]),
      ("Quote",             "Pull-quote from customer",        ["Quote", "Name", "Role", "Company"]),
      ("Related",           "3 similar stories",               ["CS 1", "CS 2", "CS 3", "View all"])]),
    ("CTA Section",   "Full-width conversion block.",
     [("Headline",          "Big headline + supporting",       ["H1", "H2", "Body", "CTA"]),
      ("CTA",               "Primary CTA row",                 ["Start free", "Book demo", "Pricing", "Docs"]),
      ("Trust",             "Logo cloud",                      ["Logo 1", "Logo 2", "Logo 3", "Logo 4"])]),
    ("Empty State Gallery","Empty states for every flow.",
     [("Inbox empty",       "No messages yet",                 ["Illustration", "Headline", "CTA", "Link"]),
      ("Search empty",      "No results",                       ["Illustration", "Headline", "CTA", "Link"]),
      ("Error 500",         "Server error",                    ["Illustration", "Headline", "CTA", "Link"])]),
    ("Error 404",      "Classic 404 page.",
     [("Graphic",            "404 illustration",                ["Glyph", "Headline", "Body", "CTA"]),
      ("Navigation",         "Links to top pages",              ["Home", "Blog", "Pricing", "Contact"]),
      ("Search",             "Inline search",                   ["Input", "Submit", "Tip", "Help"])]),
    ("FAQ",            "Accordion-style FAQ.",
     [("Top questions",      "10 accordions",                   ["Q1", "Q2", "Q3", "Q4"]),
      ("Categories",         "Tabbed categories",               ["Billing", "Account", "Product", "Support"]),
      ("Still stuck",        "Contact CTA",                     ["Chat", "Email", "Docs", "Status"])]),
    ("Feature Grid",   "Six-up feature card grid.",
     [("Row 1",              "Three cards",                     ["Speed", "Scale", "Safety", "Stability"]),
      ("Row 2",              "Three cards",                     ["Cost", "Compliance", "API", "Audit"]),
      ("Closing CTA",        "Inline CTA row",                   ["Start", "Docs", "Book demo", "Pricing"])]),
    ("Footer",         "Dense multi-column footer.",
     [("Link columns",       "Product / Company / Legal / Social", ["Product", "Company", "Legal", "Social"]),
      ("Newsletter",         "Email capture",                   ["Email", "Subscribe", "Unsubscribe", "Privacy"]),
      ("Copyright",          "Tiny legal bar",                   ["2026", "All rights", "ToS", "Privacy"])]),
    ("Logo Cloud",     "Customer logo showcase.",
     [("Primary cloud",      "6-logo marquee",                  ["Logo 1", "Logo 2", "Logo 3", "Logo 4"]),
      ("Secondary cloud",    "6-logo static",                   ["Logo 5", "Logo 6", "Logo 7", "Logo 8"]),
      ("Testimonial inline", "One-line testimonial",            ["Quote", "Name", "Role", "Company"])]),
    ("Pricing Compare","Table comparing three tiers.",
     [("Column headers",     "Plans + call-out",                 ["Free", "Pro", "Team", "Enterprise"]),
      ("Feature rows",       "Matrix of checkmarks",             ["Users", "API", "Support", "SLA"]),
      ("Contact",            "Enterprise CTA",                    ["Book demo", "Email", "Docs", "Status"])]),
    ("Testimonials",   "Customer proof grid.",
     [("Featured quote",     "Large pull-quote",                 ["Quote", "Photo", "Name", "Role"]),
      ("Quote grid",         "4-up testimonials",                ["T1", "T2", "T3", "T4"]),
      ("Company logos",      "Trust-row logos",                   ["Logo 1", "Logo 2", "Logo 3", "Logo 4"])]),
]


def build_untitled_document() -> dict[str, Any]:
    pages = []
    for i, (name, hero_copy, sections) in enumerate(UNTITLED_PAGES, start=1):
        pages.append(
            generic_template_canvas(
                idx=i,
                page_name=f"Untitled UI Pro / {name}",
                hero_copy=hero_copy,
                body_sections=sections,
                bg="#FFFFFF",
                fg="#101014",
                accent="#7F56D9",
            )
        )

    components = {
        "1:204": {"key": "uui-btn-primary",  "name": "button/primary", "description": "Solid button, 4-px radius.", "documentationLinks": [], "remote": False},
        "1:206": {"key": "uui-btn-ghost",    "name": "button/ghost",   "description": "Ghost button, 4-px radius.", "documentationLinks": [], "remote": False},
        "1:100": {"key": "uui-nav",          "name": "nav/top",        "description": "Top nav bar.", "documentationLinks": [], "remote": False},
        "1:200": {"key": "uui-hero",         "name": "hero/standard",  "description": "Standard hero slab with CTAs.", "documentationLinks": [], "remote": False},
    }

    styles = {
        "S:untitled-purple": {"key": "uui-purple-600", "name": "brand/purple-600", "styleType": "FILL", "description": "Untitled UI purple #7F56D9", "remote": False},
        "S:untitled-ink":    {"key": "uui-ink-900",    "name": "ink/900",           "styleType": "FILL", "description": "Near-black ink #101014", "remote": False},
        "S:untitled-paper":  {"key": "uui-paper",      "name": "paper/white",       "styleType": "FILL", "description": "White surface #FFFFFF", "remote": False},
        "T:uui-display":     {"key": "uui-display",    "name": "display/Satoshi-700", "styleType": "TEXT", "description": "Satoshi 700 for headlines.", "remote": False},
        "T:uui-body":        {"key": "uui-body",       "name": "body/Inter-400",     "styleType": "TEXT", "description": "Inter 400 body text.", "remote": False},
        "T:uui-mono":        {"key": "uui-mono",       "name": "mono/JBM-500",        "styleType": "TEXT", "description": "JetBrains Mono 500 for eyebrows.", "remote": False},
    }

    return {
        "name": "Untitled UI Pro — substitute design file",
        "role": "owner",
        "lastModified": "2026-04-21T00:00:00Z",
        "editorType": "figma",
        "thumbnailUrl": None,
        "version": "1",
        "document": {
            "id": "0:0",
            "name": "Document",
            "type": "DOCUMENT",
            "children": pages,
        },
        "components": components,
        "componentSets": {},
        "schemaVersion": 0,
        "styles": styles,
        "mainFileKey": "untitled-ui-pro-synth-2026-04-21",
        "linkAccess": "view",
    }


# ---------- aceternity pro ---------------------------------------------

ACE_CATEGORIES: list[tuple[str, list[str]]] = [
    ("Hero Sections — Effects", ["hero-section-with-beams-and-grid.html",
                                 "hero-section-with-dither-background.html",
                                 "hero-section-with-flickering-lights.html",
                                 "hero-section-with-mesh-gradient.html",
                                 "hero-section-with-mousemove.html",
                                 "hero-section-with-noise-background.html",
                                 "hero-section-with-shadow-and-scales.html",
                                 "hero-section-with-multi-color-background.html",
                                 "modern-hero-with-gradients.html"]),
    ("Hero Sections — Images",  ["hero-section-with-tabs.html",
                                 "hero-with-background-and-navbar.html",
                                 "hero-with-centered-image.html",
                                 "hero-with-image-and-scales.html",
                                 "hero-section-with-images-grid-and-navbar.html",
                                 "hero-section-with-infinite-scroll-cards.html",
                                 "playful-hero-section.html",
                                 "minimal-hero-section-with-parallax-images.html",
                                 "full-background-image-with-text.html"]),
    ("Bento Grids",            ["bento-grid.html",
                                "bento-grid-illustrations.html",
                                "bento-grid-with-skeletons.html",
                                "masonry-bento-grid-with-images.html",
                                "three-column-bento-grid.html",
                                "multi-illustration-bento.html",
                                "feature-section-bento-skeletons.html"]),
    ("Feature Sections",        ["feature-section-with-centered-skeleton.html",
                                 "feature-section-with-horizontal-skeletons.html",
                                 "feature-section-with-terminal.html",
                                 "feature-section-with-vertical-grids.html",
                                 "feature-with-inline-icons.html",
                                 "features-grid-with-large-skeletons.html",
                                 "features-section-with-skeletons.html",
                                 "features-with-hover-and-text-animation.html",
                                 "features-with-isometric-blocks.html",
                                 "features-with-stacked-isometric-boxes.html",
                                 "features-with-sticky-scroll.html",
                                 "multicolored-features.html",
                                 "dither-features.html"]),
    ("Testimonials",            ["testimonials-background-with-drag.html",
                                 "testimonials-grid-with-centered-carousel.html",
                                 "testimonials-hover-illustration.html",
                                 "testimonials-marquee-grid-boxed.html",
                                 "testimonials-marquee-grid.html",
                                 "testimonials-masonry-grid.html",
                                 "testimonials-with-carousel.html",
                                 "testimonials-with-centered-highlight.html",
                                 "centered-around-testimonials.html"]),
    ("Pricing",                 ["pricing-minimal.html",
                                 "pricing-page-with-featured-and-enterprise.html",
                                 "pricing-with-header-and-icons.html",
                                 "pricing-with-switch-and-add-on.html",
                                 "pricing-with-switch.html",
                                 "simple-pricing-with-three-tiers.html"]),
    ("Logo Clouds",             ["logo-cloud-marquee.html",
                                 "logo-cloud-with-blur-animation.html",
                                 "logo-cloud-with-swap-animation.html",
                                 "logos-with-blur-flip.html",
                                 "spotlight-logo-cloud.html",
                                 "centered-with-logo.html"]),
    ("Navbars",                 ["navbar-classic.html",
                                 "navbar-dark-shadow.html",
                                 "navbar-mega.html",
                                 "navbar-pill.html",
                                 "navbar-underline.html",
                                 "navbar-with-children.html",
                                 "simple-navbar-with-hover-effects.html"]),
    ("Stats",                   ["stats-for-changelog.html",
                                 "stats-with-gradient.html",
                                 "stats-with-grid-background.html",
                                 "stats-with-number-ticker.html"]),
    ("CTA Sections",            ["cta-centered-masonry-gallery.html",
                                 "cta-with-background-noise.html",
                                 "cta-with-dashed-grid-lines.html",
                                 "cta-with-masonry-images.html",
                                 "simple-cta-with-images.html"]),
    ("FAQs",                    ["faqs-with-dashed-lines.html",
                                 "faqs-with-grid.html",
                                 "simple-faqs-with-background.html"]),
    ("Blog",                    ["blog-content-centered.html",
                                 "blog-content-with-toc.html",
                                 "blog-with-search-magazine.html",
                                 "blog-with-search.html",
                                 "simple-blog-with-grid.html"]),
    ("Team",                    ["team-section-with-light-background.html",
                                 "team-section-with-scales.html",
                                 "team-section-with-small-avatars.html",
                                 "team-section-with-timeline-cards.html"]),
    ("Auth",                    ["login-form-with-gradient.html",
                                 "login-signup-minimal.html",
                                 "login-with-socials-and-email.html",
                                 "premium-auth-split.html",
                                 "registration-form-with-images.html",
                                 "simple-login-with-grid-lines.html"]),
    ("Contact",                 ["contact-form-grid-with-details.html",
                                 "contact-section-with-shader.html",
                                 "simple-centered-contact-form.html"]),
    ("Sidebars",                ["collapsible-sidebar.html",
                                 "grouped-sidebar.html",
                                 "simple-sidebar-with-hover.html"]),
    ("Backgrounds",             ["background-grid-with-dots-and-animations.html",
                                 "background-grid-with-dots.html",
                                 "background-with-full-video.html",
                                 "background-with-shooting-stars.html",
                                 "background-with-skewed-lines.html",
                                 "background-with-skewed-rectangles.html",
                                 "dot-distortion-shader.html",
                                 "lines-gradient-shader.html",
                                 "spotlight-shader.html"]),
    ("Illustrations",           ["animated-beam-path-illustration.html",
                                 "box-illustration.html",
                                 "inline-icon-illustration.html",
                                 "ipad-illustration.html",
                                 "iphone-illustration.html",
                                 "isometric-box.html",
                                 "keyboard-illustration.html",
                                 "macbook-illustration.html",
                                 "macbook-illustration-with-icons.html",
                                 "meeting-illustration.html",
                                 "slider-illustration.html",
                                 "text-highlight-illustration.html",
                                 "uptime-status-illustration.html",
                                 "world-map-illustration.html"]),
    ("Cards & Interactives",    ["draggable-cards.html",
                                 "dynamic-island.html",
                                 "expandable-card-on-click.html",
                                 "flipping-images-with-bar.html",
                                 "folder-with-files.html",
                                 "collaborative-cursors.html",
                                 "chat-conversation.html",
                                 "rotating-tabs-with-text.html",
                                 "text-generate-typewriter.html",
                                 "two-column-with-image.html"]),
    ("Footers",                 ["footer-with-big-text.html",
                                 "simple-footer-with-four-grids.html"]),
]


def build_aceternity_document() -> dict[str, Any]:
    pages = []
    for i, (cat, demos) in enumerate(ACE_CATEGORIES, start=1):
        sections: list[tuple[str, str, list[str]]] = []
        chunk_size = 4
        for j in range(0, len(demos), chunk_size):
            chunk = demos[j:j + chunk_size]
            sections.append(
                (
                    f"{cat} {j // chunk_size + 1}".strip(),
                    f"Block group {j // chunk_size + 1} — translated from Aceternity Pro HTML demos.",
                    [d.replace(".html", "").replace("-", " ") for d in chunk],
                )
            )
        if not sections:
            sections.append((cat, "Single-block category.", demos[:4]))

        pages.append(
            generic_template_canvas(
                idx=i,
                page_name=f"Aceternity Pro / {cat}",
                hero_copy=f"{cat}",
                body_sections=sections[:6],  # cap at 6 section rows per canvas
                bg="#0A0A0A",
                fg="#F5F5F5",
                accent="#A855F7",
            )
        )

    components = {
        "1:100": {"key": "ace-nav",        "name": "nav/top",         "description": "Dark nav bar, pill-style.", "documentationLinks": [], "remote": False},
        "1:200": {"key": "ace-hero-slab",  "name": "hero/slab",       "description": "Hero with beams / dither / mesh variants.", "documentationLinks": [], "remote": False},
        "1:204": {"key": "ace-btn-primary","name": "button/primary",  "description": "Purple primary CTA.", "documentationLinks": [], "remote": False},
    }

    styles = {
        "S:ace-ink":    {"key": "ace-ink",    "name": "ink/near-black", "styleType": "FILL", "description": "Dark background #0A0A0A", "remote": False},
        "S:ace-fg":     {"key": "ace-fg",     "name": "fg/near-white",  "styleType": "FILL", "description": "Text #F5F5F5", "remote": False},
        "S:ace-accent": {"key": "ace-accent", "name": "accent/violet",  "styleType": "FILL", "description": "Accent #A855F7", "remote": False},
        "T:ace-display": {"key": "ace-display", "name": "display/Satoshi-700", "styleType": "TEXT", "description": "Large display headings.", "remote": False},
        "T:ace-body":    {"key": "ace-body",    "name": "body/Inter-400",       "styleType": "TEXT", "description": "Body copy.", "remote": False},
        "T:ace-mono":    {"key": "ace-mono",    "name": "mono/JBM-500",          "styleType": "TEXT", "description": "Mono eyebrows.", "remote": False},
    }

    return {
        "name": "Aceternity Pro — substitute design file",
        "role": "owner",
        "lastModified": "2026-04-21T00:00:00Z",
        "editorType": "figma",
        "thumbnailUrl": None,
        "version": "1",
        "document": {
            "id": "0:0",
            "name": "Document",
            "type": "DOCUMENT",
            "children": pages,
        },
        "components": components,
        "componentSets": {},
        "schemaVersion": 0,
        "styles": styles,
        "mainFileKey": "aceternity-pro-synth-2026-04-21",
        "linkAccess": "view",
    }


# ---------- main -------------------------------------------------------

def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    # sanity
    assert json.loads(path.read_text())


def main() -> None:
    cm = build_clawmachine_document()
    write_json(OUT / "clawmachine-figma-schema.json", cm)
    print(f"clawmachine pages: {len(cm['document']['children'])}")

    uui = build_untitled_document()
    write_json(OUT / "untitled-ui-pro-figma-schema.json", uui)
    print(f"untitled pages: {len(uui['document']['children'])}")

    ace = build_aceternity_document()
    write_json(OUT / "aceternity-pro-figma-schema.json", ace)
    print(f"aceternity pages: {len(ace['document']['children'])}")

    total_demos = sum(len(d) for _, d in ACE_CATEGORIES)
    print(f"aceternity demos referenced: {total_demos}")


if __name__ == "__main__":
    main()
