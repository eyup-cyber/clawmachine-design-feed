# Chakra UI — README-EXTRACT

**Upstream**: https://github.com/chakra-ui/chakra-ui
**Clone**: `git clone --depth 1` (shallow)
**Size on disk**: ~297 MB (largest of the seven; still well inside budget)
**License**: MIT

## What this is

Composable React UI library built on a Panda CSS / styled-system base. Started in 2019, very mature. Heavy use of the "compound component" and "style-props + tokens" pattern. Post-v3 it moved to Panda CSS + tsstyled-system, making it a good reference for token-first theming outside Tailwind.

## Key folders for reference

Monorepo under `packages/`.

| Path | What's in it |
|---|---|
| `packages/react/src/components/` | **primary**: ~85 component dirs — accordion, alert, avatar, badge, box, button, card, checkbox, combobox, dialog, drawer, editable, field, menu, popover, select, stepper, tabs, toast, tooltip, tree-view, etc. Each is a directory containing `*.tsx`, anatomy, recipes, tests. |
| `packages/react/src/hooks/` | standalone hooks (useControllableState, useDisclosure, useLatestRef, etc.). |
| `packages/react/src/styled-system/` | the runtime style-props + recipe engine — worth reading for tokens / recipe patterns. |
| `packages/react/src/theme/` | default theme tokens (colors, radii, shadows, spacing). |
| `packages/react/src/preset-base.ts` / `preset.ts` | Panda CSS preset files — token shape. |
| `packages/panda-preset/` | Panda CSS preset for integrating Chakra's recipes into a standalone Panda setup. |
| `packages/charts/` | Recharts-based chart wrappers. |
| `packages/cli/` | `chakra` CLI (theme typegen, component scaffolding). |
| `packages/codemod/` | v2→v3 codemods. |

## Boilerplate (skip)

- `apps/` — docs website (www.chakra-ui.com) and compositions/starters; large, not reference-worthy for components themselves.
- `sandbox/` — internal test harness.
- `scripts/`, `eslint.config.mjs`, `vite.config.ts`, `vitest.setup.ts`, `pnpm-*.yaml`, `tsconfig*.json` — tooling.
- `media/` — brand logos/screenshots.
- `__stories__/`, `__tests__/`, `CHANGELOG.md`, `*.test.tsx` inside component dirs.

## Recommended entry points for Frankenstein stitch

1. **Component compound pattern**: `packages/react/src/components/accordion/` — see how `<Accordion.Root>`, `<Accordion.Item>`, `<Accordion.Trigger>` are wired. Compare against Mantine's flatter API to pick a house style.
2. **Recipes / slot recipes**: `packages/react/src/styled-system/` + a component like `button/` — variants are declared in a recipe file, consumed in the component. This is the Panda idiom; likely incompatible with a Swift/webview hybrid, but good token-plumbing reference.
3. **Default tokens**: `packages/react/src/theme/tokens/` — baseline colour/space/radius scales that survived three years of user testing.
4. **Charts wrappers**: `packages/charts/src/` — thin wrappers over Recharts with theme-aware defaults.
