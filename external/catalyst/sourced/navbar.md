# Navbar — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/navbar

## Component API

| Component | Extends | Props |
| :-- | :-- | :-- |
| **Navbar** | `<div>` | |
| **NavbarDivider** | `<div>` | |
| **NavbarSection** | `<div>` | |
| **NavbarSpacer** | `<div>` | |
| **NavbarItem** | Headless UI `Button` or `Link` | `current`, `href` |
| **NavbarLabel** | `<span>` | |

Icon sizing: navbar items are designed around 20×20 icons (badge/button icons are 16×16).

## Basic

```tsx
import { Navbar, NavbarItem, NavbarSection } from '@/components/navbar'

<Navbar>
  <NavbarSection>
    <NavbarItem href="/" current>Home</NavbarItem>
    <NavbarItem href="/events">Events</NavbarItem>
    <NavbarItem href="/orders">Orders</NavbarItem>
  </NavbarSection>
</Navbar>
```

## With logo + spacer + icon links + avatar dropdown (full shell)

```tsx
<Navbar>
  <Dropdown>
    <DropdownButton as={NavbarItem}>
      <Avatar src="/tailwind-logo.svg" />
      <NavbarLabel>Tailwind Labs</NavbarLabel>
      <ChevronDownIcon />
    </DropdownButton>
    <DropdownMenu className="min-w-64" anchor="bottom start">...</DropdownMenu>
  </Dropdown>

  <NavbarDivider className="max-lg:hidden" />
  <NavbarSection className="max-lg:hidden">
    <NavbarItem href="/" current>Home</NavbarItem>
    <NavbarItem href="/events">Events</NavbarItem>
  </NavbarSection>

  <NavbarSpacer />

  <NavbarSection>
    <NavbarItem href="/search" aria-label="Search"><MagnifyingGlassIcon /></NavbarItem>
    <NavbarItem href="/inbox" aria-label="Inbox"><InboxIcon /></NavbarItem>
    <Dropdown>
      <DropdownButton as={NavbarItem}>
        <Avatar src="/profile-photo.jpg" square />
      </DropdownButton>
      <DropdownMenu className="min-w-64" anchor="bottom end">...</DropdownMenu>
    </Dropdown>
  </NavbarSection>
</Navbar>
```

Logo sizing: 40px on mobile, 32px at `sm:` breakpoint (use `className="size-10 sm:size-8"`).

## Mobile menu
Use `StackedLayout` which bundles the navbar with a sidebar that becomes a drawer on mobile.

## Hide items on mobile
`max-lg:hidden` utility on NavbarSection / NavbarDivider.
