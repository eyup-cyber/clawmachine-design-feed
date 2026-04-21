# Design-to-Code Platform Templates

**Source:** Locofy.ai, Builder.io, Plasmic, Supabase UI, Convex UI
**Scraped:** 2026-04-21
**Scope:** each platform's public demo + template gallery
**License:** Fair-use reference. Each platform has its own terms.

These are platforms that OUTPUT React/Vue/etc from design artifacts. Their VALUES for the Clawmachine stitch:
- Supabase UI - actual React components (shadcn-based, Tailwind, MIT) - **cloneable and mergeable**
- Builder.io / Plasmic / Locofy - reference to the "design-to-code bridge" pattern, not primary sources

## Supabase UI Library (primary pickup)

- **URL:** https://supabase.com/ui
- **GitHub:** https://github.com/supabase-community/supabase-ui
- **License:** MIT
- **Stack:** Next.js + Tailwind + Shadcn + Supabase Auth helpers
- **What's in it:** Password input with zxcvbn strength meter, Auth UI (login/signup flows), Dropzone, Realtime-cursor cursor sharing, current-user avatar, infinite query hook, realtime chat, file upload via dropzone
- **Clawmachine fit: HIGH** - if the Clawmachine backend ever moves to Supabase Auth/Realtime these components are a drop-in.

## Convex UI examples

- **URL:** https://www.convex.dev/templates
- **Stack:** Convex (backend DB) + multiple frontend choices
- **Notable templates:**
  - `fullstack-convex` - Convex + Next.js + Clerk + Tailwind + Aceternity UI
  - `convex-chat` - realtime chat starter
  - `convex-web-voyager` - agentic web voyager reference
  - `fullstack-convex` + resend, multi-tenant
- **Clawmachine fit: MEDIUM** - Convex is a real-time DB with strong TS types; might not fit the Swift-backbone direction but worth mention for fast iteration.

## Builder.io Templates

- **URL:** https://www.builder.io/examples
- **Notable:** Visual CMS + React/Vue/Angular/Qwik output
- **Vercel-template direct-use:** `next.js/builderio-shopify-commerce-headless`
- **Clawmachine fit: LOW** - no dashboard templates; visual CMS for marketing sites.

## Plasmic Examples

- **URL:** https://www.plasmic.app/examples
- **Notable:** Visual builder that outputs React/Next.js code; component-library bridge
- **Stack:** React/Next.js + your own components
- **Clawmachine fit: LOW** - same reasoning; marketing-site oriented.

## Locofy.ai Templates

- **URL:** https://www.locofy.ai/templates
- **Notable:** Figma/Adobe XD -> React/Next.js/React Native code
- **Stack:** exports to any framework
- **Clawmachine fit: LOW-MEDIUM** - it's a translation layer not a template source. Useful if porting a purchased Figma UI kit (see `figma-community-top/`) into the Clawmachine repo.

## Summary

- **Primary pickup:** Supabase UI (MIT, direct git-clone-able).
- **Secondary:** Convex templates (if backend direction shifts).
- **Skip for now:** Builder.io / Plasmic / Locofy - good bridges, no dashboard templates of their own.
