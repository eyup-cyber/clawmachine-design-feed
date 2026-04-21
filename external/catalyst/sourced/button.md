# Button — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/button

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Button** extends Headless UI `Button` or `Link` |
| `type` | `button` | The button type |
| `color` | `dark/zinc` | Color variant |
| `outline` | `false` | Outline button style |
| `plain` | `false` | Plain button style (no border/shadow/bg) |
| `disabled` | `false` | Disable the button |
| `href` | - | Renders `Link` when provided |

## Basic + with icon

```tsx
import { Button } from '@/components/button'
import { PlusIcon } from '@heroicons/react/16/solid'

<Button>Save changes</Button>
<Button color="cyan">Save changes</Button>
<Button outline>Save draft</Button>
<Button plain>Save draft</Button>
<Button disabled>Save changes</Button>
<Button href="/get-started">Get started</Button>

<Button>
  <PlusIcon />
  Add item
</Button>
```

## Solid color reference

**Adaptive (3):** `dark/zinc`, `light`, `dark/white`

**Solid (20):** dark · zinc · white · red · orange · amber · yellow · lime · green · emerald · teal · cyan · sky · blue · indigo · violet · purple · fuchsia · pink · rose
