'use client'

// Catalyst-aesthetic settings page template.
// Uses Fieldset + Input + Button primitives from ./components.

import { Fieldset, Legend, Label, Description, FieldGroup, Field } from '../components/fieldset'
import { Input } from '../components/input'
import { Button } from '../components/button'
import { Heading } from '../components/heading'
import { Divider } from '../components/divider'

export default function SettingsTemplate() {
  return (
    <div className="mx-auto max-w-3xl p-6">
      <Heading>Account settings</Heading>
      <Divider className="my-8" />
      <form className="space-y-10">
        <Fieldset>
          <Legend>Profile</Legend>
          <FieldGroup>
            <Field>
              <Label>Name</Label>
              <Input name="name" defaultValue="Regan Cooney" />
            </Field>
            <Field>
              <Label>Email</Label>
              <Description>Used for workspace notifications.</Description>
              <Input name="email" type="email" defaultValue="regacooney@gmail.com" />
            </Field>
          </FieldGroup>
        </Fieldset>
        <div className="flex justify-end gap-3">
          <Button plain>Cancel</Button>
          <Button color="indigo">Save</Button>
        </div>
      </form>
    </div>
  )
}
