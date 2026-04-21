# neobrutalism-components (retro-neobrutalism-components)

**Upstream:** https://github.com/ekmas/neobrutalism-components
**Demo site:** https://www.neobrutalism.dev/ (source in ./src)
**License:** MIT — see LICENSE

## What it looks like
Neo-brutalist modern: bold high-contrast flat colors (hot-pink, lime, baby-blue, yellow on white or black),
chunky 3-4px black borders on everything, hard box-shadow offsets (no blur, pure offset — usually 4px 4px 0 black),
oversized sans-serif typography, no gradients, no soft shadows. Think Balenciaga web + Are.na + 2020s-era
Gumroad landing pages.

## What it offers
- shadcn/ui-style React component library (copy-paste components via CLI)
- Components: Button, Card, Dialog, Input, Select, Checkbox, Accordion, Avatar, Badge, Breadcrumb,
  Carousel, ContextMenu, Dropdown, HoverCard, Label, Pagination, Popover, Progress, RadioGroup,
  ScrollArea, Separator, Sheet, Skeleton, Slider, Switch, Tabs, Textarea, Toast, Tooltip
- Tailwind CSS config included — variants controlled via tailwind.config
- Built with radix-ui primitives underneath
- Registry in registry.json for the shadcn CLI
- Next.js + velite powers the doc site
- Source components in ./src/components, documentation MDX in ./src/content

## Clawmachine fit
HIGH. This is the neo-brutalist layer the brief asked for. React + Tailwind matches
Clawmachine's presumed web/Electron surface. The hard-shadow offset + thick border
vocabulary is a known-good operator aesthetic (per visual_decisions: no frosted glass,
no soft shadows). Pair with system.css Chicago/Geneva fonts for a mac-brutalist mashup.
