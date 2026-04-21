# duotone/ — Untitled UI Pro Icons 4K Synth

**3,207** SVGs in this folder. 24×24 viewBox, `stroke="currentColor"` or `fill="currentColor"`, render at any pixel size.

## Style definition

Two-layer glyphs: a low-opacity backing fill (0.2) behind the primary layer. Phosphor native duotone + Lucide synth (backing fill duplicated from stroke geometry).

Single CSS variable controls both layers via `currentColor` — the backing layer inherits at 0.2 opacity.

```html
<img src="duotone/ph-shopping-cart.svg" width="20" height="20" style="color:var(--uip-brand-700)"/>
```

## Source breakdown

| Prefix | Upstream | Count | License |
|--------|----------|-------|---------|
| `lu-` | Lucide synth | 1,695 | ISC |
| `ph-` | Phosphor Icons | 1,512 | MIT |

## Category coverage

Icons can belong to multiple categories (sum > total). 'other' is anything the keyword matcher didn't bucket — use the filename filter in `gallery.html` to search those by substring.

| Category | Count | Sample filenames |
|----------|-------|------------------|
| arrows | 282 | `lu-a-arrow-down.svg`, `lu-a-arrow-up.svg`, `lu-arrow-big-down-dash.svg`, `lu-arrow-big-down.svg` |
| alerts | 44 | `lu-badge-alert.svg`, `lu-badge-info.svg`, `lu-battery-warning.svg`, `lu-bell-dot.svg` |
| charts | 45 | `lu-activity.svg`, `lu-chart-area.svg`, `lu-chart-bar-big.svg`, `lu-chart-bar-decreasing.svg` |
| communication | 90 | `lu-bot-message-square.svg`, `lu-mail-check.svg`, `lu-mail-minus.svg`, `lu-mail-open.svg` |
| cursors | 49 | `lu-hand-coins.svg`, `lu-hand-fist.svg`, `lu-hand-grab.svg`, `lu-hand-heart.svg` |
| development | 57 | `lu-bug-off.svg`, `lu-bug-play.svg`, `lu-bug.svg`, `lu-code-xml.svg` |
| editor | 130 | `lu-align-center-horizontal.svg`, `lu-align-center-vertical.svg`, `lu-align-end-horizontal.svg`, `lu-align-end-vertical.svg` |
| files | 152 | `lu-archive-restore.svg`, `lu-archive-x.svg`, `lu-archive.svg`, `lu-file-archive.svg` |
| finance | 35 | `lu-badge-dollar-sign.svg`, `lu-banknote-arrow-down.svg`, `lu-banknote-arrow-up.svg`, `lu-banknote-x.svg` |
| general | 212 | `lu-alarm-clock-check.svg`, `lu-alarm-clock-minus.svg`, `lu-alarm-clock-plus.svg`, `lu-badge-check.svg` |
| home | 15 | `lu-door-closed-locked.svg`, `lu-door-closed.svg`, `lu-door-open.svg`, `lu-house-heart.svg` |
| images | 48 | `lu-book-image.svg`, `lu-camera-off.svg`, `lu-camera.svg`, `lu-file-image.svg` |
| layout | 66 | `lu-chart-column-big.svg`, `lu-chart-column-decreasing.svg`, `lu-chart-column-increasing.svg`, `lu-chart-column-stacked.svg` |
| maps | 55 | `lu-compass.svg`, `lu-drafting-compass.svg`, `lu-globe-lock.svg`, `lu-globe-off.svg` |
| media | 58 | `lu-book-headphones.svg`, `lu-bug-play.svg`, `lu-circle-pause.svg`, `lu-circle-play.svg` |
| security | 75 | `lu-book-key.svg`, `lu-book-lock.svg`, `lu-brick-wall-shield.svg`, `lu-door-closed-locked.svg` |
| shapes | 295 | `lu-bot-message-square.svg`, `lu-circle-alert.svg`, `lu-circle-arrow-down.svg`, `lu-circle-arrow-left.svg` |
| shopping | 28 | `lu-gift.svg`, `lu-package-2.svg`, `lu-package-check.svg`, `lu-package-minus.svg` |
| social | 51 | `lu-book-heart.svg`, `lu-calendar-heart.svg`, `lu-file-heart.svg`, `lu-folder-heart.svg` |
| time | 85 | `lu-alarm-clock-check.svg`, `lu-alarm-clock-minus.svg`, `lu-alarm-clock-off.svg`, `lu-alarm-clock-plus.svg` |
| users | 70 | `lu-book-user.svg`, `lu-circle-user-round.svg`, `lu-circle-user.svg`, `lu-contact-round.svg` |
| weather | 70 | `lu-cloud-alert.svg`, `lu-cloud-backup.svg`, `lu-cloud-check.svg`, `lu-cloud-cog.svg` |
| other | 1,619 | — |

## Verification

```bash
ls *.svg | wc -l   # 3,207
```
