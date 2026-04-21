# Input — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/input

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Input** extends Headless UI `<Input>` |
| `disabled` | `false` |
| `invalid` | `false` |
| `name`, `defaultValue`, `value`, `onChange` | | |
| **Field**, **Label**, **Description**, **ErrorMessage** — from `@/components/fieldset` |

Supported `type`: `email`, `number`, `password`, `search`, `tel`, `text`, `url`, `date`, `datetime-local`, `month`, `time`, `week`

## Basic + with description + with icon

```tsx
import { Description, Field, Label } from '@/components/fieldset'
import { Input, InputGroup } from '@/components/input'
import { MagnifyingGlassIcon } from '@heroicons/react/16/solid'

<Field>
  <Label>Product name</Label>
  <Description>Use the name you'd like people to see in their cart.</Description>
  <Input name="product_name" />
</Field>

<InputGroup>
  <MagnifyingGlassIcon />
  <Input name="search" placeholder="Search…" aria-label="Search" />
</InputGroup>
```

## Validation

```tsx
<Field>
  <Label>Full name</Label>
  <Input name="full_name" invalid={errors.has('full_name')} />
  {errors.has('full_name') && <ErrorMessage>{errors.get('full_name')}</ErrorMessage>}
</Field>
```

## Constraining width
`<Input className="max-w-24" name="cvc" pattern="[0-9]*" />`
