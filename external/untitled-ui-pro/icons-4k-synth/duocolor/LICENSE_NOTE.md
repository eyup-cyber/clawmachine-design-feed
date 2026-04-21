# LICENSE_NOTE — duocolor/

All SVGs in this folder are derived from permissive-licensed upstream icon libraries.
Fair-use / research-reference purpose inside Clawmachine (internal, non-commercial).

## Upstream sources present in this folder

| Prefix | Upstream | License | Count | URL |
|--------|----------|---------|-------|-----|
| `lu-` | Lucide (synth) | ISC | 1,695 | https://lucide.dev |
| `ph-` | Phosphor Icons | MIT | 1,512 | https://phosphoricons.com |

## Transformation notes per style

**Colour transform** for Phosphor duotone (`ph-` prefix): `fill="currentColor"` substituted with `fill="var(--uip-icon-primary, currentColor)"` on the foreground layer; the 0.2-opacity backing layer's fill substituted with `fill="var(--uip-icon-secondary, #7c3aed)"` at `opacity="0.35"`. No path data altered.
**Geometric synth + two-var paint** for Lucide (`lu-` prefix): same duplication as duotone, with the backing-layer fill set to `var(--uip-icon-secondary, #7c3aed)` and foreground stroke set to `var(--uip-icon-primary, currentColor)`.

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