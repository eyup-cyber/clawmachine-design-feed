# Dropdown — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/dropdown

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Dropdown** extends Headless UI `<Menu>` |
| **DropdownButton** extends `<Button>` | — | Inherits color/outline/plain/disabled |
| **DropdownMenu** extends Headless UI `<MenuItems>` | `anchor` default: `bottom` | |
| **DropdownItem** extends Headless UI `<MenuItem>` | `href` / `onClick` / `disabled` | |
| **DropdownHeader** extends `<div>` | | |
| **DropdownSection** extends Headless UI `<MenuSection>` | | |
| **DropdownHeading** extends Headless UI `<MenuHeading>` | | |
| **DropdownDivider** extends Headless UI `<MenuSeparator>` | | |
| **DropdownLabel** extends Headless UI `<Label>` | | |
| **DropdownDescription** extends Headless UI `<Description>` | | |
| **DropdownShortcut** extends Headless UI `<Description>` | `keys` | |

## Basic + styled variants

```tsx
import { Dropdown, DropdownButton, DropdownItem, DropdownMenu } from '@/components/dropdown'
import { ChevronDownIcon } from '@heroicons/react/16/solid'

<Dropdown>
  <DropdownButton outline>
    Options
    <ChevronDownIcon />
  </DropdownButton>
  <DropdownMenu>
    <DropdownItem href="/users/1">View</DropdownItem>
    <DropdownItem href="/users/1/edit">Edit</DropdownItem>
    <DropdownItem onClick={() => deleteUser()}>Delete</DropdownItem>
  </DropdownMenu>
</Dropdown>
```

Anchor values: `top|right|bottom|left` alone, or `top start`, `bottom end`, etc.

## With sections + heading + divider

```tsx
<DropdownMenu>
  <DropdownSection aria-label="Account">
    <DropdownItem href="/account">Account</DropdownItem>
    <DropdownItem href="/billing">Billing</DropdownItem>
  </DropdownSection>
  <DropdownDivider />
  <DropdownSection>
    <DropdownHeading>My events</DropdownHeading>
    <DropdownItem href="/upcoming-events">Upcoming events</DropdownItem>
  </DropdownSection>
</DropdownMenu>
```

## With description / icons / keyboard shortcut

```tsx
<DropdownItem href="#">
  <UserIcon />
  <DropdownLabel>Account</DropdownLabel>
  <DropdownDescription>Manage profile</DropdownDescription>
  <DropdownShortcut keys="⌘O" />
</DropdownItem>
```

## With header

```tsx
<DropdownHeader>
  <div className="pr-6">
    <div className="text-xs text-zinc-500 dark:text-zinc-400">Signed in as Tom Cook</div>
    <div className="text-sm/7 font-semibold text-zinc-800 dark:text-white">tom@example.com</div>
  </div>
</DropdownHeader>
<DropdownDivider />
```

## Icon-only / avatar trigger

```tsx
// icon-only
<DropdownButton plain aria-label="More options"><EllipsisHorizontalIcon /></DropdownButton>

// avatar trigger
<DropdownButton className="size-8" as={AvatarButton} src={currentUser.avatarUrl} aria-label="Account options" />
```

## Custom trigger via Headless.MenuButton

```tsx
<Headless.MenuButton className="flex w-48 items-center gap-3 rounded-xl border border-transparent p-1 data-active:border-zinc-200 data-hover:border-zinc-200 dark:data-active:border-zinc-700 dark:data-hover:border-zinc-700" aria-label="Account options">
  <img className="size-10 rounded-lg" src={currentUser.avatarUrl} alt="" />
  <span className="block text-left">
    <span className="block text-sm/5 font-medium">{currentUser.name}</span>
    <span className="block text-xs/5 text-zinc-500">{currentUser.role}</span>
  </span>
  <ChevronUpDownIcon className="mr-1 ml-auto size-4 shrink-0 stroke-zinc-400" />
</Headless.MenuButton>
```
