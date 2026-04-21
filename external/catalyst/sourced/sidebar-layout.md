# Sidebar layout — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/sidebar-layout

## Component API

| Component | Extends | Props |
| :-- | :-- | :-- |
| **SidebarLayout** | `<div>` | `sidebar`, `navbar`, `children` |

`sidebar` renders at all screen sizes. `navbar` is the mobile top bar.

## Basic example

```tsx
import { Navbar } from '@/components/navbar'
import { Sidebar } from '@/components/sidebar'
import { SidebarLayout } from '@/components/sidebar-layout'

<SidebarLayout
  sidebar={<Sidebar>{/* sidebar content */}</Sidebar>}
  navbar={<Navbar>{/* navbar content */}</Navbar>}
>
  {/* page content */}
</SidebarLayout>
```

## Overscroll background
Apply to `<html>`:
```
class="bg-white lg:bg-zinc-100 dark:bg-zinc-900 dark:lg:bg-zinc-950"
```
