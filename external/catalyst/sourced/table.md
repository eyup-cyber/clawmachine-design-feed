# Table — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/table

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Table** extends `<table>` | `bleed`, `dense`, `grid`, `striped` (all bool) |
| **TableHead** extends `<thead>` | |
| **TableBody** extends `<tbody>` | |
| **TableRow** extends `<tr>` | `href`, `target`, `title` — row-as-link |
| **TableHeader** extends `<th>` | |
| **TableCell** extends `<td>` | |

## Basic + responsive gutter pattern

```tsx
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/table'

<Table className="[--gutter:--spacing(6)] sm:[--gutter:--spacing(8)]">
  <TableHead>
    <TableRow>
      <TableHeader>Name</TableHeader>
      <TableHeader>Email</TableHeader>
      <TableHeader>Role</TableHeader>
    </TableRow>
  </TableHead>
  <TableBody>
    {users.map((user) => (
      <TableRow key={user.handle} href={user.url}>
        <TableCell className="font-medium">{user.name}</TableCell>
        <TableCell>{user.email}</TableCell>
        <TableCell className="text-zinc-500">{user.access}</TableCell>
      </TableRow>
    ))}
  </TableBody>
</Table>
```

## Variants
- `bleed` — full-bleed horizontal into gutters
- `dense` — condensed row spacing (stats tables)
- `grid` — vertical gridlines
- `striped` — striped rows, removes row borders

## Complex content cell (avatar + email + badge)
```tsx
<TableCell>
  <div className="flex items-center gap-4">
    <Avatar src={user.avatarUrl} className="size-12" />
    <div>
      <div className="font-medium">{user.name}</div>
      <div className="text-zinc-500"><a href="#" className="hover:text-zinc-700">{user.email}</a></div>
    </div>
  </div>
</TableCell>
<TableCell>
  {user.online ? <Badge color="lime">Online</Badge> : <Badge color="zinc">Offline</Badge>}
</TableCell>
```

## Actions cell (dropdown)
```tsx
<TableCell>
  <div className="-mx-3 -my-1.5 sm:-mx-2.5">
    <Dropdown>
      <DropdownButton plain aria-label="More options"><EllipsisHorizontalIcon /></DropdownButton>
      <DropdownMenu anchor="bottom end">
        <DropdownItem>View</DropdownItem>
        <DropdownItem>Edit</DropdownItem>
        <DropdownItem>Delete</DropdownItem>
      </DropdownMenu>
    </Dropdown>
  </div>
</TableCell>
```

In dialog, `--gutter` auto-matches dialog padding.
