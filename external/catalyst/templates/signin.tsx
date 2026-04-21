'use client'

// Catalyst-aesthetic sign-in template using AuthLayout + Field primitives.

import { AuthLayout } from '../components/auth-layout'
import { Fieldset, FieldGroup, Field, Label } from '../components/fieldset'
import { Input } from '../components/input'
import { Button } from '../components/button'
import { Heading } from '../components/heading'
import { Text } from '../components/text'
import { Link } from '../components/link'

export default function SignInTemplate() {
  return (
    <AuthLayout>
      <form className="grid w-full max-w-sm grid-cols-1 gap-8">
        <Heading>Sign in to your account</Heading>
        <Fieldset>
          <FieldGroup>
            <Field>
              <Label>Email</Label>
              <Input type="email" name="email" />
            </Field>
            <Field>
              <Label>Password</Label>
              <Input type="password" name="password" />
            </Field>
          </FieldGroup>
        </Fieldset>
        <Button color="indigo" type="submit">Sign in</Button>
        <Text>
          Don't have an account? <Link href="#">Sign up</Link>.
        </Text>
      </form>
    </AuthLayout>
  )
}
