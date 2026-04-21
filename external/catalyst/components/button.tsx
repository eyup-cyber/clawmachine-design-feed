// Catalyst-style Button — recreated from the scraped API at
// https://catalyst.tailwindui.com/docs/button
// Requires: @headlessui/react, clsx (or equivalent).

import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { forwardRef } from 'react'
import { Link } from './link'

type ButtonColor =
  | 'dark/zinc'
  | 'light'
  | 'dark/white'
  | 'dark' | 'zinc' | 'white'
  | 'red' | 'orange' | 'amber' | 'yellow'
  | 'lime' | 'green' | 'emerald' | 'teal'
  | 'cyan' | 'sky' | 'blue' | 'indigo'
  | 'violet' | 'purple' | 'fuchsia' | 'pink' | 'rose'

// Per-color class maps — solid filled variants in the Tailwind Labs palette.
// Selected pairs keep 4.5:1 contrast in both light and dark.
const solidStyles: Record<string, string> = {
  'dark/zinc':
    'text-white [--btn-bg:var(--color-zinc-900)] [--btn-border:var(--color-zinc-950)]/90 [--btn-hover-overlay:var(--color-white)]/10 dark:text-white dark:[--btn-bg:var(--color-zinc-600)] dark:[--btn-hover-overlay:var(--color-white)]/5',
  light:
    'text-zinc-950 [--btn-bg:white] [--btn-border:var(--color-zinc-950)]/10 [--btn-hover-overlay:var(--color-zinc-950)]/2.5 dark:text-white dark:[--btn-bg:var(--color-zinc-800)] dark:[--btn-hover-overlay:var(--color-white)]/5',
  'dark/white':
    'text-white [--btn-bg:var(--color-zinc-900)] [--btn-border:var(--color-zinc-950)]/90 [--btn-hover-overlay:var(--color-white)]/10 dark:text-zinc-950 dark:[--btn-bg:white] dark:[--btn-hover-overlay:var(--color-zinc-950)]/5',
  dark:   'text-white [--btn-bg:var(--color-zinc-900)] [--btn-border:var(--color-zinc-950)]/90 [--btn-hover-overlay:var(--color-white)]/10',
  white:  'text-zinc-950 [--btn-bg:white] [--btn-border:var(--color-zinc-950)]/10 [--btn-hover-overlay:var(--color-zinc-950)]/2.5',
  zinc:   'text-white [--btn-bg:var(--color-zinc-600)] [--btn-border:var(--color-zinc-700)]/90 [--btn-hover-overlay:var(--color-white)]/10',
  red:    'text-white [--btn-bg:var(--color-red-600)]',
  orange: 'text-white [--btn-bg:var(--color-orange-500)]',
  amber:  'text-amber-950 [--btn-bg:var(--color-amber-400)]',
  yellow: 'text-yellow-950 [--btn-bg:var(--color-yellow-300)]',
  lime:   'text-lime-950 [--btn-bg:var(--color-lime-300)]',
  green:  'text-white [--btn-bg:var(--color-green-600)]',
  emerald:'text-white [--btn-bg:var(--color-emerald-600)]',
  teal:   'text-white [--btn-bg:var(--color-teal-600)]',
  cyan:   'text-cyan-950 [--btn-bg:var(--color-cyan-300)]',
  sky:    'text-white [--btn-bg:var(--color-sky-500)]',
  blue:   'text-white [--btn-bg:var(--color-blue-600)]',
  indigo: 'text-white [--btn-bg:var(--color-indigo-500)]',
  violet: 'text-white [--btn-bg:var(--color-violet-500)]',
  purple: 'text-white [--btn-bg:var(--color-purple-500)]',
  fuchsia:'text-white [--btn-bg:var(--color-fuchsia-500)]',
  pink:   'text-white [--btn-bg:var(--color-pink-500)]',
  rose:   'text-white [--btn-bg:var(--color-rose-500)]',
}

const base = [
  // Layout
  'relative isolate inline-flex items-baseline justify-center gap-x-2 rounded-lg border text-base/6 font-semibold',
  // Sizing
  'px-[calc(--spacing(3.5)-1px)] py-[calc(--spacing(2.5)-1px)] sm:px-[calc(--spacing(3)-1px)] sm:py-[calc(--spacing(1.5)-1px)] sm:text-sm/6',
  // Focus
  'focus:not-data-focus:outline-hidden data-focus:outline-2 data-focus:outline-offset-2 data-focus:outline-blue-500',
  // Disabled
  'data-disabled:opacity-50',
  // Icon
  '*:data-[slot=icon]:-mx-0.5 *:data-[slot=icon]:my-0.5 *:data-[slot=icon]:size-5 *:data-[slot=icon]:shrink-0 *:data-[slot=icon]:self-center *:data-[slot=icon]:text-(--btn-icon) sm:*:data-[slot=icon]:my-1 sm:*:data-[slot=icon]:size-4',
].join(' ')

const solid = [
  'border-transparent bg-(--btn-border)',
  'before:absolute before:inset-0 before:-z-10 before:rounded-[calc(var(--radius-lg)-1px)] before:bg-(--btn-bg) before:shadow-sm',
  'after:absolute after:inset-0 after:-z-10 after:rounded-[calc(var(--radius-lg)-1px)] after:shadow-[shadow:inset_0_1px_--theme(--color-white/15%)]',
  'after:data-active:bg-(--btn-hover-overlay) after:data-hover:bg-(--btn-hover-overlay)',
  'data-disabled:before:shadow-none data-disabled:after:shadow-none',
].join(' ')

const outline = [
  'border-zinc-950/10 text-zinc-950 data-active:bg-zinc-950/2.5 data-hover:bg-zinc-950/2.5',
  'dark:border-white/15 dark:text-white dark:[--btn-bg:transparent] dark:data-active:bg-white/5 dark:data-hover:bg-white/5',
  '*:data-[slot=icon]:text-zinc-500 data-hover:*:data-[slot=icon]:text-zinc-700 dark:*:data-[slot=icon]:text-zinc-400 dark:data-hover:*:data-[slot=icon]:text-zinc-300',
].join(' ')

const plain = [
  'border-transparent text-zinc-950 data-active:bg-zinc-950/5 data-hover:bg-zinc-950/5',
  'dark:text-white dark:data-active:bg-white/10 dark:data-hover:bg-white/10',
  '*:data-[slot=icon]:text-zinc-500 data-hover:*:data-[slot=icon]:text-zinc-700 dark:*:data-[slot=icon]:text-zinc-400 dark:data-hover:*:data-[slot=icon]:text-zinc-300',
].join(' ')

type ButtonOwnProps = {
  color?: ButtonColor
  outline?: boolean
  plain?: boolean
  className?: string
  children: React.ReactNode
}

type ButtonProps = ButtonOwnProps &
  (Omit<Headless.ButtonProps, 'className' | 'as' | 'children'> | Omit<React.ComponentPropsWithoutRef<typeof Link>, 'className' | 'children'>)

export const Button = forwardRef(function Button(
  { color, outline: isOutline, plain: isPlain, className, children, ...props }: ButtonProps,
  ref: React.ForwardedRef<HTMLElement>
) {
  const variant = clsx(
    base,
    isOutline
      ? outline
      : isPlain
        ? plain
        : clsx(solid, solidStyles[color ?? 'dark/zinc']),
    className
  )
  return 'href' in props ? (
    <Link {...(props as React.ComponentPropsWithoutRef<typeof Link>)} className={variant} ref={ref as React.ForwardedRef<HTMLAnchorElement>}>
      <TouchTarget>{children}</TouchTarget>
    </Link>
  ) : (
    <Headless.Button
      {...(props as Headless.ButtonProps)}
      className={clsx(variant, 'cursor-default')}
      ref={ref as React.ForwardedRef<HTMLButtonElement>}
    >
      <TouchTarget>{children}</TouchTarget>
    </Headless.Button>
  )
})

// Expands the hit target to a minimum 44×44px per WCAG on touch.
export function TouchTarget({ children }: { children: React.ReactNode }) {
  return (
    <>
      <span className="absolute top-1/2 left-1/2 size-[max(100%,2.75rem)] -translate-x-1/2 -translate-y-1/2 [@media(pointer:fine)]:hidden" aria-hidden="true" />
      {children}
    </>
  )
}
