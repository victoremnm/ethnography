# Seed Lists

> **Ethics note:** All handles listed here are public figures with substantial public followings who engage in public discourse on their platforms. This list is for pattern analysis and community observation, not individual targeting. See [`ethics.md`](../ethics.md) for full research ethics guidelines.

---

## Twitter/X Accounts by Tier

Tier 1 = synthesis and thesis formation (follow for strategic signal).
Tier 2 = subculture-specific depth (follow when going deep on a community).
Tier 3 = discourse trackers (monitor for narrative formation, not individual posts).

### Tier 1 — Strategic Signal

| Handle | Role | Why They Matter |
|--------|------|----------------|
| `@cdixon` | a16z crypto lead | Telegraphs a16z investments; his public writing is a thesis map |
| `@marc_andreessen` | a16z co-founder | e/acc ideological anchor; watch for what he amplifies |
| `@cobie` | CT OG / irreverent analyst | Reads market psychology accurately; high signal-to-noise |
| `@MustStopMurad` | Memecoin thesis originator | Called the memecoin supercycle in 2024; narratively influential |
| `@DylanLeClair_` | On-chain data analyst | Bridges Dune/Nansen data → readable narrative; upstream of CT |
| `@RealAlexThorn` | Galaxy Research | Institutional-grade crypto analysis; cited by VCs |
| `@ceterisparibus__` | Macro + crypto intersection | Where tradfi macro meets crypto; useful for rates/regulatory framing |

### Tier 2 — Community-Specific Depth

**CT / a16z ecosystem:**
- `@VitalikButerin` — Ethereum founder; intellectual foil to e/acc
- `@naval` — aphorist, crypto-libertarian philosophy
- `@balajis` — network state thesis, crypto maximalist
- `@delphi_digital` — firm account; their threads are substantive (skip the price takes)

**AI Maxxers / e/acc:**
- `@BasedBeffJezos` (Guillaume Verdon) — e/acc founder
- `@bayeslord` — e/acc co-originator
- `@shawmakesmagic` — AI agent builder, connects e/acc to product
- `@repligate` — AI agent discourse, technical depth
- `@karpathy` — ex-OpenAI; respected by builder community; not e/acc but ambient influence

**Prediction markets:**
- `@NateSilver538` — public forecaster; useful as mainstream legitimacy signal
- `@KalshiHQ` — Kalshi official
- `@Polymarket` — Polymarket official
- `@ResearcherEllie` — active Kalshi/forecasting community participant

**DeFi / on-chain:**
- `@bantg` — Yearn/DeFi OG; technically dense but reliable
- `@0xfbifemboy` — pseudonymous degen/analyst
- `@0xHamz` — DeFi protocol researcher

### Tier 3 — Narrative Formation Trackers

These are better monitored via **Twitter Lists** than direct follows. Their value is in the aggregate discourse, not individual posts.

- a16z maintains public lists of their portfolio founders — following those lists shows you what narrative clusters are forming before they hit mainstream CT
- Kaito's "mindshare" leaderboard tracks which handles are driving conversation within a given narrative window — use it to find tier 2 handles you're missing
- `@0xfbifemboy`, `@0xHamz` and similar pseudonymous analysts often surface narratives 2–4 weeks before they reach tier 1 accounts

---

## CT Core Handles (Legacy — Pre-Tiering)
- `@marc_andreessen` — a16z co-founder, e/acc signaler
- `@cdixon` — a16z crypto lead, thesis originator
- `@VitalikButerin` — Ethereum founder, intellectual foil to e/acc
- `@naval` — aphorist, crypto-libertarian philosophy
- `@balajis` — network state thesis, crypto maximalist
- `@cobie` — irreverent CT OG, high signal
- `@0xfbifemboy` — pseudonymous degen/analyst type

## AI Maxxers / e/acc
- `@BasedBeffJezos` (Guillaume Verdon) — e/acc founder
- `@bayeslord` — e/acc co-originator
- `@shawmakesmagic` — AI agent builder, connects e/acc to product
- `@repligate` — AI agent discourse, technical depth
- `@karpathy` — ex-OpenAI, followed by builder community (not e/acc but respected)

## Prediction Markets
- Nate Silver (`@NateSilver538`) — public forecaster
- `@KalshiHQ` — Kalshi official account
- `@Polymarket` — Polymarket official
- Metaculus community — accessible via metaculus.com leaderboards
- Philip Tetlock — academic; search his Superforecaster work

## Memecoin Trenches (Observation Points)
- pump.fun leaderboard (on-site) — tracks trending tokens in real time
- `@pumpdotfun` — official account
- Dune Analytics dashboards: `@21shares_research` publishes pump.fun analytics
- Telegram: Banana Gun bot channel, Maestro Sniper channel (requires joining)
- X: search `$` + any trending ticker to find organic conversation

## Market Data Sources
- [Nansen](https://nansen.ai) — wallet intelligence, smart money tracking
- [Dune Analytics](https://dune.com) — on-chain data, open queries
- [DeFiLlama](https://defillama.com) — protocol TVL tracking
- [CoinGecko](https://coingecko.com) — market cap, narrative tracking
- [Kaito](https://kaito.ai) — AI-powered CT mindshare analytics

## Research / Academic Sources
- [a16z State of Crypto 2025](https://a16zcrypto.substack.com/p/state-of-crypto-2025-the-latest-data)
- [cyber.fund AI × Crypto Thesis 2025](https://cyber.fund/content/crypto-ai-investment-thesis-2025)
- [arXiv: AI-Based Crypto Tokens](https://arxiv.org/html/2505.07828v2)
- [Grayscale AI × Crypto Report](https://research.grayscale.com/reports/ai-is-coming-crypto-can-help-make-it-right)
- [Animoca / Yat Siu — AI agents to bring crypto to masses](https://cryptonews.com/news/animoca-yat-siu-ai-agents-2026-utility/)

---

## GitHub — Developer Attention Signals

Star velocity is the leading indicator for which OSS AI and crypto projects are capturing developer mind-share, typically 3–10 days before X discourse.

**Tracking pages (manual, no auth):**
- [GitHub Trending (daily)](https://github.com/trending) — filter by language, date range
- [GitHub Trending (weekly)](https://github.com/trending?since=weekly)
- Topics: [llm](https://github.com/topics/llm), [ai-agent](https://github.com/topics/ai-agent), [ethereum](https://github.com/topics/ethereum), [solana](https://github.com/topics/solana), [prediction-market](https://github.com/topics/prediction-market), [desci](https://github.com/topics/desci)
- [Hugging Face Trending Models](https://huggingface.co/models) — OSS AI model attention
- [Papers With Code (State of the Art)](https://paperswithcode.com/sota) — leading for ML research claims

**API extraction:**
```bash
# Repos gaining star velocity (recent AI repos)
SINCE_JAN_1=$(( $(date +%s -d "2026-01-01") 2>/dev/null || date -j -f "%Y-%m-%d" "2026-01-01" +%s ))
# Standardized portable date check:
THIRTY_DAYS_AGO=$(python3 -c "from datetime import date, timedelta; print(date.today() - timedelta(30))")

curl --fail "https://api.github.com/search/repositories?q=topic:llm+pushed:>${THIRTY_DAYS_AGO}&sort=stars&per_page=10" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}"
```

**Research value:** Use for communities: open-source-ai, desci, solana-dev-culture, ai-agent-tokens, farcaster-warpcast (Farcaster protocol repos).

---

## LessWrong / EA Forum — Idea Formation Layer

The rationalist ecosystem is where Thread 2 (EA/AI Safety) and Thread 4 (Epistemic Rationalism) ideas develop 1–4 weeks before reaching X/CT. High-upvote LW posts often become X threads weeks later.

**Access points:**
- [LessWrong](https://www.lesswrong.com) — [RSS](https://www.lesswrong.com/?format=rss)
- [EA Forum](https://forum.effectivealtruism.org) — [RSS](https://forum.effectivealtruism.org/?format=rss)
- [Alignment Forum](https://alignmentforum.org) — technical AI safety research
- LessWrong GraphQL API: `https://www.lesswrong.com/graphql` (no auth required for public posts)

**Key tags to monitor:** `AI`, `AI Safety`, `Forecasting`, `Rationality`, `DeSci`, `Prediction Markets`

**Research value:** Communities: prediction-markets, desci, open-source-ai, refi-public-goods, proof-of-personhood. Thread 2 and Thread 4 ground truth.

---

## Hacker News — OSS Developer Discourse

HN reflects what the technical developer community is discussing, typically 7–14 days after GitHub signals and 7–14 days before mainstream coverage. Best source for open-source AI community specifically.

**API (free, no auth):**
- HN Algolia: `https://hn.algolia.com/api/v1/search?query=QUERY&tags=story&hitsPerPage=20`
- Show HN (product launches): `https://hn.algolia.com/api/v1/search?query=QUERY&tags=show_hn`

**RSS feeds:**
```
https://news.ycombinator.com/rss  — front page
https://hnrss.org/newest?q=LLM&points=50  — keyword filtered (50+ points threshold)
https://hnrss.org/newest?q=solana&points=30
https://hnrss.org/newest?q=prediction+market&points=30
```

**Research value:** Communities: open-source-ai (primary), desci, prediction-markets, solana-dev-culture.

---

## Polymarket / Kalshi — Epistemic Barometers

Prediction market prices are the compressed epistemic state of a community that has staked money on outcomes. Not leading indicators but coincident — they encode current informed-participant belief.

**API access (read-only, no auth required for basic queries):**
- Polymarket CLOB: `https://clob.polymarket.com/markets?active=true`
- Polymarket Gamma: `https://gamma-api.polymarket.com/markets?active=true`
- Kalshi REST: `https://trading-api.kalshi.com/trade-api/v2/markets?status=active&limit=100`

**Research use:**
- Market *existence* = topic salience to forecasters
- Price *movement* = narrative disruption event (new information entering ecosystem)
- New market *creation* = topic entering forecaster attention for first time
- Price *divergence from community confidence* = most interesting analytical finding

**Research value:** Communities: prediction-markets (primary output), regulatory-layer, politifi, network-states. Cross-reference with community stated beliefs to find divergence.

---

## Farcaster API — Crypto-Native Builder Discourse

Farcaster's builder-heavy composition makes it a 2–5 day leading indicator for crypto-native technical narratives before they hit X.

**API:**
- Neynar trending: `https://api.neynar.com/v2/farcaster/feed/trending?limit=20` (requires free Neynar API key)
- Warpcast trending: `warpcast.com/trending` (manual browse)
- Dune Farcaster analytics: `dune.com/neynar/farcaster-protocol-stats`

**Brave search workaround (no Neynar key needed):**
```bash
curl --fail -s "https://api.search.brave.com/res/v1/web/search?q=site:warpcast.com+\"TOPIC\"&count=10" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}"
```

**Research value:** Communities: farcaster-warpcast (primary), ai-agent-tokens, solana-dev-culture, proof-of-personhood, desci.

---

## Community Pulse: Real-Time Monitoring

> This section supports the 30-min/week monitoring protocol documented in [`methods/community-pulse-monitoring.md`](../methods/community-pulse-monitoring.md). Items here are observation points, not participation points.

### Reddit Communities

| Subreddit | Members | Signal Type | Research Value |
|-----------|---------|-------------|----------------|
| [r/CryptoMoonShots](https://reddit.com/r/CryptoMoonShots) | ~2.2M | Low-cap speculation, promotional | Lagging indicator — shows what reached retail consciousness |
| [r/SatoshiStreetBets](https://reddit.com/r/SatoshiStreetBets) | ~761K | High-risk trades, meme coins | Retail sentiment barometer; chaotic but legible |
| [r/memecoins](https://reddit.com/r/memecoins) | ~200K+ | Memecoin launches, community | Low signal — mostly dev self-promotion |
| [r/solana](https://reddit.com/r/solana) | ~500K+ | Ecosystem discussion, technical | Medium signal; best Reddit source for Solana narrative |
| [r/defi](https://reddit.com/r/defi) | ~300K+ | Protocol discussion, regulatory | Higher signal; useful for institutional/regulatory framing |
| [r/MachineLearning](https://reddit.com/r/MachineLearning) | ~2.5M | Technical ML research discourse | Medium-High — practitioners lag arXiv/HN by ~7 days; useful for OSS AI |
| [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) | ~300K+ | Local/OSS LLM deployment | High for real-world usage patterns; 5 days lag on news but leading on deployment friction |
| [r/artificial](https://reddit.com/r/artificial) | ~1.2M | General AI discussion | Low-Medium; useful for mainstream AI narrative (lagging 14–28 days) |
| [r/ethereum](https://reddit.com/r/ethereum) | ~1.6M | Ethereum ecosystem | Medium; protocol discourse lags X by 7–21 days |
| [r/singularity](https://reddit.com/r/singularity) | ~700K | AI futures, e/acc-adjacent | Low-Medium; useful for Thread 1 (Accelerationism) retail consciousness |

**RSS feeds (add to reader, filter by score >500 upvotes for crypto, >100 for AI subs):**
```
https://www.reddit.com/r/CryptoMoonShots/.rss
https://www.reddit.com/r/SatoshiStreetBets/.rss
https://www.reddit.com/r/solana/.rss
https://www.reddit.com/r/MachineLearning/top/.rss?t=week
https://www.reddit.com/r/LocalLLaMA/top/.rss?t=week
https://www.reddit.com/r/ethereum/top/.rss?t=week
```

**Historical search tool:** [PullPush.io](https://pullpush-io.github.io/) — Pushshift successor; use for retrospective queries about specific token narratives on Reddit.

### X (Twitter) Lists and Accounts — Trenches Layer

These supplement the existing Tier 1/2/3 structure above with memecoin-specific observation points.

**Monitoring tools (not follow lists):**
- [Kaito.ai](https://kaito.ai) — mindshare leaderboard; use weekly to identify what narratives are gaining CT share
- [LunarCrush](https://lunarcrush.com) — social sentiment aggregation across Twitter + Reddit; "Galaxy Score" for token social signal
- [Tweetscout](https://tweetscout.io) — account influence validation; use to check whether a KOL's following is genuine before adding to monitoring

**Account validation rule:** Before adding any memecoin KOL to a monitoring list, check via Tweetscout and BubbleMaps (wallet relationship to promoted tokens). If wallet purchased before promotion, treat as paid KOL — observe the coordination pattern, not the call.

**X search operators for weekly scans:**
- `pump.fun filter:links` — finds posts sharing pump.fun token links (launch activity)
- `$[TICKER] contract` — finds organic community posts about specific tokens
- `"trenches" solana` — finds degen community language in real use

### Telegram Groups (Public/Observable)

**Official bot channels (public, no trading required):**
- `@bonkbot_io` — BONKbot official; product updates, ecosystem announcements
- `@BananaGunBot` — Banana Gun official; tool ecosystem signals
- `@MaestroBots` — Maestro official
- `@rick_bot` — Rickbot; DM the bot with a contract address for instant audit (research tool)

**Usage note:** When a memecoin launches on pump.fun, the dev's promotional post (on X or Telegram) typically includes a joinable group link. These are publicly accessible for the first 24–72 hours and show community formation in real time. Found via X search for the contract address after identifying a trending token on DEX Screener.

### Dune Analytics Dashboards

**Weekly monitoring (read-only, no account required for most):**

| Dashboard | URL | What It Shows |
|-----------|-----|---------------|
| Pump.fun main | [dune.com/pumpdotfun](https://dune.com/pumpdotfun) | Daily launches, graduation rate, fees, active addresses |
| Meme coins + narratives | [dune.com/uwusanauwu/memes](https://dune.com/uwusanauwu/memes) | Cross-chain memecoin narrative tracking |
| Pump.fun deployer records | Community dashboard via GitHub: oladeeayo/Pumpfun-Token-Deployer-Records-Dashboard | Dev behavior, self-buys, bundle detection |

**Key metric to track weekly:** Graduation rate (% of launched tokens reaching $69K market cap). This single number encodes the state of community participation:
- Rising graduation rate = active meta, community has thesis on what to buy
- Falling graduation rate = market cooling, noise increasing relative to signal

### On-Chain Analysis Tools

| Tool | URL | Use Case | Cost |
|------|-----|----------|------|
| DEX Screener | [dexscreener.com/solana/pumpfun](https://dexscreener.com/solana/pumpfun) | Real-time trending, token community links | Free |
| GMGN.ai | [gmgn.ai/trend?chain=sol](https://gmgn.ai/trend?chain=sol) | Smart money tracking, ~5s faster than DEX Screener | Free |
| BubbleMaps | [bubblemaps.io](https://bubblemaps.io) | Holder visualization, bundle/cabal detection | Free |
| Photon Memescope | [photon-sol.tinyastro.io](https://photon-sol.tinyastro.io) | Launch lifecycle view (new / graduating / graduated) | Free (read) |
| Nansen | [nansen.ai](https://nansen.ai) | Institutional wallet labeling, smart money flows | Paid |

### Political/Values Community Observation Points

**Context:** The far-right/crypto intersection is ideological (libertarianism, censorship resistance) rather than primarily memecoin-focused. Overlap exists through shared meme aesthetics (Pepe, wojak, groyper imagery being financialized on pump.fun).

**Observable without participation:**
- [Gab Trends](https://trends.gab.com) — public trends feed, no account required; shows far-right crypto/Bitcoin discussion volume
- [Cozy.tv](https://cozy.tv) — Nick Fuentes live streaming platform; publicly viewable
- X search: `"freedom money" OR "censorship resistant" crypto` — finds ideological framing without community embeds
- pump.fun + DEX Screener: filter for tokens using Pepe/groyper/wojak imagery to observe the financialization of far-right meme aesthetics

**SPLC Cryptocurrency Report:** [splcenter.org/cryptocurrency-report](https://www.splcenter.org/cryptocurrency-report) — documents far-right crypto funding patterns; useful as external reference for on-chain forensics of political communities.
