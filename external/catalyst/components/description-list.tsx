// Catalyst-style DescriptionList — recreated from the scraped API at
// https://catalyst.tailwindui.com/docs/description-list
import clsx from 'clsx'
import React from 'react'

export function DescriptionList({ className, ...props }: React.HTMLAttributes<HTMLDListElement>) {
  return (
    <dl
      {...props}
      className={clsx(
        className,
        'grid grid-cols-1 text-base/6 sm:grid-cols-[min(50%,var(--spacing-80))_auto] sm:text-sm/6'
      )}
    />
  )
}

export function DescriptionTerm({ className, ...props }: React.HTMLAttributes<HTMLElement>) {
  return (
    <dt
      {...props}
      className={clsx(
        className,
        'col-start-1 border-t border-zinc-950/5 pt-3 text-zinc-500 first:border-none sm:border-t sm:border-zinc-950/5 sm:py-3 dark:border-white/5 dark:text-zinc-400'
      )}
    />
  )
}

export function DescriptionDetails({ className, ...props }: React.HTMLAttributes<HTMLElement>) {
  return (
    <dd
      {...props}
      className={clsx(
        className,
        'pt-1 pb-3 text-zinc-950 sm:border-t sm:border-zinc-950/5 sm:py-3 sm:nth-2:border-none dark:text-white dark:sm:border-white/5'
      )}
    />
  )
}
