// Catalyst-style Sidebar — recreated from https://catalyst.tailwindui.com/docs/sidebar
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { forwardRef } from 'react'
import { Link } from './link'
import { TouchTarget } from './button'

export function Sidebar({ className, ...props }: React.ComponentPropsWithoutRef<'nav'>) { return <nav {...props} className={clsx(className, 'flex h-full min-h-0 flex-col')} /> }
export function SidebarHeader({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) { return <div {...props} className={clsx(className, 'flex flex-col border-b border-zinc-950/5 p-4 dark:border-white/5 [&>[data-slot=section]+[data-slot=section]]:mt-2.5')} /> }
export function SidebarBody({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) { return <div {...props} className={clsx(className, 'flex flex-1 flex-col overflow-y-auto p-4 [&>[data-slot=section]+[data-slot=section]]:mt-8')} /> }
export function SidebarFooter({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) { return <div {...props} className={clsx(className, 'flex flex-col border-t border-zinc-950/5 p-4 dark:border-white/5 [&>[data-slot=section]+[data-slot=section]]:mt-2.5')} /> }
export function SidebarSection({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) { return <div data-slot="section" {...props} className={clsx(className, 'flex flex-col gap-0.5')} /> }
export function SidebarDivider({ className, ...props }: React.ComponentPropsWithoutRef<'hr'>) { return <hr {...props} className={clsx(className, 'my-4 border-t border-zinc-950/5 lg:-mx-4 dark:border-white/5')} /> }
export function SidebarSpacer({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) { return <div aria-hidden="true" {...props} className={clsx(className, 'mt-8 flex-1')} /> }
export function SidebarHeading({ className, ...props }: React.ComponentPropsWithoutRef<'h3'>) { return <h3 {...props} className={clsx(className, 'mb-1 px-2 text-xs/6 font-medium text-zinc-500 dark:text-zinc-400')} /> }
export function SidebarLabel({ className, ...props }: React.ComponentPropsWithoutRef<'span'>) { return <span {...props} className={clsx(className, 'truncate')} /> }

type SidebarItemProps = { current?: boolean; className?: string; children: React.ReactNode } & (Omit<Headless.ButtonProps, 'className' | 'children'> | Omit<React.ComponentPropsWithoutRef<typeof Link>, 'className' | 'children'>)
export const SidebarItem = forwardRef(function SidebarItem({ current, className, children, ...props }: SidebarItemProps, ref: React.ForwardedRef<HTMLElement>) {
  const classes = clsx(
    className,
    'flex w-full items-center gap-3 rounded-lg px-2 py-2.5 text-left text-base/6 font-medium text-zinc-950 sm:py-2 sm:text-sm/5',
    'data-hover:bg-zinc-950/5 data-active:bg-zinc-950/5',
    'dark:text-white dark:data-hover:bg-white/5 dark:data-active:bg-white/5',
    'data-current:bg-zinc-950/5 dark:data-current:bg-white/5',
    '*:data-[slot=icon]:size-6 *:data-[slot=icon]:shrink-0 *:data-[slot=icon]:fill-zinc-500 sm:*:data-[slot=icon]:size-5',
    'data-current:*:data-[slot=icon]:fill-zinc-950 dark:data-current:*:data-[slot=icon]:fill-white',
  )
  return 'href' in props ? (
    <Link {...(props as React.ComponentPropsWithoutRef<typeof Link>)} className={classes} data-current={current ? 'true' : undefined} ref={ref as React.ForwardedRef<HTMLAnchorElement>}>
      <TouchTarget>{children}</TouchTarget>
    </Link>
  ) : (
    <Headless.Button {...(props as Headless.ButtonProps)} className={clsx('cursor-default', classes)} data-current={current ? 'true' : undefined} ref={ref as React.ForwardedRef<HTMLButtonElement>}>
      <TouchTarget>{children}</TouchTarget>
    </Headless.Button>
  )
})
