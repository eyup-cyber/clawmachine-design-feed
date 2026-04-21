// Catalyst-style Checkbox + CheckboxField + CheckboxGroup — recreated from
// https://catalyst.tailwindui.com/docs/checkbox
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { forwardRef } from 'react'

export function CheckboxGroup({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) {
  return <div data-slot="control" {...props} className={clsx(className, 'space-y-3 **:data-[slot=label]:font-normal has-data-[slot=description]:space-y-6 has-data-[slot=description]:**:data-[slot=label]:font-medium')} />
}

export function CheckboxField({ className, ...props }: Omit<Headless.FieldProps, 'className'> & { className?: string }) {
  return <Headless.Field data-slot="field" {...props} className={clsx(className, 'grid grid-cols-[1.125rem_1fr] items-center gap-x-4 gap-y-1 sm:grid-cols-[1rem_1fr]', '*:data-[slot=control]:col-start-1 *:data-[slot=control]:row-start-1 *:data-[slot=control]:justify-self-center', '*:data-[slot=label]:col-start-2 *:data-[slot=label]:row-start-1 *:data-[slot=label]:justify-self-start', '*:data-[slot=description]:col-start-2 *:data-[slot=description]:row-start-2', 'has-data-[slot=description]:**:data-[slot=label]:font-medium', '*:data-[slot=label]:select-none *:data-[slot=label]:sm:text-sm/5 *:data-[slot=label]:text-base/6')} />
}

type CheckboxColor = 'dark/zinc' | 'dark/white' | 'white' | 'dark' | 'zinc' | 'red' | 'orange' | 'amber' | 'yellow' | 'lime' | 'green' | 'emerald' | 'teal' | 'cyan' | 'sky' | 'blue' | 'indigo' | 'violet' | 'purple' | 'fuchsia' | 'pink' | 'rose'

const boxColors: Record<string, string> = {
  'dark/zinc': '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-zinc-900)] [--checkbox-checked-border:var(--color-zinc-950)]/90',
  'dark/white': '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-zinc-900)] [--checkbox-checked-border:var(--color-zinc-950)]/90 dark:[--checkbox-check:var(--color-zinc-900)] dark:[--checkbox-checked-bg:var(--color-white)] dark:[--checkbox-checked-border:var(--color-zinc-950)]/15',
  white: '[--checkbox-check:var(--color-zinc-900)] [--checkbox-checked-bg:var(--color-white)] [--checkbox-checked-border:var(--color-zinc-950)]/15',
  dark:  '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-zinc-900)] [--checkbox-checked-border:var(--color-zinc-950)]/90',
  zinc:  '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-zinc-600)] [--checkbox-checked-border:var(--color-zinc-700)]/90',
  red:   '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-red-600)] [--checkbox-checked-border:var(--color-red-700)]/90',
  orange:'[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-orange-500)] [--checkbox-checked-border:var(--color-orange-600)]/90',
  amber: '[--checkbox-check:var(--color-amber-950)] [--checkbox-checked-bg:var(--color-amber-400)] [--checkbox-checked-border:var(--color-amber-500)]/80',
  yellow:'[--checkbox-check:var(--color-yellow-950)] [--checkbox-checked-bg:var(--color-yellow-300)] [--checkbox-checked-border:var(--color-yellow-400)]/80',
  lime:  '[--checkbox-check:var(--color-lime-950)] [--checkbox-checked-bg:var(--color-lime-300)] [--checkbox-checked-border:var(--color-lime-400)]/80',
  green: '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-green-600)] [--checkbox-checked-border:var(--color-green-700)]/90',
  emerald:'[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-emerald-600)] [--checkbox-checked-border:var(--color-emerald-700)]/90',
  teal:  '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-teal-600)] [--checkbox-checked-border:var(--color-teal-700)]/90',
  cyan:  '[--checkbox-check:var(--color-cyan-950)] [--checkbox-checked-bg:var(--color-cyan-300)] [--checkbox-checked-border:var(--color-cyan-400)]/80',
  sky:   '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-sky-500)] [--checkbox-checked-border:var(--color-sky-600)]/80',
  blue:  '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-blue-600)] [--checkbox-checked-border:var(--color-blue-700)]/90',
  indigo:'[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-indigo-500)] [--checkbox-checked-border:var(--color-indigo-600)]/90',
  violet:'[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-violet-500)] [--checkbox-checked-border:var(--color-violet-600)]/90',
  purple:'[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-purple-500)] [--checkbox-checked-border:var(--color-purple-600)]/90',
  fuchsia:'[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-fuchsia-500)] [--checkbox-checked-border:var(--color-fuchsia-600)]/90',
  pink:  '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-pink-500)] [--checkbox-checked-border:var(--color-pink-600)]/90',
  rose:  '[--checkbox-check:var(--color-white)] [--checkbox-checked-bg:var(--color-rose-500)] [--checkbox-checked-border:var(--color-rose-600)]/90',
}

type CheckboxProps = { className?: string; color?: CheckboxColor; indeterminate?: boolean } & Omit<Headless.CheckboxProps, 'as' | 'className' | 'children'>

export const Checkbox = forwardRef(function Checkbox({ className, color = 'dark/zinc', ...props }: CheckboxProps, ref: React.ForwardedRef<HTMLSpanElement>) {
  return (
    <Headless.Checkbox
      data-slot="control"
      ref={ref}
      {...props}
      className={clsx(className, 'group inline-flex focus:outline-hidden')}
    >
      <span className={clsx(
        'relative isolate flex size-4.5 items-center justify-center rounded-[0.3125rem] sm:size-4',
        'before:absolute before:inset-0 before:-z-10 before:rounded-[calc(0.3125rem-1px)] before:bg-white before:shadow-sm',
        'dark:before:hidden',
        'dark:bg-white/5 dark:group-data-checked:bg-(--checkbox-checked-bg)',
        'border border-zinc-950/15 group-data-checked:border-transparent group-data-checked:group-data-hover:border-transparent group-data-hover:border-zinc-950/30 group-data-checked:bg-(--checkbox-checked-bg)',
        'dark:border-white/15 dark:group-data-hover:border-white/30 dark:group-data-checked:border-white/5',
        boxColors[color],
      )}>
        <svg className="size-4 stroke-(--checkbox-check) opacity-0 group-data-checked:opacity-100 sm:h-3.5 sm:w-3.5" viewBox="0 0 14 14" fill="none">
          <path className="opacity-100 group-data-indeterminate:opacity-0" d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
          <path className="opacity-0 group-data-indeterminate:opacity-100" d="M3 7H11" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </span>
    </Headless.Checkbox>
  )
})
