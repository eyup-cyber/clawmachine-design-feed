# design-to-code — LICENSE & SOURCING NOTE

**Scrape date:** 2026-04-21
**Operator:** Regan Cooney (regacooney@gmail.com)

## Contents

- `recreated/` — 10 HTML structural approximations covering Supabase UI (auth, realtime-chat, dropzone), Convex templates (fullstack, realtime-chat), Builder.io (visual-editor sample), Plasmic, Locofy, shadcn dashboard, Radix Themes.
- `metadata.json` — 5 platform entries with URL, GitHub, licence, stack, Clawmachine-fit rating, and carry-forward notes.

## Why no `previews/` directory

The design-to-code platforms surveyed here (Supabase UI / Convex / Builder.io / Plasmic / Locofy) are primarily developer-facing component libraries or visual builders. A 1440x900 preview of their homepage captures the marketing surface, not the actual component output. Value is in the carried-forward code, not the marketing screenshot.

## Licence posture — upstream

- **Supabase UI** (github.com/supabase-community/supabase-ui) — **MIT**. Drop-in if Clawmachine backend uses Supabase. Carry forward the LICENSE file if components are imported.
- **Convex** — templates are community-contributed, per-template licence. Check each.
- **Builder.io / Plasmic / Locofy** — proprietary visual builders. Output code is yours under the tier you pay for; the builder itself is not redistributable.
- **shadcn/ui** — **MIT**, copy-paste component library.
- **Radix UI / Radix Themes** — **MIT**.

## Licence posture — recreated HTML

The `recreated/*.html` files are authored approximations of the documented component behaviours (password-strength meter, realtime-chat window, upload dropzone, workflow-canvas node graph). No upstream component code was imported. Every recreation has a visible footer crediting the platform and linking to the source documentation.

## Fair-use basis

UK fair-dealing for non-commercial research. MIT-licensed components can be copy-pasted into the Clawmachine build under the upstream LICENSE; proprietary builders (Builder.io / Plasmic) remain out of scope unless paid tiers are adopted.
