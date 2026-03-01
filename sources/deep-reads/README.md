# Deep Reads — Full Extractions & Multimedia Summaries

Full-text extractions and multimedia summaries of high-signal sources. Content here feeds back into community dossiers in `communities/` — the dossiers hold the analysis; this directory holds the raw material.

## Workflow

```bash
# Extract full text of a web article (no API key needed)
summarize "https://..." > sources/deep-reads/<slug>.md

# Summarize with AI (requires ANTHROPIC_API_KEY or OPENAI_API_KEY)
ANTHROPIC_API_KEY=$(op read "op://Personal/Anthropic API/credential") \
  summarize --length xl "https://..."

# YouTube transcript + slides (requires yt-dlp: brew install yt-dlp)
brew install yt-dlp
ANTHROPIC_API_KEY=... summarize --youtube auto --slides --length xl "https://youtube.com/..."
```

## Setup for Full Capability

`summarize` v0.10.0 works in two modes:
- **Extraction only** (no key): Returns full article text. Useful for web articles.
- **AI summary** (needs key): Condenses + structures content. Better for long video transcripts.

```bash
# One-time: store key in 1Password
op item create --category login --title "Summarize CLI" --vault Personal \
  "ANTHROPIC_API_KEY[password]=sk-ant-..."

# Per-session use
export ANTHROPIC_API_KEY=$(op read "op://Personal/Summarize CLI/ANTHROPIC_API_KEY")
```

## Priority Sources for Multimedia Enrichment

| Source | Type | Community | Priority |
|--------|------|-----------|----------|
| a16z YouTube: "AI Agents" talks | Video | AI agents, VC thesis | High |
| Bankless podcast episodes on prediction markets | Audio/Video | Prediction markets | High |
| Balaji Srinivasan: Network State talks | Video | Crypto sovereignty | High |
| Zvi Mowshowitz: recorded AI safety talks | Video | Rationalist/safety | Medium |
| Scott Alexander: EA Global presentations | Video | EA/Longtermism | Medium |
| EigenLayer verifiable inference explainers | Video | Agent infrastructure | Medium |

## Naming Convention

`<source>-<slug>-<YYYY-MM>.md`

Examples:
- `bankless-agent-economy-ethereum-2026-02.md`
- `a16z-ai-agents-infrastructure-2026-01.md`
- `vitalik-ethereum-ai-framework-2026-02.md`
