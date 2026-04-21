# LICENSE_NOTE — icons-4k-synth

This directory contains icon SVGs copied from, or synthesised from, the
following upstream libraries. Each upstream project's original license
applies to files derived from it. All are permissive and compatible with
internal non-commercial fair-use research reference use inside Clawmachine.

## Upstream sources and licenses

| Source                   | License      | Files      | Filename prefix        | Upstream URL                                       |
|--------------------------|--------------|------------|------------------------|----------------------------------------------------|
| Lucide                   | ISC          | stroke: ~1695, duotone/duocolor synth: ~1695 each | (none), `lu-` | https://lucide.dev                                 |
| Phosphor Icons           | MIT          | stroke ~1512 (regular), solid ~1512 (fill), duotone ~1512 (native), duocolor ~1512 (transform) | `ph-`, `phb-` | https://phosphoricons.com                         |
| Feather Icons            | MIT          | stroke ~287 | `feather-`             | https://feathericons.com                           |
| Iconoir                  | MIT          | solid ~288 | `iconoir-`             | https://iconoir.com                                |
| Material Symbols         | Apache-2.0   | solid ~3858 | `ms-`                  | https://fonts.google.com/icons                     |

## Attribution requirements

- **Lucide (ISC):** preserve copyright notice in distribution. Derivative duotone/duocolor remain under ISC.
- **Phosphor (MIT):** preserve copyright notice in distribution. Two-tone transforms remain under MIT — the transform is colour-substitution only, not a re-draw.
- **Feather (MIT):** preserve copyright notice.
- **Iconoir (MIT):** preserve copyright notice.
- **Material Symbols (Apache-2.0):** preserve copyright notice and attribution.

## Transformation statements

Two kinds of derivation are applied to upstream SVGs:

1. **Rename-only** — no visual change, file renamed with source prefix
   (stroke/, solid/, duotone/ from native variants).

2. **Two-tone colour transform** (duocolor/) — the base `fill="currentColor"`
   is replaced with `fill="var(--uip-icon-primary, currentColor)"` and the
   `opacity="0.2"` backing layer is replaced with
   `fill="var(--uip-icon-secondary, #7c3aed)"` at `opacity="0.35"`. No
   path data is altered; this is a CSS custom-property re-binding, which
   is arguably not a derivative work in any strict sense.

3. **Lucide synth** (duotone/, duocolor/ with `lu-` prefix) — the original
   `<path>`, `<rect>`, `<circle>`, `<polygon>`, `<ellipse>`, `<line>` elements
   are duplicated into a backing fill layer at 0.2 opacity, keeping the
   original stroke layer on top. No path data is altered; the transform
   is geometric duplication only.

No upstream was re-drawn, no Pro-tier (paid) proprietary icon was copied.
The intent is to provide Untitled UI Pro tier equivalents from permissive
licenses only.

## Fair-use statement

These files are consolidated as an internal, non-commercial research
reference for a single-user project (Clawmachine) to evaluate
visual-identity primitives against Pro-tier UI kits. Files are NOT
redistributed publicly and are NOT part of any shipped product. If any
upstream maintainer objects to the derivative transform, contact the
operator and the affected files will be removed.

## Quick attribution block (for any shipped derivative work)

```
Icons derived from:
- Lucide    (ISC)           https://lucide.dev
- Phosphor  (MIT, 2020-)    https://phosphoricons.com  — © Phosphor Icons
- Feather   (MIT, 2017-)    https://feathericons.com   — © Cole Bemis
- Iconoir   (MIT, 2021-)    https://iconoir.com        — © Luca Burgio
- Material Symbols (Apache-2.0, Google) https://fonts.google.com/icons
```
