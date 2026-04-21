# Text — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/text

## Component API

| Component | Extends | Props |
| :-- | :-- | :-- |
| **Text** | `<p>` | `children` |
| **TextLink** | Catalyst `Link` | `href`, `children` |
| **Strong** | `<strong>` | `children` |
| **Code** | `<code>` | `children` |

## Example

```tsx
import { Code, Strong, Text, TextLink } from '@/components/text'

<Text>
  This feature is only available to users on the <Strong>Business Plan</Strong>. To upgrade, visit your{' '}
  <TextLink href="#">billing settings</TextLink>.
</Text>

<Text>
  Your new API token is <Code>BaVrRKpRMS_ndKU</Code>. Store this token somewhere safe as it will only be displayed once.
</Text>
```

Automatically dark-mode responsive.
