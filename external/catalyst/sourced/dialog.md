# Dialog — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/dialog

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Dialog** extends Headless UI `<Dialog>` |
| `open` | - | Whether the dialog is open |
| `onClose` | - | Dismiss handler |
| `size` | `lg` | max-width — xs, sm, md, lg, xl, 2xl, 3xl, 4xl, 5xl |
| **DialogTitle** extends Headless UI `<DialogTitle>` |
| **DialogDescription** extends Headless UI `<Description>` |
| **DialogBody** extends `<div>` |
| **DialogActions** extends `<div>` |

## Basic example

```tsx
import { Button } from '@/components/button'
import { Dialog, DialogActions, DialogBody, DialogDescription, DialogTitle } from '@/components/dialog'
import { Field, Label } from '@/components/fieldset'
import { Input } from '@/components/input'
import { useState } from 'react'

function Example() {
  let [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <Button onClick={() => setIsOpen(true)}>Refund payment</Button>
      <Dialog open={isOpen} onClose={setIsOpen}>
        <DialogTitle>Refund payment</DialogTitle>
        <DialogDescription>
          The refund will be reflected in the customer’s bank account 2 to 3 business days after processing.
        </DialogDescription>
        <DialogBody>
          <Field>
            <Label>Amount</Label>
            <Input name="amount" placeholder="$0.00" />
          </Field>
        </DialogBody>
        <DialogActions>
          <Button plain onClick={() => setIsOpen(false)}>Cancel</Button>
          <Button onClick={() => setIsOpen(false)}>Refund</Button>
        </DialogActions>
      </Dialog>
    </>
  )
}
```

## Opening from Dropdown
Render the `Dialog` outside the `Dropdown` — otherwise it unmounts when the dropdown closes.

## Scrolling content
Dialogs become scrollable automatically when content exceeds viewport height.
