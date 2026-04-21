// Catalyst-style Listbox — recreated from https://catalyst.tailwindui.com/docs/listbox
import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { Fragment } from 'react'

export function Listbox<T>({ className, placeholder, autoFocus, 'aria-label': ariaLabel, children: options, ...props }: { className?: string; placeholder?: React.ReactNode; autoFocus?: boolean; 'aria-label'?: string; children?: React.ReactNode } & Omit<Headless.ListboxProps<typeof Fragment, T>, 'as' | 'className' | 'children'>) {
  return (
    <Headless.Listbox {...props}>
      <Headless.ListboxButton autoFocus={autoFocus} data-slot="control" aria-label={ariaLabel} className={clsx([
        className,
        'group relative block w-full',
        'before:absolute before:inset-px before:rounded-[calc(var(--radius-lg)-1px)] before:bg-white before:shadow-sm dark:before:hidden',
        'after:pointer-events-none after:absolute after:inset-0 after:rounded-lg after:ring-transparent after:ring-inset data-focus:after:ring-2 data-focus:after:ring-blue-500',
        'cursor-default appearance-none rounded-lg py-[calc(--spacing(2.5)-1px)] pr-[calc(--spacing(10)-1px)] pl-[calc(--spacing(3.5)-1px)] sm:py-[calc(--spacing(1.5)-1px)] sm:pr-[calc(--spacing(9)-1px)] sm:pl-[calc(--spacing(3)-1px)]',
        'text-left text-base/6 text-zinc-950 placeholder:text-zinc-500 sm:text-sm/6 dark:text-white forced-colors:text-[CanvasText]',
        'border border-zinc-950/10 group-data-active:border-zinc-950/20 group-data-hover:border-zinc-950/20 dark:border-white/10 dark:group-data-active:border-white/20 dark:group-data-hover:border-white/20',
        'bg-transparent dark:bg-white/5',
        'focus:outline-hidden',
        'data-invalid:border-red-500 data-invalid:group-data-hover:border-red-500 dark:data-invalid:border-red-600 dark:data-invalid:group-data-hover:border-red-600',
        'data-disabled:border-zinc-950/20 data-disabled:opacity-100 dark:data-disabled:border-white/15 dark:data-disabled:bg-white/2.5 dark:data-disabled:data-hover:border-white/15',
      ])}>
        <Headless.ListboxSelectedOption as="span" options={options} placeholder={placeholder && <span className="block truncate text-zinc-500">{placeholder}</span>} />
        <span className="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2 sm:pr-1.5">
          <svg className="size-5 stroke-zinc-500 sm:size-4 dark:stroke-zinc-400" viewBox="0 0 16 16" aria-hidden="true" fill="none">
            <path d="M5.75 10.75L8 13L10.25 10.75" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" />
            <path d="M10.25 5.25L8 3L5.75 5.25" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </span>
      </Headless.ListboxButton>
      <Headless.ListboxOptions transition anchor="selection start" className="isolate min-w-[calc(var(--button-width)+1.75rem)] select-none scroll-py-1 rounded-xl p-1 outline outline-transparent focus:outline-hidden overflow-y-scroll overscroll-contain bg-white/75 backdrop-blur-xl ring-1 ring-zinc-950/10 dark:bg-zinc-800/75 dark:ring-white/10 shadow-lg transition-opacity duration-100 ease-in data-closed:data-leave:opacity-0 data-transition:pointer-events-none">
        {options}
      </Headless.ListboxOptions>
    </Headless.Listbox>
  )
}

export function ListboxOption<T>({ children, className, ...props }: { className?: string; children?: React.ReactNode } & Omit<Headless.ListboxOptionProps<'div', T>, 'as' | 'className'>) {
  return (
    <Headless.ListboxOption as="div" {...props} className={clsx(className, 'group/option grid cursor-default grid-cols-[--spacing(5)_1fr] items-baseline gap-x-2 rounded-lg py-2.5 pr-3.5 pl-2 sm:grid-cols-[--spacing(4)_1fr] sm:py-1.5 sm:pr-3 sm:pl-1.5 text-base/6 text-zinc-950 sm:text-sm/6 dark:text-white', 'data-focus:bg-blue-500 data-focus:text-white', 'data-disabled:opacity-50')}>
      <svg className="relative hidden size-5 self-center stroke-current group-data-selected/option:inline sm:size-4" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8.5l3 3L12 4" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" /></svg>
      <span className="col-start-2 flex items-center gap-2 truncate">{children}</span>
    </Headless.ListboxOption>
  )
}

export function ListboxLabel({ className, ...props }: React.ComponentPropsWithoutRef<'span'>) {
  return <span {...props} className={clsx(className, 'ml-2.5 truncate first:ml-0 sm:ml-2 sm:first:ml-0')} />
}

export function ListboxDescription({ className, children, ...props }: React.ComponentPropsWithoutRef<'span'>) {
  return <span {...props} className={clsx(className, 'flex flex-1 overflow-hidden text-zinc-500 before:w-2 before:min-w-0 before:shrink group-data-focus/option:text-white dark:text-zinc-400')}><span className="flex-1 truncate">{children}</span></span>
}
