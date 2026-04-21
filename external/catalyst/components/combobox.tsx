// Catalyst-style Combobox — recreated from https://catalyst.tailwindui.com/docs/combobox
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { Fragment, useState } from 'react'

export function Combobox<T>({ options, filter, displayValue, placeholder, autoFocus, 'aria-label': ariaLabel, children, className, anchor = 'bottom', ...props }: {
  className?: string; options: T[]; filter?: (o: T, q: string) => boolean; displayValue?: (o?: T | null) => string | undefined; placeholder?: string; autoFocus?: boolean; 'aria-label'?: string; children: (o: T) => React.ReactNode; anchor?: string;
} & Omit<Headless.ComboboxProps<T, false, typeof Fragment>, 'as' | 'children' | 'multiple'>) {
  const [query, setQuery] = useState('')
  const filtered = query === '' ? options : options.filter(o => filter ? filter(o, query) : String(displayValue?.(o) ?? '').toLowerCase().includes(query.toLowerCase()))
  return (
    <Headless.Combobox {...props} virtual={{ options: filtered }} onClose={() => setQuery('')}>
      <span data-slot="control" className={clsx(className, 'relative block w-full', 'before:absolute before:inset-px before:rounded-[calc(var(--radius-lg)-1px)] before:bg-white before:shadow-sm dark:before:hidden', 'after:pointer-events-none after:absolute after:inset-0 after:rounded-lg after:ring-transparent after:ring-inset sm:focus-within:after:ring-2 sm:focus-within:after:ring-blue-500', 'has-data-invalid:before:shadow-red-500/10')}>
        <Headless.ComboboxInput autoFocus={autoFocus} data-slot="control" aria-label={ariaLabel} displayValue={(o: T | null) => displayValue?.(o) ?? ''} onChange={e => setQuery(e.target.value)} placeholder={placeholder} className={clsx('relative block w-full appearance-none rounded-lg py-[calc(--spacing(2.5)-1px)] pr-[calc(--spacing(10)-1px)] pl-[calc(--spacing(3.5)-1px)] sm:py-[calc(--spacing(1.5)-1px)] sm:pr-[calc(--spacing(9)-1px)] sm:pl-[calc(--spacing(3)-1px)]', 'text-base/6 text-zinc-950 placeholder:text-zinc-500 sm:text-sm/6 dark:text-white', 'border border-zinc-950/10 data-hover:border-zinc-950/20 dark:border-white/10 dark:data-hover:border-white/20', 'bg-transparent dark:bg-white/5', 'focus:outline-hidden', 'data-invalid:border-red-500 dark:data-invalid:border-red-500', 'data-disabled:border-zinc-950/20 dark:data-disabled:border-white/15 dark:data-disabled:bg-white/2.5')} />
        <Headless.ComboboxButton className="absolute inset-y-0 right-0 flex items-center px-2 sm:px-1.5">
          <svg className="size-5 stroke-zinc-500 sm:size-4 dark:stroke-zinc-400" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <path d="M5.75 10.75L8 13L10.25 10.75" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" />
            <path d="M10.25 5.25L8 3L5.75 5.25" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </Headless.ComboboxButton>
      </span>
      <Headless.ComboboxOptions transition anchor={anchor as any} className="isolate min-w-(--input-width) select-none scroll-py-1 rounded-xl p-1 outline outline-transparent focus:outline-hidden overflow-y-scroll overscroll-contain bg-white/75 backdrop-blur-xl ring-1 ring-zinc-950/10 dark:bg-zinc-800/75 dark:ring-white/10 shadow-lg transition-opacity duration-100 ease-in data-closed:data-leave:opacity-0 data-transition:pointer-events-none empty:invisible">
        {({ option }: { option: T }) => children(option)}
      </Headless.ComboboxOptions>
    </Headless.Combobox>
  )
}

export function ComboboxOption<T>({ children, className, ...props }: { className?: string; children?: React.ReactNode } & Omit<Headless.ComboboxOptionProps<'div', T>, 'as' | 'className'>) {
  return (
    <Headless.ComboboxOption as="div" {...props} className={clsx(className, 'group/option grid cursor-default grid-cols-[--spacing(5)_1fr] items-baseline gap-x-2 rounded-lg py-2.5 pr-3.5 pl-2 sm:grid-cols-[--spacing(4)_1fr] sm:py-1.5 sm:pr-3 sm:pl-1.5 text-base/6 text-zinc-950 sm:text-sm/6 dark:text-white', 'data-focus:bg-blue-500 data-focus:text-white', 'data-disabled:opacity-50')}>
      <svg className="relative hidden size-5 self-center stroke-current group-data-selected/option:inline sm:size-4" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8.5l3 3L12 4" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" /></svg>
      <span className="col-start-2 flex items-center gap-2 truncate">{children}</span>
    </Headless.ComboboxOption>
  )
}
export function ComboboxLabel({ className, ...p }: React.ComponentPropsWithoutRef<'span'>) { return <span {...p} className={clsx(className, 'ml-2.5 truncate first:ml-0 sm:ml-2 sm:first:ml-0')} /> }
export function ComboboxDescription({ className, children, ...p }: React.ComponentPropsWithoutRef<'span'>) { return <span {...p} className={clsx(className, 'flex flex-1 overflow-hidden text-zinc-500 before:w-2 before:min-w-0 before:shrink group-data-focus/option:text-white dark:text-zinc-400')}><span className="flex-1 truncate">{children}</span></span> }
