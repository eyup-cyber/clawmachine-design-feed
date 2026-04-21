# LICENSE_NOTE — solid/

All SVGs in this folder are derived from permissive-licensed upstream icon libraries.
Fair-use / research-reference purpose inside Clawmachine (internal, non-commercial).

## Upstream sources present in this folder

| Prefix | Upstream | License | Count | URL |
|--------|----------|---------|-------|-----|
| `ms-` | Material Symbols | Apache-2.0 | 3,858 | https://fonts.google.com/icons |
| `ph-` | Phosphor Icons | MIT | 1,512 | https://phosphoricons.com |
| `iconoir-` | Iconoir | MIT | 288 | https://iconoir.com |

## Transformation notes per style

**Rename-only** for all sources.
- Phosphor fill: `assets/fill/*.svg` copied with `ph-` prefix.
- Iconoir solid: `icons/solid/*.svg` copied with `iconoir-` prefix.
- Material Symbols: rounded-filled variant copied with `ms-` prefix.

## Attribution (reproduced verbatim per upstream requirements)

- **Material Symbols** (Apache-2.0) — https://fonts.google.com/icons
  - Copyright (c) 2022 Google LLC
- **Phosphor Icons** (MIT) — https://phosphoricons.com
  - Copyright (c) 2023 Phosphor Icons
- **Iconoir** (MIT) — https://iconoir.com
  - Copyright (c) 2021-2024 Luca Burgio

## Why we treat these as recreation-safe

- No paid Pro-tier proprietary icon (Untitled UI Pro's own SVGs) is included.
- All transforms are colour/opacity substitutions and geometric duplication of already-public paths — they do not introduce new expressive path data.
- The folder is an internal research reference, not a redistributed product. If an upstream maintainer objects to the derivative transform, contact the operator and the affected files are removed.

## Quick attribution block for any downstream shipped derivative

```
Icons derived from:
- Material Symbols (Apache-2.0) https://fonts.google.com/icons
- Phosphor Icons (MIT) https://phosphoricons.com
- Iconoir (MIT) https://iconoir.com
```