# Once UI — README-EXTRACT

**Upstream**: https://github.com/once-ui-system/core
**Clone**: `git clone --depth 1` (shallow)
**Size on disk**: ~40 MB
**License**: MIT

## What this is

Once UI is Lorant Toth's indie React component system for Next.js apps, marketed as "the indie design system". Minimalist visual language, SCSS modules, token-driven. Smaller surface than Mantine/Chakra but opinionated and aesthetically close to the kind of restrained motion-first look we're aiming for.

Note: the upstream has *two* canonical repos — `once-ui-system/core` is the component library itself; `once-ui-system/magic-portfolio` is a template using it. We cloned `core`.

## Key folders for reference

Monorepo under `packages/`.

| Path | What's in it |
|---|---|
| `packages/core/src/components/` | **primary**: ~120 component files (`.tsx`) + co-located `.module.scss`. Including: Accordion, Animation, Arrow, AutoScroll, Avatar, Background (animated fx), Badge, Button, Card, Carousel, CelebrationFx, Checkbox, Chip, ColorInput, Column, CompareImage, ContextMenu, CountdownFx, CountFx, Cursor, etc. Unlike Mantine/Chakra, files sit flat in one directory rather than one-dir-per-component. |
| `packages/core/src/core/` | provider, context, primitives. |
| `packages/core/src/hooks/` | custom hooks. |
| `packages/core/src/styles/` | global SCSS (tokens, reset, theme). |
| `packages/core/src/tokens/` | design tokens (colors, typography, motion). |
| `packages/core/src/modules/` | higher-level composed modules. |
| `packages/core/src/contexts/` | React contexts (theme, toast, dialog). |
| `packages/core/src/data/`, `server/`, `utils/` | helpers. |

## Boilerplate (skip)

- `apps/` — documentation site and demo app.
- `sandbox/`, `scripts/`, `turbo.json`, `pnpm-*.yaml`, `tsconfig.json` — tooling.
- Any `__tests__/` or `*.test.tsx`.

## Recommended entry points for Frankenstein stitch

1. **Motion-fx components**: `packages/core/src/components/{Animation,AutoScroll,Background,CelebrationFx,CountdownFx,CountFx,Cursor}.tsx` — these are exactly the "motion as accent" pieces we decided on per the visual-decisions note. Worth reviewing before committing to a React-Bits-style animated kit or writing from scratch.
2. **SCSS module pattern**: each component has a colocated `.module.scss`. If we go SCSS-modules (not Tailwind, not Panda), this is the cleanest reference.
3. **Token surface**: `packages/core/src/tokens/` is a tight, small token set — good floor reference; compare against our 32+6 palette shortlist.
4. **CompareImage / CelebrationFx / CountFx** — novel components not in Mantine or Chakra; worth stealing outright.
