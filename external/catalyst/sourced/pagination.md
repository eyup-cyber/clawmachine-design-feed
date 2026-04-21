# Pagination — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/pagination

## Component API

| Component | Extends | Props |
| :-- | :-- | :-- |
| **Pagination** | `<nav>` | `aria-label` default `Page navigation` |
| **PaginationPrevious** | `<a>` | `href` (omit to disable), `children` default `Previous` |
| **PaginationNext** | `<a>` | `href` (omit to disable), `children` default `Next` |
| **PaginationList** | — | |
| **PaginationPage** | `<a>` | `href`, `children` (page number), `current` |
| **PaginationGap** | — | |

## Full example with ellipsis

```tsx
import {
  Pagination, PaginationGap, PaginationList, PaginationNext, PaginationPage, PaginationPrevious,
} from '@/components/pagination'

<Pagination>
  <PaginationPrevious href="?page=2" />
  <PaginationList>
    <PaginationPage href="?page=1">1</PaginationPage>
    <PaginationPage href="?page=2">2</PaginationPage>
    <PaginationPage href="?page=3" current>3</PaginationPage>
    <PaginationPage href="?page=4">4</PaginationPage>
    <PaginationGap />
    <PaginationPage href="?page=65">65</PaginationPage>
    <PaginationPage href="?page=66">66</PaginationPage>
  </PaginationList>
  <PaginationNext href="?page=4" />
</Pagination>
```

## Cursor-style (no page numbers)
```tsx
<Pagination>
  <PaginationPrevious />
  <PaginationNext href="?after=421c1b0" />
</Pagination>
```
