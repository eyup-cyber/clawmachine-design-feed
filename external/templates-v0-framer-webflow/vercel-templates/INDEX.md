# Vercel Template Marketplace

**Source:** https://vercel.com/templates
**Scraped:** 2026-04-21
**Scope:** AI category + Next.js category
**License:** Open-source templates (most MIT / Apache). Each link in `metadata.json` goes to a GitHub repo under `vercel-labs` or the template author.

Vercel templates are first-party, production-grade, AND usually come with cloneable GitHub repos - unlike v0 previews. For the Clawmachine stitch this is the single most VALUABLE external source because source code IS portable.

## Top 10 Clawmachine-fit picks

Ranked by immediate stitch value (chatbot, agent, multi-tenant, MCP, Workflow, Slack integration, AI SDK):

1. **AI SDK Computer Use** (`next.js/ai-sdk-computer-use`) - Open-source AI agent demonstrating Claude Sonnet's computer-use capabilities, built with Next.js + Vercel Sandbox + AI SDK. Top fit for Clawmachine's agentic layer.
2. **AI Research Agent** (`next.js/ai-research-agent`) - AI research agent that runs 5 parallel browsers via Stagehand + Browserbase. Direct parallel-browser pattern for scout-bridge.
3. **Coding Agent Platform** (`next.js/coding-agent-platform`) - Run coding agents in Vercel AI Cloud with Vercel Sandbox + AI Gateway. Sandbox + gateway wiring as template.
4. **Tersa: AI Workflow Canvas** (`next.js/tersa-ai-workflow-canvas`) - Free, open-source template for building image/video workflows using AI Gateway. Closest analogue to an agentic flowchart surface.
5. **Workflow Builder** (`next.js/workflow-builder`) - Free, open-source template for visual workflow automation.
6. **Chatbot** (`next.js/chatbot`) - Full-featured, hackable Next.js AI chatbot by Vercel. The baseline for any chat surface.
7. **Chatbot by Aceternity** (`next.js/chatbot-by-aceternity`) - Modern interactive chatbot with AI SDK, Aceternity UI, and Neon serverless Postgres. Aceternity UI is already in the Clawmachine codex (`claude-design-feed/external/aceternity-ui-pro`).
8. **Vibe Coding Platform** (`next.js/vibe-coding-platform`) - End-to-end text-to-app coding platform. Parallel reference to v0's v0 Agent Builder.
9. **Lead Agent** (`next.js/lead-processing-agent`) - Inbound lead qualification + research agent built with AI SDK + Workflow DevKit + Vercel Slack Adapter. Template for operator-inbox/triage.
10. **MCP Apps Next.js Starter** (`next.js/mcp-apps-next-js-starter`) - MCP Apps = provider-agnostic open standard for embedded UIs. Stitch point for the MCP-first Clawmachine direction.

## Other notable catches

- **Platforms Starter Kit** (`next.js/platforms-starter-kit`) - multi-tenant apps with App Router + Redis
- **Stripe Subscription Starter** (`next.js/subscription-starter`) - Stripe + Supabase + Vercel
- **Morphic** (`next.js/morphic-ai-answer-engine-generative-ui`) - AI answer engine with generative UI
- **Swift - AI Voice Assistant** (`next.js/swift-ai-voice-assistant`) - Groq + Cartesia + VAD
- **OpenAI Assistants Quickstart** (`next.js/openai-assistants-quickstart`) - OpenAI Assistants + Next.js
- **Gemini AI Chatbot** (`next.js/gemini-ai-chatbot`) - Gemini + AI SDK + Next.js + React (relevant to Clawmachine's Gemma-4 wish)
- **Vercel x xAI Chatbot** (`next.js/vercel-x-xai-chatbot`) - xAI + Next.js + AI SDK
- **Pinecone AI SDK Starter** (`next.js/pinecone-vercel-ai`) - RAG + Pinecone
- **No Schema Output Mode** (`next.js/ai-sdk-no-schema`) - streamObject without schema
- **Automatic Tool Call Roundtrips** (`next.js/ai-sdk-roundtrips`) - streamText multi-tool orchestration
- **Advanced AI Bot Protection** (`next.js/advanced-ai-bot-protection`) - Kasada integration to block abusive LLM calls
- **AI Chat Telemetry** (`next.js/ai-chatbot-telemetry`) - OTel-wired Vercel AI SDK chatbot

## Notes

- All templates cloneable via `Deploy / Clone` from the template page. GitHub URL is usually `github.com/vercel-labs/<slug>` or similar.
- Licenses typically MIT / Apache. Each repo has its own LICENSE file - check per-item before redistribution.
- Vercel AI SDK is the unifying layer across 80% of these templates.
- DO NOT confuse with v0 templates: Vercel Templates = cloneable repos; v0 templates = AI-generated previews that you must fork inside v0.
