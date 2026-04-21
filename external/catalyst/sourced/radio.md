# Radio — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/radio

## Component API

| Component | Extends | Props |
| :-- | :-- | :-- |
| **RadioGroup** | Headless UI `<RadioGroup>` | `disabled`, `name`, `defaultValue`, `value`, `onChange` |
| **Radio** | Headless UI `<Radio>` | `color` (`dark/zinc` default), `disabled`, `value` |
| **RadioField** | Headless UI `<Field>` | `disabled` |
| **Label**, **Description** | Headless UI counterparts | |

## With fieldset + descriptions (canonical)

```tsx
import { Description, Fieldset, Label, Legend } from '@/components/fieldset'
import { Radio, RadioField, RadioGroup } from '@/components/radio'
import { Text } from '@/components/text'

<Fieldset>
  <Legend>Resale and transfers</Legend>
  <Text>Decide if people buy tickets from you or from scalpers.</Text>
  <RadioGroup name="resale" defaultValue="permit">
    <RadioField>
      <Radio value="permit" />
      <Label>Allow tickets to be resold</Label>
      <Description>Customers can resell or transfer their tickets if they can’t make it to the event.</Description>
    </RadioField>
    <RadioField>
      <Radio value="forbid" />
      <Label>Don’t allow tickets to be resold</Label>
      <Description>Tickets cannot be resold or transferred to another person.</Description>
    </RadioField>
  </RadioGroup>
</Fieldset>
```

## Custom layout (horizontal rating)
```tsx
<Headless.RadioGroup name="rating" defaultValue={3} className="mt-4 flex gap-6 sm:gap-8">
  {[1,2,3,4,5].map((r) => (
    <Headless.Field key={r} className="flex items-center gap-2">
      <Radio value={r} />
      <Headless.Label className="text-base/6 select-none sm:text-sm/6">{r}</Headless.Label>
    </Headless.Field>
  ))}
</Headless.RadioGroup>
```

## Color reference — 2 adaptive (`dark/zinc`, `dark/white`) + 20 solid colors
