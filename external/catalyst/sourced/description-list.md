# Description list — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/description-list

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **DescriptionList** extends `<dl>` |
| **DescriptionTerm** extends `<dt>` |
| **DescriptionDetails** extends `<dd>` |

## Basic example

```tsx
import { DescriptionDetails, DescriptionList, DescriptionTerm } from '@/components/description-list'

<DescriptionList>
  <DescriptionTerm>Customer</DescriptionTerm>
  <DescriptionDetails>Michael Foster</DescriptionDetails>

  <DescriptionTerm>Event</DescriptionTerm>
  <DescriptionDetails>Bear Hug: Live in Concert</DescriptionDetails>

  <DescriptionTerm>Amount</DescriptionTerm>
  <DescriptionDetails>$150.00 USD</DescriptionDetails>
</DescriptionList>
```

## With heading (Subheading)

```tsx
<Subheading>Order #1011</Subheading>
<DescriptionList className="mt-4">
  {/* ... */}
</DescriptionList>
```
