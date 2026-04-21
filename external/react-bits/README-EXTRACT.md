# React Bits — README-EXTRACT

**Upstream**: https://github.com/DavidHDev/react-bits
**Clone**: `git clone --depth 1` (shallow)
**Size on disk**: ~117 MB
**License**: **MIT + Commons Clause v1.0** — see `LICENSE_NOTE.md` (this is NOT pure MIT).

## What this is

David Haz's animated React component gallery — 110+ motion-first components (animated backgrounds, text effects, interactive cards, 3D viewers). Exists in four parallel implementations: JS + default CSS, JS + Tailwind, TS + default CSS, TS + Tailwind. Reference for "what does modern motion-forward React UI look like when the goal is visual impact, not composability."

## Key folders for reference

The repo is a Vite React app that *both* demos the components and ships them as copy-paste source. The actual component source is split across four parallel folders so consumers can pick a style/language variant:

| Path | What's in it |
|---|---|
| `src/ts-tailwind/Animations/` | **TypeScript + Tailwind: animation primitives** |
| `src/ts-tailwind/Backgrounds/` | **TS + Tailwind: animated backgrounds** (Aurora, Beams, Gradient, Grid, Hyperspeed, Iridescence, Meteors, Particles, Plasma, Ripple, Silk, Squares, Threads, Waves…). |
| `src/ts-tailwind/Components/` | **TS + Tailwind: ~35 interactive components**: AnimatedList, BorderGlow, BounceCards, BubbleMenu, CardNav, CardSwap, Carousel, ChromaGrid, CircularGallery, Counter, DecayCard, Dock, DomeGallery, ElasticSlider, FlowingMenu, FluidGlass, FlyingPosters, Folder, GlassIcons, GlassSurface, GooeyNav, InfiniteMenu, Lanyard, MagicBento, Masonry, ModelViewer, PillNav, PixelCard, ProfileCard, ReflectiveCard, ScrollStack, SpotlightCard, Stack, StaggeredMenu, Stepper, TiltedCard … |
| `src/ts-tailwind/TextAnimations/` | **TS + Tailwind: text animations** (BlurText, CircularText, CountUp, DecryptedText, FallingText, GlitchText, GradientText, RotatingText, ScrambledText, ScrollFloat, ScrollReveal, ScrollVelocity, ShinyText, SplitText, TextCursor, TextPressure, TextReveal, TextTrail, TrueFocus, VariableProximity…). |
| `src/ts-default/` | same four categories in TS + default CSS (no Tailwind). |
| `src/Animations/`, `src/Backgrounds/`, `src/Components/`, `src/TextAnimations/` (at top of `src/`?) | If present, these are the JS + default CSS variants. |

Pick one variant and ignore the others. **Recommendation: `ts-tailwind/` is the most house-ready, matches the stack Mantine/Chakra consumers use, and Tailwind is already present elsewhere in our design-feed.**

## Boilerplate (skip)

- `src/{App.jsx, main.jsx, pages/, demo/, docs/}` — the Vite demo app scaffolding, not the library itself.
- `src/{assets, content, css, hooks, tailwind, tools, utils}/`, `src/styles.css`, `src/global.d.ts`, `src/vite-env.d.ts` — app wiring.
- `public/`, `scripts/`, `jsrepo.config.ts`, `package.json`, `package-lock.json`, `tsconfig.json`, `vite.config.js`, `wrangler.jsonc`, `index.html`, `CONTRIBUTING.md`, `README.md` — tooling.

**Important**: the `Liquid Glass` / `FluidGlass` / `GlassSurface` / `GlassIcons` / `ReflectiveCard` family is exactly the frosted/translucent Apple-style aesthetic flagged in `memory/feedback_visual_antithesis_liquid_glass.md` as **anti-goal**. Do NOT carry these forward into the Frankenstein stitch — note them and skip.

## Recommended entry points for Frankenstein stitch

1. **Text animations**: `src/ts-tailwind/TextAnimations/GlitchText.tsx`, `ScrambledText.tsx`, `DecryptedText.tsx`, `VariableProximity.tsx` — aligns with the motion-as-accent / retro-industrial direction. Candidate carry-forward.
2. **Backgrounds**: `Aurora.tsx`, `Silk.tsx`, `Threads.tsx`, `Waves.tsx` — restrained animated backgrounds. `Hyperspeed.tsx`, `Plasma.tsx`, `Iridescence.tsx` are the anti-goal (too much).
3. **PixelCard / DecayCard / TiltedCard / ProfileCard** — visually distinctive card treatments worth stealing selectively per-theme (per `feedback_visual_restraint_decoration.md`, don't apply wholesale).
4. **Components to actively ignore**: the whole Glass-* family, MagicBento (too busy), GooeyNav (kitsch), Lanyard (novelty).
