# Mantine — README-EXTRACT

**Upstream**: https://github.com/mantinedev/mantine
**Clone**: `git clone --depth 1` (shallow, single commit)
**Size on disk**: ~44 MB
**License**: MIT (see `LICENSE`, mirrored into `LICENSE_NOTE.md`)

## What this is

Mantine is a ~120-component React UI library (hooks + components + theming) authored by Vitaly Rtishchev. Mature (since 2021), broad coverage, vanilla-extract / CSS-modules styling, not Tailwind-based. Good reference for component API design, theme-token plumbing, and accessibility-correct primitives.

## Key folders for reference

Monorepo — everything useful is under `packages/@mantine/*`.

| Path | What's in it |
|---|---|
| `packages/@mantine/core/src/components/` | **primary**: 100+ component source dirs (Accordion, Button, Card, Combobox, DatePicker, Drawer, Menu, Modal, Notifications, Popover, Select, Stepper, Tabs, Tooltip, …). Each dir has `.tsx`, `.module.css`, `.story.tsx`, `.test.tsx`. |
| `packages/@mantine/core/src/core/` | theme engine, MantineProvider, CSS variables resolver, style-system plumbing. |
| `packages/@mantine/hooks/src/` | standalone hook library (use-click-outside, use-debounced-value, use-disclosure, use-form, use-hotkeys, use-intersection, use-media-query, etc.). |
| `packages/@mantine/form/src/` | form state + validation primitives. |
| `packages/@mantine/dates/src/` | DatePicker, DateInput, Calendar, TimeInput. |
| `packages/@mantine/charts/src/` | Recharts-based chart wrappers. |
| `packages/@mantine/notifications/src/` | toast/notification system. |
| `packages/@mantine/modals/src/` | imperative modal manager. |
| `packages/@mantine/spotlight/src/` | command-palette primitive. |
| `packages/@mantine/carousel/src/` | Embla-based carousel wrapper. |
| `packages/@mantine/tiptap/src/` | Tiptap rich-text editor integration. |
| `packages/@mantine/code-highlight/src/` | Shiki-based code block. |
| `packages/@mantine/dropzone/src/` | file upload. |
| `packages/@mantine/nprogress/src/` | top-bar progress indicator. |
| `packages/@mantine/colors-generator/src/` | generates 10-shade palettes from a single colour — relevant to our 32+6 palette work. |
| `packages/@mantine/emotion/src/` | emotion CSS-in-JS bridge (legacy, deprecating). |
| `packages/@mantine/vanilla-extract/src/` | vanilla-extract tokens bridge. |
| `packages/@mantine/store/src/` | tiny state store (observable). |
| `packages/@mantine/mcp-server/src/` | **Mantine ships an MCP server** — worth a look given our Claude-driven workflow. |

## Boilerplate (skip)

- `apps/` — docs website + mantine.dev marketing site; heavy next.js app, not a reference for components.
- `llms/` — model-context export, secondary.
- `scripts/`, `babel.config.json`, `jest.*`, `jsdom.mocks.ts`, `postcss.config.cjs`, `tsconfig.json` — tooling.
- `@mantine-tests/`, `@mantinex/` — internal test fixtures and private utilities.
- any `__stories__/`, `__tests__/`, `CHANGELOG.md`, `*.story.tsx`, `*.test.tsx` inside component dirs.

## Recommended entry points for Frankenstein stitch

1. Component API shape — look at `core/src/components/{Button,Menu,Popover,Modal,Select,Combobox}/` for the definitive "how to factor a React component with compound children + polymorphic `component` prop + CSS-module theming" pattern.
2. Theme plumbing — `core/src/core/MantineProvider/` and `core/src/core/Box/style-props/` (CSS-variable token surface).
3. Palette generation — `colors-generator/src/` (could directly inform our 32+6 shortlist tooling).
4. Hooks library — `hooks/src/` is standalone, zero-React-component dependency, good copy-candidates for Swift-UI-adjacent utilities if reused via webview.
