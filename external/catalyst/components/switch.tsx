// Catalyst-style Switch + SwitchField + SwitchGroup — recreated from
// https://catalyst.tailwindui.com/docs/switch
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { forwardRef } from 'react'

export function SwitchGroup({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) {
  return <div data-slot="control" {...props} className={clsx(className, 'space-y-3 **:data-[slot=label]:font-normal has-data-[slot=description]:space-y-6 has-data-[slot=description]:**:data-[slot=label]:font-medium')} />
}

export function SwitchField({ className, ...props }: Omit<Headless.FieldProps, 'className'> & { className?: string }) {
  return <Headless.Field data-slot="field" {...props} className={clsx(className, 'grid grid-cols-[1fr_auto] items-center gap-x-4 gap-y-1 sm:grid-cols-[1fr_auto] [&>*:last-child]:justify-self-end', '*:data-[slot=label]:col-start-1 *:data-[slot=label]:row-start-1', '*:data-[slot=description]:col-start-1 *:data-[slot=description]:row-start-2', '*:data-[slot=control]:col-start-2 *:data-[slot=control]:row-span-2', '*:data-[slot=label]:text-base/6 *:data-[slot=label]:select-none *:data-[slot=label]:sm:text-sm/5')} />
}

type SwitchColor = 'dark/zinc' | 'dark/white' | 'dark' | 'zinc' | 'white' | 'red' | 'orange' | 'amber' | 'yellow' | 'lime' | 'green' | 'emerald' | 'teal' | 'cyan' | 'sky' | 'blue' | 'indigo' | 'violet' | 'purple' | 'fuchsia' | 'pink' | 'rose'

const switchColors: Record<string, string> = {
  'dark/zinc': '[--switch-bg:var(--color-zinc-900)] [--switch:var(--color-white)] dark:[--switch-bg:var(--color-zinc-600)] dark:[--switch-bg-ring:transparent]',
  'dark/white': '[--switch-bg:var(--color-zinc-900)] [--switch:var(--color-white)] dark:[--switch-bg:var(--color-white)] dark:[--switch:var(--color-zinc-900)]',
  dark:  '[--switch-bg:var(--color-zinc-900)] [--switch:var(--color-white)]',
  zinc:  '[--switch-bg:var(--color-zinc-600)] [--switch:var(--color-white)]',
  white: '[--switch-bg:var(--color-white)] [--switch:var(--color-zinc-900)] [--switch-bg-ring:var(--color-zinc-950)]/15',
  red:   '[--switch-bg:var(--color-red-600)] [--switch:var(--color-white)]',
  orange:'[--switch-bg:var(--color-orange-500)] [--switch:var(--color-white)]',
  amber: '[--switch-bg:var(--color-amber-400)] [--switch:var(--color-amber-950)]',
  yellow:'[--switch-bg:var(--color-yellow-300)] [--switch:var(--color-yellow-950)]',
  lime:  '[--switch-bg:var(--color-lime-300)] [--switch:var(--color-lime-950)]',
  green: '[--switch-bg:var(--color-green-600)] [--switch:var(--color-white)]',
  emerald:'[--switch-bg:var(--color-emerald-600)] [--switch:var(--color-white)]',
  teal:  '[--switch-bg:var(--color-teal-600)] [--switch:var(--color-white)]',
  cyan:  '[--switch-bg:var(--color-cyan-300)] [--switch:var(--color-cyan-950)]',
  sky:   '[--switch-bg:var(--color-sky-500)] [--switch:var(--color-white)]',
  blue:  '[--switch-bg:var(--color-blue-600)] [--switch:var(--color-white)]',
  indigo:'[--switch-bg:var(--color-indigo-500)] [--switch:var(--color-white)]',
  violet:'[--switch-bg:var(--color-violet-500)] [--switch:var(--color-white)]',
  purple:'[--switch-bg:var(--color-purple-500)] [--switch:var(--color-white)]',
  fuchsia:'[--switch-bg:var(--color-fuchsia-500)] [--switch:var(--color-white)]',
  pink:  '[--switch-bg:var(--color-pink-500)] [--switch:var(--color-white)]',
  rose:  '[--switch-bg:var(--color-rose-500)] [--switch:var(--color-white)]',
}

type SwitchProps = { className?: string; color?: SwitchColor } & Omit<Headless.SwitchProps, 'as' | 'className' | 'children'>

export const Switch = forwardRef(function Switch({ className, color = 'dark/zinc', ...props }: SwitchProps, ref: React.ForwardedRef<HTMLButtonElement>) {
  return (
    <Headless.Switch
      data-slot="control"
      ref={ref}
      {...props}
      className={clsx(className, 'group relative isolate inline-flex h-6 w-10 cursor-default rounded-full p-[3px] sm:h-5 sm:w-8', switchColors[color])}
    >
      <span aria-hidden="true" className={clsx(
        'pointer-events-none relative inline-block size-[1.125rem] translate-x-0 rounded-full sm:size-3.5',
        'bg-white shadow-sm ring-1 ring-black/5 transition-transform duration-200 ease-in-out',
        'group-data-checked:translate-x-4 group-data-checked:bg-(--switch)',
        'group-data-focus:outline-none group-data-focus:ring-2 group-data-focus:ring-blue-500 group-data-focus:ring-offset-2',
        'group-not-data-checked:bg-zinc-200 dark:group-not-data-checked:bg-white/25',
      )} />
    </Headless.Switch>
  )
})
