# Checkbox — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/checkbox

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Checkbox** extends Headless UI `<Checkbox>` |
| `color` | `dark/zinc` | color variant |
| `disabled` | `false` | Disable the checkbox |
| `name` | - | Form name |
| `value` | - | Form value |
| `defaultChecked` | - | Initial state |
| `checked` | - | Controlled state |
| `onChange` | - | Change handler |
| `indeterminate` | - | Neither on nor off |
| **CheckboxField** extends Headless UI `<Field>` |
| `disabled` | `false` | Disable whole field |
| **CheckboxGroup** extends `<div>` |
| **Label** extends Headless UI `<Label>` |
| **Description** extends Headless UI `<Description>` |

## Fieldset example (label + description + group)

```tsx
import { Checkbox, CheckboxField, CheckboxGroup } from '@/components/checkbox'
import { Description, Fieldset, Label, Legend } from '@/components/fieldset'
import { Text } from '@/components/text'

<Fieldset>
  <Legend>Discoverability</Legend>
  <Text>Decide where your events can be found across the web.</Text>
  <CheckboxGroup>
    <CheckboxField>
      <Checkbox name="discoverability" value="show_on_events_page" defaultChecked />
      <Label>Show on events page</Label>
      <Description>Make this event visible on your profile.</Description>
    </CheckboxField>
    <CheckboxField>
      <Checkbox name="discoverability" value="allow_embedding" />
      <Label>Allow embedding</Label>
      <Description>Allow others to embed your event details on their own site.</Description>
    </CheckboxField>
  </CheckboxGroup>
</Fieldset>
```

## Indeterminate "select all" pattern

```tsx
<CheckboxField>
  <Checkbox
    checked={selected.length > 0}
    indeterminate={selected.length !== options.length}
    onChange={(checked) => setSelected(checked ? options : [])}
  />
  <Label>Select all</Label>
</CheckboxField>
```

## Color reference — 2 adaptive (`dark/zinc`, `dark/white`) + 20 solid
