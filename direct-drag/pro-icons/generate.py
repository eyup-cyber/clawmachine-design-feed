#!/usr/bin/env python3
"""
Pro-icon synth for Clawmachine — generates 60 semantic icons × 4 styles = 240 SVGs.
Styles: stroke / solid / duotone / duocolor.
Grammar: 24×24 viewBox, 1.67 stroke-width (Untitled UI Pro house value), rounded caps/joins.
Authored 2026-04-21 by Opus 4.7, no external lib, no agent.

Run: python3 generate.py
Output: ./svg/{style}/{name}.svg for every icon.
"""

import os
from pathlib import Path

OUT = Path(__file__).parent / "svg"
STYLES = ["stroke", "solid", "duotone", "duocolor"]

# color tokens — Clawmachine scheme #02 DEEP CURRENT
PRIMARY = "#00E5A0"
SECONDARY = "#0080FF"
DUOTONE_OP = "0.28"  # primary stroke + 28%-opacity fill
DUO_LAYER_BASE = "#00E5A0"
DUO_LAYER_ACCENT = "#FFB830"

# 60 semantic primitives — each is a list of SVG path ops given in "stroke" base.
# For solid we close + fill. For duotone we draw primary plus opacity-base fill.
# For duocolor we emit base+accent overlay.
#
# Each primitive is (name, path_ops_as_tuples_of_d_strings).
# Where two d-strings exist, the second is the "accent layer" used for duotone/duocolor.

ICONS = {
    # ---------- NAVIGATION / ARROWS ----------
    "arrow-up":     ("M12 4v16M6 10l6-6 6 6", None),
    "arrow-down":   ("M12 4v16M6 14l6 6 6-6", None),
    "arrow-left":   ("M4 12h16M10 6l-6 6 6 6", None),
    "arrow-right":  ("M4 12h16M14 6l6 6-6 6", None),
    "chevron-up":   ("M6 15l6-6 6 6", None),
    "chevron-down": ("M6 9l6 6 6-6", None),
    "chevron-left": ("M15 6l-6 6 6 6", None),
    "chevron-right":("M9 6l6 6-6 6", None),
    "external":     ("M14 4h6v6M20 4L10 14M14 10v8H6V6h8", None),
    "corner-up":    ("M4 20l8-8h8", "M12 12l4-4-4-4"),

    # ---------- SYSTEM / HOME ----------
    "home":         ("M3 11L12 3l9 8v10a1 1 0 0 1-1 1h-5v-7H9v7H4a1 1 0 0 1-1-1z", None),
    "search":       ("M11 19a8 8 0 1 1 0-16 8 8 0 0 1 0 16zM21 21l-4.5-4.5", None),
    "settings":     ("M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z", "M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82A1.65 1.65 0 0 0 3.09 15H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"),
    "grid":         ("M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z", None),
    "list":         ("M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01", None),
    "menu":         ("M3 6h18M3 12h18M3 18h18", None),
    "close":        ("M18 6L6 18M6 6l12 12", None),
    "plus":         ("M12 4v16M4 12h16", None),
    "minus":        ("M4 12h16", None),
    "check":        ("M5 13l4 4 10-10", None),
    "refresh":      ("M23 4v6h-6M1 20v-6h6", "M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"),

    # ---------- FILE / DATA ----------
    "file":         ("M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z", "M14 2v6h6"),
    "folder":       ("M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z", None),
    "download":     ("M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3", None),
    "upload":       ("M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12", None),
    "database":     ("M3 6a9 3 0 0 0 18 0 9 3 0 0 0-18 0zM3 6v6a9 3 0 0 0 18 0V6M3 12v6a9 3 0 0 0 18 0v-6", None),
    "server":       ("M4 4h16v6H4zM4 14h16v6H4z", "M6 7h.01M6 17h.01"),
    "terminal":     ("M4 4h16v16H4z", "M7 10l3 3-3 3M13 16h4"),
    "code":         ("M16 4l4 8-4 8M8 4l-4 8 4 8", None),

    # ---------- COMMERCE / MONEY ----------
    "tag":          ("M20 13l-8 8a2 2 0 0 1-3 0l-6-6a2 2 0 0 1 0-3l8-8h6a2 2 0 0 1 2 2z", "M8 8h.01"),
    "cart":         ("M3 3h2l3 12a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2l1-7H6M10 21a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM18 21a1 1 0 1 0 0-2 1 1 0 0 0 0 2z", None),
    "wallet":       ("M20 6H5a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4h-4a2 2 0 0 1 0-4h4V7a1 1 0 0 0-1-1z", "M17 14h.01"),
    "coins":        ("M8 14a6 6 0 1 0 0-12 6 6 0 0 0 0 12z", "M16 22a6 6 0 1 0 0-12 6 6 0 0 0 0 12z"),
    "credit-card":  ("M3 6h18v12H3z", "M3 10h18"),
    "receipt":      ("M5 3h14l-2 18-5-3-5 3z", "M8 7h8M8 11h8M8 15h6"),
    "chart-up":     ("M3 3v18h18M7 14l4-4 4 4 6-6", None),
    "chart-bar":    ("M3 3v18h18M7 17V11M11 17V7M15 17V13M19 17V9", None),
    "pie":          ("M21 12a9 9 0 1 1-9-9v9z", "M21 12h-9v-9"),
    "trending":     ("M23 6l-9.5 9.5-5-5L1 18M17 6h6v6", None),

    # ---------- COMMUNICATION ----------
    "mail":         ("M4 4h16v16H4z", "M4 4l8 8 8-8"),
    "message":      ("M21 12a8 8 0 1 1-16 0 8 8 0 0 1 16 0z", "M8 21l1.5-4H12a8 8 0 0 0 0-16 8 8 0 0 0-3.5 15"),
    "phone":        ("M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z", None),
    "bell":         ("M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M13.73 21a2 2 0 0 1-3.46 0", None),
    "send":         ("M22 2L11 13M22 2l-7 20-4-9-9-4z", None),
    "at":           ("M16 12a4 4 0 1 1-8 0 4 4 0 0 1 8 0zM16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-4 7.75", None),

    # ---------- USER / IDENTITY ----------
    "user":         ("M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z", None),
    "users":        ("M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75", None),
    "lock":         ("M5 11h14v10H5z", "M7 11V7a5 5 0 0 1 10 0v4"),
    "unlock":       ("M5 11h14v10H5z", "M7 11V7a5 5 0 0 1 9.9-1"),
    "shield":       ("M12 2l9 4v6c0 5-4 9-9 10-5-1-9-5-9-10V6z", None),
    "key":          ("M15 7a5 5 0 1 0-4.9 6H12v2h2v2h2v-2h2v-2h-2v-2h-.1A5 5 0 0 0 15 7z", None),

    # ---------- STATE / STATUS ----------
    "info":         ("M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 16v-4M12 8h.01", None),
    "alert":        ("M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0zM12 9v4M12 17h.01", None),
    "check-circle": ("M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z", "M8 12l3 3 5-5"),
    "x-circle":     ("M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z", "M15 9l-6 6M9 9l6 6"),
    "help":         ("M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3M12 17h.01", None),

    # ---------- MEDIA / TOOLS ----------
    "image":        ("M4 4h16v16H4z", "M10 10a2 2 0 1 1-4 0 2 2 0 0 1 4 0zM20 15l-5-5L4 21"),
    "camera":       ("M20 7h-3l-2-2H9l-2 2H4v13h16z", "M12 17a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"),
    "star":         ("M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z", None),
    "heart":        ("M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z", None),
    "bookmark":     ("M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z", None),
    "flag":         ("M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1zM4 22V15", None),
    "clock":        ("M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 7v5l3 3", None),
    "calendar":     ("M3 4h18v18H3z", "M3 10h18M8 2v4M16 2v4"),
    "eye":          ("M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z", "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"),
    "eye-off":      ("M17.94 17.94A10.94 10.94 0 0 1 12 20c-7 0-11-8-11-8a18.64 18.64 0 0 1 5.06-5.94M9.9 5a10.94 10.94 0 0 1 2.1-.2c7 0 11 8 11 8a18.64 18.64 0 0 1-2.16 3.19M14.12 14.12a3 3 0 1 1-4.24-4.24", "M1 1l22 22"),

    # ---------- DEVICES / HARDWARE ----------
    "phone-mobile": ("M7 2h10v20H7z", "M11 18h2"),
    "laptop":       ("M3 5h18v12H3zM1 21h22", None),
    "tv":           ("M3 5h18v14H3z", "M8 21h8"),
    "printer":      ("M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2M6 14h12v8H6z", None),
    "speaker":      ("M6 4h12v16H6z", "M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"),
    "watch":        ("M12 19a7 7 0 1 0 0-14 7 7 0 0 0 0 14z", "M8 2h8l1 3H7zM7 22h10l-1-3H8zM12 9v3l2 2"),
}

def wrap(paths_str, style, duo_accent_d=None):
    """Render a single SVG file body for the given icon + style."""
    common_attrs = 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"'
    if style == "stroke":
        return (f'<svg {common_attrs} fill="none" stroke="currentColor" stroke-width="1.67" '
                f'stroke-linecap="round" stroke-linejoin="round">'
                f'<path d="{paths_str}"/>'
                + (f'<path d="{duo_accent_d}"/>' if duo_accent_d else '')
                + '</svg>')
    if style == "solid":
        return (f'<svg {common_attrs} fill="currentColor" stroke="none">'
                f'<path fill-rule="evenodd" clip-rule="evenodd" d="{paths_str}"/>'
                + (f'<path fill-rule="evenodd" clip-rule="evenodd" d="{duo_accent_d}"/>' if duo_accent_d else '')
                + '</svg>')
    if style == "duotone":
        # stroke primary + duo-accent-layer at low opacity
        return (f'<svg {common_attrs}>'
                f'<path d="{paths_str}" stroke="currentColor" stroke-width="1.67" fill="none" '
                f'stroke-linecap="round" stroke-linejoin="round"/>'
                + (f'<path d="{duo_accent_d}" stroke="currentColor" stroke-width="1.67" fill="currentColor" '
                   f'fill-opacity="{DUOTONE_OP}" stroke-linecap="round" stroke-linejoin="round"/>' if duo_accent_d else '')
                + '</svg>')
    if style == "duocolor":
        # base stroke + accent layer filled w/ secondary color
        return (f'<svg {common_attrs}>'
                f'<path d="{paths_str}" stroke="{DUO_LAYER_BASE}" stroke-width="1.67" fill="none" '
                f'stroke-linecap="round" stroke-linejoin="round"/>'
                + (f'<path d="{duo_accent_d}" stroke="{DUO_LAYER_ACCENT}" stroke-width="1.67" fill="{DUO_LAYER_ACCENT}" '
                   f'fill-opacity="0.25" stroke-linecap="round" stroke-linejoin="round"/>' if duo_accent_d else '')
                + '</svg>')
    raise ValueError(style)

def main():
    for style in STYLES:
        (OUT / style).mkdir(parents=True, exist_ok=True)
    written = 0
    for name, (d, d_accent) in ICONS.items():
        for style in STYLES:
            content = wrap(d, style, d_accent)
            (OUT / style / f"{name}.svg").write_text(content)
            written += 1
    print(f"{written} SVG files written to {OUT}")

if __name__ == "__main__":
    main()
