# solid/ — Untitled UI Pro Icons 4K Synth

**5,658** SVGs in this folder. 24×24 viewBox, `stroke="currentColor"` or `fill="currentColor"`, render at any pixel size.

## Style definition

Filled glyphs. Phosphor fill variant + Material Symbols rounded-fill + Iconoir solid. `fill="currentColor"` throughout.

```html
<img src="solid/ph-user.svg" width="20" height="20" style="color:var(--uip-brand-600)"/>
```

## Source breakdown

| Prefix | Upstream | Count | License |
|--------|----------|-------|---------|
| `ms-` | Material Symbols | 3,858 | Apache-2.0 |
| `ph-` | Phosphor Icons | 1,512 | MIT |
| `iconoir-` | Iconoir | 288 | MIT |

## Category coverage

Icons can belong to multiple categories (sum > total). 'other' is anything the keyword matcher didn't bucket — use the filename filter in `gallery.html` to search those by substring.

| Category | Count | Sample filenames |
|----------|-------|------------------|
| arrows | 243 | `iconoir-arrow-down-circle.svg`, `iconoir-arrow-down-left-circle.svg`, `iconoir-arrow-down-left-square.svg`, `iconoir-arrow-down-right-circle.svg` |
| alerts | 38 | `iconoir-bell-notification.svg`, `iconoir-chat-bubble-warning.svg`, `iconoir-headset-warning.svg`, `iconoir-info-circle.svg` |
| charts | 28 | `ms-activity_zone.svg`, `ms-analytics.svg`, `ms-bar_chart.svg`, `ms-bar_chart_4_bars.svg` |
| communication | 106 | `iconoir-chat-bubble-check.svg`, `iconoir-chat-bubble-empty.svg`, `iconoir-chat-bubble-question.svg`, `iconoir-chat-bubble-translate.svg` |
| cursors | 37 | `iconoir-square-cursor.svg`, `ms-hand_bones.svg`, `ms-hand_gesture.svg`, `ms-hand_gesture_off.svg` |
| development | 29 | `iconoir-bug.svg`, `ms-bug_report.svg`, `ms-code.svg`, `ms-code_blocks.svg` |
| editor | 163 | `iconoir-align-bottom-box.svg`, `iconoir-align-horizontal-centers.svg`, `iconoir-align-horizontal-spacing.svg`, `iconoir-align-left-box.svg` |
| files | 100 | `ms-archive.svg`, `ms-audio_description.svg`, `ms-description.svg`, `ms-document_scanner.svg` |
| finance | 34 | `iconoir-credit-card.svg`, `iconoir-dollar-circle.svg`, `iconoir-money-square.svg`, `iconoir-wallet.svg` |
| general | 184 | `iconoir-bubble-search.svg`, `iconoir-calendar-check.svg`, `iconoir-calendar-minus.svg`, `iconoir-calendar-plus.svg` |
| home | 34 | `ms-door_back.svg`, `ms-door_front.svg`, `ms-door_open.svg`, `ms-door_sensor.svg` |
| images | 69 | `iconoir-adobe-photoshop.svg`, `iconoir-camera.svg`, `ms-browse_gallery.svg`, `ms-camera.svg` |
| layout | 75 | `iconoir-dots-grid-3x3.svg`, `ms-add_column_left.svg`, `ms-add_column_right.svg`, `ms-admin_panel_settings.svg` |
| maps | 62 | `iconoir-compass.svg`, `iconoir-pin-slash.svg`, `iconoir-pin.svg`, `ms-add_location.svg` |
| media | 66 | `iconoir-music-note-plus.svg`, `iconoir-music-note.svg`, `iconoir-pause.svg`, `iconoir-phone-paused.svg` |
| security | 72 | `iconoir-eye.svg`, `ms-battery_android_frame_shield.svg`, `ms-battery_android_shield.svg`, `ms-eye_tracking.svg` |
| shapes | 212 | `iconoir-arrow-down-circle.svg`, `iconoir-arrow-down-left-circle.svg`, `iconoir-arrow-down-left-square.svg`, `iconoir-arrow-down-right-circle.svg` |
| shopping | 38 | `iconoir-arrow-left-tag.svg`, `iconoir-arrow-right-tag.svg`, `iconoir-bluetooth-tag.svg`, `iconoir-cable-tag.svg` |
| social | 39 | `iconoir-heart.svg`, `iconoir-share-android.svg`, `ms-favorite.svg`, `ms-heart_broken.svg` |
| time | 97 | `iconoir-alarm.svg`, `iconoir-calendar-arrow-down.svg`, `iconoir-calendar-arrow-up.svg`, `iconoir-calendar-check.svg` |
| users | 79 | `ms-connect_without_contact.svg`, `ms-contact_emergency.svg`, `ms-contact_mail.svg`, `ms-contact_page.svg` |
| weather | 77 | `iconoir-cloud-square.svg`, `iconoir-droplet-snow-flake-in.svg`, `ms-chair_umbrella.svg`, `ms-cloud.svg` |
| other | 3,990 | — |

## Verification

```bash
ls *.svg | wc -l   # 5,658
```
