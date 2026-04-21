# Icons 4K Synth — Untitled UI Pro Tier Equivalent

4-style icon library (stroke / solid / duotone / duocolor) synthesised from
MIT/OFL/ISC upstream sources to cover the Untitled UI Pro tier's 4,600-icon
catalogue. Internal non-commercial fair-use research reference for Clawmachine.

## Counts

| Style     | Count | Primary sources                                                    |
|-----------|-------|--------------------------------------------------------------------|
| stroke    | 3,494 | Lucide (1,695) + Phosphor regular (1,512) + Feather (287)          |
| solid     | 5,658 | Material Symbols rounded-fill (3,858) + Phosphor fill (1,512) + Iconoir solid (288) |
| duotone   | 3,207 | Phosphor duotone native (1,512) + Lucide-synth (1,695)             |
| duocolor  | 3,207 | Phosphor duotone two-tone transform (1,512) + Lucide-synth (1,695) |
| **total** |**15,566**|                                                                  |

## Filename prefix → source map

| Prefix     | Upstream                         | License |
|------------|----------------------------------|---------|
| (none)     | Lucide                           | ISC     |
| `ph-`      | Phosphor (regular / fill / duotone) | MIT  |
| `phb-`     | Phosphor (bold + fill pair synth)| MIT     |
| `lu-`      | Lucide synth (duotone/duocolor)  | ISC     |
| `feather-` | Feather Icons                    | MIT     |
| `iconoir-` | Iconoir solid                    | MIT     |
| `ms-`      | Material Symbols rounded-fill    | Apache-2.0 |

## Untitled UI Pro semantic category coverage

Each Pro category below maps to filename patterns you can grep. The file
`CATEGORIES.json` at the end of this document (parseable) holds the same
data for programmatic use.

### arrows
`arrow-*`, `chevron-*`, `corner-*`, `move-*`, `trend-*`, `ph-arrow-*`, `ph-caret-*`, `ms-arrow_*`, `ms-keyboard_arrow_*`.

### alerts
`alert-*`, `bell*`, `siren*`, `shield-alert*`, `octagon-alert*`, `info*`, `ph-warning*`, `ph-bell*`, `ms-notification*`, `ms-warning*`.

### charts
`chart-*`, `bar-chart*`, `line-chart*`, `pie-chart*`, `activity*`, `trending-*`, `ph-chart-*`, `ms-analytics*`, `ms-bar_chart*`, `ms-monitoring*`.

### communication
`message-*`, `mail*`, `phone*`, `send*`, `reply*`, `ph-chat-*`, `ph-envelope*`, `ph-phone*`, `ms-chat*`, `ms-mail*`, `ms-call*`.

### cursors
`mouse-pointer*`, `cursor*`, `hand*`, `pointer*`, `ph-cursor*`, `ph-hand*`, `ms-mouse*`, `ms-pan_tool*`.

### development
`code*`, `terminal*`, `bug*`, `command*`, `git-*`, `github*`, `ph-code*`, `ph-terminal*`, `ms-code*`, `ms-bug_report*`.

### editor
`type*`, `bold*`, `italic*`, `underline*`, `align-*`, `indent*`, `list*`, `ph-text*`, `ms-format_*`, `ms-edit*`.

### files
`file-*`, `folder*`, `paperclip*`, `archive*`, `ph-file-*`, `ph-folder*`, `ms-folder*`, `ms-file_*`, `ms-description*`.

### finance
`dollar-sign*`, `credit-card*`, `receipt*`, `banknote*`, `wallet*`, `coins*`, `ph-credit-card*`, `ph-wallet*`, `ph-money*`, `ms-payments*`, `ms-credit_card*`, `ms-account_balance*`.

### general
`check*`, `x*`, `plus*`, `minus*`, `settings*`, `more-*`, `filter*`, `search*`, `ph-check*`, `ph-x*`, `ph-plus*`, `ph-gear*`, `ms-check*`, `ms-close*`, `ms-search*`.

### home
`home*`, `house*`, `door*`, `ph-house*`, `ph-door*`, `ms-home*`, `ms-house*`.

### images
`image*`, `camera*`, `video*`, `film*`, `gallery*`, `ph-image*`, `ph-camera*`, `ms-image*`, `ms-photo*`, `ms-camera*`.

### layout
`layout-*`, `grid-*`, `columns*`, `rows*`, `sidebar*`, `panel*`, `ph-grid*`, `ph-columns*`, `ms-grid*`, `ms-view_*`, `ms-dashboard*`.

### maps
`map*`, `navigation*`, `compass*`, `pin*`, `globe*`, `locate*`, `ph-map-*`, `ph-compass*`, `ph-pin*`, `ms-map*`, `ms-place*`, `ms-location_*`.

### media
`play*`, `pause*`, `stop*`, `skip-*`, `rewind*`, `volume*`, `music*`, `headphones*`, `ph-play*`, `ph-pause*`, `ph-music*`, `ms-play_*`, `ms-pause*`, `ms-music_*`.

### security
`lock*`, `unlock*`, `shield*`, `key*`, `eye*`, `eye-off*`, `fingerprint*`, `ph-lock*`, `ph-shield*`, `ph-key*`, `ms-lock*`, `ms-shield*`, `ms-security*`.

### shapes
`circle*`, `square*`, `triangle*`, `hexagon*`, `pentagon*`, `star*`, `ph-circle*`, `ph-square*`, `ph-star*`, `ms-square*`, `ms-circle*`, `ms-star*`.

### shopping
`shopping-*`, `cart*`, `bag*`, `gift*`, `tag*`, `package*`, `ph-shopping-*`, `ph-basket*`, `ph-gift*`, `ms-shopping_*`, `ms-add_shopping_*`, `ms-gift*`.

### social
`share*`, `heart*`, `thumbs-*`, `smile*`, `ph-heart*`, `ph-thumbs-*`, `ph-share*`, `ms-favorite*`, `ms-thumb_*`, `ms-share*`.

### time
`clock*`, `timer*`, `calendar*`, `alarm*`, `hourglass*`, `ph-clock*`, `ph-calendar*`, `ph-timer*`, `ms-schedule*`, `ms-calendar_*`, `ms-timer*`.

### users
`user*`, `users*`, `user-plus*`, `user-check*`, `contact*`, `ph-user*`, `ph-users*`, `ms-person*`, `ms-people*`, `ms-account_*`.

### weather
`sun*`, `moon*`, `cloud*`, `rain*`, `snow*`, `wind*`, `lightning*`, `umbrella*`, `ph-sun*`, `ph-cloud*`, `ph-thermometer*`, `ms-wb_*`, `ms-cloud*`, `ms-thermostat*`.

## Usage in Untitled UI Pro HTML

```html
<!-- stroke -->
<img src="../icons-4k-synth/stroke/arrow-right.svg" width="20" height="20" style="color:var(--uip-fg-primary)" />

<!-- solid: renders as filled glyph at currentColor -->
<img src="../icons-4k-synth/solid/ph-user.svg" width="20" height="20" style="color:var(--uip-brand-600)" />

<!-- duotone: renders as two-tone at currentColor base, lighter secondary at 0.2 opacity -->
<img src="../icons-4k-synth/duotone/ph-shopping-cart.svg" width="20" height="20" style="color:var(--uip-brand-700)" />

<!-- duocolor: two independent CSS vars -->
<div style="
  --uip-icon-primary: var(--uip-brand-600);
  --uip-icon-secondary: var(--uip-accent-500);
">
  <img src="../icons-4k-synth/duocolor/ph-shield-check.svg" width="20" height="20" />
</div>
```

## Verification

```bash
ls icons-4k-synth/{stroke,solid,duotone,duocolor}/*.svg | wc -l   # 15,566
for d in stroke solid duotone duocolor; do echo "$d: $(ls icons-4k-synth/$d/*.svg | wc -l)"; done
```
