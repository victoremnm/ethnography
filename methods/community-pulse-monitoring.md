# Community Pulse Monitoring

**Purpose:** A systematic, low-time protocol for monitoring memecoin/crypto communities from the outside — without daily scrolling or community participation.

**For:** A tech-industry professional with limited time who is outside the generational and values context of these communities.

**Time budget:** 30 minutes per week.

---

## The Problem (Why Normal Browsing Doesn't Work)

The memecoin/shitcoin space has four properties that defeat casual monitoring:

**1. Speed asymmetry.** The relevant signal in memecoin culture is measured in hours, not days. A coin goes from launch to peak to rug in 24–48 hours on pump.fun. By the time something trends on Reddit or hits mainstream CT, the interesting moment has already passed. The ethnographic interest (the moment of cultural formation) is often *before* price peaks, not after.

**2. Platform fragmentation.** The community is simultaneously on Telegram (trading ops, alpha chats), X (narrative formation, KOL calls), Reddit (retail sentiment lag), and on-chain (actual behavior). No single platform gives you a complete picture. Each layer tells a different truth.

**3. Signal/noise inversion.** On X and Telegram, the loudest voices are often the most compromised (paid KOLs, coordinated pump operators). On Reddit, most crypto posts are promotional or retail-lagging. The authentic signal is quieter and harder to find without community context.

**4. Generational and values gap.** The "trenches" culture assumes familiarity with specific aesthetics (wojak, frog memes, ironic accelerationism), a comfort with financial risk-as-entertainment, and implicit knowledge of who is trusted vs. dismissed. An outsider reading a Telegram degen chat cold will miss the social layer entirely.

**The workaround:** Treat on-chain data as ground truth, use social platforms as narrative trackers rather than trading sources, and use tools built by community insiders (Photon Memescope, DEX Screener, GMGN.ai) as observation infrastructure rather than trading infrastructure.

---

## Reddit: Signal vs. Noise by Subreddit

Reddit sits at the retail end of the information cascade — it reflects narratives that originated on X and Telegram, usually 24–72 hours later. This makes it a poor source for real-time alpha, but a useful barometer for **when something has crossed from degen culture into broader retail consciousness.**

### Subreddit Assessment (February 2026)

| Subreddit | Members | Signal Type | Authenticity | Researcher Use |
|-----------|---------|-------------|--------------|----------------|
| **r/CryptoMoonShots** | ~2.2M | Low-cap speculation, promotional | Low — heavy promotional noise, shill-bots | Useful as retail sentiment lag indicator; what shows up here has already run |
| **r/SatoshiStreetBets** | ~761K | High-risk trade discussion, meme stocks/coins | Low-Medium — chaotic, retail-oriented | Watch for when a meme narrative reaches mass retail consciousness |
| **r/memecoins** | ~200K+ | Memecoin launches, discussion | Low — dominated by promotional posts | Not useful for research; mostly dev self-promotion |
| **r/solana** | ~500K+ | Technical discussion, Solana ecosystem | Medium — mix of genuine builders and hype | Higher signal than memecoin subs; useful for ecosystem development signals |
| **r/defi** | ~300K+ | DeFi protocol discussion | Medium-High — more technical, less shilling | Useful for protocol legitimacy signals, regulatory concerns |
| **r/CryptoCurrency** | ~6M+ | General crypto news, discussion | Low-Medium — high volume, moderated but noisy | Use only for macro sentiment; too broad for memecoin research |

### The Key Insight on Reddit Timing

Reddit activity is a **lagging indicator**, not a leading one. When r/CryptoMoonShots lights up for a specific token, the token is usually already in its distribution phase. For ethnographic purposes, this lag is actually *useful*: watching Reddit tells you what the retail participation moment looked like, not what the degen launch moment looked like. These are two different cultural artifacts.

**What Reddit does uniquely well:**
- Captures written community lore (the long-form explanations degens write for normies about why a coin matters)
- Surfaces the "belief narrative" — the story the community tells itself about why this isn't gambling
- Shows geographic distribution (comment tone and framing shifts by user origin)

### Monitoring Reddit Without Daily Scrolling

**Option 1: Reddit's native RSS feeds** (free, no API needed)
```
https://www.reddit.com/r/CryptoMoonShots/.rss
https://www.reddit.com/r/SatoshiStreetBets/.rss
https://www.reddit.com/r/solana/.rss
```
Feed into any RSS reader (Feedly, NetNewsWire). Filter by post score threshold — only read posts above 500 upvotes. This eliminates 90% of noise.

**Option 2: PullPush (Pushshift successor)**
PullPush.io is the community-maintained successor to the Pushshift API, which Reddit shut down in 2023. It allows historical search across Reddit and limited real-time ingestion. Useful for research queries like "find all posts mentioning $PNUT between date X and date Y." Not useful for real-time monitoring but excellent for retrospective analysis of how a specific narrative formed on Reddit.

**Option 3: n8n workflow automation**
An open-source no-code tool that can connect Reddit RSS → CoinGecko price API → Slack/Discord notification. Allows you to trigger alerts only when a mentioned coin shows unusual price action simultaneously. Reduces monitoring to exception handling only.

**Option 4: SocialGrep**
socialgrep.com provides real-time Reddit search with date filtering. Better than Reddit's native search for research queries. Free tier available.

---

## X (Twitter): Monitoring Without Immersion

X is where memecoin narratives are **formed**, not just discussed. KOL calls, meme virality, and narrative launches all originate on X before reaching Telegram (trading) and Reddit (retail). The challenge is that the signal is buried in paid shill volume.

### The Information Cascade on X

```
Insider/Cabal pre-buy → Telegram degen chats (alpha)
    → Tier 2 KOL posts (10K–100K followers)
        → Tier 1 KOL posts (100K+ followers)
            → X trending / broader CT
                → Reddit / mainstream media
```

As a researcher, you want to observe **Tiers 2 and 3** — early enough to see formation, late enough to have legible artifact. Tier 1 KOL posts are already compromised by pay-for-play mechanics.

### Core Monitoring Tools

**Kaito.ai — Mindshare Tracking (PRIMARY)**
Kaito is the highest-leverage tool for X monitoring without immersion. It quantifies which topics, narratives, and accounts are driving conversation within the crypto ecosystem — numerically, not qualitatively. Key features for research:
- **Mindshare leaderboard**: shows which tokens/narratives are gaining relative share of CT conversation
- **Narrative rotation tracking**: identifies when conversation is shifting from one meta to another
- **Yapper rankings**: shows which accounts are most influential within a given narrative window

Use Kaito weekly to identify what the CT conversation is *actually* about, then use X search to read the specific threads. This inverts the workflow: instead of scrolling X to find what matters, let Kaito tell you what matters and then go read it.

Note: Kaito updated its algorithm in 2025 to reduce spam and gamification — the signal quality improved but the "mindshare farming" dynamic means some highly-ranked accounts are optimizing for Kaito metrics rather than genuine contribution. Read rankings as evidence of attention, not endorsement.

**LunarCrush — Social Sentiment Aggregation**
LunarCrush aggregates Twitter, Reddit, and YouTube mentions for specific tokens and produces sentiment scores. Useful for:
- Identifying when a specific token is experiencing unusual social attention
- Comparing social volume across tokens
- Detecting sentiment divergence (high mentions, negative sentiment = community controversy worth observing)

Free tier provides meaningful signal. The "Galaxy Score" and "AltRank" metrics are useful as relative comparators, not absolute measurements.

**Tweetscout — Account Analysis**
tweetscout.io shows the "real social weight" of any account — how much genuine influence vs. purchased/bot following. Useful for qualifying KOL accounts before deciding whether to monitor them. When a KOL call seems coordinated, check their Tweetscout profile.

**TweetDeck (X Pro) — Column Monitoring**
Still functional as of 2026, though now requires X Premium. Useful for simultaneous monitoring of:
- A curated list (see below)
- Keyword searches (`$SOL memecoin`, `pump.fun trending`, specific contract addresses)
- Specific high-signal accounts

### Distinguishing Signal from Paid KOL Noise

The core problem documented in `communities/memecoin-culture.md`: most KOL calls are paid promotional content, not genuine alpha. Detection methods:

1. **On-chain timing check**: Does the KOL's wallet show purchases of the token *before* their promotional post? Use BubbleMaps or Nansen to check. If yes, the post is almost certainly paid/coordinated.

2. **Coordination check**: Did multiple KOLs post about the same token within a 2–4 hour window? This is the signature pattern of coordinated paid campaigns. Use LunarCrush mention timeline to detect.

3. **Disclosure absence**: Legitimate calls in the US should disclose paid promotion under SEC guidance (2022). Absence of disclosure is a signal, not proof, of paid content.

4. **Follower quality**: Use Tweetscout to check whether an account's followers are genuine or purchased. KOLs with purchased follower bases are more likely operating paid promotion pipelines.

### X List Strategy for Research

Rather than following individual accounts (which creates an immersive feed), create or subscribe to X Lists that you check weekly:

- **Memecoin Trenches List**: Accounts that post primarily about low-cap Solana coins, pump.fun activity, and degen trades. Look for accounts with 10K–50K followers, pseudonymous, posting contract addresses. This is where to see the cultural formation layer.
- **CT Macro List**: Accounts in the existing `sources/seed-lists.md` Tier 1 and 2. Check weekly for narrative signals.
- **Dune/On-Chain Analysts**: `@DylanLeClair_`, `@dune`, on-chain researchers who translate data into readable narrative.

Public lists maintained by others:
- a16z crypto maintains public lists of their portfolio founders
- Search "crypto memecoin list" on X to find curated public lists by community members — evaluate by checking whether the accounts on the list are posting authentically or promotionally

---

## Telegram: Observation Without Participation

Telegram is where the actual trading operations happen. It is the most authentic and the hardest to access from the outside. The BONKbot doc describes its function accurately: Telegram degen chats are where alpha is shared, calls are made, and community forms in real time around specific tokens.

### Public vs. Invite-Only Groups

**Publicly accessible (no invite required):**
- **BONKbot official channel** (`@bonkbot_io`): Product announcements, not trading alpha. Useful for monitoring tool ecosystem changes.
- **Banana Gun official** (`@BananaGunBot`): Similarly product-focused.
- **Maestro Bot** (`@MaestroBots`): Public channel.
- Launchpad announcement channels: pump.fun, Meteora, and similar platforms often maintain public announcement channels.

**Semi-public (findable, joinable without direct invite):**
- Most memecoin community groups are technically joinable via link-sharing — they're public by Telegram's definition but not indexed. Finding them requires either network access (someone shares the link) or monitoring CT for shared links.
- Telegram group links shared on X: When a memecoin launches, the dev typically posts the Telegram link in the promotional material. These are joinable at launch, though activity peaks in the first 24–48 hours.

**Invite-only (effectively inaccessible to outsiders):**
- The high-conviction degen chats where actual alpha is shared are typically invite-only. These are the most valuable and the least accessible. Do not attempt to infiltrate — it's both ethically problematic and practically futile (members are sophisticated enough to detect outsiders).

### Observer Posture on Telegram

For groups that are publicly joinable:
- Join with a neutral account that has no posting history
- Do not post, react, or respond — pure observation
- Note: Many groups use bots that flag inactive members or require periodic interaction. A research account that never interacts will often be auto-removed after 1–4 weeks.

**The ethics note:** Joining Telegram groups under a false pretense (pretending to be a trader when you're a researcher) is a methodological problem. For netnography, the standard guidance is that publicly accessible groups can be observed without disclosure, but your consent standard should be commensurate with the sensitivity of the content. The degen chats are not sharing personally sensitive information — they are discussing tokens. Observation without participation is ethically defensible for public/semi-public groups.

### Telegram as a Tool Ecosystem (Not Community)

The more valuable Telegram entry point for outside observation is **using the trading bots themselves as data tools** without actually trading:

- **Rickbot** (`@rick_bot`): Add to any group or use in direct message. Paste a contract address and receive an instant audit: holder distribution, liquidity lock status, bundle detection (whether wallets were coordinated at launch), and links to DEX Screener and BubbleMaps. This is a research tool dressed as a trading tool.
- **BONKbot**: Even without funding a wallet, the bot's interface shows you what information degens are checking when they evaluate a token. Using it as a read-only audit tool is legitimate.

---

## On-Chain as Ground Truth

On-chain data is the most important single data source for this research because it is:
- **Unfalsifiable** (unlike social media claims)
- **Behavioral, not attitudinal** (what people actually did, not what they said)
- **Timestamped** (when behavior happened, enabling sequencing with social narrative)

The core interpretive principle from `methods/netnography.md` applies here: when on-chain behavior diverges from stated community belief, that divergence is the most interesting finding.

### Primary On-Chain Tools

**Dune Analytics (Free, Public)**
The highest-leverage single tool for pump.fun ecosystem observation. Key dashboards:

- **`dune.com/uwusanauwu/memes`** — "Meme Coins and on-chain narratives" — tracks memecoin activity across multiple chains with historical data
- **pump.fun main dashboard**: tracks daily launches, graduation rate (% of tokens that reach $69K market cap threshold), daily fees, and active addresses — all public, no login required for read access
- **Deployer behavior tracking**: Dune queries tracking self-buys (devs buying own tokens at launch), bundle detection, and suspicious launch patterns

Use Dune weekly: 5 minutes checking the pump.fun graduation rate and daily launches tells you more about the state of memecoin culture than an hour on X.

**DEX Screener (Free, Real-Time)**
`dexscreener.com/solana/pumpfun` — the real-time trending view of what's happening on pump.fun right now. Organized by:
- Newest tokens
- Trending (by volume/price action)
- Graduating tokens (approaching the $69K threshold)

As an observation tool: the Trending view shows you what the community is *actually* paying attention to at any given moment. The token that trends here, with community activity, is generating the cultural content (memes, Telegram groups, X posts) you can then analyze.

**GMGN.ai (Free Tier, Real-Time)**
`gmgn.ai/trend?chain=sol` — real-time memecoin trending on Solana, approximately 5 seconds faster than DEX Screener according to the platform. Useful for:
- Seeing what's trending before it shows up on DEX Screener
- Smart money wallet tracking: which wallets consistently buy early (these are the sophisticated participants whose moves generate cultural narratives downstream)
- Multi-chain comparison

**Nansen (Paid, Institutional-Grade)**
Nansen provides wallet labeling across 500M+ addresses — categorizing wallets as "smart money," VCs, exchanges, whale holders, etc. For research purposes:
- "Smart Money" dashboard shows what high-performing wallets are accumulating
- "Token God Mode" allows analysis of top buyers/sellers of any token over time
- Relevant for understanding whether a meme narrative is being driven by genuine community formation or by sophisticated whale positioning

Nansen requires a paid subscription. For research with limited budget, check their blog — they regularly publish free analyses using their platform data.

**BubbleMaps (Free, Visual)**
`bubblemaps.io` — visualizes token holder distribution as an interactive bubble map. Each wallet is a bubble; size indicates share of supply; connections show wallet relationships. Integrated directly into pump.fun, Photon, and DEX Screener.

Research use: paste any contract address into BubbleMaps to immediately see whether a token has:
- Concentrated ownership (few wallets holding large %) — indicates bundling/insider control
- Connected wallets (multiple bubbles with common funding source) — indicates cabal coordination
- Distributed ownership — indicates genuine community formation

This is the tool for visualizing the "Cabal" dynamic described in the BONKbot doc.

### Reading On-Chain Data for Community Research

| On-Chain Signal | What It Tells You | Community Interpretation |
|----------------|-------------------|--------------------------|
| High unique wallet count, low average buy size | Genuine broad participation | Community is real, not manufactured |
| Few wallets, large buys, connected origins | Bundled/insider-controlled launch | "Crime" — likely rug setup |
| Graduation rate spike | Community momentum turning real tokens | A "meta" is forming around a category |
| Smart money wallet accumulation before CT noise | Sophisticated positioning | The narrative is manufactured downstream |
| High DEX volume, low unique buyers | Wash trading / bot activity | KOL coordination with no organic following |

---

## The Shitcoining Ecosystem as Observation Layer

The tools described in the BONKbot Shitcoining 101 doc are valuable for research precisely *because* they are designed by insiders, for insiders. Using them as observation tools (not trading tools) gives you the information architecture the community itself uses.

### Photon Memescope (photon-sol.tinyastro.io)

Photon is a web trading terminal for Solana memecoins. The **Memescope** tab is its most valuable feature for research observation. It provides three category views:

- **Newly Created**: Every token as it launches on pump.fun, with holder count, social presence indicators, and early volume. This is the "trenches" in real time — the raw material of what may become a cultural moment.
- **About to Graduate**: Tokens approaching the $69K market cap threshold. These have achieved enough community momentum to survive the first hours. Cultural content (memes, community Telegram, X posts) will be forming around these.
- **Graduated**: Tokens that have reached open market listing. These have crossed from "speculative launch" to "established community" (even if briefly).

**As an observation tool:** Spend 10 minutes on Memescope weekly. Note which tokens in the "About to Graduate" and "Graduated" categories have recognizable meme formats — animals, political figures, internet characters. The categories that recur across multiple tokens indicate active cultural metas (the "animal coin meta," the "political meme meta," etc.).

Photon also added **Dev Profile** functionality: paste a contract address and see the developer's history of previous token launches, their success/failure rate, and whether they have bundled wallets in prior launches. This is forensic information that was previously only available to sophisticated on-chain analysts.

### DEX Screener as Cultural Barometer

Beyond token prices, DEX Screener's trending view is a real-time cultural barometer:
- Which category of meme is generating volume (animal, political, internet character, AI persona)?
- Are most trending tokens sharing a visual aesthetic (indicating a coordinated meta)?
- What narrative-anchoring events (real-world news) are visible in token names and symbols?

DEX Screener's "social links" feature on each token page links directly to the token's Telegram, X account, and website — these are the community artifacts worth analyzing.

### Rickbot as Ethnographic Audit Tool

Rickbot's core function from the outside: paste any contract address and receive a formatted report covering:
- **Holder concentration**: Is this community-owned or insider-owned?
- **Liquidity status**: Is the liquidity locked (dev can't rug easily) or unlocked?
- **Bundle detection**: Were coordinated wallet clusters present at launch?
- **Dev history**: What is this developer's track record?

For research: Rickbot is the difference between analyzing a token based on its community narrative alone vs. analyzing it against the on-chain behavioral reality. The divergence between what a community *says* about a token and what Rickbot *shows* about its on-chain structure is primary research data.

### GMGN.ai Smart Money as Community Signal

GMGN.ai's smart money tracking shows you the wallet behavior of sophisticated participants — the "Cabal" that the BONKbot doc references. When smart money wallets accumulate a token before it gains social visibility, you are observing the moment of coordinated pre-positioning that precedes community narrative formation. This is the behavioral trace of what the community calls "alpha."

As a research tool: tracking which tokens smart money has positioned in before CT discourse begins lets you reconstruct the information cascade after the fact — who knew, when, and what they did.

---

## Political/Values Communities (Groyper-Adjacent)

The intersection of far-right political communities and crypto is real but diffuse. Key findings:

### Where the Community Exists

**X/Twitter — Primary Platform**
The groyper-adjacent crypto community is primarily on X. Since Musk's acquisition and reinstatement of previously banned accounts (including Nick Fuentes briefly in 2023), the far-right presence on X has increased. Key characteristics:
- Uses crypto libertarianism as political framing ("freedom money," "censorship-resistant")
- Overlaps significantly with the "Bitcoin maximalism" community, which has historically attracted right-libertarian participants
- The Fuentes/groyper network specifically is not predominantly crypto-focused — crypto is one of multiple platforms they discuss

**Gab.com — Secondary Platform**
Gab received documented crypto funding surges around January 6, 2021. The Gab.com community maintains crypto discussions, particularly around Bitcoin and Monero (the latter for payment censorship-resistance). Trends.gab.com provides a public trends feed without requiring account creation.

**Telegram — Private Channels**
Far-right political Telegram channels exist but are largely invite-only. Their crypto discussion is primarily about Bitcoin/Monero as "censorship-resistant money" rather than memecoin speculation. This is ideologically distinct from the memecoin trenches community.

**Cozy.tv**
Nick Fuentes's live streaming platform. Political content, not primarily crypto-focused. Accessible publicly for viewing.

### The Memecoin-to-Politics Intersection

There is a specific overlap worth tracking: **politically-themed memecoins** that launch on pump.fun. The BONKbot doc's reference to "Metas: internet memes (Pepe, Chud, Wojak)" names the visual vocabulary of 4chan/far-right internet culture. When these memes are financialized:

- The cultural community that produced the meme (4chan /pol/, far-right forums) intersects with the memecoin trading community
- The coin becomes both a speculative vehicle and a political identity marker
- "$GROYPER" coin exists on Solana — built by memecoin community using the groyper image, not by the Fuentes political organization

**Research approach:** Monitor pump.fun and DEX Screener for tokens using politically charged meme imagery (Pepe, groyper frog, Wojak variants). When these launch, the associated X accounts and Telegram groups will show you the intersection of meme culture, political identity, and financial speculation.

### What an Outsider Gets Wrong About This Intersection

The far-right/crypto connection is more ideological (libertarianism, anti-state) than operational in the memecoin space. The trenches community is more interested in financial extraction than political organizing. Treating all "edgy meme coin" culture as groyper-affiliated would be a significant analytical error. The aesthetic vocabulary overlaps; the political commitment often does not.

---

## Weekly Monitoring Routine (30-min/week protocol)

Structure: Monday morning, 30 minutes total.

### Week-Open Dashboard Check (10 minutes)

1. **Dune Analytics** — pump.fun main dashboard (2 min)
   - What is today's daily launch count vs. last week?
   - What is the graduation rate? Rising = active meta forming; falling = market cooling
   - Note any anomalies in fees or active addresses

2. **DEX Screener Trending** — dexscreener.com/solana/pumpfun (3 min)
   - What visual/narrative categories dominate the trending list?
   - Are there recognizable real-world anchors (news events, cultural moments) visible in token names?
   - Identify 1–2 tokens in the "Graduated" category to analyze more deeply

3. **Kaito.ai Mindshare** (3 min)
   - What narratives are gaining share this week vs. last week?
   - What tokens or projects are driving CT conversation?
   - Note any narrative rotations (e.g., AI agent meta → animal coin meta → political coin meta)

4. **GMGN.ai Trending** — gmgn.ai/trend?chain=sol (2 min)
   - Quick scan of top trending tokens by volume
   - Note any tokens with unusual smart money accumulation before CT visibility

### Deep Observation (15 minutes)

Pick 1–2 items surfaced by the dashboard check and go deeper:

5. **Token analysis** (for 1 token from DEX Screener trending):
   - BubbleMaps: is this community-owned or bundled?
   - Rickbot: contract audit
   - X search for the contract address: what is the organic community saying?
   - DEX Screener social links: what does the community Telegram/X look like?

6. **Narrative tracking** (for 1 narrative from Kaito):
   - Find the 2–3 accounts driving this narrative
   - Read the originating thread/post
   - Check their Tweetscout profile to assess genuine influence vs. paid

### Weekly Memo (5 minutes)

Write a brief observation memo capturing:
- What meta/narrative is active this week?
- What real-world event (if any) is anchoring the current memecoin wave?
- What divergence exists between on-chain reality and community narrative?
- Anything worth coding into a community profile update?

File these in the project's fieldnotes structure. Even brief memos accumulate into temporal maps of narrative cycles.

### Monthly Retrospective (quarterly addition)

Once per month, add 30 additional minutes for:
- Reddit scan: check top posts of the month in r/CryptoMoonShots and r/SatoshiStreetBets to see what reached retail consciousness
- LunarCrush sentiment check: what tokens showed social volume anomalies?
- Update `sources/seed-lists.md` with any new accounts or tools surfaced during the month

---

## Tools Reference

### Free, No-Account-Required

| Tool | URL | Primary Use | Time Investment |
|------|-----|-------------|-----------------|
| DEX Screener | dexscreener.com/solana/pumpfun | Real-time trending, token analysis | 3 min/week |
| Dune Analytics (read) | dune.com | On-chain data, pump.fun dashboards | 2 min/week |
| BubbleMaps | bubblemaps.io | Token holder visualization | Per-token, 2 min |
| Photon Memescope | photon-sol.tinyastro.io | Lifecycle view of launches | 5 min/week |
| GMGN.ai Trending | gmgn.ai/trend?chain=sol | Smart money + trending | 2 min/week |
| PullPush | pullpush.io | Historical Reddit search | Research queries only |
| SocialGrep | socialgrep.com | Real-time Reddit search | Research queries only |
| Reddit RSS | reddit.com/r/[sub]/.rss | Passive subreddit monitoring | Set-and-forget |

### Free, Account Required

| Tool | URL | Primary Use | Time Investment |
|------|-----|-------------|-----------------|
| Kaito.ai | kaito.ai | CT mindshare tracking | 3 min/week |
| LunarCrush | lunarcrush.com | Social sentiment aggregation | 5 min/month |
| Tweetscout | tweetscout.io | Account influence validation | Per-account, 1 min |
| Rickbot (Telegram) | @rick_bot | Contract audit tool | Per-token, 1 min |

### Paid (Optional Upgrade)

| Tool | URL | Primary Use | Cost Tier |
|------|-----|-------------|-----------|
| Nansen | nansen.ai | Institutional wallet intelligence | Paid (starts ~$150/mo) |
| X Pro (TweetDeck) | twitter.com | Column-based X monitoring | X Premium subscription |
| LunarCrush Premium | lunarcrush.com/pricing | Full social analytics | Paid tiers |

### Tool Stack Priority

For minimum viable monitoring with maximum signal:
1. **DEX Screener** — real-time cultural pulse (free)
2. **Kaito.ai** — CT narrative tracking (free)
3. **Dune Analytics** — on-chain ground truth (free)
4. **BubbleMaps** — token community validation (free)
5. **Rickbot** — contract forensics (free)

These five tools, 20 minutes per week, cover the essential observation surface.

---

## Sources

- [Top Crypto Subreddits — Milkroad](https://milkroad.com/social/reddit/)
- [r/CryptoMoonShots Stats — GummySearch](https://gummysearch.com/r/CryptoMoonShots/)
- [Memecoin Twitter Tracker Guide 2025 — Super](https://trysuper.co/blog/memecoin-twitter-tracker-an-ultimate-guide-(2025))
- [Kaito Mindshare — TokenInsight](https://tokeninsight.com/en/tokenwiki/all/mindshare-in-crypto-what-it-is-and-how-to-track-it)
- [Kaito Algorithm Update — BeInCrypto](https://beincrypto.com/kaito-updates-crypto-mindshare-algorithm/)
- [Photon Memescope Guide — Solana Leveling](https://solanaleveling.com/memescope/)
- [Photon Platform Review — Whisper UI](https://whisperui.com/cryptocoins/photon-trading-platform)
- [GMGN.ai Overview — Solana Compass](https://solanacompass.com/projects/gmgn)
- [BubbleMaps on Solana — Solana Box](https://solanabox.tools/tools/bubblemaps)
- [BubbleMaps Unmasks Rug Pulls — CoinTelegraph](https://cointelegraph.com/news/how-bubble-based-mapping-unmasks-memecoin-rug-pulls-and-insider-threats)
- [Rickbot Overview — Solana Box](https://solanabox.tools/tools/rick-bot)
- [Nansen Smart Money Guide 2025](https://www.nansen.ai/post/how-to-monitor-crypto-wallet-activity-track-smart-money)
- [Dune: On-Chain Signals 2026 — BeInCrypto](https://beincrypto.com/dune-on-chain-signals-crypto-2026/)
- [Top Telegram Trading Bots — CoinGecko](https://www.coingecko.com/learn/top-telegram-trading-bots)
- [Banana Gun Blog](https://blog.bananagun.io/blog/the-best-trading-bot-for-meme-coins-airdrops-and-pre-migration-sniping-in-2025)
- [PullPush — Pushshift successor](https://pullpush-io.github.io/)
- [Reddit API Tools 2026 — PainOnSocial](https://painonsocial.com/blog/reddit-api-tools-2)
- [Groypers — Wikipedia](https://en.wikipedia.org/wiki/Groypers)
- [Crypto and the Far Right — IPS](https://ips-dc.org/crypto-and-the-far-right/)
- [Far-Right Bitcoin Adoption — CoinDesk](https://www.coindesk.com/tech/2021/12/08/bitcoin-adoption-among-far-right-extremists-leaves-its-mark-on-the-blockchain)
- [n8n Reddit-CoinGecko workflow](https://n8n.io/workflows/10394-reddit-crypto-market-intelligence-with-coingecko-alerts-to-discord/)
- [Tweetscout — Web3 Social Analytics](https://tweetscout.io/)
- [LunarCrush](https://lunarcrush.com/)
