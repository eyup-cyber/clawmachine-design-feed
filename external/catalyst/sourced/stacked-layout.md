# Stacked layout — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/stacked-layout

## Component API

| Component | Extends | Props |
| :-- | :-- | :-- |
| **StackedLayout** | `<div>` | `navbar`, `sidebar`, `children` |

`navbar` is the desktop top bar; `sidebar` is the mobile drawer.

## Basic example

```tsx
import { Navbar } from '@/components/navbar'
import { Sidebar } from '@/components/sidebar'
import { StackedLayout } from '@/components/stacked-layout'

<StackedLayout
  navbar={<Navbar>{/* navbar content */}</Navbar>}
  sidebar={<Sidebar>{/* mobile sidebar content */}</Sidebar>}
>
  {/* page content */}
</StackedLayout>
```

## Overscroll background (same as sidebar-layout)
`<html class="bg-white lg:bg-zinc-100 dark:bg-zinc-900 dark:lg:bg-zinc-950">`
