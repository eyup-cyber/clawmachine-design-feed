# LICENSE_NOTE — stroke/

All SVGs in this folder are derived from permissive-licensed upstream icon libraries.
Fair-use / research-reference purpose inside Clawmachine (internal, non-commercial).

## Upstream sources present in this folder

| Prefix | Upstream | License | Count | URL |
|--------|----------|---------|-------|-----|
| (none) | Lucide | ISC | 1,695 | https://lucide.dev |
| `ph-` | Phosphor Icons | MIT | 1,512 | https://phosphoricons.com |
| `feather-` | Feather Icons | MIT | 287 | https://feathericons.com |

## Transformation notes per style

**Rename-only.** Upstream SVGs copied without visual changes.
- Lucide: `src/icons/*.svg` copied verbatim.
- Phosphor: `assets/regular/*.svg` copied with `ph-` prefix.
- Feather: `icons/*.svg` copied with `feather-` prefix.

## Attribution (reproduced verbatim per upstream requirements)

- **Lucide** (ISC) — https://lucide.dev
  - Copyright (c) Lucide Contributors
- **Phosphor Icons** (MIT) — https://phosphoricons.com
  - Copyright (c) 2023 Phosphor Icons
- **Feather Icons** (MIT) — https://feathericons.com
  - Copyright (c) 2013-2023 Cole Bemis

## Why we treat these as recreation-safe

- No paid Pro-tier proprietary icon (Untitled UI Pro's own SVGs) is included.
- All transforms are colour/opacity substitutions and geometric duplication of already-public paths — they do not introduce new expressive path data.
- The folder is an internal research reference, not a redistributed product. If an upstream maintainer objects to the derivative transform, contact the operator and the affected files are removed.

## Quick attribution block for any downstream shipped derivative

```
Icons derived from:
- Lucide (ISC) https://lucide.dev
- Phosphor Icons (MIT) https://phosphoricons.com
- Feather Icons (MIT) https://feathericons.com
```