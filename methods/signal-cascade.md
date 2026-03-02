# Signal Cascade: Lead/Lag Timing Map

**Purpose:** Map every signal source to its position in the information cascade — how many days/weeks before or after mainstream crypto discourse a signal appears. Use this to extract maximum intelligence from minimum monitoring time.

**Key principle:** The same narrative exists simultaneously at multiple layers. On-chain data reflects it in hours; Reddit reflects it weeks later. The researcher's job is to triangulate across layers, not just monitor the most accessible one.

---

## The Cascade Model

```
HOURS ──────────────────────────────────────── WEEKS

On-Chain  →  Telegram  →  GitHub/Farcaster  →  X Tier 2  →  Kaito/LessWrong  →  X Tier 1  →  HN/Substack  →  Reddit  →  YouTube  →  Media
(behavioral)  (insider)    (builders)           (analysts)  (ideas)             (consensus)  (synthesized)    (retail)    (lag)       (lagging)
```

Three fundamentally different signal types:
- **Behavioral traces** (on-chain, GitHub stars): what people *did*, unfalsifiable
- **Community artifacts** (X, Telegram, Reddit): what people *said*, may be performed
- **Epistemic aggregates** (Kaito, Polymarket, LessWrong): what communities *believe*, compressed

The most powerful analysis comes from divergence between layers — when behavioral traces contradict stated community beliefs.

---

## Timing Map

| Source | Lead (+) / Lag (-) | Type | Primary Utility | Coverage |
|--------|-------------------|------|-----------------|----------|
| On-chain DEX/Dune | +7–30 days | Behavioral | Ground truth for crypto communities | Memecoins, DeFi, RWA, Solana |
| Telegram alpha | +3–7 days | Community artifact | Insider narrative formation | Memecoins, AI agents |
| GitHub star velocity | +3–10 days | Behavioral | Dev attention to OSS projects | Open-source AI, Solana devs, DeSci |
| Farcaster trending | +2–7 days | Community artifact | Crypto-native builder discourse | Farcaster, AI agents, DeSci |
| LessWrong / EA Forum | +7–28 days (ideas) | Analysis | Rationalist thesis formation | AI safety, DeSci, Prediction markets |
| arXiv preprints | +7–21 days | Primary source | Technical leadership signals | Open-source AI, DeSci, Prediction markets |
| X Tier 2 (pseudonymous) | +1–5 days | Community artifact | Narrative seeding | All crypto/AI |
| Kaito mindshare | +1–3 days | Signal aggregate | CT narrative heat map | All crypto |
| Polymarket / Kalshi prices | Coincident | Epistemic aggregate | Market-consensus probability | Prediction markets, Regulatory, PolitiFi |
| X Tier 1 KOLs | Neutral | Community artifact | Narrative confirmation | All |
| Hacker News | -7–14 days | Community artifact | OSS AI developer attention | Open-source AI, DeSci |
| Substack essays | -7–21 days | Analysis | Synthesized narrative | All |
| Reddit (AI subs) | -14–42 days | Community artifact | Developer retail consciousness | Open-source AI |
| Reddit (crypto subs) | -14–60 days | Community artifact | Retail crypto consciousness | Memecoins, Solana, DeFi |
| YouTube / podcasts | -28–84 days | Community artifact | Mass-market narrative framing | All |
| Mainstream media | -42–180 days | Counter-discourse | Institutional reception | Regulatory, Network states |

**Reading the table:** A "+7 days" lead means this source typically reflects a narrative 7 days *before* it becomes visible on mainstream X/CT. A "-14 days" lag means it shows up 14 days *after*.

---

## Layer 1: On-Chain Behavioral (Most Leading — Hours to Days)

The blockchain is a public behavioral trace. Token purchases, DAO votes, and liquidity events happen before any social narrative forms around them.

**Primary tools:**
- Dune Analytics — `dune.com` (free, no login for reads)
- DEX Screener — `dexscreener.com/solana/pumpfun`
- GMGN.ai — `gmgn.ai/trend?chain=sol`
- DeFiLlama — `defillama.com` (TVL/protocol data)
- RWA.xyz — `rwa.xyz` (RWA tokenization data)
- Etherscan / Solscan (contract-level forensics)

**What to extract:**
- Token launch velocity on pump.fun (graduation rate = community engagement metric)
- Smart money wallet accumulation before CT narrative
- DAO vote participation rates (governance engagement proxy)
- TVL flows (capital conviction proxy for DeFi/RWA communities)
- NFT mint/transfer activity (attention economy proxy)

**Extraction method:**
```bash
# Requires: BRAVE_API_KEY set (see Environment Setup)
# Brave search for specific on-chain analytics
curl -s "https://api.search.brave.com/res/v1/web/search?q=site:dune.com+solana+memecoin&count=5" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}"

# DeFiLlama API (no auth required)
curl "https://api.llama.fi/tvl/aave"
curl "https://api.llama.fi/protocols" | jq '.[] | select(.category == "RWA") | {name, tvl}'
```

**For which communities:** Memecoins, Solana dev culture, RWA/Stablecoin, DeFi, AI agent tokens, Hyperliquid

---

## Layer 2: Alpha Networks (Leading — 1–7 Days)

Telegram alpha channels and private Discord servers are where insider narratives form. Most are invite-only and effectively inaccessible, but public entry points exist.

**Observable Telegram channels:**
- `@bonkbot_io`, `@BananaGunBot`, `@MaestroBots` — tool ecosystem signals
- `@rick_bot` — contract audits (research tool)
- Ephemeral token-launch groups (findable via X search of contract address in first 24h)

**Discord (partial access):**
- Solana Foundation Discord — `discord.gg/solana` — developer discussions accessible in public channels
- a16z Discord — select public channels
- DeSci ecosystem Discords — VitaDAO, Molecule, AthenaDAO
- Farcaster Neynar Discord — protocol development discussion

**Signal type:** Most leading for *which* narratives will hit X in 3–7 days, but requires network access for the highest-quality channels.

---

## Layer 3: Builder Discourse (Leading — 2–14 Days)

GitHub star velocity and Farcaster are the two most actionable leading indicators for technical narratives.

### GitHub (Leading for dev attention)

GitHub trending is the earliest public signal for which OSS AI projects and crypto tools are capturing developer attention. A repo going from 100 to 10,000 stars in a week will generate X discourse and HN coverage days later.

**Manual monitoring:**
- `github.com/trending` — daily/weekly trending repos, filter by language
- `github.com/topics/llm` — repos tagged with relevant topics
- `github.com/topics/ai-agent`, `ethereum`, `solana`, `prediction-market`

**GitHub API extraction:**
```bash
# Requires: GITHUB_TOKEN, BRAVE_API_KEY set (see Environment Setup)
THIRTY_DAYS_AGO=$(python3 -c "from datetime import date, timedelta; print(date.today() - timedelta(30))")

# Trending AI repos (by recent stars)
curl -s "https://api.github.com/search/repositories?q=topic:llm+stars:>500+pushed:>${THIRTY_DAYS_AGO}&sort=stars&order=desc&per_page=10" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}"

# Repos by star velocity (new repos gaining traction)
FOURTEEN_DAYS_AGO=$(python3 -c "from datetime import date, timedelta; print(date.today() - timedelta(14))")
curl -s "https://api.github.com/search/repositories?q=topic:ai-agent+created:>${FOURTEEN_DAYS_AGO}&sort=stars&order=desc&per_page=10" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}"

# Brave search for GitHub activity on specific topics
curl -s "https://api.search.brave.com/res/v1/web/search?q=site:github.com+\"ai+agents\"+stars&count=10" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}"
```

**For which communities:** Open-source AI (primary), Solana dev culture, DeSci, AI agent tokens, Farcaster ecosystem

**Star velocity heuristic:** Repos gaining >1,000 stars/week are generating community attention. >10,000 stars/week (like DeepSeek R1 at peak) indicates narrative inflection point that will dominate X and HN.

### Farcaster (as monitoring source, not just community)

Farcaster's builder-heavy composition makes it a leading indicator for crypto-native technical narratives — typically 2–5 days ahead of the same narrative appearing prominently on X CT.

**Monitoring without full embeds:**
```bash
# Requires: NEYNAR_KEY set (see Environment Setup)
# Get a free Neynar API key at: https://neynar.com
curl "https://api.neynar.com/v2/farcaster/feed/trending?limit=20" \
  -H "api_key: ${NEYNAR_KEY}"

# Dune Farcaster analytics (public dashboards)
# dune.com/neynar/farcaster-protocol-stats
# dune.com/pixelhack/farcaster

# Warpcast trending (browser-based, no API needed)
# warpcast.com/trending
```

**Brave search workaround for Farcaster:**
```bash
curl -s "https://api.search.brave.com/res/v1/web/search?q=site:warpcast.com+\"ai+agent\"&count=10" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}"
```

**For which communities:** Farcaster/Warpcast, AI agent tokens, Solana dev culture, Proof of Personhood, DeSci

---

## Layer 4: Epistemic Aggregators (Varied Timing)

These sources compress signals from other layers into ranked, quantified form.

### Kaito.ai (Leading 1–3 days for CT)

Kaito measures "mindshare" — the share of CT conversation a given topic captures. More accurate than raw mention counts because it weights by account quality.

**API access:** Kaito provides an API for mindshare scores (requires account, free tier).
- Weekly mindshare leaderboard: `kaito.ai/leaderboard`
- Narrative rotation visible when a topic's mindshare changes >20% week-over-week

**Research use:** Don't just read which topics are high — read which are *rising fastest*. A topic at 5% mindshare growing 50% week-over-week is more analytically interesting than one at 20% that's been stable.

### Polymarket / Kalshi (Coincident — Epistemic Barometer)

Prediction market prices are the compressed epistemic state of a community that has staked real money on outcomes. They're not leading indicators but coincident ones — they encode what the most informed participants believe *right now*.

**Why this matters for research:** The existence of a market tells you something is salient to forecasters. A moving price signals new information entering the ecosystem. A new market being created signals a topic is entering forecaster attention for the first time.

**Extraction:**
```bash
# Polymarket active markets (CLOB API, no auth required for reads)
curl "https://clob.polymarket.com/markets?active=true" | jq '.[] | {question, outcomePrices}'

# Search for markets on specific topics
curl "https://gamma-api.polymarket.com/markets?search=ai+regulation&active=true" \
  | jq '.[] | {question, endDate, outcomePrices}'

# Kalshi markets (REST API)
curl "https://trading-api.kalshi.com/trade-api/v2/markets?status=active&limit=100" \
  | jq '.markets[] | {title, yes_bid, yes_ask}'
```

**Research application:** For the Regulatory Layer community and PolitiFi communities, Polymarket prices are primary data — they encode what the market thinks will happen on regulatory questions and elections. For prediction-markets.md, they're the community's output, not input.

---

## Layer 5: Idea Formation — Long Lead (7–28 Days)

These sources are where the intellectual frameworks that will later appear on X as "alpha" are first worked out.

### LessWrong / EA Forum

LessWrong and the EA Forum are where ideas originating in Thread 2 (EA/AI Safety) and Thread 4 (Epistemic Rationalism) get developed before entering broader discourse. A post that gets significant upvotes on LessWrong in week 1 often becomes the intellectual scaffolding for X threads 2–4 weeks later.

**Why it's leading:** The LW/EA community is upstream of AI safety discourse, prediction market epistemics, and DeSci framework development. Tracking what's getting traction there gives you 2–4 weeks of lead on ideas that will hit mainstream AI Twitter.

**Access:**
```bash
# Requires: BRAVE_API_KEY set (see Environment Setup)
# LessWrong RSS (most recent posts)
# Add to RSS reader: https://www.lesswrong.com/?format=rss

# LessWrong GraphQL API — top posts from last 30 days
THIRTY_DAYS_AGO=$(python3 -c "from datetime import date, timedelta; print(date.today() - timedelta(30))")
curl -X POST "https://www.lesswrong.com/graphql" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"{ posts(input: {terms: {view: \\\"top\\\", limit: 10, after: \\\"${THIRTY_DAYS_AGO}\\\"}}) { results { title url score commentCount } } }\"}"

# Brave search for recent LessWrong posts on specific topics
curl -s "https://api.search.brave.com/res/v1/web/search?q=site:lesswrong.com+\"AI+agents\"&count=10" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}"

# EA Forum (same pattern)
curl -s "https://api.search.brave.com/res/v1/web/search?q=site:forum.effectivealtruism.org+\"AI+safety\"&count=10" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}"
```

**For which communities:** DeSci, Prediction markets, Open-source AI, AI safety content within ai-maxxers counter-discourse, Proof of Personhood

### arXiv Preprints

For Thread 3 (Cybernetics/Info Theory), Thread 4 (Epistemic Rationalism), and the technical wing of open-source AI, arXiv preprints are primary source material that generates discourse before papers reach conferences.

```bash
# Requires: BRAVE_API_KEY set (see Environment Setup)
# arXiv API (free, no auth)
curl "https://export.arxiv.org/api/query?search_query=cat:cs.AI+AND+ti:agent&sortBy=submittedDate&max_results=10"

# Recent ML papers (last 30 days — update date range manually)
curl "https://export.arxiv.org/api/query?search_query=cat:cs.LG+AND+submittedDate:[20260201+TO+20260301]&sortBy=submittedDate&max_results=20"

# Brave search for recent influential preprints
curl -s "https://api.search.brave.com/res/v1/web/search?q=site:arxiv.org+AI+agents+2026&count=10" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}"
```

**Signal heuristic:** A preprint getting traction on Papers With Code or HN within a week of posting will influence practitioner behavior 2–4 weeks later.

---

## Layer 6: Developer Community Discourse (Lagging 7–14 Days)

### Hacker News

HN is the leading signal source for the OSS AI developer community specifically — typically reflecting what GitHub stars signaled 1–2 weeks earlier. For the open-source-ai.md and desci.md communities, HN is the most important public forum.

**HN Algolia API (free, no auth):**
```bash
# Search recent HN posts by topic (last 30 days)
SINCE_30D=$(( $(date +%s) - 30 * 86400 ))
curl "https://hn.algolia.com/api/v1/search?query=local+llm&tags=story&hitsPerPage=20&numericFilters=created_at_i>${SINCE_30D}"

# Recent "Show HN" posts (product launches)
curl "https://hn.algolia.com/api/v1/search?query=AI+agent&tags=show_hn&hitsPerPage=10"

# Posts from last 7 days with high points
SINCE_7D=$(( $(date +%s) - 7 * 86400 ))
curl "https://hn.algolia.com/api/v1/search?query=open+source+ai&tags=story&numericFilters=points>100,created_at_i>${SINCE_7D}"
```

**RSS (add to feed reader):**
```
https://news.ycombinator.com/rss  — front page
https://hnrss.org/newest?q=LLM&points=50  — keyword filtered
https://hnrss.org/newest?q=solana&points=30
```

**For which communities:** Open-source AI (primary), DeSci, Prediction markets, Solana dev culture

**HN sentiment as community health indicator:** Comment tone on HN threads about specific projects reflects builder community sentiment. Highly upvoted skeptical comments often anticipate broader community backlash by 2–4 weeks.

---

## Layer 7: Long-Form Analysis (Neutral to Lagging 1–3 Weeks)

### Substack Tiers (from ai-substack-discourse.md)

Substack sits in the middle of the cascade — better than Reddit for synthesis, worse than X Tier 2 for lead time. High-quality Substack essays often crystallize the intellectual frame for a narrative that's been circulating on X for 1–2 weeks.

**Tier 1 (thesis formation):** Bankless, Delphi Digital, Multicoin Capital
**Tier 2 (analysis):** The Generalist, Not Boring, Dirt.xyz
**Tier 3 (counter-discourse):** Molly White (Web3 is Going Great), David Rosenthal, Lily Frankel

**Extraction:**
```bash
# Substack via summarize CLI (already in workflow)
summarize "https://banklesshq.substack.com/p/latest" --length xl --plain

# Brave search for recent relevant essays
# Requires: BRAVE_API_KEY set (see Environment Setup)
curl -s "https://api.search.brave.com/res/v1/web/search?q=site:substack.com+\"AI+agents\"+crypto&count=10" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}"
```

---

## Layer 8: Retail Consciousness — Reddit

Reddit is where narratives that originated on X 2–8 weeks earlier reach general retail awareness. Low signal for real-time intelligence; high signal for when a narrative has achieved mass adoption.

**Current coverage in seed-lists.md:**
- r/CryptoMoonShots, r/SatoshiStreetBets, r/memecoins, r/solana, r/defi ✓

**Missing — AI/Technical communities:**

| Subreddit | Members | Signal Type | Cascade Position |
|-----------|---------|-------------|-----------------|
| r/MachineLearning | ~2.5M | Technical ML discourse | Lagging 7–14 days (practitioners, not researchers) |
| r/LocalLLaMA | ~300K | Local/OSS LLM deployment | Mixed — 5 days lag for news, leading for real-world usage patterns |
| r/artificial | ~1.2M | General AI discussion | Lagging 14–28 days |
| r/ethereum | ~1.6M | Ethereum ecosystem | Lagging 7–21 days for protocol discourse |
| r/CryptoCurrency | ~6M | General crypto | Lagging 21–60 days; use only for macro sentiment |
| r/singularity | ~700K | AI futures discourse | Lagging 7–21 days; e/acc-adjacent but broader |
| r/AIAssistants | ~200K+ | Consumer AI tool discussion | Lagging 14–30 days; useful for mainstream adoption signals |

**RSS feeds for new coverage:**
```
https://www.reddit.com/r/MachineLearning/top/.rss?t=week
https://www.reddit.com/r/LocalLLaMA/top/.rss?t=week
https://www.reddit.com/r/ethereum/top/.rss?t=week
https://www.reddit.com/r/artificial/top/.rss?t=week
```

**Brave search extraction pattern (no Reddit API needed):**
```bash
# Historical Reddit search via Brave
# Requires: BRAVE_API_KEY set (see Environment Setup)
QUERY="\"open source AI\" site:reddit.com after:2026-01-01"
ENCODED_QUERY=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" "${QUERY}")
curl -s "https://api.search.brave.com/res/v1/web/search?q=${ENCODED_QUERY}&count=10" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}" \
  | jq '.web.results[] | {title, url, description}'
```

**PullPush for historical Reddit research:**
```bash
# PullPush.io — Pushshift successor, historical Reddit search
curl "https://api.pullpush.io/reddit/search/submission/?q=memecoin+solana&after=1704067200&size=25&sort_type=score"
```

**What Reddit does uniquely well that other sources don't:**
- Long-form "what is this?" explanatory posts that degens write for normie audiences — these are the community's own mythology
- Comment section debates reveal the specific objections mainstream audiences raise to new narratives
- Upvote counts as ground truth for what resonates at mass scale
- Geographic signal: comment framing shifts by user region (UK users ask about regulation differently than US users)

---

## Layer 9: Mass Market (Lagging 4–24 Weeks)

YouTube, podcasts, and mainstream media. Useful only as:
1. Confirmation that a narrative has reached fully mainstream consciousness
2. Understanding how narratives get framed for non-native audiences
3. Detecting backlash cycles (mainstream coverage often triggers counter-narrative formation)

**Key YouTube channels (monitoring, not participation):**
- Bankless — institutional-grade crypto/DeFi analysis; episodes 4–8 weeks after X discourse
- Unchained (Laura Shin) — regulatory and VC interviews; 4–12 weeks lag
- Lex Fridman — AI/tech; often 2–4 months after ideas circulate in specialist communities
- Coin Bureau — retail-facing; >8 weeks lag on any given narrative

**LunarCrush** aggregates YouTube + Reddit + Twitter mentions and can surface when a token/topic is entering YouTube discussion.

---

## Per-Community Signal Map

Which sources to prioritize for each of the 21 active community profiles (silent-majority and institutional are listed in HOME.md but do not yet have full profile files):

| Community | Primary Sources (Leading) | Secondary Sources | Reddit/Lag |
|-----------|--------------------------|-------------------|------------|
| ai-maxxers | X Tier 2, LessWrong, arXiv | Substack (Beff Jezos blog), GitHub | r/singularity |
| a16z-ecosystem | GitHub (portfolio repos), X Tier 1, a16z blog | Substack Tier 1, Farcaster | r/CryptoCurrency |
| ai-agent-tokens | Farcaster, X Tier 2, GitHub stars | On-chain (agent token prices), Telegram | r/CryptoCurrency |
| memecoin-culture | On-chain (pump.fun), Telegram, DEX Screener | X Tier 2 KOLs, Kaito | r/CryptoMoonShots |
| prediction-markets | Polymarket/Kalshi prices, LessWrong, X Tier 1 forecasters | Metaculus, Substack | r/MachineLearning |
| red-pill-black-pill | X Tier 2 (far-right), Gab Trends | Telegram (invite-only) | r/CryptoCurrency |
| tiktok-creators | TikTok trending (manual), X Tier 2 | LunarCrush | r/AIAssistants |
| crypto-twitter | X Tier 1+2, Kaito mindshare | Substack Tier 1 | r/CryptoCurrency |
| network-states | Substack (Balaji), LessWrong, Farcaster | X Tier 1 | r/ethereum |
| proof-of-personhood | GitHub (Worldcoin, Proof of Humanity repos), arXiv | Farcaster, LessWrong | r/ethereum |
| agentic-governance | arXiv, Farcaster, GitHub | LessWrong, Substack | r/MachineLearning |
| hyperliquid | On-chain (Hyperliquid perps), X Tier 2 | Dune (Hyperliquid dashboards) | r/defi |
| groyper-pipeline | Gab Trends, X (far-right accounts), Telegram | SPLC reports | r/CryptoCurrency |
| solana-dev-culture | GitHub (Solana repos), Farcaster, X Tier 2 | HN, Solana Discord | r/solana |
| desci | arXiv, LessWrong, GitHub (bio/chem tooling) | Farcaster, HN | r/MachineLearning |
| refi-public-goods | Farcaster, LessWrong, GitHub (Gitcoin, Karma) | Substack, HN | r/ethereum |
| regulatory-layer | Polymarket (regulatory markets), X Tier 1 (policy accounts) | Congressional records, DC Substacks | r/CryptoCurrency |
| politifi | Polymarket (election markets), X Tier 2, on-chain (PolitiFi token prices) | Gab Trends, X far-right accounts | r/CryptoCurrency |
| farcaster-warpcast | Farcaster itself, Neynar API, GitHub (Farcaster protocol) | X Tier 1, Dune Farcaster dashboards | r/ethereum |
| open-source-ai | GitHub stars, HN, arXiv, Hugging Face trending | LessWrong, X Tier 2 ML accounts | r/MachineLearning, r/LocalLLaMA |
| rwa-stablecoin | On-chain (DeFiLlama TVL, RWA.xyz), X Tier 1 institutional | Polymarket (rate markets), Substack | r/defi |

---

## Environment Setup

Before running any snippet in this document, load credentials into your shell once:

```bash
# Run once per shell session — requires 1Password CLI authenticated
export BRAVE_API_KEY=$(op read "op://Agent/Brave API Key/password")
export GITHUB_TOKEN=$(gh auth token)   # or: op read "op://Agent/GitHub Token/credential"
export NEYNAR_KEY=$(op read "op://Agent/Neynar API/credential")
```

> **macOS date note:** Snippets below use portable shell arithmetic `$(( $(date +%s) - N * 86400 ))` for time offsets. Do not substitute macOS-only `date -v-Nd` flags — they will fail on Linux/GNU systems.

---

## Integrated Extraction Workflow

### Daily (5-minute scan, automated)

```bash
#!/bin/bash
# Quick pulse check — run daily or pipe output to RSS reader
# Requires: BRAVE_API_KEY, GITHUB_TOKEN set (see Environment Setup above)

TWO_DAYS_AGO=$(python3 -c "from datetime import date, timedelta; print(date.today() - timedelta(2))")

echo "=== GITHUB TRENDING (AI/Crypto) ==="
curl -s "https://api.github.com/search/repositories?q=topic:llm+pushed:>${TWO_DAYS_AGO}&sort=stars&per_page=5" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  | jq '.items[] | {name, stargazers_count, html_url}'

echo "=== HN TOP AI POSTS ==="
curl -s "https://hn.algolia.com/api/v1/search?query=AI+crypto&tags=story&numericFilters=points>50&hitsPerPage=5" \
  | jq '.hits[] | {title, url, points}'

echo "=== POLYMARKET ACTIVE MARKETS ==="
curl -s "https://gamma-api.polymarket.com/markets?active=true&limit=5" \
  | jq '.[] | {question, outcomePrices}'
```

### Weekly (30-minute deep scan)

See `methods/community-pulse-monitoring.md` for the full 30-minute protocol.

**Add to existing weekly protocol — AI layer:**
1. GitHub Trending (weekly filter) — 3 min
2. HN top AI/crypto posts (last 7 days) — 5 min
3. LessWrong top posts (last 2 weeks) — 5 min
4. Polymarket markets by category — 3 min
5. r/MachineLearning + r/LocalLLaMA top posts — 4 min

### Research queries (ad hoc, via Brave API)

```bash
# Requires: BRAVE_API_KEY, GITHUB_TOKEN set (see Environment Setup above)

# Reddit retrospective (any topic, any timeframe)
function reddit_search() {
  local encoded_q
  encoded_q=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote('site:reddit.com ' + sys.argv[1]))" "$1")
  curl -s "https://api.search.brave.com/res/v1/web/search?q=${encoded_q}&count=10" \
    -H "X-Subscription-Token: ${BRAVE_API_KEY}" | jq '.web.results[] | {title, url}'
}

# GitHub repo search
function github_search() {
  local encoded_q
  encoded_q=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" "$1")
  curl -s "https://api.github.com/search/repositories?q=${encoded_q}&sort=stars&per_page=10" \
    -H "Accept: application/vnd.github.v3+json" \
    -H "Authorization: Bearer ${GITHUB_TOKEN}" \
    | jq '.items[] | {name, stargazers_count, description}'
}

# LessWrong search
function lw_search() {
  local encoded_q
  encoded_q=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote('site:lesswrong.com ' + sys.argv[1]))" "$1")
  curl -s "https://api.search.brave.com/res/v1/web/search?q=${encoded_q}&count=10" \
    -H "X-Subscription-Token: ${BRAVE_API_KEY}" | jq '.web.results[] | {title, url}'
}

# HN search
function hn_search() {
  local encoded_q
  encoded_q=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" "$1")
  curl -s "https://hn.algolia.com/api/v1/search?query=${encoded_q}&tags=story&hitsPerPage=10" \
    | jq '.hits[] | {title, url, points, created_at}'
}
```

---

## The Divergence Protocol

The highest-value analytical move is finding divergence between cascade layers. Four divergence patterns to watch for:

**1. On-chain contradicts community narrative**
When a community claims decentralization but on-chain shows whale concentration (BubbleMaps), or claims volume but has low unique wallets (Dune analytics). This is the most reliable counter-signal.

**2. LessWrong/arXiv contradicts X consensus**
When the technical research community (LW, arXiv, HN) reaches different conclusions than the X-CT consensus about a technical claim. Example: academic ML researchers questioning a capability claim that X CT has accepted as fact.

**3. Reddit lag longer than expected**
If a narrative has been prominent on X for 8+ weeks without appearing on Reddit, it may indicate the narrative is contained within a specialist community and hasn't crossed into retail consciousness — an important finding for community boundary analysis.

**4. Polymarket contradicts community confidence**
When a community expresses high confidence in an outcome (regulatory approval, technical milestone) but Polymarket prices assign low probability, the market is encoding information the community is ignoring. Track this divergence.

---

## Source Gaps and Research Debt

**Not yet systematically monitored:**
- [ ] Discord servers for each community (access varies)
- [ ] Hugging Face model trending (leading for OSS AI attention)
- [ ] Papers With Code trending (leading for ML research attention)
- [ ] Substack comment sections (engagement signal beyond subscriber counts)
- [ ] Metaculus community questions (alternative to Polymarket for longer-horizon questions)
- [ ] Stack Overflow tags (lagging, useful for developer technology adoption)

**Tools needing investigation:**
- [ ] Neynar API pricing and free tier scope for Farcaster monitoring
- [ ] Kaito API documentation (programmatic mindshare access)
- [ ] LunarCrush API for Reddit + Twitter combined sentiment

*Update this file when new sources are validated in field use.*
