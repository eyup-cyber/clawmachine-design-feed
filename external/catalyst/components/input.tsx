// Catalyst-style Input + InputGroup — recreated from the scraped API at
// https://catalyst.tailwindui.com/docs/input
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { forwardRef } from 'react'

const DATE_TYPES = ['date', 'datetime-local', 'month', 'time', 'week']

export function InputGroup({ children }: React.PropsWithChildren) {
  return (
    <span data-slot="control" className={clsx(
      'relative isolate block',
      '*:data-[slot=icon]:pointer-events-none *:data-[slot=icon]:absolute *:data-[slot=icon]:top-3 *:data-[slot=icon]:z-10 *:data-[slot=icon]:size-5 sm:*:data-[slot=icon]:top-2.5 sm:*:data-[slot=icon]:size-4',
      '*:data-[slot=icon]:first:left-3 *:data-[slot=icon]:last:right-3 sm:*:data-[slot=icon]:first:left-2.5 sm:*:data-[slot=icon]:last:right-2.5',
      '*:data-[slot=icon]:text-zinc-500 dark:*:data-[slot=icon]:text-zinc-400',
      '[&>[data-slot=control]:has(+[data-slot=icon])]:pr-10 [&>[data-slot=icon]+[data-slot=control]]:pl-10 sm:[&>[data-slot=control]:has(+[data-slot=icon])]:pr-8 sm:[&>[data-slot=icon]+[data-slot=control]]:pl-8',
    )}>
      {children}
    </span>
  )
}

type InputProps = { className?: string; type?: React.InputHTMLAttributes<HTMLInputElement>['type'] } & Omit<Headless.InputProps, 'as' | 'className'>

export const Input = forwardRef(function Input({ className, ...props }: InputProps, ref: React.ForwardedRef<HTMLInputElement>) {
  return (
    <span data-slot="control" className={clsx(
      className,
      'relative block w-full',
      'before:absolute before:inset-px before:rounded-[calc(var(--radius-lg)-1px)] before:bg-white before:shadow-sm',
      'dark:before:hidden',
      'after:pointer-events-none after:absolute after:inset-0 after:rounded-lg after:ring-transparent after:ring-inset sm:focus-within:after:ring-2 sm:focus-within:after:ring-blue-500',
      'has-data-invalid:before:shadow-red-500/10',
    )}>
      <Headless.Input
        ref={ref}
        {...props}
        className={clsx(
          'relative block w-full appearance-none rounded-lg px-[calc(--spacing(3.5)-1px)] py-[calc(--spacing(2.5)-1px)] sm:px-[calc(--spacing(3)-1px)] sm:py-[calc(--spacing(1.5)-1px)]',
          'text-base/6 text-zinc-950 placeholder:text-zinc-500 sm:text-sm/6 dark:text-white',
          'border border-zinc-950/10 data-hover:border-zinc-950/20 dark:border-white/10 dark:data-hover:border-white/20',
          'bg-transparent dark:bg-white/5',
          'focus:outline-hidden',
          'data-invalid:border-red-500 data-invalid:data-hover:border-red-500 dark:data-invalid:border-red-500 dark:data-invalid:data-hover:border-red-500',
          'data-disabled:border-zinc-950/20 dark:data-disabled:border-white/15 dark:data-disabled:bg-white/2.5 data-disabled:data-hover:data-disabled:border-zinc-950/20',
          props.type && DATE_TYPES.includes(props.type) && '[&::-webkit-datetime-edit-fields-wrapper]:p-0 [&::-webkit-date-and-time-value]:min-h-[1.5em] [&::-webkit-datetime-edit]:inline-flex [&::-webkit-datetime-edit]:p-0',
        )}
      />
    </span>
  )
})
