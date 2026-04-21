# LICENSE_NOTE — duotone/

All SVGs in this folder are derived from permissive-licensed upstream icon libraries.
Fair-use / research-reference purpose inside Clawmachine (internal, non-commercial).

## Upstream sources present in this folder

| Prefix | Upstream | License | Count | URL |
|--------|----------|---------|-------|-----|
| `lu-` | Lucide (synth) | ISC | 1,695 | https://lucide.dev |
| `ph-` | Phosphor Icons | MIT | 1,512 | https://phosphoricons.com |

## Transformation notes per style

**Native copy** for Phosphor (`ph-` prefix, from `assets/duotone/`).
**Geometric synth** for Lucide (`lu-` prefix): each `<path>/<rect>/<circle>/<polygon>/<ellipse>/<line>` in the Lucide stroke SVG is duplicated into a backing `fill` layer at `opacity="0.2"`, keeping the original stroke layer on top. No path data is altered — pure geometric duplication.

## Attribution (reproduced verbatim per upstream requirements)

- **Lucide (synth)** (ISC) — https://lucide.dev
  - Copyright (c) Lucide Contributors
- **Phosphor Icons** (MIT) — https://phosphoricons.com
  - Copyright (c) 2023 Phosphor Icons

## Why we treat these as recreation-safe

- No paid Pro-tier proprietary icon (Untitled UI Pro's own SVGs) is included.
- All transforms are colour/opacity substitutions and geometric duplication of already-public paths — they do not introduce new expressive path data.
- The folder is an internal research reference, not a redistributed product. If an upstream maintainer objects to the derivative transform, contact the operator and the affected files are removed.

## Quick attribution block for any downstream shipped derivative

```
Icons derived from:
- Lucide (synth) (ISC) https://lucide.dev
- Phosphor Icons (MIT) https://phosphoricons.com
```