# Textarea — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/textarea

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Textarea** extends Headless UI `<Textarea>` | `disabled`, `invalid`, `resizable` (default true), `name`, `defaultValue`, `value`, `onChange`, `rows` |

## Canonical example

```tsx
import { Field, Label, Description, ErrorMessage } from '@/components/fieldset'
import { Textarea } from '@/components/textarea'

<Field>
  <Label>Description</Label>
  <Description>This will be shown under the product title.</Description>
  <Textarea name="description" invalid={errors.has('description')} />
  {errors.has('description') && <ErrorMessage>{errors.get('description')}</ErrorMessage>}
</Field>
```

## Custom grid layout (label side-by-side)
```tsx
<Headless.Field className="grid grid-cols-12 gap-6">
  <div className="col-span-5">
    <Label>Description</Label>
    <Description className="mt-1">This will be shown under the product title.</Description>
  </div>
  <div className="col-span-7">
    <Textarea name="description" rows="3" />
  </div>
</Headless.Field>
```
