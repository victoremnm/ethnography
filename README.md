# Ethnography Research Hub

Netnographic research into AI/crypto online communities. Structured for a practitioner-outsider (engineering background, VC-adjacent) trying to understand and engage credibly with communities forming around AI agents, e/acc, prediction markets, and the a16z ecosystem.

**How to use this repo:**
- Start at `theory/philosophical-roots.md` — every community draws from these 11 intellectual threads
- Use `theory/argument-map.md` to understand who is arguing with whom right now
- Read `communities/` for community-specific intelligence
- Check `sources/canonical-texts.md` for anchored primary sources
- Run `/ethnography-ingest <url>` to add new sources

---

## Directory Navigator

### `theory/` — The Intellectual Backbone

| File | Purpose |
|------|---------|
| `philosophical-roots.md` | 11 intellectual threads tracing the ideological DNA of each community. Start here. |
| `argument-map.md` | Fault lines between threads — who is arguing with whom, and which debates are heating up now. |

### `methods/` — How to Research

| File | Purpose |
|------|---------|
| `netnography.md` | Research method, the `summarize` CLI workflow, credibility tiers, research debt tracker. |

### `communities/` — Field Profiles

| Community | Status | Core Threads |
|-----------|--------|-------------|
| `ai-maxxers.md` | Active | 1, 3, 6 |
| `a16z-ecosystem.md` | Active | 1, 5, 6 |
| `ai-agent-tokens.md` | Active | 7, 8 |
| `memecoin-culture.md` | Active | 8 |
| `prediction-markets.md` | Active | 4, 3 |
| `red-pill-black-pill.md` | Active | 6, 8 |
| `tiktok-creators.md` | Active | 8 |
| `bjj-community.md` | Analogy | Status mechanics |
| `cedh-community.md` | Analogy | Competitive subculture |
| `lambda-phi-epsilon.md` | Active | Initiation culture |
| `crypto-twitter.md` | Active | 5, 8 |
| **Farcaster / Warpcast** | 🔴 Missing | 5, 7 |
| **DeSci** | 🔴 Missing | 2, 5 |
| **Open-Source AI** | 🔴 Missing | 1, 2 |
| **RWA / Stablecoin** | 🔴 Missing | 5 |
| **Regulatory Layer** | 🔴 Missing | 5, 6 |

### `sources/` — Evidence Base

| File | Purpose |
|------|---------|
| `canonical-texts.md` | Primary sources with thread tags, credibility tiers, and analytical use notes. |
| `ai-substack-discourse.md` | Four-tier Substack map (thesis formation → counter-discourse). |
| `seed-lists.md` | Tiered Twitter/X handles, Telegram observation points, market data sources. |
| `analytical-lenses-troemel-contrapoints.md` | Brad Troemel (attention-as-sport) and ContraPoints (aesthetic radicalization pipeline) as analytical lenses. |

### `reports/` — Synthesized Intelligence

| File | Purpose |
|------|---------|
| `where-the-puck-goes.md` | Strategic synthesis — AI/crypto/prediction market convergence and positioning. |
| `forward-deployed-engineers.md` | FDE model deep dive — Palantir origin, diffusion across enterprise AI. |
| `template.md` | Weekly deep dive + 1-page shareable summary template. |

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

See `theory/argument-map.md` for full analysis. Current heat map:

| Debate | Heat |
|--------|------|
| Can AI self-regulate? (e/acc vs EA) | 🔥🔥 |
| Exit or transform? (NRx vs L/ACC) | 🔥 |
| Can markets replace epistemics? | 🔥 |
| Is agent autonomy real or performed? | 🔥 |
| Who is "permissionless" for? | 🌡 |
| Open vs. closed AI (emerging) | 🌡 |

---

*Ethics: public sources only, no doxxing, no individual targeting. See `ethics.md`.*
