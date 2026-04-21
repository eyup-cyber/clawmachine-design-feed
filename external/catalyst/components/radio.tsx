// Catalyst-style Radio + RadioField + RadioGroup — recreated from
// https://catalyst.tailwindui.com/docs/radio
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { forwardRef } from 'react'

export function RadioGroup({ className, ...props }: Omit<Headless.RadioGroupProps, 'as' | 'className'> & { className?: string }) {
  return <Headless.RadioGroup data-slot="control" {...props} className={clsx(className, 'space-y-3 **:data-[slot=label]:font-normal has-data-[slot=description]:space-y-6 has-data-[slot=description]:**:data-[slot=label]:font-medium')} />
}

export function RadioField({ className, ...props }: Omit<Headless.FieldProps, 'className'> & { className?: string }) {
  return <Headless.Field data-slot="field" {...props} className={clsx(className, 'grid grid-cols-[1.125rem_1fr] items-center gap-x-4 gap-y-1 sm:grid-cols-[1rem_1fr]', '*:data-[slot=control]:col-start-1 *:data-[slot=control]:row-start-1 *:data-[slot=control]:justify-self-center', '*:data-[slot=label]:col-start-2 *:data-[slot=label]:row-start-1 *:data-[slot=label]:justify-self-start', '*:data-[slot=description]:col-start-2 *:data-[slot=description]:row-start-2', '*:data-[slot=label]:select-none *:data-[slot=label]:text-base/6 *:data-[slot=label]:sm:text-sm/5')} />
}

type RadioColor = 'dark/zinc' | 'dark/white' | 'white' | 'dark' | 'zinc' | 'red' | 'orange' | 'amber' | 'yellow' | 'lime' | 'green' | 'emerald' | 'teal' | 'cyan' | 'sky' | 'blue' | 'indigo' | 'violet' | 'purple' | 'fuchsia' | 'pink' | 'rose'

const dotColors: Record<string, string> = {
  'dark/zinc': '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-zinc-900)]',
  'dark/white':'[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-zinc-900)] dark:[--radio-indicator:var(--color-zinc-900)] dark:[--radio-bg:var(--color-white)]',
  dark:  '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-zinc-900)]',
  white: '[--radio-indicator:var(--color-zinc-900)] [--radio-bg:var(--color-white)]',
  zinc:  '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-zinc-600)]',
  red:   '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-red-600)]',
  orange:'[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-orange-500)]',
  amber: '[--radio-indicator:var(--color-amber-950)] [--radio-bg:var(--color-amber-400)]',
  yellow:'[--radio-indicator:var(--color-yellow-950)] [--radio-bg:var(--color-yellow-300)]',
  lime:  '[--radio-indicator:var(--color-lime-950)] [--radio-bg:var(--color-lime-300)]',
  green: '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-green-600)]',
  emerald:'[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-emerald-600)]',
  teal:  '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-teal-600)]',
  cyan:  '[--radio-indicator:var(--color-cyan-950)] [--radio-bg:var(--color-cyan-300)]',
  sky:   '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-sky-500)]',
  blue:  '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-blue-600)]',
  indigo:'[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-indigo-500)]',
  violet:'[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-violet-500)]',
  purple:'[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-purple-500)]',
  fuchsia:'[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-fuchsia-500)]',
  pink:  '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-pink-500)]',
  rose:  '[--radio-indicator:var(--color-white)] [--radio-bg:var(--color-rose-500)]',
}

type RadioProps = { className?: string; color?: RadioColor } & Omit<Headless.RadioProps, 'as' | 'className' | 'children'>

export const Radio = forwardRef(function Radio({ className, color = 'dark/zinc', ...props }: RadioProps, ref: React.ForwardedRef<HTMLSpanElement>) {
  return (
    <Headless.Radio data-slot="control" ref={ref} {...props} className={clsx(className, 'group inline-flex focus:outline-hidden')}>
      <span className={clsx(
        'relative isolate flex size-4.5 items-center justify-center rounded-full sm:size-4',
        'before:absolute before:inset-0 before:-z-10 before:rounded-full before:bg-white before:shadow-sm dark:before:hidden',
        'dark:bg-white/5 dark:group-data-checked:bg-(--radio-bg)',
        'border border-zinc-950/15 group-data-checked:border-transparent group-data-hover:border-zinc-950/30 group-data-checked:bg-(--radio-bg)',
        'dark:border-white/15 dark:group-data-hover:border-white/30 dark:group-data-checked:border-white/5',
        dotColors[color],
      )}>
        <span className="size-full rounded-full border-[4.5px] border-transparent bg-(--radio-indicator) bg-clip-padding opacity-0 group-data-checked:opacity-100 sm:border-[3.5px] forced-colors:border-[Canvas] forced-colors:group-data-checked:border-[Highlight]" />
      </span>
    </Headless.Radio>
  )
})
