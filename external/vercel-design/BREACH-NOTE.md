# Vercel April 2026 security incident — provenance note for this folder

## What happened (facts, not speculation)

On 2026-04-19 Vercel disclosed a security incident. Root cause: OAuth supply-chain compromise. A Vercel employee installed a Context AI application and linked it to their Google Workspace account; a Context AI employee had been infected with Lumma Stealer in February 2026, which gave attackers the OAuth tokens to pivot into the Vercel employee's Google account and from there into "certain internal Vercel systems" and "environment variables not marked as sensitive."

A threat actor claiming ShinyHunters affiliation (ShinyHunters publicly denied) listed what they called Vercel customer API keys, source code, and database records for $2M on BreachForums. Vercel has brought in Mandiant, said services remain operational, and urged customers to rotate secrets.

## What's in this folder

All assets here are **public Vercel web presence** — marketing pages, Geist fonts, `_next/static` CSS chunks scraped from `vercel.com` on 2026-04-21 (two days after breach disclosure).

**None of this touches the breach payload.** The breach is about internal OAuth / env-vars / customer data. Our scrape is of the production CDN that every anonymous visitor to vercel.com downloads.

## Risk evaluation for Clawmachine feed use

| Asset class | Breach risk | Handling |
|---|---|---|
| Geist fonts (woff2) | None — OFL, git-verifiable upstream at `github.com/vercel/geist-font`. CDN scrape risk: theoretical CDN tampering during breach window. | **SWAPPED.** The 8 CDN-scraped `.woff2` files at `css/fonts/` have been DELETED. Replaced by git-cloned upstream at `fonts-from-git/` (sha-verifiable commit). |
| CSS bundles from `_next/static/immutable/chunks/` | Low — CSS cannot execute code. Presentation-layer only. | KEPT, but reference-only. Do NOT `<link>` these into the app runtime. They exist so you can trace a token to its extracted value. |
| Scraped marketing page HTML (`html/`) | Low — static HTML reference. | KEPT, reference-only. |
| Extracted design tokens (`tokens/design-tokens.json`) | None — derived from public computed styles. | KEPT. Safe to use. |
| Signature pattern HTMLs (`patterns/*.html`) | None — authored by our agent, use only Vercel's public token values. | KEPT. Safe to use. |

## Decision

Keep the Vercel design reference in the feed. The aesthetic language is not what was breached. Replace anything fetched from the Vercel CDN during the post-disclosure window with git-verifiable upstream where an equivalent exists (fonts done; CSS bundles are immutable-hash chunks with no OSS equivalent and are reference-only anyway).

**Do not use any CSS bundle from `css/` as a runtime import.** Claude Design can read them to understand the token system; the app shouldn't load them.

## Sources

- [Vercel April 2026 security incident — Vercel Knowledge Base](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)
- [Vercel confirms breach as hackers claim to be selling stolen data — BleepingComputer](https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/)
- [App host Vercel says it was hacked and customer data stolen — TechCrunch](https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/)
- [Vercel Breach Tied to Context AI Hack Exposes Limited Customer Credentials — The Hacker News](https://thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html)
- [The Vercel Breach: OAuth Supply Chain Attack Exposes the Hidden Risk in Platform Environment Variables — Trend Micro](https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html)
- [Vercel Employee's AI Tool Access Led to Data Breach — Dark Reading](https://www.darkreading.com/application-security/vercel-employees-ai-tool-access-data-breach)
