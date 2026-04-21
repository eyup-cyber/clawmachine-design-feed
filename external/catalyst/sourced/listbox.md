# Listbox — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/listbox

Listbox = a re-engineered `<select>` that can hold icons, flags, avatars, secondary text, placeholder.

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Listbox** extends Headless UI `<Listbox>` |
| `disabled`, `invalid`, `name`, `defaultValue`, `value`, `onChange`, `placeholder` | | |
| **ListboxOption** extends Headless UI `<ListboxOption>` | `value` | |
| **ListboxLabel** extends `<span>` | | |
| **ListboxDescription** extends `<span>` | | |

## Basic

```tsx
import { Field, Label } from '@/components/fieldset'
import { Listbox, ListboxLabel, ListboxOption } from '@/components/listbox'

<Field>
  <Label>Project status</Label>
  <Listbox name="status" defaultValue="active">
    <ListboxOption value="active"><ListboxLabel>Active</ListboxLabel></ListboxOption>
    <ListboxOption value="paused"><ListboxLabel>Paused</ListboxLabel></ListboxOption>
    <ListboxOption value="delayed"><ListboxLabel>Delayed</ListboxLabel></ListboxOption>
    <ListboxOption value="canceled"><ListboxLabel>Canceled</ListboxLabel></ListboxOption>
  </Listbox>
</Field>
```

## With icons / avatars / flags / secondary text

```tsx
<ListboxOption value="left">
  <Bars3BottomLeftIcon />
  <ListboxLabel>Left</ListboxLabel>
</ListboxOption>

<ListboxOption value={user}>
  <Avatar src={user.avatarUrl} initials={user.initials} className="bg-purple-500 text-white" alt="" />
  <ListboxLabel>{user.name}</ListboxLabel>
</ListboxOption>

<ListboxOption value={country.code}>
  <Flag className="w-5 sm:w-4" code={country.code} />
  <ListboxLabel>{country.name}</ListboxLabel>
</ListboxOption>

<ListboxOption value={user}>
  <ListboxLabel>{user.name}</ListboxLabel>
  <ListboxDescription>@{user.handle}</ListboxDescription>
</ListboxOption>
```

## Placeholder / validation

```tsx
<Listbox name="status" placeholder="Select status…" invalid={errors.has('status')}>...</Listbox>
{errors.has('status') && <ErrorMessage>{errors.get('status')}</ErrorMessage>}
```
