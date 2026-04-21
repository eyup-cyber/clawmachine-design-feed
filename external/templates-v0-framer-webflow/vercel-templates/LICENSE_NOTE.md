# vercel-templates — LICENSE & SOURCING NOTE

**Scrape date:** 2026-04-21
**Operator:** Regan Cooney (regacooney@gmail.com)

## Contents

- `recreated/` — 10 HTML structural approximations of top vercel.com/templates entries (AI SDK Computer Use, AI Research Agent, Tersa Workflow Canvas, Chatbot, Coding Agent Platform, Platforms Starter, Commerce, Liveblocks Starter, MCP Next.js Starter, Stripe Subscription Starter).
- `metadata.json` — full catalogue: 41 AI-category templates + 27 Next.js-category templates with slugs, authors, frameworks, integrations, and Clawmachine-fit flags.
- `INDEX.md` — top picks ranked for Clawmachine carry-forward.

## Why no `previews/` directory

Vercel templates are open-source projects (typically MIT/Apache licensed) hosted at `github.com/vercel-labs/<slug>`. The best way to use them is `vercel clone <slug>` or a direct git clone — a preview PNG adds nothing that the live deploy or the README doesn't cover. The hero images on the vercel.com/templates index page are marketing renders, not the actual app UI.

## Licence posture — upstream

Most vercel-labs templates are permissively licensed (MIT or Apache-2.0). Per-template licensing is at `github.com/vercel-labs/<slug>/LICENSE`. If the Clawmachine build incorporates any of these, carry the original licence file forward.

## Licence posture — recreated HTML

The `recreated/*.html` files in this directory are authored approximations for research reference. They are NOT a substitute for the actual template; they only show the layout pattern we would expect to see when running each template locally.

## Fair-use basis

UK fair-dealing for non-commercial research. To actually use any of these templates: `git clone github.com/vercel-labs/<slug>` and follow the upstream README.
