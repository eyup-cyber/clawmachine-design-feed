#!/usr/bin/env python3
"""Build a self-contained gallery.html (no external refs) from manifest.json.

Categories are derived from filename keyword matching against Untitled UI
Pro's public taxonomy. An icon that matches no category falls into 'other'.
"""
from __future__ import annotations
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "manifest.json"
OUT = HERE / "gallery.html"

CATEGORY_PATTERNS = [
    ("arrows",        [r"\barrow", r"\bchevron", r"\bcorner", r"\bmove", r"\btrend", r"\bcaret", r"keyboard[_-]arrow"]),
    ("alerts",        [r"\balert", r"\bbell", r"\bsiren", r"shield[_-]alert", r"octagon[_-]alert", r"\bwarning", r"\binfo"]),
    ("charts",        [r"\bchart", r"bar[_-]chart", r"line[_-]chart", r"pie[_-]chart", r"\bactivity", r"\btrending", r"analytics", r"monitoring"]),
    ("communication", [r"\bmessage", r"\bchat", r"\bmail", r"envelope", r"\bphone", r"\bsend", r"\breply", r"\bcall"]),
    ("cursors",       [r"mouse[_-]pointer", r"\bcursor", r"\bhand", r"\bpointer", r"pan[_-]tool"]),
    ("development",   [r"\bcode", r"\bterminal", r"\bbug", r"command", r"\bgit-", r"github", r"bug[_-]report"]),
    ("editor",        [r"\btype\b", r"\bbold\b", r"\bitalic", r"underline", r"align[_-]", r"indent", r"\blist\b", r"\btext\b", r"format[_-]", r"\bedit\b"]),
    ("files",         [r"\bfile", r"\bfolder", r"paperclip", r"archive", r"\bdocument", r"description"]),
    ("finance",       [r"dollar", r"credit[_-]card", r"receipt", r"banknote", r"wallet", r"\bcoins", r"\bmoney", r"payments?", r"account[_-]balance"]),
    ("general",       [r"\bcheck", r"\bclose", r"\bplus", r"\bminus", r"settings", r"\bmore-", r"\bfilter", r"\bsearch", r"\bgear", r"\bx-", r"^x\."]),
    ("home",          [r"\bhome", r"\bhouse", r"\bdoor"]),
    ("images",        [r"\bimage", r"\bcamera", r"\bvideo", r"\bfilm", r"gallery", r"\bphoto"]),
    ("layout",        [r"layout[_-]", r"\bgrid", r"columns?", r"\brows?\b", r"sidebar", r"panel", r"view[_-]", r"dashboard"]),
    ("maps",          [r"\bmap", r"navigation", r"compass", r"\bpin\b", r"\bglobe", r"locate", r"\bplace\b", r"location"]),
    ("media",         [r"\bplay", r"\bpause", r"\bstop\b", r"\bskip-", r"rewind", r"volume", r"\bmusic", r"headphones"]),
    ("security",      [r"\block", r"unlock", r"shield", r"\bkey\b", r"\beye", r"fingerprint", r"security"]),
    ("shapes",        [r"\bcircle", r"\bsquare", r"triangle", r"hexagon", r"pentagon", r"\bstar\b"]),
    ("shopping",      [r"shopping[_-]", r"\bcart", r"\bbag\b", r"\bgift", r"\btag\b", r"package", r"basket"]),
    ("social",        [r"\bshare\b", r"\bheart", r"thumbs?[_-]", r"\bsmile", r"favorite", r"\bthumb[_-]"]),
    ("time",          [r"\bclock", r"\btimer", r"calendar", r"\balarm", r"hourglass", r"schedule"]),
    ("users",         [r"\buser", r"\bpeople", r"contact", r"\bperson"]),
    ("weather",       [r"\bsun\b", r"\bmoon", r"\bcloud", r"\brain\b", r"\bsnow", r"\bwind\b", r"lightning", r"umbrella", r"thermometer", r"thermostat", r"\bwb[_-]"]),
]
# Pre-compile
CATEGORY_REGEX = [(name, [re.compile(p) for p in pats]) for name, pats in CATEGORY_PATTERNS]

def categorize(stem: str) -> list[str]:
    """Return list of matched categories (icons can belong to multiple)."""
    hits = []
    for name, regs in CATEGORY_REGEX:
        if any(r.search(stem) for r in regs):
            hits.append(name)
    return hits or ["other"]

def strip_prefix(stem: str) -> str:
    for p in ("ph-", "phb-", "lu-", "feather-", "iconoir-", "ms-"):
        if stem.startswith(p):
            return stem[len(p):]
    return stem

def main():
    manifest = json.loads(MANIFEST.read_text())

    # Build per-style list of {name, cats}
    entries = {}
    cat_counts = {"all": 0}
    for cat, _ in CATEGORY_PATTERNS:
        cat_counts[cat] = 0
    cat_counts["other"] = 0

    for style, names in manifest.items():
        style_entries = []
        for n in names:
            stem = n.rsplit(".", 1)[0]
            cats = categorize(strip_prefix(stem))
            style_entries.append({"n": n, "c": cats})
            cat_counts["all"] += 1
            for c in cats:
                cat_counts[c] = cat_counts.get(c, 0) + 1
        entries[style] = style_entries

    manifest_json = json.dumps(entries, separators=(",", ":"))
    categories = ["all"] + [c for c, _ in CATEGORY_PATTERNS] + ["other"]
    totals = {s: len(v) for s, v in manifest.items()}

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Untitled UI Pro Icons 4K Synth Gallery</title>
<style>
  :root{{
    --bg-canvas: #0b0d0c;
    --bg-surface: #0f1311;
    --border-subtle: #1f2422;
    --border-hover: #2d8460;
    --fg-primary: #e8ede9;
    --fg-dim: #838a87;
    --brand: #2d8460;
    --accent: #7c3aed;
    --icon-primary: #e8ede9;
    --icon-secondary: #7c3aed;
  }}
  *, *::before, *::after {{ box-sizing: border-box; }}
  html, body {{ height: 100%; }}
  body{{
    margin:0;
    background: var(--bg-canvas);
    color: var(--fg-primary);
    font-family: "IBM Plex Sans", "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
    line-height: 1.45;
    -webkit-font-smoothing: antialiased;
  }}
  header{{
    position: sticky; top: 0; z-index: 10;
    background: var(--bg-canvas);
    border-bottom: 1px solid var(--border-subtle);
    padding: .9rem 1.1rem;
    display: flex; flex-direction: column; gap: .7rem;
  }}
  header .row {{ display: flex; gap: .75rem; align-items: center; flex-wrap: wrap; }}
  header h1{{ font-size: .95rem; font-weight: 600; margin: 0; letter-spacing: -0.01em; }}
  header input{{
    flex: 1 1 240px; min-width: 200px; max-width: 420px;
    padding: .5rem .8rem;
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 4px;
    color: inherit;
    font: inherit; font-size: .85rem;
    font-family: "JetBrains Mono", ui-monospace, monospace;
  }}
  header input:focus {{ outline: 1px solid var(--brand); outline-offset: 0; border-color: var(--brand); }}
  .tabs, .cat-tabs {{ display: flex; gap: .25rem; flex-wrap: wrap; }}
  .tabs button, .cat-tabs button {{
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    color: inherit;
    padding: .35rem .65rem;
    border-radius: 4px;
    font: inherit; font-size: .78rem;
    font-family: "JetBrains Mono", ui-monospace, monospace;
    text-transform: lowercase;
    cursor: pointer;
    transition: background 120ms cubic-bezier(0.34,1.56,0.64,1), border-color 120ms cubic-bezier(0.34,1.56,0.64,1);
  }}
  .tabs button:hover, .cat-tabs button:hover {{ border-color: var(--brand); }}
  .tabs button[aria-pressed="true"], .cat-tabs button[aria-pressed="true"] {{
    background: var(--brand); border-color: transparent; color: #000;
  }}
  .count {{ color: var(--fg-dim); font-size: .78rem; margin-left: auto; font-family: "JetBrains Mono", ui-monospace, monospace; font-variant-numeric: tabular-nums; }}
  main {{ padding: 1rem 1.1rem 4rem; }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(20, minmax(0, 1fr));
    gap: 2px;
  }}
  @media (max-width: 1400px) {{ .grid {{ grid-template-columns: repeat(15, minmax(0, 1fr)); }} }}
  @media (max-width: 1000px) {{ .grid {{ grid-template-columns: repeat(10, minmax(0, 1fr)); }} }}
  @media (max-width: 600px)  {{ .grid {{ grid-template-columns: repeat(6,  minmax(0, 1fr)); }} }}
  .cell {{
    aspect-ratio: 1 / 1;
    border: 1px solid var(--border-subtle);
    background: var(--bg-surface);
    display: flex; align-items: center; justify-content: center;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
  }}
  .cell:hover {{ border-color: var(--border-hover); z-index: 2; }}
  .cell img {{
    width: 24px; height: 24px;
    color: var(--icon-primary);
    display: block;
  }}
  .cell .name {{
    position: absolute; inset: auto 0 100% 0;
    background: #000; color: #fff;
    font-size: 10px; padding: 3px 5px;
    display: none;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    pointer-events: none;
    border-radius: 3px;
    font-family: ui-monospace, monospace;
  }}
  .cell:hover .name {{ display: block; }}
  .empty {{ padding: 3rem 1rem; text-align: center; color: var(--fg-dim); }}
  footer {{
    padding: 2rem 1.25rem;
    border-top: 1px solid var(--border-subtle);
    font-size: .78rem; color: var(--fg-dim);
  }}
  footer code {{ background: var(--bg-surface); padding: 1px 4px; border-radius: 3px; }}
  /* Duocolor cells paint secondary via CSS var the SVG already uses */
  .grid.duocolor .cell {{
    --icon-primary: var(--brand);
  }}
  .grid.solid .cell img,
  .grid.stroke .cell img,
  .grid.duotone .cell img {{ color: var(--brand); }}
</style>
</head>
<body>

<header>
  <div class="row">
    <h1>Untitled UI Pro Icons 4K Synth</h1>
    <div class="tabs" id="style-tabs"></div>
    <input id="search" type="search" placeholder="Filter by name (e.g. arrow, heart, shield)" autocomplete="off"/>
    <span class="count" id="count">loading…</span>
  </div>
  <div class="cat-tabs" id="cat-tabs"></div>
</header>

<main>
  <div class="grid stroke" id="grid"></div>
  <div class="empty" id="empty" style="display:none;">No icons match your filter.</div>
</main>

<footer>
  Hover an icon to see its filename. Filename prefix → source:
  (none) = Lucide, <code>ph-</code> = Phosphor, <code>phb-</code> = Phosphor bold synth,
  <code>lu-</code> = Lucide synth (duotone/duocolor), <code>feather-</code> = Feather,
  <code>iconoir-</code> = Iconoir solid, <code>ms-</code> = Material Symbols.
  Licenses per style in <code>{{style}}/LICENSE_NOTE.md</code>. Categories in <code>INDEX.md</code>.
  This gallery is self-contained — no external stylesheets or fetches. Open directly (<code>file://</code> OK) or via static server.
</footer>

<script id="manifest-data" type="application/json">{manifest_json}</script>
<script>
  const manifest = JSON.parse(document.getElementById('manifest-data').textContent);
  const styles = {json.dumps(list(manifest.keys()))};
  const categories = {json.dumps(categories)};
  const totals = {json.dumps(totals)};

  let currentStyle = 'stroke';
  let currentCat = 'all';
  let filter = '';

  const grid = document.getElementById('grid');
  const count = document.getElementById('count');
  const emptyEl = document.getElementById('empty');
  const styleTabs = document.getElementById('style-tabs');
  const catTabs = document.getElementById('cat-tabs');
  const search = document.getElementById('search');

  // Build style tabs
  for (const s of styles) {{
    const b = document.createElement('button');
    b.dataset.style = s;
    b.textContent = s + ' (' + totals[s].toLocaleString() + ')';
    b.setAttribute('aria-pressed', s === currentStyle ? 'true' : 'false');
    styleTabs.appendChild(b);
  }}

  // Build category tabs
  for (const c of categories) {{
    const b = document.createElement('button');
    b.dataset.cat = c;
    b.textContent = c;
    b.setAttribute('aria-pressed', c === currentCat ? 'true' : 'false');
    catTabs.appendChild(b);
  }}

  function entriesForStyle(s) {{
    return manifest[s] || [];
  }}

  function render() {{
    const all = entriesForStyle(currentStyle);
    const f = filter;
    const cat = currentCat;
    const filtered = [];
    for (const e of all) {{
      if (cat !== 'all' && !e.c.includes(cat)) continue;
      if (f && !e.n.toLowerCase().includes(f)) continue;
      filtered.push(e);
    }}
    count.textContent = filtered.length.toLocaleString() + ' / ' + all.length.toLocaleString() + ' icons';
    grid.className = 'grid ' + currentStyle;
    grid.innerHTML = '';
    if (!filtered.length) {{ emptyEl.style.display = ''; return; }}
    emptyEl.style.display = 'none';
    const frag = document.createDocumentFragment();
    for (const e of filtered) {{
      const cell = document.createElement('div');
      cell.className = 'cell';
      const img = document.createElement('img');
      img.loading = 'lazy';
      img.decoding = 'async';
      img.src = currentStyle + '/' + e.n;
      img.alt = e.n;
      const nm = document.createElement('span');
      nm.className = 'name';
      nm.textContent = e.n;
      cell.appendChild(img);
      cell.appendChild(nm);
      frag.appendChild(cell);
    }}
    grid.appendChild(frag);
  }}

  styleTabs.addEventListener('click', (ev) => {{
    if (ev.target.tagName !== 'BUTTON') return;
    for (const b of styleTabs.querySelectorAll('button')) b.setAttribute('aria-pressed', 'false');
    ev.target.setAttribute('aria-pressed', 'true');
    currentStyle = ev.target.dataset.style;
    render();
  }});

  catTabs.addEventListener('click', (ev) => {{
    if (ev.target.tagName !== 'BUTTON') return;
    for (const b of catTabs.querySelectorAll('button')) b.setAttribute('aria-pressed', 'false');
    ev.target.setAttribute('aria-pressed', 'true');
    currentCat = ev.target.dataset.cat;
    render();
  }});

  let searchTimer = null;
  search.addEventListener('input', () => {{
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {{
      filter = search.value.trim().toLowerCase();
      render();
    }}, 120);
  }});

  render();
</script>

</body>
</html>
"""

    OUT.write_text(html)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    # Also emit per-style category stats
    stats = {s: {"total": len(v), "categories": {}} for s, v in entries.items()}
    for s, es in entries.items():
        for e in es:
            for c in e["c"]:
                stats[s]["categories"][c] = stats[s]["categories"].get(c, 0) + 1
    (HERE / "category_stats.json").write_text(json.dumps(stats, indent=2, sort_keys=True))
    print(f"wrote category_stats.json")

if __name__ == "__main__":
    main()
