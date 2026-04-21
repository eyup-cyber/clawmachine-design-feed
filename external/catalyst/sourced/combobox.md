# Combobox — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/combobox

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Combobox** extends Headless UI `<Combobox>` |
| `disabled` | `false` | Disable |
| `invalid` | `false` | Validation error |
| `anchor` | `bottom` | Dropdown anchor position |
| `name` | - | Form name |
| `options` | - | Collection of option data |
| `filter` | - | Custom `(option, query) => bool` filter |
| `displayValue` | - | `(option) => string` render for selected |
| `defaultValue` | - | Initial uncontrolled value |
| `value` | - | Controlled value |
| `onChange` | - | Change handler |
| `placeholder` | - | Empty-state text |
| **ComboboxOption** extends Headless UI `<ComboboxOption>` |
| **ComboboxLabel** extends `<span>` |
| **ComboboxDescription** extends `<span>` |

## Basic example

```tsx
import { Combobox, ComboboxLabel, ComboboxOption } from '@/components/combobox'
import { Field, Label } from '@/components/fieldset'

<Field>
  <Label>Assigned to</Label>
  <Combobox name="user" options={users} displayValue={(u) => u?.name} defaultValue={currentUser}>
    {(user) => (
      <ComboboxOption value={user}>
        <ComboboxLabel>{user.name}</ComboboxLabel>
      </ComboboxOption>
    )}
  </Combobox>
</Field>
```

## With avatar / flag / description / custom filter

```tsx
{(user) => (
  <ComboboxOption value={user}>
    <Avatar src={user.avatarUrl} initials={user.initials} className="bg-purple-500 text-white" alt="" />
    <ComboboxLabel>{user.name}</ComboboxLabel>
    <ComboboxDescription>@{user.handle}</ComboboxDescription>
  </ComboboxOption>
)}

// custom filter
filter={(u, query) =>
  u.name.toLowerCase().includes(query.toLowerCase()) ||
  `@${u.handle}`.toLowerCase().includes(query.toLowerCase())
}
```

## Validation

```tsx
<Field>
  <Label>Assigned to</Label>
  <Combobox invalid name="user" options={users} displayValue={(u) => u?.name} placeholder="Select user…" />
  <ErrorMessage>A user is required.</ErrorMessage>
</Field>
```
