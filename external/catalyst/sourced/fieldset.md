# Fieldset — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/fieldset

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Fieldset** extends `<div>` | `disabled` (bool) |
| **Legend** extends `<div>` | |
| **FieldGroup** extends `<div>` | |

## Basic + without legend + grid + custom layout

```tsx
import { Description, Field, FieldGroup, Fieldset, Label, Legend } from '@/components/fieldset'
import { Input } from '@/components/input'
import { Select } from '@/components/select'
import { Text } from '@/components/text'
import { Textarea } from '@/components/textarea'

<Fieldset>
  <Legend>Shipping details</Legend>
  <Text>Without this your odds of getting your order are low.</Text>
  <FieldGroup>
    <Field>
      <Label>Street address</Label>
      <Input name="street_address" />
    </Field>
    <Field>
      <Label>Country</Label>
      <Select name="country">
        <option>Canada</option>
        <option>Mexico</option>
        <option>United States</option>
      </Select>
      <Description>We currently only ship to North America.</Description>
    </Field>
    <Field>
      <Label>Delivery notes</Label>
      <Textarea name="notes" />
      <Description>If you have a tiger, we'd like to know about it.</Description>
    </Field>
  </FieldGroup>
</Fieldset>
```

## Grid layout
Use a plain `<div>` with grid utilities inside a `FieldGroup`:
```tsx
<FieldGroup>
  <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 sm:gap-4">
    <Field><Label>First name</Label><Input name="first_name" /></Field>
    <Field><Label>Last name</Label><Input name="last_name" /></Field>
  </div>
  <Field className="sm:col-span-2">...</Field>
</FieldGroup>
```

## data-slot="control"
Add `data-slot="control"` to a child of your `Fieldset` to receive the same layout styles as a `FieldGroup` (used for fully custom subgrid layouts).
