# Sidebar — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/sidebar

## Component API

| Component | Extends | Props |
| :-- | :-- | :-- |
| **Sidebar** | — | |
| **SidebarHeader** | `<div>` | |
| **SidebarBody** | `<nav>` | |
| **SidebarFooter** | `<div>` | |
| **SidebarSection** | `<div>` | |
| **SidebarDivider** | `<hr>` | |
| **SidebarSpacer** | `<div>` | |
| **SidebarHeading** | `<div>` | |
| **SidebarItem** | Headless UI `Button` or `Link` | `current`, `href` |
| **SidebarLabel** | `<span>` | |

Icon sizing: SidebarItem designed around 20×20 icons.

## Full shell (header / body / footer with account dropdown)

```tsx
<Sidebar>
  <SidebarHeader>
    <Dropdown>
      <DropdownButton as={SidebarItem} className="mb-2.5">
        <Avatar src="/tailwind-logo.svg" />
        <SidebarLabel>Tailwind Labs</SidebarLabel>
        <ChevronDownIcon />
      </DropdownButton>
      <DropdownMenu className="min-w-64" anchor="bottom start">…</DropdownMenu>
    </Dropdown>
    <SidebarSection>
      <SidebarItem href="/search"><MagnifyingGlassIcon /><SidebarLabel>Search</SidebarLabel></SidebarItem>
      <SidebarItem href="/inbox"><InboxIcon /><SidebarLabel>Inbox</SidebarLabel></SidebarItem>
    </SidebarSection>
  </SidebarHeader>
  <SidebarBody>
    <SidebarSection>
      <SidebarItem href="/home"><HomeIcon /><SidebarLabel>Home</SidebarLabel></SidebarItem>
      <SidebarItem href="/events"><Square2StackIcon /><SidebarLabel>Events</SidebarLabel></SidebarItem>
      <SidebarItem href="/orders"><TicketIcon /><SidebarLabel>Orders</SidebarLabel></SidebarItem>
    </SidebarSection>
    <SidebarSpacer />
    <SidebarSection>
      <SidebarItem href="/support"><QuestionMarkCircleIcon /><SidebarLabel>Support</SidebarLabel></SidebarItem>
    </SidebarSection>
  </SidebarBody>
  <SidebarFooter>
    <Dropdown>
      <DropdownButton as={SidebarItem}>
        <span className="flex min-w-0 items-center gap-3">
          <Avatar src="/profile-photo.jpg" className="size-10" square alt="" />
          <span className="min-w-0">
            <span className="block truncate text-sm/5 font-medium text-zinc-950 dark:text-white">Erica</span>
            <span className="block truncate text-xs/5 font-normal text-zinc-500 dark:text-zinc-400">erica@example.com</span>
          </span>
        </span>
        <ChevronUpIcon />
      </DropdownButton>
      <DropdownMenu className="min-w-64" anchor="top start">…</DropdownMenu>
    </Dropdown>
  </SidebarFooter>
</Sidebar>
```

## Section heading / divider / spacer / active state
- `<SidebarItem href="/" current>…</SidebarItem>` for active link
- `<SidebarHeading>Resources</SidebarHeading>` inside a `SidebarSection`
- `<SidebarSpacer />` between sections — pushes subsequent section to bottom
- `<SidebarDivider />` hr line between sections
