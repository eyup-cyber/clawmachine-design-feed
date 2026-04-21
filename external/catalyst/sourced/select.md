# Select — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/select

Styled wrapper around native `<select>` (vs. Listbox which is a Headless re-engineered one).

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Select** extends Headless UI `<Select>` | `disabled`, `invalid`, `name`, `defaultValue`, `value`, `onChange` | |

## Basic + placeholder pattern + validation

```tsx
import { Field, Label, Description, ErrorMessage } from '@/components/fieldset'
import { Select } from '@/components/select'

<Field>
  <Label>Project status</Label>
  <Select name="status" defaultValue="" invalid={errors.has('status')}>
    <option value="" disabled>Select a status…</option>
    <option value="active">Active</option>
    <option value="paused">Paused</option>
    <option value="delayed">Delayed</option>
    <option value="canceled">Canceled</option>
  </Select>
  {errors.has('status') && <ErrorMessage>{errors.get('status')}</ErrorMessage>}
</Field>

// width constrain
<Select className="max-w-40" name="day_of_the_week">…</Select>
```
