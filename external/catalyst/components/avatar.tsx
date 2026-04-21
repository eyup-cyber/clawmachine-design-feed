// Catalyst-style Avatar + AvatarButton — recreated from the scraped API at
// https://catalyst.tailwindui.com/docs/avatar

import * as Headless from '@headlessui/react'
import clsx from 'clsx'
import React, { forwardRef } from 'react'
import { Link } from './link'
import { TouchTarget } from './button'

type AvatarProps = { src?: string | null; square?: boolean; initials?: string; alt?: string; className?: string } & React.HTMLAttributes<HTMLSpanElement>

export function Avatar({ src = null, square = false, initials, alt = '', className, ...props }: AvatarProps) {
  return (
    <span
      data-slot="avatar"
      {...props}
      className={clsx(
        className,
        'inline-grid shrink-0 align-middle [--avatar-radius:20%] *:col-start-1 *:row-start-1 *:rounded-(--avatar-radius)',
        'outline outline-1 -outline-offset-1 outline-black/10 dark:outline-white/10',
        square && '*:rounded-md [--avatar-radius:var(--radius-md)] outline-offset-0'
      )}
    >
      {initials && (
        <svg className="size-full fill-current p-[5%] text-[48px] font-medium uppercase select-none" viewBox="0 0 100 100" aria-hidden={alt ? undefined : 'true'} aria-label={alt ? alt : undefined}>
          {alt && <title>{alt}</title>}
          <text x="50%" y="50%" alignmentBaseline="middle" dominantBaseline="middle" textAnchor="middle" dy=".125em">
            {initials}
          </text>
        </svg>
      )}
      {src && <img src={src} alt={alt} className="size-full object-cover" />}
    </span>
  )
}

type AvatarButtonProps = AvatarProps & (Omit<Headless.ButtonProps, 'className'> | Omit<React.ComponentPropsWithoutRef<typeof Link>, 'className'>)

export const AvatarButton = forwardRef(function AvatarButton({ src, square = false, initials, alt, className, ...props }: AvatarButtonProps, ref: React.ForwardedRef<HTMLElement>) {
  const classes = clsx(className, square ? 'rounded-md' : 'rounded-full', 'relative inline-grid focus:outline-hidden data-focus:outline-2 data-focus:outline-offset-2 data-focus:outline-blue-500')
  return 'href' in props ? (
    <Link {...(props as React.ComponentPropsWithoutRef<typeof Link>)} className={classes} ref={ref as React.ForwardedRef<HTMLAnchorElement>}>
      <TouchTarget><Avatar src={src} square={square} initials={initials} alt={alt} /></TouchTarget>
    </Link>
  ) : (
    <Headless.Button {...(props as Headless.ButtonProps)} className={classes} ref={ref as React.ForwardedRef<HTMLButtonElement>}>
      <TouchTarget><Avatar src={src} square={square} initials={initials} alt={alt} /></TouchTarget>
    </Headless.Button>
  )
})
