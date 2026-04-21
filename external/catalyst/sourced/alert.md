# Alert — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/alert

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Alert** extends Headless UI `<Dialog>` |
| `open` | - | Whether the alert is open or not |
| `onClose` | - | Called when the alert is dismissed |
| `size` | `md` | max-width of the alert (`xs` sm md lg xl 2xl 3xl 4xl 5xl) |
| **AlertTitle** extends Headless UI `<DialogTitle>` |
| **AlertDescription** extends Headless UI `<Description>` |
| **AlertBody** extends `<div>` |
| **AlertActions** extends `<div>` |

## Basic example

```tsx
import { Alert, AlertActions, AlertDescription, AlertTitle } from '@/components/alert'
import { Button } from '@/components/button'
import { useState } from 'react'

function Example() {
  let [isOpen, setIsOpen] = useState(false)
  return (
    <>
      <Button onClick={() => setIsOpen(true)}>Refund payment</Button>
      <Alert open={isOpen} onClose={setIsOpen}>
        <AlertTitle>Are you sure you want to refund this payment?</AlertTitle>
        <AlertDescription>
          The refund will be reflected in the customer’s bank account 2 to 3 business days after processing.
        </AlertDescription>
        <AlertActions>
          <Button plain onClick={() => setIsOpen(false)}>Cancel</Button>
          <Button onClick={() => setIsOpen(false)}>Refund</Button>
        </AlertActions>
      </Alert>
    </>
  )
}
```

## With body (password confirmation)

```tsx
<Alert open={isOpen} onClose={setIsOpen} size="sm">
  <AlertTitle>Verification required</AlertTitle>
  <AlertDescription>To continue, please enter your password.</AlertDescription>
  <AlertBody>
    <Input autoFocus name="password" type="password" aria-label="Password" placeholder="•••••••" />
  </AlertBody>
  <AlertActions>
    <Button plain onClick={() => setIsOpen(false)}>Cancel</Button>
    <Button onClick={() => setIsOpen(false)}>Continue</Button>
  </AlertActions>
</Alert>
```
