// Catalyst-style Heading / Subheading — recreated from the scraped API at
// https://catalyst.tailwindui.com/docs/heading
import clsx from 'clsx'
import React from 'react'

type HeadingLevel = 1 | 2 | 3 | 4 | 5 | 6

export function Heading({ className, level = 1, ...props }: { level?: HeadingLevel; className?: string } & React.HTMLAttributes<HTMLHeadingElement>) {
  const Element: `h${HeadingLevel}` = `h${level}`
  return <Element {...props} className={clsx(className, 'text-2xl/8 font-semibold text-zinc-950 sm:text-xl/8 dark:text-white')} />
}

export function Subheading({ className, level = 2, ...props }: { level?: HeadingLevel; className?: string } & React.HTMLAttributes<HTMLHeadingElement>) {
  const Element: `h${HeadingLevel}` = `h${level}`
  return <Element {...props} className={clsx(className, 'text-base/7 font-semibold text-zinc-950 sm:text-sm/6 dark:text-white')} />
}
