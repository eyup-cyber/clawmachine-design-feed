// Catalyst-style Dropdown (Menu) — recreated from https://catalyst.tailwindui.com/docs/dropdown
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React from 'react'
import { Button } from './button'
import { Link } from './link'

export function Dropdown(props: Headless.MenuProps) { return <Headless.Menu {...props} /> }

export function DropdownButton<T extends React.ElementType = typeof Button>({ as = Button as T, ...props }: { as?: T } & Omit<React.ComponentPropsWithoutRef<T>, 'as'>) {
  return <Headless.MenuButton as={as} {...(props as any)} />
}

export function DropdownMenu({ anchor = 'bottom', className, ...props }: { anchor?: string; className?: string } & Omit<Headless.MenuItemsProps, 'as' | 'className'>) {
  return (
    <Headless.MenuItems
      transition
      anchor={anchor as any}
      {...props}
      className={clsx(
        className,
        'isolate w-max rounded-xl p-1',
        'outline outline-1 outline-transparent focus:outline-hidden',
        'overflow-y-auto',
        'bg-white/75 ring-1 ring-zinc-950/10 backdrop-blur-xl dark:bg-zinc-800/75 dark:ring-white/10',
        'shadow-lg',
        'supports-[grid-template-columns:subgrid]:grid supports-[grid-template-columns:subgrid]:grid-cols-[auto_1fr_1.5rem_0.5rem_auto]',
        'transition data-closed:data-leave:opacity-0 data-leave:duration-100 data-leave:ease-in',
      )}
    />
  )
}

export function DropdownItem({ className, ...props }: { className?: string; href?: string } & Omit<Headless.MenuItemProps<'button'>, 'as' | 'className'>) {
  const classes = clsx(
    className,
    'group cursor-default rounded-lg px-3.5 py-2.5 focus:outline-hidden sm:px-3 sm:py-1.5',
    'text-left text-base/6 text-zinc-950 sm:text-sm/6 dark:text-white',
    'data-focus:bg-blue-500 data-focus:text-white',
    'data-disabled:opacity-50',
    'forced-color-adjust-none forced-colors:text-[CanvasText] forced-colors:data-focus:bg-[Highlight] forced-colors:data-focus:text-[HighlightText] forced-colors:data-focus:*:data-[slot=icon]:text-[HighlightText]',
    'col-span-full grid grid-cols-[auto_1fr_1.5rem_0.5rem_auto] items-center supports-[grid-template-columns:subgrid]:grid-cols-subgrid',
    '*:data-[slot=icon]:col-start-1 *:data-[slot=icon]:row-start-1 *:data-[slot=icon]:-ml-0.5 *:data-[slot=icon]:mr-2.5 *:data-[slot=icon]:size-5 sm:*:data-[slot=icon]:mr-2 sm:*:data-[slot=icon]:size-4',
    '*:data-[slot=icon]:text-zinc-500 data-focus:*:data-[slot=icon]:text-white dark:*:data-[slot=icon]:text-zinc-400 dark:data-focus:*:data-[slot=icon]:text-white',
  )
  return 'href' in props ? (
    <Headless.MenuItem as={Link} {...(props as any)} className={classes} />
  ) : (
    <Headless.MenuItem as="button" type="button" {...(props as Headless.MenuItemProps<'button'>)} className={classes} />
  )
}

export function DropdownHeader({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) {
  return <div {...props} className={clsx(className, 'col-span-5 px-3.5 pt-2.5 pb-1 sm:px-3')} />
}

export function DropdownSection({ className, ...props }: Omit<Headless.MenuSectionProps, 'as' | 'className'> & { className?: string }) {
  return <Headless.MenuSection {...props} className={clsx(className, 'col-span-full supports-[grid-template-columns:subgrid]:grid supports-[grid-template-columns:subgrid]:grid-cols-[auto_1fr_1.5rem_0.5rem_auto]')} />
}

export function DropdownHeading({ className, ...props }: Omit<Headless.MenuHeadingProps, 'as' | 'className'> & { className?: string }) {
  return <Headless.MenuHeading {...props} className={clsx(className, 'col-span-full grid grid-cols-[1fr_auto] gap-x-12 px-3.5 pt-2 pb-1 text-sm/5 font-medium text-zinc-500 sm:px-3 sm:text-xs/5 dark:text-zinc-400')} />
}

export function DropdownDivider({ className, ...props }: Omit<Headless.MenuSeparatorProps, 'as' | 'className'> & { className?: string }) {
  return <Headless.MenuSeparator {...props} className={clsx(className, 'col-span-full mx-3.5 my-1 h-px border-0 bg-zinc-950/5 sm:mx-3 dark:bg-white/10 forced-colors:bg-[CanvasText]')} />
}

export function DropdownLabel({ className, ...props }: Omit<Headless.LabelProps, 'as' | 'className'> & { className?: string }) {
  return <Headless.Label {...props} data-slot="label" className={clsx(className, 'col-start-2 row-start-1')} {...props} />
}

export function DropdownDescription({ className, ...props }: Omit<Headless.DescriptionProps, 'as' | 'className'> & { className?: string }) {
  return <Headless.Description data-slot="description" {...props} className={clsx(className, 'col-span-2 col-start-2 row-start-2 text-sm/5 text-zinc-500 group-data-focus:text-white sm:text-xs/5 dark:text-zinc-400 forced-colors:group-data-focus:text-[HighlightText]')} />
}

export function DropdownShortcut({ keys, className, ...props }: { keys: string | string[]; className?: string } & Omit<Headless.DescriptionProps, 'as' | 'className' | 'children'>) {
  return <Headless.Description as="kbd" {...props} className={clsx(className, 'col-start-5 row-start-1 flex justify-self-end')}>
    {(Array.isArray(keys) ? keys : keys.split('')).map((ch, i) => (
      <kbd key={i} className={clsx(['min-w-[2ch] text-center font-sans text-zinc-400 capitalize group-data-focus:text-white forced-colors:group-data-focus:text-[HighlightText]', i > 0 && ch.length > 1 && 'pl-1'])}>{ch}</kbd>
    ))}
  </Headless.Description>
}
