# Ethnography Research Hub

Netnographic research into AI/crypto online communities. Structured for a practitioner-outsider (engineering background, VC-adjacent) trying to understand and engage credibly with communities forming around AI agents, e/acc, prediction markets, and the a16z ecosystem.

**How to use this repo:**
- **Obsidian users:** Open this folder as a vault → `Cmd+G` for graph view → start at [HOME.md](HOME.md)
- Start at [`theory/philosophical-roots.md`](theory/philosophical-roots.md) — every community draws from these 11 intellectual threads
- Use [`theory/argument-map.md`](theory/argument-map.md) to understand who is arguing with whom right now
- Read [`communities/`](communities/) for community-specific intelligence
- Check [`sources/canonical-texts.md`](sources/canonical-texts.md) for anchored primary sources
- Run `/ethnography-ingest <url>` to add new sources

---

## Directory Navigator

### `theory/` — The Intellectual Backbone

| File | Purpose |
|------|---------|
| [`philosophical-roots.md`](theory/philosophical-roots.md) | 11 intellectual threads tracing the ideological DNA of each community. Start here. |
| [`argument-map.md`](theory/argument-map.md) | Fault lines between threads — who is arguing with whom, and which debates are heating up now. |

### `methods/` — How to Research

| File | Purpose |
|------|---------|
| [`netnography.md`](methods/netnography.md) | Research method, the `summarize` CLI workflow, credibility tiers, research debt tracker. |
| [`community-pulse-monitoring.md`](methods/community-pulse-monitoring.md) | 30-min/week monitoring protocol across signal sources. |
| [`signal-cascade.md`](methods/signal-cascade.md) | Lead/lag timing map — all 23 communities mapped to signal sources, extraction methods, API endpoints. |

### `communities/` — Field Profiles

| Community | Status | Core Threads |
|-----------|--------|-------------|
| [`ai-maxxers.md`](communities/ai-maxxers.md) | Active | 1, 3, 6 |
| [`a16z-ecosystem.md`](communities/a16z-ecosystem.md) | Active | 1, 5, 6 |
| [`ai-agent-tokens.md`](communities/ai-agent-tokens.md) | Active | 7, 8 |
| [`memecoin-culture.md`](communities/memecoin-culture.md) | Active | 8 |
| [`prediction-markets.md`](communities/prediction-markets.md) | Active | 4, 3 |
| [`red-pill-black-pill.md`](communities/red-pill-black-pill.md) | Active | 6, 8 |
| [`tiktok-creators.md`](communities/tiktok-creators.md) | Active | 8 |
| [`crypto-twitter.md`](communities/crypto-twitter.md) | Active | 5, 8 |
| [`network-states.md`](communities/network-states.md) | Active | 5, 6 |
| [`proof-of-personhood.md`](communities/proof-of-personhood.md) | Active | 5, 9 |
| [`agentic-governance.md`](communities/agentic-governance.md) | Active | 7, 5 |
| [`hyperliquid.md`](communities/hyperliquid.md) | Active | 5, 3, 8 |
| [`groyper-pipeline.md`](communities/groyper-pipeline.md) | Active | 6, 1, 8 |
| [`solana-dev-culture.md`](communities/solana-dev-culture.md) | Active | 3, 5, 7 |
| [`desci.md`](communities/desci.md) | Active | 5, 2, 3 |
| [`refi-public-goods.md`](communities/refi-public-goods.md) | Active | 10, 2, 4 |
| [`regulatory-layer.md`](communities/regulatory-layer.md) | Active | 5, 6, 4 |
| [`politifi.md`](communities/politifi.md) | Active | 8, 6, 5 |
| [`farcaster-warpcast.md`](communities/farcaster-warpcast.md) | Active | 5, 7 |
| [`open-source-ai.md`](communities/open-source-ai.md) | Active | 1, 2, 5, 10 |
| [`rwa-stablecoin.md`](communities/rwa-stablecoin.md) | Active | 5, 4, 6 |

### `sources/` — Evidence Base

| File | Purpose |
|------|---------|
| [`canonical-texts.md`](sources/canonical-texts.md) | Primary sources with thread tags, credibility tiers, and analytical use notes. |
| [`capital-thesis-map.md`](sources/capital-thesis-map.md) | Who is funding the AI/crypto intersection — VC and AI lab positions, the collision course, and who wins. |
| [`ai-substack-discourse.md`](sources/ai-substack-discourse.md) | Four-tier Substack map (thesis formation → counter-discourse). |
| [`seed-lists.md`](sources/seed-lists.md) | Tiered Twitter/X handles, Telegram observation points, market data sources. |
| [`analytical-lenses-troemel-contrapoints.md`](sources/analytical-lenses-troemel-contrapoints.md) | Brad Troemel (attention-as-sport) and ContraPoints (aesthetic radicalization pipeline) as analytical lenses. |
| [`deep-reads/`](sources/deep-reads/) | Full-text extractions and multimedia summaries. |

### `reports/` — Synthesized Intelligence

| File | Purpose |
|------|---------|
| [`where-the-puck-goes.md`](reports/where-the-puck-goes.md) | Strategic synthesis — AI/crypto/prediction market convergence and positioning. |
| [`game-theory-synthesis.md`](reports/game-theory-synthesis.md) | Why communities behave as they do — 5 game structures with cross-community dynamics. |
| [`forward-deployed-engineers.md`](reports/forward-deployed-engineers.md) | FDE model deep dive — Palantir origin, diffusion across enterprise AI. |
| [`template.md`](reports/template.md) | Weekly deep dive + 1-page shareable summary template. |

---

## Spectrum Map: The 2026 Techno-Capital Ecosystem

| Quadrant | Core Thesis | Primary Community | Key Conflict (2026) |
|----------|-------------|-------------------|----------------------|
| **The Accelerationist Layer** | "Accelerate or Die" | **e/acc** / AI Maxxers | **Institutional Hollowing** vs. **Thermodynamic Vitalism** |
| **The Attention Layer** | "Attention = Value" | **Memecoins** / CT | **Speculative Alpha** vs. **KOL Wash-Trading** |
| **The Epistemic Layer** | "Markets = Truth" | **Prediction Markets** | **Western Epistemics** (Polymarket) vs. **Eastern Liquidity** (O.LAB) |
| **The Sovereignty Layer** | "Self-Sovereignty" | **d/acc** / Network States | **AI Agent Autonomy** vs. **Human Biometric Gating** |

---

## Research Workflow

**Adding a new source:**
```
/ethnography-ingest <url>
```
Runs `summarize`, maps to threads, formats entry for `sources/canonical-texts.md`.

**Researching a missing community:**
```
/ethnography-ingest community farcaster
```
Searches for primary sources, summarizes 2-3, drafts community profile.

**Batch processing seed list:**
```
/ethnography-ingest batch
```
Identifies unprocessed URLs in `sources/seed-lists.md` and runs Mode 1 on each.

---

## Active Fault Lines (Feb 2026)

See [`theory/argument-map.md`](theory/argument-map.md) for full analysis. Current heat map:

| Debate | Heat |
|--------|------|
| Can AI self-regulate? (e/acc vs EA) | High |
| Open vs. closed AI | High |
| Exit or transform? (NRx vs L/ACC) | Medium |
| Can markets replace epistemics? | Medium |
| Is agent autonomy real or performed? | Medium |
| Who is "permissionless" for? | Low-Medium |

---

*Ethics: public sources only, no doxxing, no individual targeting. See [`ethics.md`](ethics.md).*
