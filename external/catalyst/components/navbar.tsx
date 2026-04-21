// Catalyst-style Navbar — recreated from https://catalyst.tailwindui.com/docs/navbar
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { forwardRef } from 'react'
import { Link } from './link'
import { TouchTarget } from './button'

export function Navbar({ className, ...props }: React.ComponentPropsWithoutRef<'nav'>) {
  return <nav {...props} className={clsx(className, 'flex flex-1 items-center gap-4 py-2.5')} />
}
export function NavbarDivider({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) {
  return <div aria-hidden="true" {...props} className={clsx(className, 'h-6 w-px bg-zinc-950/10 dark:bg-white/10')} />
}
export function NavbarSection({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) {
  return <div {...props} className={clsx(className, 'flex items-center gap-3')} />
}
export function NavbarSpacer({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) {
  return <div aria-hidden="true" {...props} className={clsx(className, '-ml-4 flex-1')} />
}
export function NavbarLabel({ className, ...props }: React.ComponentPropsWithoutRef<'span'>) {
  return <span {...props} className={clsx(className, 'truncate')} />
}

type NavbarItemProps = { current?: boolean; className?: string; children: React.ReactNode } & (Omit<Headless.ButtonProps, 'className' | 'children'> | Omit<React.ComponentPropsWithoutRef<typeof Link>, 'className' | 'children'>)

export const NavbarItem = forwardRef(function NavbarItem({ current, className, children, ...props }: NavbarItemProps, ref: React.ForwardedRef<HTMLElement>) {
  const classes = clsx(
    className,
    'relative flex min-w-0 items-center gap-3 rounded-lg p-2 text-left text-base/6 font-medium text-zinc-950 sm:text-sm/5',
    'data-hover:bg-zinc-950/5 data-active:bg-zinc-950/5',
    'dark:text-white dark:data-hover:bg-white/5 dark:data-active:bg-white/5',
    '*:data-[slot=icon]:size-6 *:data-[slot=icon]:shrink-0 *:data-[slot=icon]:fill-zinc-500 sm:*:data-[slot=icon]:size-5',
    'data-current:*:data-[slot=icon]:fill-zinc-950 dark:data-current:*:data-[slot=icon]:fill-white',
    '*:last-data-[slot=avatar]:ml-0.5 *:last-data-[slot=avatar]:*:size-6 sm:*:last-data-[slot=avatar]:*:size-5',
  )
  return (
    <span className={clsx('relative', current && 'before:absolute before:inset-x-2 before:-bottom-2.5 before:h-0.5 before:rounded-full before:bg-zinc-950 dark:before:bg-white')}>
      {'href' in props ? (
        <Link {...(props as React.ComponentPropsWithoutRef<typeof Link>)} className={classes} data-current={current ? 'true' : undefined} ref={ref as React.ForwardedRef<HTMLAnchorElement>}>
          <TouchTarget>{children}</TouchTarget>
        </Link>
      ) : (
        <Headless.Button {...(props as Headless.ButtonProps)} className={clsx('cursor-default', classes)} data-current={current ? 'true' : undefined} ref={ref as React.ForwardedRef<HTMLButtonElement>}>
          <TouchTarget>{children}</TouchTarget>
        </Headless.Button>
      )}
    </span>
  )
})
