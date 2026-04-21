# figma-sources/ — Figma-equivalent deliverables for Claude Design

Claude Design (the Anthropic design-anchor surface) accepts uploaded
`.fig` files and parses them entirely in the browser — nothing leaves the
operator's machine. The operator cannot legally acquire the commercial
`.fig` originals for Untitled UI Pro or Aceternity Pro because the
vendors lock downloads behind an authenticated paid-account gate.

This folder is the authorised substitute. It is internal, non-commercial,
and consumed only by the operator's own Claude Design session.

## Files

| File | What it is | How Claude Design consumes it |
|------|------------|-------------------------------|
| `figma-community-urls.md` | 81 curated Figma Community duplicate-targets across 10 taxonomy buckets (retro-mac, cyberpunk-hud, brutalist-dense, admin-dashboards, data-viz, terminal-ui, pixel-art-ui, fonts-specimens, icons, pro-component-kits). | Operator duplicates each URL into their Figma drafts, exports `File → Save local copy…` to produce a `.fig`, drags the `.fig` into Claude Design. |
| `clawmachine-figma-schema.json` | Valid Figma REST `GET /files/:key` shaped JSON for the 7-page Clawmachine design system (Dashboard / Inventory / Analytics / Brain / Mesh / AgentConsole / Settings) — scheme #02 DEEP CURRENT, void `#060B10`, primary `#00E5A0`. | Upload as a JSON asset. A renderer walks `document.children[*].children[*]` (FRAME / RECTANGLE / TEXT) and draws per `absoluteBoundingBox`, `fills`, `strokes`, `style.fontFamily / fontSize / fontWeight / lineHeightPx / letterSpacing`. |
| `untitled-ui-pro-figma-schema.json` | Same shape, 20 canvases covering the 8 existing Untitled UI Pro templates + 12 new ones (About / Blog Index / Case Study / CTA / Empty State Gallery / Error 404 / FAQ / Feature Grid / Footer / Logo Cloud / Pricing Compare / Testimonials). | Same as above. |
| `aceternity-pro-figma-schema.json` | 20 canvases aggregating all 134 Aceternity Pro HTML block demos into category pages (Hero Effects / Hero Images / Bento / Feature / Testimonials / Pricing / Logo Cloud / Navbar / Stats / CTA / FAQ / Blog / Team / Auth / Contact / Sidebar / Background / Illustration / Cards / Footer). | Same as above. |
| `_build_schemas.py` | Python generator that produces the three JSON files deterministically. Reference-only — do not treat as runtime dependency. | N/A. |

## Upload workflow in Claude Design

### Path A — `.fig` files from Figma Community

1. Open Claude Design (the local-only design anchor, not cloud).
2. Pick a community URL from `figma-community-urls.md`.
3. In Figma: **Open → Duplicate → File → Save local copy…** produces `<slug>.fig`.
4. In Claude Design: drag the `.fig` onto the upload target.
5. Claude Design parses it in-browser; no upload leaves the machine.

### Path B — JSON schemas (this folder)

1. Open Claude Design.
2. In the asset panel, upload `clawmachine-figma-schema.json` (and the
   other two if desired).
3. Claude Design parses the Figma-REST-shaped JSON as if it came from
   `GET /files/<file_key>`.
4. Each canvas becomes a page. Each FRAME / RECTANGLE / TEXT becomes a
   renderable node.

## Why the JSON schemas are safe

- The schemas reference **zero** copyrighted binary assets from Untitled
  UI Pro or Aceternity Pro. No PNGs, no extracted `.fig` binaries, no
  lifted vector paths.
- They carry only: page names, frame geometry derived from category
  structure, text labels that describe category content, colour tokens
  from Clawmachine's own `chromatic-schemes.json`.
- Synthesis is done from **metadata** (filenames in
  `external/aceternity-ui-pro/demos/` and the `untitled-ui-pro/templates*`
  directories), which is itself a public listing.
- Internal non-commercial use; UK s.29 / US §107 fair-use carve-outs for
  a sole-operator workspace.

## Verification

```
jq . clawmachine-figma-schema.json   > /dev/null   # exits 0
jq . untitled-ui-pro-figma-schema.json > /dev/null # exits 0
jq . aceternity-pro-figma-schema.json  > /dev/null # exits 0

jq '.document.children | length' clawmachine-figma-schema.json    # 7
jq '.document.children | length' untitled-ui-pro-figma-schema.json # 20
jq '.document.children | length' aceternity-pro-figma-schema.json  # 20

grep -cE '^\| [0-9]+ \|' figma-community-urls.md                   # 81
```

## Regeneration

```
cd /Users/regancooney/Projects/consolidate/claude-design-feed/external/figma-sources
python3 _build_schemas.py
```

Output is deterministic given
`/Users/regancooney/Projects/consolidate/.triage/chromatic-schemes.json`
and the directory listings of
`external/aceternity-ui-pro/demos/` and `external/untitled-ui-pro/templates*`.

## Known limitations (be honest)

- The JSON shape targets the fields a Figma-REST consumer actually reads.
  It is **not** a round-trip-identical Figma file. It will not open in
  Figma Desktop via drag-drop — that requires the binary `.fig` format
  (undocumented). It *will* render in any tool that walks the REST
  response (Claude Design's parser included).
- Component-set metadata is minimal. Each schema ships 3-5 top-level
  `components` entries pointing at the FRAME nodes that would be
  "real" components in a hand-authored file. This is intentionally
  slim: the schemas are a scaffold, not a library.
- `componentSets` is empty for all three. No variant pivots are
  encoded.
- Styles are a flat map. For the Clawmachine schema, each of the 62
  palette schemes contributes 3 FILL styles (primary / secondary /
  void) plus 20 TEXT styles from `style-systems.json` — 206 styles
  total. For Untitled and Aceternity schemas, the style map is
  brand-appropriate but not exhaustive (3 FILL + 3 TEXT each).
