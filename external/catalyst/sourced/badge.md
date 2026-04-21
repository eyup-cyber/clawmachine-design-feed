# Badge — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/badge

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Badge** extends `<span>` |
| `color` | `zinc` | Color of the badge |
| **BadgeButton** extends Headless UI `Button` or `Link` |
| `color` | `zinc` | Color of the badge |
| `href` | - | Renders as link when provided |

## Basic example

```tsx
import { Badge } from '@/components/badge'

<div className="flex gap-3">
  <Badge color="lime">documentation</Badge>
  <Badge color="purple">help wanted</Badge>
  <Badge color="rose">bug</Badge>
</div>
```

## BadgeButton

```tsx
<BadgeButton href="#">documentation</BadgeButton>
```

## Color reference (18 adaptive colors, light/dark)

red · orange · amber · yellow · lime · green · emerald · teal · cyan · sky · blue · indigo · violet · purple · fuchsia · pink · rose · zinc
