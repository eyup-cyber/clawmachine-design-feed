# Heading — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/heading

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Heading** extends `<h1>` | `level` (number 1-6) |
| **Subheading** extends `<h2>` | `level` (number 1-6) |

## Examples

```tsx
import { Heading, Subheading } from '@/components/heading'

<Heading>Recent orders</Heading>           // renders <h1>
<Subheading>Recent orders</Subheading>     // renders <h2>
<Heading level={2}>Recent orders</Heading>  // <h2>, visual h1 style
```

## Header row pattern
```tsx
<div className="flex w-full flex-wrap items-end justify-between gap-4 border-b border-zinc-950/10 pb-6 dark:border-white/10">
  <Heading>Order #1011</Heading>
  <div className="flex gap-4">
    <Button outline>Refund</Button>
    <Button>Resend invoice</Button>
  </div>
</div>
```
