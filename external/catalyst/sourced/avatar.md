# Avatar — Catalyst UI Kit (scraped reference)

Source: https://catalyst.tailwindui.com/docs/avatar

## Component API

| Prop | Default | Description |
| :-- | :-- | :-- |
| **Avatar** extends `<span>` |
| `src` | - | URL of the avatar image |
| `square` | `false` | Make the avatar square |
| `initials` | - | Initials used when no `src` provided |
| **AvatarButton** extends Headless UI `Button` or `Link` |
| `src` | - | URL of the avatar image |
| `square` | `false` | Make the avatar square |
| `initials` | - | Initials used when no `src` provided |
| `href` | - | When provided, renders as link |

## Basic example

```tsx
import { Avatar } from '@/components/avatar'

<Avatar className="size-6" src={user.avatarUrl} />
<Avatar className="size-8" src={user.avatarUrl} />
<Avatar className="size-10" src={user.avatarUrl} />
```

## With initials (and fallback)

```tsx
<Avatar initials="tw" className="size-10 bg-zinc-900 text-white dark:bg-white dark:text-black" />
<Avatar src={user.avatarUrl} initials={user.initials} className="size-10 bg-purple-500 text-white" />
```

## Square

```tsx
<Avatar square className="size-8" src={user.avatarUrl} />
<Avatar square initials={user.initials} className="size-8 bg-zinc-900 text-white dark:bg-white dark:text-black" />
```

## Avatar group (overlap)

```tsx
<div className="flex items-center justify-center -space-x-2">
  {users.map((user) => (
    <Avatar src={user.avatarUrl} className="size-8 ring-2 ring-white dark:ring-zinc-900" />
  ))}
</div>
```

## AvatarButton (link)

```tsx
<AvatarButton href={user.url} className="size-8" src={user.avatarUrl} />
```
