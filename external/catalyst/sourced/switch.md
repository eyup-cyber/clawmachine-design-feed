# Switch — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/switch

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Switch** extends Headless UI `<Switch>` | `color` (`dark/zinc` default), `disabled`, `name`, `value`, `defaultChecked`, `checked`, `onChange` |
| **SwitchField** extends Headless UI `<Field>` | `disabled` |
| **SwitchGroup** extends `<div>` | |

## Canonical example

```tsx
import { Description, Label } from '@/components/fieldset'
import { Switch, SwitchField, SwitchGroup } from '@/components/switch'

<SwitchField>
  <Label>Allow embedding</Label>
  <Description>Allow others to embed your event details on their own site.</Description>
  <Switch name="allow_embedding" defaultChecked />
</SwitchField>

// stacked
<SwitchGroup>
  <SwitchField>
    <Label>Show on events page</Label>
    <Description>Make this event visible on your profile.</Description>
    <Switch name="show_on_events_page" defaultChecked />
  </SwitchField>
  <SwitchField disabled>
    <Label>Allow embedding</Label>
    <Description>Allow others to embed your event details on their own site.</Description>
    <Switch name="allow_embedding" />
  </SwitchField>
</SwitchGroup>
```

## Color reference — 2 adaptive (`dark/zinc`, `dark/white`) + 20 solids
