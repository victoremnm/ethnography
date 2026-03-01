# Hyperliquid

**Profile written:** February 28, 2026
**Status:** Active — dominant perpetual DEX, post-JELLY crisis, HyperEVM ecosystem expanding
**Community archetype:** Performance-maximalist trading community with anti-VC founding myth

---

## What It Is

Hyperliquid is a decentralized perpetual futures exchange that runs on its own purpose-built Layer 1 blockchain, the Hyperliquid L1. It is, as of early 2026, the dominant on-chain derivatives venue by volume: $2.95 trillion in trading volume in 2025, 70%+ market share in decentralized perpetuals, and $844 million in revenue — outpacing Ethereum in revenue terms.

The founding myth is clean and culturally potent: a Harvard-educated HFT engineer (Jeff Yan, former Hudson River Trading) bootstrapped the exchange entirely from trading profits, refused all venture capital, distributed 31% of the token supply directly to users via airdrop, and built a product that matches centralized exchange performance while running on-chain. No VCs. No seed rounds. No allocation to insiders at the expense of traders.

The community that formed around this product is something specific: it is not memecoin culture (though it overlaps), it is not the VC/builder ecosystem (it is explicitly opposed to this), and it is not pure DeFi idealism (performance and user experience matter as much as decentralization claims). It is, more precisely, a **performance-first trading community** organized around a product they believe is categorically better than both centralized exchanges and other DEXes, wrapped in an anti-establishment founding narrative.

The JELLY incident of March 2025 stress-tested this identity in ways that still echo. Hyperliquid's validators intervened to delist a token and settle positions at an arbitrary price to protect the protocol's liquidity vault — a move that was simultaneously praised as competent risk management and condemned as centralized censorship. The community split is instructive: many traders sided with the protocol; DeFi idealists, competing exchanges, and on-chain investigators (ZachXBT, Arthur Hayes) attacked it.

---

## Product Mechanics (How It Works)

### The Hyperliquid L1

Hyperliquid runs on a custom blockchain, not an existing L1 like Ethereum, Solana, or Cosmos. The chain uses **HyperBFT**, a modified BFT consensus mechanism inspired by HotStuff, implemented in Rust. Performance specs as of 2025:

- Sub-second finality (~0.2 second block times)
- Up to 200,000 transactions per second
- Zero gas fees for order placement and cancellation

This puts it in the same performance tier as centralized exchanges (Bybit, OKX), which is the explicit design intent. Most DEXes (dYdX on Cosmos, GMX on Arbitrum) process perhaps 2,000 orders per second at best; Hyperliquid's custom L1 is orders of magnitude faster.

### HyperCore (The Trading Engine)

The flagship product is a fully **on-chain Central Limit Order Book (CLOB)** — not an Automated Market Maker (AMM) like Uniswap or GMX. Every order, every trade, every cancellation is reflected directly in blockchain state. This is technically ambitious because AMMs were historically favored in DeFi precisely because CLOBs require the kind of throughput that general-purpose chains can't handle. Hyperliquid's custom L1 is built specifically to make on-chain CLOB viable.

Key trading mechanics:
- Perpetual futures with up to 50x leverage on major pairs (up to 40x on others)
- 100+ perpetual markets
- Taker fee: ~0.045%; maker fee: ~0.015% (among the lowest in the space)
- No KYC required
- USDC-collateralized (bridged from Arbitrum One)

### HyperEVM

Launched February 18, 2025, HyperEVM is an EVM-compatible execution environment running alongside HyperCore on the same L1. Developers can deploy Ethereum-compatible smart contracts and access native Hyperliquid order books via precompiled contracts. This turns Hyperliquid from a single-product trading venue into a programmable blockchain with a native trading layer. By late 2025, 100+ dApps had deployed — spanning DeFi, lending, launchpads, stablecoins, and AI tools.

### The HLP Vault (Hyperliquidity Provider)

HLP is a **community liquidity pool** embedded directly in the L1's financial engine — not a third-party smart contract. It performs three functions simultaneously:

1. **Market making**: Takes the opposite side of trades when external liquidity is insufficient; runs proprietary high-frequency mean-reverting strategies
2. **Backstop liquidations**: When a trader's position cannot be liquidated through the orderbook, HLP absorbs the underwater position to ensure market stability
3. **Fee accrual**: Receives a portion of all trading fees and redistributes to depositors

HLP historically maintained a net-short bias, which has been profitable in bull markets (retail traders tend to go long). This design creates a structural tension: HLP can be exploited by sophisticated traders who can force favorable liquidations onto it — which is precisely what happened in the JELLY incident.

### The Assurance Fund (AF)

A separate safety pool funded by a portion of trading fees. Acts as a final backstop if HLP losses exceed a threshold. Holds approximately 1.16% of total HYPE supply. If an oracle error prices a position incorrectly, the AF reimburses affected users.

### Fee Buyback and Burn

Hyperliquid uses protocol fees to buy back and burn HYPE tokens, creating deflationary pressure. As of late February 2026, HyperCore was repurchasing ~43,000 HYPE per day. This buyback mechanism is part of what distinguishes Hyperliquid's tokenomics from exchange tokens that don't have direct fee-to-holder value flows.

---

## Community Identity ("HL Maxis")

### Who They Are

The Hyperliquid community is primarily composed of **active derivatives traders** — people who trade perpetual futures as a meaningful part of their financial life. This distinguishes them from:

- Memecoin degens (pump.fun Solana crowd) — primarily spot gamblers on short timeframes
- DeFi idealists — who prioritize decentralization over performance
- VC-ecosystem builders — who Hyperliquid's founding explicitly rejected

The "HL maxi" label is informal. The community's identity is organized less around tribal affiliation and more around **product loyalty reinforced by financial alignment**. After the airdrop created significant wealth for early users, the community has a strong incentive to defend the platform's reputation and stay — their HYPE bags matter.

### Key Identity Markers

**The no-VC narrative.** This is the founding myth that shapes everything. Jeff Yan famously refused all venture capital, arguing that VCs create an "illusion of progress" and that a "scar on the network." When HYPE launched, 76.2% of the token supply was earmarked for the community — a structural fact that differentiated it from every major VC-backed token launch of the same era. This creates a specific form of identity: the community feels ownership in a way that users of VC-backed protocols often do not.

**Performance as virtue.** Unlike DeFi communities that valorize decentralization as the terminal goal, Hyperliquid's community values performance. "CEX-killer" framing is common — the claim that Hyperliquid matches or beats Bybit/OKX on user experience while being on-chain. This is not idealism; it is a product superiority claim.

**Public PnL culture.** Hyperliquid has a native leaderboard showing top traders' all-time and period PnL. This creates a **performance transparency dynamic** unlike most DeFi protocols. Traders broadcast their on-chain positions and results. James Wynn, a pseudonymous trader who turned $6M into $48M (then lost most of it) on 40-50x leverage positions, attracted hundreds of thousands of followers and drove significant trading volume through pure spectacle. His positions sometimes exceeded $1.25 billion notional. His full liquidation became a memorialized cautionary tale.

**The .hl identity domain.** Hyperliquid introduced .hl names as blockchain-native identity markers, functioning as on-chain handles across wallets and dApps. These serve as a cultural shibboleth — having a .hl name signals ecosystem commitment.

**Anti-VC sentiment.** The community's response to competing protocols that took VC money is often derisive. This sentiment extends to dYdX (venture-backed), to Binance-listed tokens (perceived as captured), and to the broader "VC token" meta of 2023-2024 that Hyperliquid positioned itself against.

### Community Archetypes

| Archetype | Behavior | Self-Image |
|-----------|----------|------------|
| **The Power Trader** | Uses Hyperliquid as primary trading venue; high leverage; follows leaderboard | "Serious trader, not a degen" |
| **The HYPE Holder** | Accumulated HYPE during or post-airdrop; stakes for validator rewards; tracks buyback/burn | "Long-term aligned, not speculating" |
| **The HLP Depositor** | Provides liquidity to HLP vault; earns fees; tracks vault P&L | "Running my own market-making book" |
| **The Ecosystem Builder** | Deploying on HyperEVM; building on Hyperliquid infrastructure | "This is the next Ethereum for trading" |
| **The Airdrop Millionaire** | Early user who received significant HYPE at TGE; psychologically attached | "I earned this" |
| **The Watching Whale** | Follows large positions on the public leaderboard; uses copy-trading signals | "Following the smart money" |

---

## The Airdrop and Its Cultural Weight

### What Happened

On November 29, 2024, Hyperliquid launched the HYPE token via genesis airdrop. Key facts:

- **310 million HYPE** distributed to over 94,000 addresses (31% of total supply)
- No manual claim required — tokens sent automatically to wallets
- Distributed based on historical trading activity, points accrued on the platform
- Initial price: ~$3.90; within 48 hours it surged to ~$9.74
- All-time high: $59.39 (September 18, 2025)
- Peak airdrop value: approximately $10.8 billion at ATH

At peak prices, the average recipient received approximately $28,500 worth of HYPE. The distribution was highly skewed: 56.6% of recipients received 100 HYPE or fewer; 83.9% received fewer than 1,000. The top whale claimed $9.56 million worth of tokens in a single address — the largest individual airdrop claim of 2024.

This airdrop is widely described as the largest in crypto history by fully-unlocked value at distribution. The prior record holders (Arbitrum, Uniswap, Jupiter) all came with lock-ups or were substantially smaller in dollar terms. The closest comparator — and the precedent that the community constantly references — is the UNI airdrop of 2020, which also rewarded early users of a DEX.

### Cultural Significance

The airdrop created a specific psychological dynamic: early users who had been grinding on a product before it had a token were suddenly wealthy. This is meaningfully different from people who bought into a token pre-launch. The narrative is "I earned this by using the product" — it generates a sense of meritocratic legitimacy that pure token purchases lack.

This narrative translates into intense product loyalty. People who made $40,000 from an airdrop do not easily switch platforms. They have a financial and psychological stake in the thesis proving out.

The "no VCs" structure amplified this. Because Hyperliquid had no early investor tranches that needed to dump at unlock, the community could genuinely believe that aligned holders held most of the supply. Whether this was strictly true (the Hyper Foundation controls significant HYPE; team tokens vest over multiple years) became a source of ongoing debate — but the narrative was clean enough to be culturally sticky.

### The Anti-VC Backlash and Broader Impact

Hyperliquid's airdrop triggered a wave of community sentiment against VC token structures more broadly. In the 2023-2024 cycle, many projects launched tokens with 20-40% allocations to investors, minimal unlocks at TGE, creating predictable dump patterns. By distributing 76% to the community and 0% to external investors, Hyperliquid made explicit what many in DeFi had been arguing: that VC-token structures extract from retail rather than align with it. This generated genuine industry-wide conversation about tokenomics standards.

---

## The $JELLY Incident (Decentralization Under Pressure)

### Timeline

**March 26, 2025.** A trader opened a $6M short position on JELLYJELLY (a low-cap memecoin perpetual on Hyperliquid) while simultaneously buying JELLY spot on-chain. The spot purchases pumped the JELLY price, triggering the Hyperliquid liquidation engine to absorb the short position into the HLP vault via backstop liquidation. JELLY's price spiked over 400% in under an hour.

With HLP now holding the inherited short position, the attacker continued buying JELLY on-chain, attempting to force HLP into catastrophic losses. At peak, HLP was sitting on ~$13.5 million in unrealized losses. Hyperliquid's $230 million vault was potentially at risk.

**Within two minutes.** Hyperliquid's validators convened and voted to delist JELLYJELLY perpetual contracts. The market was settled at $0.0095 — the price at which the original short was opened, not the manipulated market price of ~$0.50. This price settlement eliminated HLP's losses and clawed back gains from the attacker. Users on the other side of the trade (JELLY longs who had profited from the squeeze) received settlement at $0.0095 rather than $0.50, effectively reversing their profits.

Hyperliquid announced it would make whole all affected users (excluding the flagged attacker's addresses) from the Hyper Foundation.

**Same day.** Binance and OKX both listed JELLYJELLY perpetual futures — interpreted by many as coordinated competitive pressure or at minimum opportunistic capitalization on Hyperliquid's crisis. JELLY's market cap briefly reached $25 million on the external listings.

**March 27, 2025.** HYPE dropped below $15, down from ~$20 pre-incident. TVL fell by over $200 million in 24 hours.

### The Decentralization Critique

The incident crystallized a structural tension that had been latent in Hyperliquid's design:

**The critique:** Hyperliquid's validators (at the time approximately 16 validators, largely Hyper Foundation-controlled) made a unilateral decision to delist an asset and retroactively settle positions at an arbitrary price — in under two minutes. This is not behavior consistent with a decentralized protocol. The fact that it was the "right" decision from a market-protection standpoint does not change its governance character.

ZachXBT's framing was particularly sharp: Hyperliquid had done nothing when North Korean-linked wallets had traded on the platform and moved funds. But when HLP's vault was threatened by a low-cap memecoin squeeze, validators moved in minutes. The selectivity of intervention mapped neatly onto self-interest.

Arthur Hayes: "HYPE can't handle the JELLY. Let's stop pretending Hyperliquid is decentralized."

Bitget CEO Gracy Chen: "[Hyperliquid] operates more like an offshore CEX... immature, unethical, and unprofessional."

**The counterargument (from the Hyperliquid community):** The protocol acted to protect depositors from clear market manipulation. Every major exchange — centralized or decentralized — would have intervened under similar circumstances. The alternative was allowing a coordinated attack to drain community funds. The validators did not enrich themselves; they settled at a price that protected the community at the expense of the attacker.

**The structural reality:** Hyperliquid was never designed to be maximally decentralized — it was designed to be maximally performant. The 16-validator set (expanded from 4 in January 2025) is small enough to coordinate in minutes, which is a feature for the trading product and a vulnerability for the decentralization claim.

### Post-JELLY Protocol Changes

Hyperliquid responded to criticism with concrete governance upgrades:

1. **On-chain validator voting** for asset delistings — validators must publicly announce voting intentions in advance, giving the community time to respond
2. **Maximum open interest caps** for new and small-cap perpetuals — reducing the attack surface for JELLY-style manipulations
3. **Leverage reduction on large-cap assets** to reduce systemic risk from whale positions
4. **Reduced margin allowed at certain profit levels** for open positions, limiting the ability to withdraw collateral from a manipulated long position

These changes addressed the mechanics of the attack but did not resolve the fundamental governance question: a small group of validators remains capable of overriding market outcomes in emergencies.

---

## Security Concerns (North Korea / Validator Centralization)

### The DPRK Warning (December 2024)

In late December 2024, Taylor Monahan (security researcher at MetaMask, known for tracking North Korean hacker activity) posted a warning on X. She identified wallets linked to North Korean hackers that had been trading ETH on Hyperliquid, resulting in approximately $700,000 in liquidations. Her interpretation: "DPRK doesn't trade. DPRK tests."

The implication was that North Korean state-affiliated hackers were performing reconnaissance — learning the platform's liquidation mechanics and behavior, probing for exploitable patterns — in preparation for a larger attack.

**Market reaction:** HYPE dropped ~23% within hours. Over $256 million in net USDC outflows occurred in ~30 hours. December 23 alone saw $502 million in net outflows.

**Hyperliquid's response:** "There has been no DPRK exploit — or any exploit for any matter — of Hyperliquid." The team acknowledged awareness of the reported wallet activity but denied any security breach.

### Why the Security Warning Was Taken Seriously

Monahan's concern was not just that North Korean wallets had traded on the platform. The structural vulnerability she identified was more alarming:

- At the time, Hyperliquid ran on **only 4 validators**, all controlled by the core team
- A two-thirds quorum was required for consensus — meaning 3 of 4 validators needed to be compromised for an attacker to control the chain
- Monahan claimed to have reason to believe the validator machines were not security-hardened, and that founders may have accessed them via devices also used for social media and video calls
- $2.3 billion in USDC was bridged from Arbitrum One and secured by these 4 validators

The attack surface: compromise 3 validators, gain consensus, potentially drain the USDC bridge.

Hyperliquid has since expanded from 4 to 24 validator slots (with high stake requirements for entry), reduced its own direct control through the Foundation Delegation Program, and committed to open-sourcing node code. Whether this fully addresses the security concern is contested.

### Validator Centralization as Ongoing Issue

As of late 2025, Hyperliquid controls approximately 81% of staked HYPE tokens through the Hyper Foundation. This gives the Foundation dominant influence over validator selection and network governance. The community sees this as evidence of meaningful centralization even with an expanded validator set. Critics from traditional DeFi point out that governance by foundation stake is structurally similar to corporate equity voting rights — not meaningfully different from a CEX with a governance token.

The closed-source node code (since being committed to open-sourcing, but not yet fully open as of late 2025) was a separate concern: validators were operating software they didn't fully understand, creating a dependency on the core team's ongoing involvement.

---

## Comparison to Competitors

### vs. GMX

GMX is the original DeFi perps success story, running on Arbitrum. It uses an AMM-style liquidity pool model (GLP/GM pools) rather than a CLOB, meaning traders trade against a pooled collateral base using oracle prices rather than against a live order book. GMX offers lower slippage on large trades via this model but lacks real price discovery — it relies on Chainlink oracles, creating oracle manipulation attack vectors. Hyperliquid's CLOB has genuine price formation and can handle high-frequency order flow that GMX cannot. As of 2025, Hyperliquid has substantially eclipsed GMX in volume and mindshare.

### vs. dYdX

dYdX was the early CLOB pioneer, migrating from Ethereum L2 to its own Cosmos-based chain (dYdX v4, 2023). It offers 200+ markets and up to 100x leverage, making it technically richer in market variety. But dYdX is venture-backed (prominent investors include a16z, Andreessen Horowitz) — a structural fact that the Hyperliquid community uses to dismiss it. dYdX's Cosmos-based architecture also doesn't integrate with EVM tooling as naturally as HyperEVM. In trading volume and community size, Hyperliquid has outgrown dYdX substantially.

### vs. Centralized Exchanges (Bybit, OKX)

This is the real competition framing for the Hyperliquid community. The comparison:

| Dimension | Bybit/OKX | Hyperliquid |
|-----------|-----------|-------------|
| KYC | Required | Not required |
| Custody | Exchange holds funds | Self-custody |
| Speed | Sub-100ms | ~200ms (sub-second) |
| Fee structure | ~0.1% taker | ~0.045% taker |
| Transparency | Black box | All on-chain, verifiable |
| Censorship risk | High (can freeze accounts) | Lower (in theory) |

The honest assessment: Hyperliquid is genuinely close to CEX performance. Its speed is not "DeFi speed" — it is competitive. The no-KYC advantage is real for users in restricted jurisdictions or those who value financial privacy. The self-custody advantage is real after FTX.

But the $JELLY incident demonstrated that Hyperliquid can and does intervene in ways that centralized exchanges intervene — just via validators rather than compliance officers. The question of whether on-chain validator voting is meaningfully more censorship-resistant than a centralized exchange's risk team is unresolved.

### vs. Other Perp DEXes (edgeX, Lighter, Vertex)

By 2025, Hyperliquid had established itself as the clear S-tier perp DEX, with Lighter at A-tier and others further behind. Community tier lists (such as the Stacy Muur X thread circulated in mid-2025) formalized this perception. The competitive threat is less from current alternatives and more from whether a new entrant builds something that replicates Hyperliquid's performance-first design with better governance properties.

---

## Observation Points

### Primary Communities

**Discord (Official)**
- discord.com/invite/hyperliquid
- ~81,780 members as of early 2026
- Technical support, governance discussions, ecosystem development
- Moderated by team; relatively formal compared to Telegram

**X (Twitter) — Primary Cultural Layer**
- @HyperliquidX — official account
- Community lives on X; most cultural production (memes, criticism, whale watching) happens here
- Key accounts to follow:
  - @HyperliquidX (official)
  - @HyperliquidNews (community news aggregator)
  - Traders who build public followings through leaderboard performance
  - @jeff_wangwang (Jeff Yan's X — sporadic, cryptic, high signal)

**Telegram**
- Multiple alpha groups oriented around Hyperliquid trading signals
- Not officially affiliated; primarily trading-focused, not governance-focused
- Higher noise than Discord; appropriate for tracking community sentiment in real-time

### Leaderboard as Cultural Object

The native Hyperliquid leaderboard (app.hyperliquid.xyz/leaderboard) is a cultural artifact. Top 100 traders by all-time and period PnL. This is not just analytics — it creates a visible performance meritocracy. Traders who break into top 10 gain social capital on X. Multiple third-party trackers (hyperdash.info, ASXN stats.hyperliquid.xyz) have been built around this data.

James Wynn's ascent to public prominence via the leaderboard — turning $6M to $48M in 2 months through 40x BTC longs, then losing ~99% — is the ur-example of how leaderboard culture translates into social media following and real trading volume.

### Key Research Venues

- **Hyperliquid Gitbook Docs** (hyperliquid.gitbook.io) — official technical documentation
- **Hyperliquid Wiki** (hyperliquid-co.gitbook.io/wiki) — community-maintained knowledge base
- **stats.hyperliquid.xyz** — ASXN analytics dashboard; real-time TVL, open interest, HLP performance
- **DeFiLlama** (defillama.com/protocol/hyperliquid) — cross-protocol TVL comparison
- **Hyperliquid Policy Center** (hyperliquidpolicy.org) — Washington DC advocacy org, funded by Hyper Foundation (1M HYPE); signals institutional ambitions

---

## Thread Mapping

### Thread 5 — Cypherpunks / Crypto Sovereignty (Decentralized Exchange)

**Fit: High, but complicated**

Hyperliquid aligns with the cypherpunk aspiration of permissionless, self-custodial financial infrastructure. No KYC. On-chain settlement. Access for any wallet holder globally.

But the $JELLY incident revealed that Hyperliquid's "decentralization" is instrumental, not ideological. The founders built a fast exchange that happens to run on-chain; they did not build a censorship-resistant system as a first-order goal. When the vault was at risk, they intervened — and most of their community agreed this was the right call.

This is an important distinction for Thread 5 analysis: Hyperliquid represents a **pragmatic sovereignty** claim, not an absolutist one. Users value it for self-custody and permissionless access, but they accept that the founding team retains meaningful control. This is similar to the governance of Uniswap Labs versus the Uniswap Protocol — the front end and core team retain more power than the "decentralized" framing suggests.

**Research question for Thread 5:** Does Hyperliquid represent a new synthesis of performant centralization + sovereign access? Or is it a DeFi product temporarily wearing decentralization clothes until it needs to take them off?

### Thread 3 — Cybernetics (The Matching Engine)

**Fit: Direct**

The Hyperliquid L1 is a cybernetic system: the matching engine processes information (orders) and produces outputs (trades) at sub-second speed, with feedback loops built into the liquidation and market-making mechanics. The HLP vault is an adaptive agent that adjusts its exposure in real time based on market conditions.

More interesting for Thread 3: the interaction between the automated liquidation engine and human traders represents a genuine cybernetic tension. The $JELLY attack was, at its core, an attempt to exploit the automatic rules of the liquidation system — to make the engine behave predictably in an adversarial way. The validators' override broke the deterministic system and introduced human judgment. This is a live example of the limits of fully automated financial cybernetics.

The order book itself — matching anonymous buyers and sellers in sub-second cycles without human intermediaries — is an expression of Wiener's original cybernetics vision applied to finance.

### Thread 8 — Status / Desire (The Trader Identity)

**Fit: Very high**

Hyperliquid's community is organized explicitly around performance status. The public leaderboard makes PnL a visible, social fact. James Wynn's public positions attracted hundreds of thousands of followers not because of what he thought, but because of what he *did* — the scale and audacity of his bets. His liquidation was mourned and memorialized.

The Hyperliquid trader identity is aspirational in a very specific way: it is about being a "serious" trader, not a "degen." Memecoins are luck; perpetuals are skill. The distinction may be partly illusory (leveraged perps are not necessarily more skill-dependent than spot memecoins), but the community holds it firmly. Hyperliquid's CLOB, with its maker-taker mechanics and order types, is a credential — it is the platform serious traders use.

The no-VC founding myth translates into a status claim: "I was here before it was obvious." The airdrop made this claim financially legible. Holding HYPE became a statement of having been right, early, about something. Selling HYPE is psychologically complex because it means acknowledging that the bet is complete.

---

## Contested Views

**"Hyperliquid is not actually decentralized and never was."**
Accurate as a technical statement. The validator set is small, the Hyper Foundation controls most staked HYPE, the code was long closed-source, and the team can and does intervene. The platform's performance advantages require centralization at the consensus layer. Defenders argue this is a temporary state on the road to meaningful decentralization; skeptics argue that systems that are centralized when stakes are high will always intervene when stakes are high.

**"The $JELLY intervention was the right call."**
Contested within crypto itself. The Hyperliquid community largely agrees it was correct — the alternative was a $230M vault potentially being drained by manipulation. Critics argue that a genuinely decentralized system should not be able to make this call at all, and that the precedent now exists for future interventions. The comparison to FTX is inflammatory and mostly wrong (FTX stole user funds; Hyperliquid protected them), but the governance question is legitimate.

**"Hyperliquid will face regulatory action."**
An increasingly serious concern. The no-KYC model, North Korean wallet activity, and the scale of the platform have put it on regulators' radar. The Hyperliquid Policy Center (DC lobbying funded by Hyper Foundation) signals the team is aware of this risk and is trying to get ahead of it. The JELLY incident also triggered comparisons to regulated financial venues — if Hyperliquid can intervene in markets, regulators may argue it functions more like an exchange that should be regulated as one. [Confidence: MEDIUM — this is an evolving situation]

**"The HLP vault model is fundamentally exploitable."**
The $JELLY incident was not unique — a similar (smaller) exploit had occurred earlier in 2025 involving the ETH whale who forced $4M in losses onto HLP. The community's response was risk management upgrades. Critics argue the fundamental design — HLP as both market maker and backstop liquidator — creates a structural vulnerability that clever traders will continue to probe. [Confidence: HIGH based on documented exploits]

**"Jeff Yan and team are still essentially in control."**
The Hyper Foundation controls 81% of staked HYPE and thus validator selection. The team allocated significant supply to itself (vesting over 1+ year from TGE). The "community-owned" narrative is accurate in that most supply eventually goes to community, but the current concentration means governance is effectively team-controlled. [Confidence: HIGH based on staking data]

---

## What to Watch

**Token unlock schedule.** March 6, 2026 releases 9.92M HYPE (~$271M) for Core Contributors — the first significant team unlock. Community perception of how team members sell or hold will shape trust dynamics significantly.

**Validator decentralization.** Current trajectory: expanding from 24 validators, increasing non-foundation stake, open-sourcing node code. Watch whether foundation delegation share decreases meaningfully over 2026.

**HyperEVM ecosystem traction.** Whether the 100+ dApps on HyperEVM generate genuine TVL and user activity, or remain speculative. If Hyperliquid becomes a full-stack financial blockchain (lending, stablecoins, structured products) rather than just a perp DEX, the community and competitive dynamics change substantially.

**Regulatory developments.** The Hyperliquid Policy Center's DC work, any SEC/CFTC guidance on perp DEXes, and the evolving KYC question. If regulation forces KYC onto Hyperliquid, a significant portion of its user base advantage disappears.

**The next manipulation attempt.** HLP remains a structural target. The risk management upgrades post-JELLY reduced the attack surface but did not eliminate it. Watch for sophisticated actors probing new vectors.

**Institutional entry.** As 2025 was described as the year CLOB perp DEXes proved they could scale, 2026 is framed as the year institutional capital begins treating on-chain perps as real infrastructure. If Hyperliquid captures institutional flow, the community dynamics shift: HLP volatility decreases, the platform becomes more stable, and the governance questions matter more to counterparties who care about legal certainty.

**Competitive pressure from Lighter, edgeX.** Lighter generated $1.3T in volume in 2025 (vs. Hyperliquid's $2.95T). If the gap closes, and if a competitor offers better governance transparency at comparable performance, Hyperliquid's community could face defection pressure.

---

## Sources

### Primary (HIGH confidence — official sources, industry publications)

- Hyperliquid Official Documentation: hyperliquid.gitbook.io/hyperliquid-docs
- Hyperliquid Wiki: hyperliquid-co.gitbook.io/wiki
- [CoinDesk: Crypto Exchange HyperLiquid Announces Native Asset HYPE, Users to Receive 310M Tokens](https://www.coindesk.com/business/2024/11/28/crypto-exchange-hyper-liquid-to-airdrop-310-m-tokens-to-early-adopters)
- [Fortune: How a Harvard grad helped make Hyperliquid the biggest new player in crypto](https://fortune.com/2026/01/12/hyperliquid-jeff-yan-defi-perpetuals-perps-exchange-defi/)
- [CoinDesk: HyperLiquid Delists JELLY After Vault Squeezed in $13M Tussle](https://www.coindesk.com/markets/2025/03/26/hyperliquid-delists-jellyjelly-after-vault-squeezed-in-usd13m-tussle)
- [Blockworks: Hyperliquid under scrutiny amid signs of North Korean hacker activity](https://blockworks.co/news/hyperliquid-security-fuels-decentralization-concerns)
- [CoinTelegraph: Hyperliquid net outflows top $250M amid fears over North Korea hackers](https://cointelegraph.com/news/hyperliquid-outflow-north-korea-exploit-fears)
- [The Block: Hyperliquid delists JELLYJELLY memecoin amid whale manipulation fiasco](https://www.theblock.co/post/348314/hyperliquid-delists-jellyjelly-memecoin-amid-whale-manipulation-fiasco)
- [CoinDesk: Most Influential: Jeff Yan (2025)](https://www.coindesk.com/business/2025/12/19/most-influential-jeff-yan)
- [BlockEden: Hyperliquid's $844M Revenue Machine](https://blockeden.xyz/blog/2026/01/10/hyperliquid-revenue-dominance-onchain-trading-solana/)
- [CoinTelegraph: Bitget CEO slams Hyperliquid's handling of JELLY incident](https://cointelegraph.com/news/bitget-ceo-slams-hyperliquid-jelly-perps-delisting)

### Secondary (MEDIUM confidence — verified reporting, community sources)

- [CoinGecko: What Is Hyperliquid and What the Hyperliquid Airdrop Means for DeFi](https://www.coingecko.com/learn/what-is-hyperliquid-and-what-the-hyperliquid-airdrop-means-for-defi)
- [Blocmates: Founder Jeff Yan Explains Why Hyperliquid Said 'No' to VCs and Still Won Big](https://www.blocmates.com/news-posts/founder-jeff-yan-explains-why-hyperliquid-said-no-to-vcs-and-still-won-big)
- [ForkLog: The largest airdrop in history: Hyperliquid becomes a new standard](https://forklog.com/en/hype-or-a-new-standard-what-hyperliquids-airdrop-historys-most-generous-teaches-us/)
- [PANews: Jeff Yan — No venture capital, no CEX](https://www.panewslab.com/en/articles/1f6379af-33f3-4601-b711-48eeeffe5ec8)
- [OAK Research: Hyperliquid and the JELLY attack](https://oakresearch.io/en/analyses/investigations/hyperliquid-jelly-attack-context-vulnerability-team-solution)
- [Talos: $JELLY's Last Jam - Adventures in Hyperliquid Margin Risk Management](https://www.talos.com/insights/jellys-last-jam)
- [Halborn: Explained: The Hyperliquid Hack (March 2025)](https://www.halborn.com/blog/post/explained-the-hyperliquid-hack-march-2025)
- [Messari: Understanding the Hyperliquid Jelly Drama](https://messari.io/copilot/share/understanding-the-hyperliquid-jelly-drama-feaac2b3-c05e-43e5-80f9-b6988dcce812?destination=copilot)
- [RocknBlock: How Hyperliquid Works: Architecture, Order Book, HyperEVM](https://rocknblock.io/blog/how-does-hyperliquid-work-a-technical-deep-dive)
- [Nansen: What Is Hyperliquid?](https://www.nansen.ai/post/what-is-hyperliquid)
- [CoinDesk: How Centralization Concerns Hit the Hype Around a Decentralized Exchange](https://www.coindesk.com/business/2025/04/10/how-the-hype-for-hyperliquid-s-vault-evaporated-on-concerns-over-centralization)
- [Phemex: Hyperliquid's 2025 Growth: $6 Billion TVL, 1.4M Users](https://phemex.com/news/article/hyperliquid-achieves-major-growth-in-2025-with-6-billion-tvl-51621)
- [CoinDesk: Hyperliquid Whale James Wynn Fully Liquidated](https://www.coindesk.com/markets/2025/05/31/cryptos-most-watched-whale-gets-fully-liquidated-after-placing-billions-in-risky-bets)
- [Cryptobriefing: Hyperliquid Labs addresses reports of North Korean-linked activity](https://cryptobriefing.com/north-korean-wallet-activity-hyperliquid/)
- [The Defiant: Hyper Foundation Backs New DC Lobby with 1M HYPE](https://thedefiant.io/news/defi/hyperliquid-policy-center-launches)

### Flags / Unverified

- Claim that Hyperliquid controls "81% of staked HYPE" is widely reported but the original source is community analysis, not official disclosure. Treat as approximate.
- James Wynn's claimed trading trajectory ($6M to $48M to near-zero) comes from self-reported X posts and community analytics tools, not formally audited.
- North Korean wallet identification relied on Taylor Monahan's analysis at MetaMask — not formally confirmed by government attribution.
