# stroke/ — Untitled UI Pro Icons 4K Synth

**3,494** SVGs in this folder. 24×24 viewBox, `stroke="currentColor"` or `fill="currentColor"`, render at any pixel size.

## Style definition

Outline-only glyphs, 2 px strokes, `fill="none"`. Lucide/Feather are 2.0 px baseline; Untitled UI Pro's 1.67 px visual weight is achieved by rendering at 20 px target (`width=20 height=20`).

```html
<img src="stroke/arrow-right.svg" width="20" height="20" style="color:var(--uip-fg-primary)"/>
```

## Source breakdown

| Prefix | Upstream | Count | License |
|--------|----------|-------|---------|
| (none) | Lucide | 1,695 | ISC |
| `ph-` | Phosphor Icons | 1,512 | MIT |
| `feather-` | Feather Icons | 287 | MIT |

## Category coverage

Icons can belong to multiple categories (sum > total). 'other' is anything the keyword matcher didn't bucket — use the filename filter in `gallery.html` to search those by substring.

| Category | Count | Sample filenames |
|----------|-------|------------------|
| arrows | 313 | `a-arrow-down.svg`, `a-arrow-up.svg`, `arrow-big-down-dash.svg`, `arrow-big-down.svg` |
| alerts | 50 | `badge-alert.svg`, `badge-info.svg`, `battery-warning.svg`, `bell-dot.svg` |
| charts | 51 | `activity.svg`, `chart-area.svg`, `chart-bar-big.svg`, `chart-bar-decreasing.svg` |
| communication | 101 | `bot-message-square.svg`, `feather-mail.svg`, `feather-message-circle.svg`, `feather-message-square.svg` |
| cursors | 50 | `feather-mouse-pointer.svg`, `hand-coins.svg`, `hand-fist.svg`, `hand-grab.svg` |
| development | 67 | `bug-off.svg`, `bug-play.svg`, `bug.svg`, `code-xml.svg` |
| editor | 143 | `align-center-horizontal.svg`, `align-center-vertical.svg`, `align-end-horizontal.svg`, `align-end-vertical.svg` |
| files | 161 | `archive-restore.svg`, `archive-x.svg`, `archive.svg`, `feather-archive.svg` |
| finance | 37 | `badge-dollar-sign.svg`, `banknote-arrow-down.svg`, `banknote-arrow-up.svg`, `banknote-x.svg` |
| general | 236 | `alarm-clock-check.svg`, `alarm-clock-minus.svg`, `alarm-clock-plus.svg`, `badge-check.svg` |
| home | 16 | `door-closed-locked.svg`, `door-closed.svg`, `door-open.svg`, `feather-home.svg` |
| images | 54 | `book-image.svg`, `camera-off.svg`, `camera.svg`, `feather-camera-off.svg` |
| layout | 69 | `chart-column-big.svg`, `chart-column-decreasing.svg`, `chart-column-increasing.svg`, `chart-column-stacked.svg` |
| maps | 61 | `compass.svg`, `drafting-compass.svg`, `feather-compass.svg`, `feather-globe.svg` |
| media | 72 | `book-headphones.svg`, `bug-play.svg`, `circle-pause.svg`, `circle-play.svg` |
| security | 82 | `book-key.svg`, `book-lock.svg`, `brick-wall-shield.svg`, `door-closed-locked.svg` |
| shapes | 322 | `bot-message-square.svg`, `circle-alert.svg`, `circle-arrow-down.svg`, `circle-arrow-left.svg` |
| shopping | 33 | `feather-gift.svg`, `feather-package.svg`, `feather-shopping-bag.svg`, `feather-shopping-cart.svg` |
| social | 57 | `book-heart.svg`, `calendar-heart.svg`, `feather-heart.svg`, `feather-share-2.svg` |
| time | 87 | `alarm-clock-check.svg`, `alarm-clock-minus.svg`, `alarm-clock-off.svg`, `alarm-clock-plus.svg` |
| users | 76 | `book-user.svg`, `circle-user-round.svg`, `circle-user.svg`, `contact-round.svg` |
| weather | 83 | `cloud-alert.svg`, `cloud-backup.svg`, `cloud-check.svg`, `cloud-cog.svg` |
| other | 1,726 | — |

## Verification

```bash
ls *.svg | wc -l   # 3,494
```
