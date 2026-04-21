import type { Meta } from 'storybook-solidjs-vite'

const meta: Meta = {
  title: 'Typography / DisplayValue',
}

export default meta

export { App as basic } from './basic'
export { App as withFormatting } from './with-formatting'
export { App as withNoValue } from './with-no-value'
