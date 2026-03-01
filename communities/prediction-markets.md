# Prediction Markets

## What They Are

Prediction markets are platforms where participants buy and sell contracts tied to the outcomes of future events — elections, economic data, scientific findings, sports results. Prices represent crowd-sourced probability estimates. The core thesis: **markets aggregate information better than polls, pundits, or experts** because participants put real money behind their beliefs.

---

## The Major Platforms

| Platform | Model | Notes |
|---------|-------|-------|
| **Polymarket** | Decentralized, USDC-settled, Polygon | Dominant; ~70% of CT mindshare; returned to US after CFTC approval |
| **Kalshi** | Regulated US exchange (CFTC) | ~17% CT mindshare; structured safety, more accessible to retail |
| **Manifold** | Social/play-money | Research-oriented; real-money features largely dormant as of 2025 |
| **Metaculus** | Aggregated forecasting, no real money | Elite forecaster community; longest calibration track record |
| **OpinionLabs** | Decentralized, BNB Chain focus | The "Eastern" counterpart; AI-scaled long-tail markets; volume leader in Asia |

**The 2026 dynamic**: Polymarket vs. Kalshi is a 4:1 CT mindshare split (Kaito data, 24H window: 69.51% vs 17.36%). Both platforms are growing; the competition is real but Polymarket's on-chain volume is an order of magnitude larger.

---

## OpinionLabs (The Eastern Counterpart)

While Polymarket dominates the Western/Global narrative, **OpinionLabs (O.LAB)** has emerged as the volume leader in Asia (BNB Chain, Mantle, opBNB).

**Key Differentiators:**
1.  **AI-Powered Long-Tail:** Uses AI oracles to automate market creation and settlement for niche events (local gossip, regional esports) that Western platforms ignore.
2.  **Content-First:** The "AlphaOrBeta" app serves as a gamified, social top-of-funnel that feeds users into the financialized O.LAB markets.
3.  **Fee Capture:** Unlike Polymarket's growth-first zero-fee model, OpinionLabs generated $13M+ in protocol fees by Jan 2026.

**Risks (Devil's Advocate):**
- **Wash Trading:** On-chain analysis suggests trade sizes 13-25x larger than competitors, hinting at "airdrop farming."
- **Oracle Failures:** The **Jan 1, 2026 "Context Contamination" incident** saw AI oracles settle markets incorrectly based on poisoned open-source data.
- **Regulatory Arbitrage:** No-KYC structure on BNB Chain invites eventual regulatory crackdown.

---

## Primary Source Index (2026 Prediction Markets)

- **On-Chain Audit:** [Dune Analytics: "Is OpinionLabs' $8B Volume Real?"](https://dune.com/datadashboards) (Feb 23, 2026). Note: the original Dune dashboard title uses "Opinion Lab's" spelling — standardized here to "OpinionLabs" per platform branding.
- **Social Hub:** [@vitalik.eth on Farcaster](https://warpcast.com/vitalik.eth) — Primary source for d/acc and "epistemic infrastructure" discourse.
- **Leaderboard:** [Kaito Information Markets](https://kaito.ai) — Real-time mindshare tracking for platforms and creators.

---

## Contested Views: Building Around the Periphery

### The Wash-Trading Reality
The Feb 23 Dune Report confirms that OpinionLabs' volume is largely illusory.
- **Fact-Check:** OpinionLabs produced 31% of industry volume with **<3% of total transactions**.
- **The "Points Trap":** Much of this volume is high-value addresses (likely bots/farmers) cycling capital to maximize airdrop points.
- **Epistemic Dilution:** While Polymarket serves as a "truth machine," OpinionLabs currently functions as a **"liquidity machine."** Its prices are less a reflection of crowd wisdom and more a reflection of farming efficiency.

---

## On-Chain Reality (Live Dune Data)

Polymarket processes **$160–190M in USDC per day** through its CTF Exchange contract on Polygon, with **6–8 million outcome token transfers per day** representing position opens, trades, and settlements.

| Day | USDC Volume | Transfers |
|-----|-------------|-----------|
| Feb 27, 2026 | $192M | 8.2M |
| Feb 26 | $171M | 7.1M |
| Feb 25 | $177M | 7.6M |
| Feb 24 | $161M | 7.1M |
| Feb 22 | $164M | 6.1M |

**Source:** Live query against `tokens.transfers` for USDC → Polymarket CTF Exchange contract (`0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e`) on Polygon. Query reproducible via Dune Analytics with a free API key.

Volume nearly 5x'd from the start of 2025 per a16z's State of Crypto 2025 report. The on-chain data confirms — this is not narrative; it is settlement volume.

---

## What the 2024 Election Changed

The 2024 US Presidential Election was a mainstreaming event for prediction markets. Polymarket and Kalshi provided real-time probability data that outperformed traditional polling, drawing institutional attention and coverage from mainstream financial media.

This single event:
1. Proved prediction markets could beat the media/polling complex at information aggregation in a high-stakes public test
2. Drew institutional attention and capital
3. Gave the space political legitimacy it previously lacked

**On the French whale**: The $30M Trump bet on Polymarket generated the most narrative attention. The "proprietary polling" interpretation is one hypothesis. Others: aggressively risk-tolerant and right; coordinating with others to move the market; hedging real-world exposure. Any confident assertion about motive here is not grounded.

---

## Who Uses Them

| Participant Type | Motivation | Edge |
|----------------|------------|------|
| **Epistemic rationalists** | Calibrate beliefs against market; intellectual sport | Deep reading, probabilistic reasoning |
| **Political insiders** | Access to non-public information or networks | Information asymmetry |
| **Macro traders** | Express views on policy, fed rates, geopolitics | Existing financial sophistication |
| **Sports bettors** | Familiar mechanics, new venue | Domain expertise |
| **Researchers** | Study information aggregation and market efficiency | Academic interest |

---

## Two Very Different Cultures Within One Label

**Metaculus / Superforecaster culture and Polymarket culture are not points on a spectrum — they are nearly separate communities.**

**Metaculus / Superforecasters:**
- Professional forecasters treating this as a discipline with 10-year track records
- Calibration scores, Brier scores as primary status credentials
- View Polymarket with mild contempt as "a gambling site with good PR"
- Deliberately small, knowledge-selective community
- LessWrong / Rationalist adjacent

**Polymarket / Kalshi:**
- PnL is the actual status currency, not calibration score
- Most participants don't track calibration at all
- The rationalist epistemic frame is the *aspiration*, not the description
- A large portion of volume is here to win; the intellectual project is incidental

The revealed preference is PnL. The stated preference is intellectual rigor. Conflating these is a significant analytical error.

---

## Cultural Identity and Status Mechanics

**Status by platform:**
- **Metaculus**: Calibration scores, Brier scores, long-form reasoning. "I was wrong and here's why" earns genuine respect.
- **Polymarket/Kalshi**: PnL, first to call a major event correctly, size of winning position.

**Shared community norms (where they do apply):**
- **Reasoning is visible** — you share your thesis, not just your position (stronger norm on Metaculus than Polymarket)
- **Contrarianism is rewarded** when backed by evidence
- **Conflict of interest is at least acknowledged** in the Metaculus/rationalist community

**Linguistic register**: formal and analytical. References to "base rates," "outside view," "reference class forecasting," "Superforecasters" (Tetlock's work). LessWrong / Rationalist adjacent.

---

## CT Mindshare: Who's Actually Driving This Discourse

Source: Kaito Information Markets leaderboard, 3-month window.

**Platform mindshare (24H snapshot):**

| Platform | Mindshare |
|----------|-----------|
| Polymarket | 69.51% |
| Kalshi | 17.36% |
| OpinionLabs | 3.54% |
| MYR | 2.50% |
| Limitless | 2.09% |
| All others | ~5% |

**Creator leaderboard (top signal nodes, 3M):**

The "smart follower ratio" (smart followers / total followers) measures audience quality — how concentrated the following is in people who are themselves influential. High ratio = high-quality signal node.

| Rank | Handle | Mindshare | Smart Followers | Total | Smart % | Identity |
|------|--------|-----------|----------------|-------|---------|----------|
| 1 | IcoBeast.eth | 2.27% | 2,714 | 68,944 | 3.9% | CT-native PM commentator |
| 2 | John Wang | 2.21% | 3,735 | 61,033 | **6.1%** | High-density audience |
| 3 | CJ (晨杰) | 1.48% | 906 | 23,338 | 3.9% | Chinese-language CT voice |
| 5 | Tarek Mansour | 1.28% | 1,453 | 69,147 | 2.1% | **Kalshi CEO** |
| 6 | Shayne Coplan | 1.21% | 4,222 | 160,881 | 2.6% | **Polymarket CEO** |
| 13 | Nick Tomaino | 0.65% | 4,484 | 76,624 | **5.9%** | 1confirmation VC |
| 23 | jesse.base.eth | 0.53% | 7,256 | 346,836 | 2.1% | Jesse Pollak, Base/Coinbase |
| 53 | hildobby | 0.28% | 2,428 | 31,187 | **7.8%** | Dune Analytics researcher |
| 88 | Haseeb | 0.20% | 5,606 | 141,667 | 4.0% | Dragonfly Capital |

**Three structural observations:**

1. **Both platform CEOs in the top 6.** Tarek Mansour (Kalshi) and Shayne Coplan (Polymarket) are personally generating CT mindshare. Founder credibility is the product's credibility in this space.

2. **hildobby at rank 53 has the highest smart follower ratio (7.8%).** He's a Dune Analytics researcher focused on on-chain prediction market data. Low total reach, maximum audience quality. The practitioner most worth following for analytical signal.

3. **CJ (晨杰) at rank 3** — a Chinese handle in the top 3 of an English-dominant leaderboard. Confirms that prediction markets CT is not exclusively US/English.

**OpinionLabs** at 3.54% — newer than MYR and Limitless but already outpacing both. The one to watch for platform competition.

---

## Structural Developments (Feb 2026)

Three events in Feb 2026 that signal where the space is heading:

**1. Polymarket acquired Dome (Feb 19)**
Dome was a prediction market API startup. The acquisition signals Polymarket is building toward becoming the **infrastructure backbone of the predictions industry** — not just a consumer app but an API layer that other markets and data products plug into. This changes the competitive dynamics: Polymarket isn't competing with Kalshi for retail users; it's building the plumbing Kalshi would have to pay to use.

**2. Polymarket + Kaito launched Attention Markets (Feb 10)**
Polymarket and Kaito AI launched prediction markets based on **social media mindshare and sentiment data** across X, TikTok, and YouTube. This is the direct bridge between CT analytics and prediction markets: you can now bet on which token, person, or narrative will win mindshare. The Kaito data this repo tracks (creator leaderboards, mindshare percentages) becomes directly financializable.

**3. Three regulatory battles (Bankless, Feb 14)**
The prediction market boom has triggered three distinct fights: (1) whether they're gambling or financial instruments under CFTC jurisdiction; (2) the Polymarket vs. Kalshi regulatory model competition (permissionless vs. CFTC-registered); (3) the political legitimacy question post-2024 election. The CFTC chair (Michael Selig) filed a brief declaring federal supremacy over US prediction markets (Feb 17) — defending CFTC exclusive jurisdiction against state-level attempts to regulate.

**Bankless thesis (Feb 21)**: "Prediction markets are markets. Markets should be regulated at the federal level." — Bankless has taken an explicitly pro-federal-regulation stance, framing CFTC oversight as legitimizing rather than restricting.

---

## Intersection with AI and Crypto

1. **Crypto rails**: Polymarket runs on Polygon, settling in USDC. Trustless settlement for trustless predictions is genuine product-market fit — not a technical choice looking for a use case.
2. **AI as participant**: LLMs are being benchmarked against Polymarket. Research ongoing into whether LLM forecasts approach human Superforecaster calibration.
3. **Crypto narratives as markets**: Prediction markets bet on crypto events (ETF approvals, protocol launches, regulatory decisions), creating feedback loops between CT and prediction markets.
4. **AI + market design**: Next frontier is AI-generated markets — automatically creating resolvable questions from news events, automating liquidity provision. PiP World (tracked by Kaito's AI category) is explicitly building this.
5. **Attention markets**: Polymarket × Kaito attention markets (Feb 2026) make social media mindshare directly tradeable — CT discourse now has a financial instrument attached to it.

---

## Post-2024 Political Contamination

The 2024 election success created a legitimacy problem: **Polymarket became politically associated with the right** because it called Trump's victory more aggressively and earlier than polls did.

The epistemic claim — "markets aggregate information better than polls" — became entangled with a political one — "Trump supporters were right, pollsters were wrong." The result:
- Left-leaning journalists and researchers became more skeptical of prediction markets as a neutral information source
- The French whale narrative concentrated attention on one actor rather than the mechanism
- The market mechanism's neutrality claim became contested political territory

This is a real reputational liability for the space. Kalshi's regulated structure insulates it somewhat; Polymarket's permissionless design makes it harder to distance from.

---

## The Epistemics Foundation

The rationalist community (LessWrong, Slate Star Codex lineage) sees prediction markets as **epistemic infrastructure** — holding intellectuals accountable for claims in ways think-pieces never do. The Metaculus track record is the closest thing that exists to empirical accountability for public intellectual claims.

The **Hayek question** is foundational: can prices aggregate distributed information efficiently? Prediction markets are the empirical test. The answer so far: yes, better than polls and pundits, but with structural vulnerabilities (adverse selection, liquidity concentration, political capture of interpretation).

---

## Key Entry Points

| Handle / Resource | Role | Platform |
|------------------|------|----------|
| `@hildobby` | On-chain PM data analyst; highest smart-follower ratio in the space | X / Dune |
| `@ShayneCoplan` | Polymarket CEO; personally drives CT discourse | X |
| `@TarekMansour` | Kalshi CEO | X |
| `@NateSilver538` | Public forecaster; mainstream legitimacy signal | X / Substack |
| Philip Tetlock | Academic; *Superforecasters* author | Academic |
| Scott Alexander | Astral Codex Ten; rationalist framing | Substack |
| Polymarket CTF Contract | `0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e` on Polygon | Dune |
| Kaito PM Leaderboard | Real-time mindshare tracking | kaito.ai |

---

## Sources
- [Prediction Markets Explode in 2025 — The Block](https://www.theblock.co/post/383733/prediction-markets-kalshi-polymarket-duopoly-2025)
- [Prediction Markets Go Mainstream — Nieman Lab](https://www.niemanlab.org/2024/12/prediction-markets-go-mainstream/)
- [a16z State of Crypto 2025](https://a16zcrypto.substack.com/p/state-of-crypto-2025-the-latest-data)
- [Great Prediction War 2026 — FinancialContent](https://markets.financialcontent.com/stocks/article/predictstreet-2026-2-5-the-great-prediction-war-polymarket-vs-kalshi)
- [The 3 Fights Over Prediction Markets — Bankless, Feb 14 2026](https://www.bankless.com/read/the-3-fights-over-prediction-markets)
- [A First-Principles Defense of Prediction Markets — Bankless, Feb 21 2026](https://www.bankless.com/read/a-first-principles-defense-of-prediction-markets)
- [Polymarket Snaps Up Prediction Market API Startup Dome — Bankless, Feb 19 2026](https://www.bankless.com/read/news/polymarket-snaps-up-prediction-market-api-startup-dome)
- [Polymarket Partners With Kaito to Launch Attention Markets — Bankless, Feb 10 2026](https://www.bankless.com/read/news/polymarket-partners-with-kaito-to-launch-attention-markets)
- [CFTC Chief Defends Agency's Exclusive Control over Prediction Markets — Bankless, Feb 17 2026](https://www.bankless.com/read/news/cftc-chair-selig-defends-exclusive-federal-jurisdiction-over-prediction-markets)
- Dune Analytics: live query, `tokens.transfers` on Polygon → CTF Exchange contract, Feb 2026
- Kaito Information Markets leaderboard: kaito.ai, 24H and 3M windows, Feb 2026
