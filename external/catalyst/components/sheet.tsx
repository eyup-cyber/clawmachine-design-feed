'use client'

import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import type React from 'react'
import { Fragment } from 'react'

// Catalyst-style off-canvas sheet (reimplementation from public docs).
// Props follow Catalyst Dialog's documented API, but slides from edge.

type SheetSide = 'left' | 'right' | 'top' | 'bottom'

const sideClasses: Record<SheetSide, string> = {
  left: 'inset-y-0 left-0 w-80 max-w-full',
  right: 'inset-y-0 right-0 w-80 max-w-full',
  top: 'inset-x-0 top-0 h-80 max-h-full',
  bottom: 'inset-x-0 bottom-0 h-80 max-h-full',
}

const transforms: Record<SheetSide, { enter: string; leave: string }> = {
  left: { enter: 'translate-x-0', leave: '-translate-x-full' },
  right: { enter: 'translate-x-0', leave: 'translate-x-full' },
  top: { enter: 'translate-y-0', leave: '-translate-y-full' },
  bottom: { enter: 'translate-y-0', leave: 'translate-y-full' },
}

export function Sheet({
  open,
  onClose,
  side = 'right',
  children,
  className,
  ...props
}: {
  open: boolean
  onClose: (open: false) => void
  side?: SheetSide
  children: React.ReactNode
  className?: string
} & Omit<Headless.DialogProps<typeof Fragment>, 'as' | 'children'>) {
  return (
    <Headless.Transition show={open} as={Fragment}>
      <Headless.Dialog onClose={onClose} as="div" className="relative z-50" {...props}>
        <Headless.Transition.Child
          as={Fragment}
          enter="ease-out duration-200"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in duration-150"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-zinc-950/25 dark:bg-zinc-950/50" />
        </Headless.Transition.Child>

        <div className="fixed inset-0 overflow-hidden">
          <Headless.Transition.Child
            as={Fragment}
            enter="transform transition ease-out duration-200"
            enterFrom={transforms[side].leave}
            enterTo={transforms[side].enter}
            leave="transform transition ease-in duration-150"
            leaveFrom={transforms[side].enter}
            leaveTo={transforms[side].leave}
          >
            <Headless.Dialog.Panel
              className={clsx(
                'fixed bg-white p-6 shadow-xl dark:bg-zinc-900 ring-1 ring-zinc-950/5 dark:ring-white/10',
                sideClasses[side],
                className
              )}
            >
              {children}
            </Headless.Dialog.Panel>
          </Headless.Transition.Child>
        </div>
      </Headless.Dialog>
    </Headless.Transition>
  )
}

export function SheetTitle({ className, ...props }: React.ComponentPropsWithoutRef<'h2'>) {
  return (
    <Headless.Dialog.Title
      as="h2"
      {...props}
      className={clsx(className, 'text-lg/6 font-semibold text-balance text-zinc-950 dark:text-white')}
    />
  )
}

export function SheetDescription({ className, ...props }: React.ComponentPropsWithoutRef<'p'>) {
  return (
    <Headless.Description
      as="p"
      {...props}
      className={clsx(className, 'mt-2 text-base/6 text-zinc-500 sm:text-sm/6 dark:text-zinc-400')}
    />
  )
}

export function SheetBody({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) {
  return <div {...props} className={clsx(className, 'mt-6')} />
}

export function SheetActions({ className, ...props }: React.ComponentPropsWithoutRef<'div'>) {
  return (
    <div
      {...props}
      className={clsx(className, 'mt-8 flex flex-col-reverse items-center justify-end gap-3 *:w-full sm:flex-row sm:*:w-auto')}
    />
  )
}
