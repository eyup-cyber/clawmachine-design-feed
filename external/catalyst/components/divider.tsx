// Catalyst-style Divider — recreated from the scraped API at
// https://catalyst.tailwindui.com/docs/divider

import clsx from 'clsx'
import React from 'react'

export function Divider({ soft = false, className, ...props }: { soft?: boolean; className?: string } & React.ComponentPropsWithoutRef<'hr'>) {
  return (
    <hr
      role="presentation"
      {...props}
      className={clsx(
        className,
        'w-full border-t',
        soft ? 'border-zinc-950/5 dark:border-white/5' : 'border-zinc-950/10 dark:border-white/10'
      )}
    />
  )
}
