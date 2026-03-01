# ReFi / Public Goods

## What This Is

Regenerative Finance (ReFi) is the ideological counterweight to extractive crypto — the community that insists blockchains can be pointed at positive externalities rather than maximizing individual yield. It sits at the intersection of mechanism design, environmental finance, and Ethereum-native governance, and it has produced the most sophisticated body of thought about *how to fund things that markets systematically underfund*.

The community has two distinct wings that sometimes overlap and sometimes operate independently:

**The Mechanism Design Wing**: Gitcoin, Optimism's Retro Funding, Protocol Guild, clr.fund, Octant — projects that apply cryptoeconomic mechanisms (quadratic funding, retroactive grants, conviction voting, staking yield redirection) to fund public goods, primarily software and Ethereum infrastructure.

**The Climate/Nature Wing**: Toucan Protocol, KlimaDAO, ReFi DAO — projects that tokenize environmental assets (carbon credits, biodiversity credits) and attempt to route DeFi capital toward environmental restoration.

These wings share vocabulary and philosophical ancestry but have diverged sharply on credibility. The mechanism design wing has shipped real products, distributed $60M+ in grants, and produced peer-reviewed mechanism papers. The climate wing peaked in late 2021 with KlimaDAO's meteoric rise and near-total collapse, leaving behind a trail of legitimate critiques about carbon credit quality and a deep reputational hangover that the broader ReFi label has not fully escaped.

The core thesis, stated cleanly: **"It's easier to agree on what was useful in the past than on what might be useful in the future."** This is Optimism's founding insight for retroactive public goods funding — and it is the most important intellectual contribution this community has made to mechanism design.

---

## On-Chain / Platform Evidence

### Gitcoin Grants Program

The flagship public goods funding experiment in Ethereum. Since 2019, Gitcoin has run 24+ grant rounds distributing over **$60 million** via quadratic funding to 3,500+ projects, with an additional $50M+ in matching from protocols and foundations.

Key facts:
- **GG20 (2024)**: Community rounds spanning ETH Infrastructure, OSS, Climate, Education, and DeSci
- **GG24 (October 2025)**: Introduced the "Domain Allocator" model; Gitcoin manages a unified program across 4-5 domains; a $350,000 Dev Tooling/Web3 Infra round approved via deep funding
- **The pivot**: Gitcoin wound down **Grants Lab** (its primary software development unit) in April 2025 and **Grants Stack** (its grants infrastructure product) in May 2025 — "due to a lack of profitability." The software-as-a-service thesis failed. What remains is the grants program itself, now running on partner infrastructure and focused exclusively on the Ethereum ecosystem.
- **Allo Protocol**: The open-source capital allocation protocol Gitcoin built before the wind-down. A permissioned-but-open framework for running QF rounds. Projects like Giveth and custom round operators still run on it, but Gitcoin is no longer maintaining the consumer-facing Grants Stack interface.

**GTC token**: The governance token for Gitcoin DAO. As of February 2026, trading at approximately $0.09 — a 97%+ decline from its 2021 all-time high. The token's collapse is the financial expression of the broader tension: the mission is real, the market cap was speculation.

### Optimism Retro Funding (RPGF → Retro Funding)

The most ambitious retroactive public goods funding experiment in crypto. The core thesis: reward impact that already happened, because it's easier to measure than to predict.

| Round | Amount | Recipients | Scope |
|-------|--------|------------|-------|
| Round 1 (2021) | $1M | 58 projects | Early Optimism ecosystem |
| Round 2 (2022) | 10M OP | 195 projects | Broad ecosystem |
| Round 3 (2023) | 30M OP (~$110M) | 501 contributors | Builders, educators, creators |
| Round 4 (2024) | 10M OP | ~100 projects | OP Stack contributors |
| Round 5 (2024) | 8M OP | Focused pool | OP Stack infrastructure |
| Round 6 (2024) | 2.4M OP | Focused pool | Q4 2024 domain-specific |

**The $3B commitment**: In March 2024, the Optimism Collective committed 850 million OP tokens (~$3B) to retro funding over multiple years.

**The name change controversy**: In Round 4, Optimism dropped "Public Goods" from the branding, renaming "RPGF" to simply "Retro Funding." This drew significant community criticism — it was read as a retreat from the public goods mandate in favor of narrow Superchain ecosystem capture. The community tension was real: VC-backed projects were receiving "public goods" funding, which critics called definitional corruption.

**2025 evolution**: Smaller, more targeted rounds. The lesson from mega-rounds (Round 3) was explicit in the governance forum: "mega rounds devolve into popularity contests." The 2025 strategy involves faster iteration cycles and domain-specific focus.

**Karl Floersch's role**: Floersch (co-founder, OP Labs CEO) was the original intellectual architect of RPGF. His 2021 ETHOnline talk with Vitalik remains the canonical statement of the retroactive funding thesis.

### Protocol Guild

**What it is**: A curated split contract that directs donated tokens directly to 150+ active Ethereum core protocol contributors via a 4-year vesting schedule. No central organization — the membership self-curates, the contract is immutable, the math does the distributing.

**Why it matters mechanically**: Protocol Guild solves the free-rider problem for Ethereum L1 development. Ethereum core dev work is an enormous positive externality that the market consistently underprices. Protocol Guild routes value back to the people who actually maintain the blockchain everyone else profits from.

**Funding model**: Projects built on Ethereum donate 1% of their native token allocation to Protocol Guild. ENS DAO passed EP1.9 donating to the pilot. The target is $100M passing through the vesting contract annually.

**The split contract**: Donations flow to `theprotocolguild.eth` → immutable 4-year vesting contract → pass-through wallet → split contract distributing to individual members. The architecture is the ideology made code: no intermediary, no committee, trust-minimized.

### Octant

**What it is**: A public goods funding platform built by the Golem Foundation, powered by 100,000 ETH staked from the Golem treasury. Staking yield is split: 70% to users who lock GLM, 25% to public goods projects, 5% to the Octant Community Fund.

**The mechanism**: 90-day "epochs." Users lock at least 100 GLM → earn proportional ETH rewards → at epoch end, choose to: (a) withdraw ETH, (b) donate ETH to public goods projects of their choice. The community votes on which projects are eligible. Donation decisions are matched against a participation-weighted formula.

**Scale**: $1.5M+ distributed to public goods projects across the first several epochs. Small by Optimism standards, but the funding mechanism is novel: it's yield-sustained, not reliant on a foundation writing checks.

### clr.fund

A permissionless, trust-minimized quadratic funding protocol that uses **MACI** (Minimal Anti-Collusion Infrastructure) — a zk-SNARK-based system that prevents bribery and coordination attacks on quadratic voting. Built for the Ethereum ecosystem, backed by the Ethereum Foundation.

The 2024 ETHStaker × clr.fund round had a $350K DAI matching pool. clr.fund runs lighter and more technically rigorous than Gitcoin — smaller rounds, stronger anti-collusion guarantees, less community infrastructure.

### Hypercerts

A new primitive: semi-fungible ERC tokens that represent claims of past work and impact. The mechanism:
1. A project creates a hypercert for completed work
2. Funders (retroactive or forward-looking) buy fractions of the hypercert
3. The transaction creates a traceable, on-chain record of both the work and the recognition
4. Future retroactive funders can use hypercerts as signal

Originated at Protocol Labs, adopted by Gitcoin's Supermodular ecosystem. The intended function is to create impact markets — where claims of impact are verified, valued, and traded — as an alternative to subjective grant committee decisions.

---

## Community Mechanics

### Status Mechanics

Status in this community is almost perfectly inverted from the rest of CT:

**What earns status:**
- Running a multi-year public goods project with documented impact
- Mechanism design contributions (papers, implementations, novel protocol designs)
- Consistent participation in grant rounds as donor, not just recipient
- Track record of open-source contributions that benefited many
- Intellectual clarity about what "public goods" actually means economically

**What destroys status:**
- Token speculation framed as mission alignment
- Claiming public goods while holding a VC-backed treasury
- Impact reports that are vague, unverifiable, or metric-gamed
- Moving from ReFi to more profitable narratives without acknowledgment
- "Public goods washing" — using the frame to extract grant money without meaningful impact

**The key shibboleth**: Can you distinguish a public good (non-excludable, non-rivalrous) from a club good from a toll good from a private good? People who understand Samuelson's taxonomy are in. People who use "public good" as synonymous with "socially beneficial" are adjacent but not core.

### Governance Participation

The community is unusually governance-dense. Active participants:
- Vote in Gitcoin community rounds (as donors, weight by quadratic matching)
- Hold "badgeholder" status in Optimism's Citizens' House (responsible for retro funding allocation)
- Participate in Octant epoch governance
- Contribute to Allo Protocol's governance forum
- Engage seriously in mechanism design debates on the Ethereum Magicians forum

Being a badgeholder in Optimism's Citizens' House is the highest status credential in this space — it signals that the Optimism Collective has recognized you as having good judgment about what benefits the public good.

### The Green Pill Frame

Kevin Owocki's 2022 book *GreenPilled: How Crypto Can Regenerate the World* introduced the "Green Pill" as the ReFi community's counter-mythology to the Red Pill / Blue Pill discourse.

**The Red Pill** (NRx/e/acc framing, per Thread 6 of this corpus): taking the red pill means seeing that democratic institutions are captured and corrupt. The response is exit, sovereignty, and founder rule.

**The Green Pill**: takes the same awareness of institutional failure but draws the opposite conclusion. Yes, existing institutions are failing to fund public goods, coordinate on climate, or prevent tragedy of the commons. The response is not exit into sovereign enclaves but *building better coordination mechanisms* that can compete with extraction on its own terrain.

The green pill is explicitly a counter-mythology to the red pill, not an ignorance of it. Owocki's book was co-authored by Vitalik Buterin, Glen Weyl, Danny Ryan, and Balaji Srinivasan — the latter inclusion notable given that Balaji is a Network State / sovereign individual thinker. The community explicitly engages with the critique from the right.

The phrase "meme public goods into existence" appears in the original GreenPill podcast announcement. This is not accidental — it acknowledges that the community's power is partly memetic, that changing what people believe to be valuable *is* funding those things.

### Circles of Participation

**Inner circle**: Mechanism designers, academic economists working on public goods theory (Glen Weyl / RadicalxChange orbit), Gitcoin and Optimism core contributors, Protocol Guild members, Ethereum Foundation researchers.

**Second circle**: Gitcoin grant round operators, badgeholders, active Octant participants, ReFi DAO node operators.

**Third circle**: Grant recipients, regular donors in QF rounds, people who follow Green Pill podcast, broader "impact in web3" adjacent community.

**Adjacent/overlapping**: EA/longtermism community (significant overlap on mechanism design and positive externality logic), DeSci (decentralized science uses similar grant mechanisms), Ethereum social layer.

---

## Philosophical Roots

### Thread 10 — Left Accelerationism

The ReFi / public goods community is the most direct application of Thread 10 in this corpus. The premise is explicitly L/ACC: technology is accelerating, crypto infrastructure is being built, the question is not whether but *toward what*. The response is not to slow the machine (not EA's precautionary approach) but to redirect it: "keep the tech, change the incentive direction."

Kevin Owocki's formulation: "cryptoeconomic systems that create positive externalities for their neighbors and for the world." This is L/ACC applied to token engineering — not "stop building DeFi" but "use DeFi primitives to fund non-DeFi goods."

### Thread 2 — EA / Longtermism

Heavy overlap with effective altruism on mechanism design. The EA community has engaged seriously with quadratic funding (Vitalik's paper has an EA Forum entry with substantive debate), hypercerts, and retroactive funding. The shared vocabulary is "positive externalities," "expected impact," and "mechanism design as applied ethics."

The difference: EA tends toward centralized grant-making with expert evaluation panels; the ReFi community tends toward decentralized community signal aggregation (quadratic voting as the epistemic mechanism). Both optimize for impact; they disagree on whether expertise or community preference is the better signal.

Longtermist adjacent: maintaining Ethereum L1 infrastructure is framed as an existential risk reduction activity — "if Ethereum fails, we lose the coordination platform for solving coordination problems."

### Thread 4 — Epistemic Rationalism

Mechanism design IS applied epistemics in this community. The central questions:
- What incentive structures produce accurate signals about what is valuable?
- How do you aggregate individual preferences without collusion?
- How do you prevent the measurement of impact from becoming a game?

Quadratic funding is specifically an answer to the Hayekian distributed-knowledge problem applied to public goods. The argument: communities know what is valuable to them better than central planners do, but markets underprovide non-excludable goods. QF is the mechanism that aggregates distributed community preference (the Hayekian epistemic claim) and corrects for market failure (the public goods claim) simultaneously.

**The Buterin-Hitzig-Weyl paper** ("Liberal Radicalism: A Flexible Design for Philanthropic Matching Funds," 2018, published in Management Science) is the canonical text. It proves mathematically that under the "standard model," quadratic funding achieves first-best public goods provision. Every quadratic funding implementation in crypto is downstream of this paper.

**MACI (Minimal Anti-Collusion Infrastructure)** is the rationalist's solution to the rationalist's problem: if you build a mechanism to aggregate preference, you must also build a mechanism to prevent that aggregation from being gamed. MACI uses zero-knowledge proofs to make it impossible for buyers to verify to sellers whether they voted a certain way — removing the collusion incentive.

### The Public Goods Problem (Economic Grounding)

The community is unusually literate about the actual economic theory:

**Paul Samuelson's taxonomy** (1954): goods are non-excludable (can't prevent consumption) and non-rivalrous (one person's consumption doesn't reduce another's). Open-source software is the paradigm case — I can't stop you from reading the code, and your reading doesn't stop me from reading it.

**The free rider problem**: rational actors don't fund non-excludable goods because they can benefit without paying. This produces chronic underfunding of software infrastructure, basic research, and environmental goods.

**The matching problem**: traditional matching grants (1:1 matching) favor rich donors. Quadratic funding inverts this: many small donations are matched more generously than few large donations, because the count of donors is a stronger signal of community preference than the total amount.

---

## Key Figures

**Kevin Owocki** (@owocki): Co-founded Gitcoin in 2017, left in 2022, founded Supermodular (a ReFi venture studio) to continue the mission. Author of *GreenPilled* (2022), host of the Green Pill podcast (200+ episodes). The ideological center of gravity for this community — the person who most consistently bridges mechanism design, Ethereum culture, and climate impact. His departure from Gitcoin and the subsequent wind-down of Grants Lab is the central biographical narrative of the community's institutional struggles.

**Vitalik Buterin**: Co-author of the quadratic funding paper; has written extensively on public goods funding, open source, and coordination problems. His March 2025 essay "We should talk less about public goods funding and more about open source funding" is a significant update to the community's framing — arguing that "open source" is more legible and less gameable than the term "public goods," which has become a "social game" where insiders define what qualifies.

**Karl Floersch**: CEO of OP Labs; intellectual architect of RPGF. Co-invented the retroactive public goods funding model. His "Ether's Phoenix" framing — that Ethereum's fees create a fund that can be retroactively allocated to what made Ethereum valuable — is the mechanism's intellectual origin.

**E. Glen Weyl**: Microsoft Research economist; co-inventor of quadratic funding and quadratic voting; founder of RadicalxChange. The academic grounding for the entire mechanism design wing. His work with Buterin produced the mathematical proof underlying QF. His current focus is "plurality" — democratic technology that reflects genuine diversity rather than flattening it.

**Tobi Shorin**: Design researcher; wrote "Life After Lifestyle" and other influential essays about the limits of identity-as-consumption. Adjacent to ReFi through his work on how communities develop genuine shared purpose vs. aesthetic signals. More influential in the broader "coordination" adjacent discourse than in direct ReFi building.

**Tim Beiko**: Ethereum core developer, Protocol Guild. Representative of the "people who actually maintain the thing everyone uses" layer — Protocol Guild's credibility comes partly from his profile as someone who is visibly underfunded relative to the value created.

---

## Language and Shibboleths

| Term | What it reveals |
|------|----------------|
| **"Positive externalities"** | Samuelson/Pigou economic vocabulary; signals real familiarity with the underlying theory, not just vibes |
| **"Quadratic"** | Shorthand for the entire QF mechanism family; using it correctly signals mechanism design literacy |
| **"Retroactive PGF" / "RPGF"** | The O.G. term; still used by people from the pre-rename era; using it vs. "Retro Funding" signals whether you're old guard or newer entrant |
| **"Regen"** | Casual shorthand; "regen not degen." Used self-referentially, often with some irony |
| **"Public goods washing"** | Critical term; using it signals that you're aware of the failure mode and have a principled stance |
| **"Impact = profit"** | Optimism's founding mantra; the claim that building public goods should become a profitable activity through retroactive funding |
| **"Coordination failure"** | The framing for why public goods are underfunded; everyone in this community can define this |
| **"Sybil resistance"** | The mechanism challenge: how do you prevent one entity from registering many identities to game QF? Gitcoin Passport / Human Passport was the product answer |
| **"Green pill"** | Taking the green pill means believing crypto can be regenerative; used without irony in this community, with self-awareness about its mythological construction |
| **"Schelling point"** | Gitcoin has called itself a "Schelling point for public goods funding" — meaning it's the natural coordination point even without explicit communication |
| **"Long-tail funding"** | QF's ability to fund many small projects that centralized grants miss — the democratic argument for the mechanism |

**Farcaster, not Twitter**: The core ReFi community has migrated heavily to Farcaster. Vitalik's Farcaster presence (`@vitalik.eth`) is the signal node; Protocol Guild members and Gitcoin contributors are disproportionately present there. Following the discourse on CT alone misses significant community depth.

**Mirror and Paragraph**: Long-form writing in this community lives on Mirror (for Ethereum-native credibility) and Paragraph. Optimism's major announcements go to `optimism.mirror.xyz`. Gitcoin's governance debates live on `gov.gitcoin.co`.

---

## Intersection with Other Communities

### vs. DeFi / Memecoin Culture (Thread 8)

Explicit counter-culture. The community explicitly uses "regen" as the antonym of "degen." The status mechanism is perfectly inverted: in CT, conspicuous risk-taking and PnL are the status signals; in ReFi, sustained contribution to public goods that earns you no personal financial return is the status signal.

This creates a real structural tension: the community depends on crypto rails and crypto capital, but it's culturally hostile to the financialization instinct that generates the capital. The people writing checks to Gitcoin rounds often made that money by activities the ReFi community would characterize as extractive.

### vs. Ethereum Foundation / Ethereum Social Layer

ReFi is Ethereum-native in a way that is not incidental. The reasons:

1. Ethereum's account-based model (vs. Bitcoin's UTXO) enables smart contracts that can implement QF mechanisms on-chain
2. Ethereum's fee structure (sequencer revenue, MEV, transaction fees) creates a natural pool that can be routed to public goods — this is literally the Optimism model
3. The Ethereum community's cultural identity as "the blockchain that cares about values" (vs. Solana's speed/throughput focus) makes it the natural home for public goods discourse
4. Ethereum core devs are the primary beneficiaries of Protocol Guild and a significant beneficiary of RPGF

**Is ReFi Ethereum-native or chain-agnostic?** The mechanism design wing is deeply Ethereum-native. The climate wing (KlimaDAO, Toucan) ran primarily on Polygon (cheaper fees for small credit trades). ReFi DAO positions itself as chain-agnostic. But the center of gravity, the canonical texts, the people who matter — all Ethereum.

### vs. EA / Longtermism (Thread 2)

Significant philosophical overlap; meaningful institutional separation. EA has engaged with QF papers; EA Forum has substantive posts about impact markets and hypercerts. But:

- EA tends toward expert-panel grant evaluation; ReFi tends toward community-preference aggregation
- EA is skeptical of crypto as a funding mechanism (high transaction costs, speculation contamination); ReFi is premise-committed to crypto rails
- The longtermist wing of EA is primarily focused on AI safety, not open-source infrastructure; ReFi's longtermism is focused on Ethereum infrastructure as coordination layer for everything else

The overlap is most real with the **DeSci** (decentralized science) community, which is using Gitcoin grants and Allo Protocol for scientific research funding — the same mechanism design, different domain.

### vs. a16z Ecosystem

Complicated. a16z has backed Optimism (the company). Optimism runs RPGF. There is therefore a direct line from a16z capital to the ReFi public goods experiment.

The tension: a16z's thesis is about protocol monopolies and VC-backed infrastructure; the ReFi thesis is that public goods should be community-owned and infrastructure-funded. These can coexist at the company level (Optimism is a company) but create friction at the ideological level.

The controversy over VC-backed projects receiving RPGF funding (Blockworks covered this in 2024) is the live expression of this tension: if a project has VC backing, is its work still a "public good" for RPGF purposes? The community has not resolved this.

### vs. Prediction Markets (Thread 4)

Mechanism design cousins rather than the same community. Both communities believe that well-designed incentive structures aggregate information better than central decision-makers. But prediction markets are about aggregating beliefs; QF is about aggregating preferences for public goods funding. The shared ancestor is Glen Weyl (who has written on both).

**Robin Hanson's futarchy** is the deepest convergence point: "vote on values, bet on beliefs." RPGF can be read as a form of futarchy for public goods — badgeholders vote on what was valuable (beliefs about impact), but this is governed by community values expressed through which domains get funded.

---

## Counter-Discourse

### "Public Goods Washing"

The harshest internal criticism. The claim: "public goods" has become a social category that projects adopt to access grant money, not a rigorous economic category that describes actual public provision. The signal: projects with functioning revenue models, venture funding, and private user bases are receiving QF matching as if they're providing non-excludable, non-rivalrous goods.

Vitalik's March 2025 essay is the most significant acknowledgment of this from a core figure. His argument: "public goods" has become ambiguous enough to enable "social games" — insiders define it expansively to include their allies and restrictively to exclude competitors. "Open source" is more defensible because it has a legal definition, a technical verification method, and a track record of community assessment.

**The specific failures cited:**
- Projects game QF by organizing donor coordination (Sybil attacks, collusion rings where communities agree to vote for each other)
- RPGF rounds allocate to projects primarily based on popularity metrics, not impact metrics — the badgeholder voting process in Round 3 was widely criticized as a popularity contest
- Climate/carbon ReFi projects made environmental claims that were not verifiable on-chain and depended on the integrity of legacy carbon credit registries that turned out to be compromised

### The KlimaDAO Collapse

KlimaDAO launched in August 2021, used Olympus DAO-style (3,3) bonding mechanisms to acquire carbon credits via Toucan Protocol, and briefly held more than 17 million tons of CO2-equivalent in its treasury. The KLIMA token launched at ~$3,600 and was below $5 within six months.

**The carbon credit quality problem**: Toucan's bridging mechanism had no quality filter — any Verra-certified carbon credit could be tokenized. CarbonPlan's analysis ("Zombies on the Blockchain") documented that a significant portion of credits tokenized by Toucan and held by KlimaDAO were low-quality, non-additional, or outright problematic credits that Verra's verification process had failed to catch. KlimaDAO later spent $1M+ from its treasury retiring the lowest-quality credits — an admission that the original thesis was compromised.

**The deeper critique**: Toucan's arbitrage model drew the cheapest credits on the market, not the best ones. A $2 credit from a legacy registry could be bridged onto Polygon and traded at a premium because "blockchain carbon." This is not ReFi — it's using blockchain rails to put lipstick on junk offsets.

**The reputational consequence**: The KlimaDAO collapse gave every critic of ReFi a concrete case study. "ReFi was KlimaDAO and look what happened" is a real obstacle for the mechanism design wing, which is substantially different in structure and rigor but shares the brand.

### Impact Measurement as Unsolved Problem

The deepest unsolved problem in the entire community: **how do you measure impact of public goods?**

QF can aggregate preference but cannot verify impact. RPGF can allocate retroactively but depends on badgeholders' subjective judgment. Hypercerts can create auditable records of claimed work but cannot verify whether the work actually produced the claimed benefit.

The mechanism design community has produced sophisticated proposals (impact attestations, evaluator networks, on-chain proof of impact) but none have achieved production scale. Every RPGF round has faced criticism for specific allocation decisions that looked political rather than impact-driven.

The honest state of the field: preference aggregation is solved (quadratic funding works as described); impact measurement is unsolved. The community is building toward the latter but has not arrived.

### Gitcoin's Financial Failure

Gitcoin distributed $60M+ in grants but could not find a sustainable business model. The Grants Stack (the software it built to run QF rounds) was not adopted at scale by paying customers. The software division burned capital without generating revenue, and the GTC token's collapse destroyed the treasury value.

The failure is real and should be named clearly: **Gitcoin built real public goods (the grants rounds), but it built them on a speculative token treasury that evaporated with the market, and it could not monetize the software it built to run those rounds.**

This is not a critique of the mission — it is a critique of the organizational structure. A public benefit corporation (like Optimism PBC) funded by protocol revenue is a more durable model than a DAO funded by a governance token.

---

## What to Watch

**1. Optimism Retro Funding's institutional drift**

The rename from RPGF to "Retro Funding" is one signal. The pressure to fund VC-backed projects is another. The question for 2026: does the Citizens' House (the badgeholder system) develop enough independent institutional identity to resist capture by Superchain business interests, or does it become a marketing budget for OP Labs portfolio?

The 2025 move to smaller, more targeted rounds is a double-edged development: more focused impact potential, but also more opportunity for the foundation to define what counts as impactful.

**2. Gitcoin 3.0 / GG25 and beyond**

After sunsetting Grants Stack and Grants Lab, Gitcoin refocused entirely on running the grants program. GG24 (October 2025) showed the new model working: unified program, domain allocators, external infrastructure. GG25 is the real test of whether a grants program without proprietary software is viable. Follow `gov.gitcoin.co` for real-time governance signal.

**3. Hypercerts reaching production scale**

Hypercerts have been in development since 2022. If impact certificates achieve genuine liquidity and verification infrastructure in 2026, they create a new asset class that links retroactive funding to forward investment in public goods. The Hypercerts Foundation (backed by Protocol Labs) is the org to watch.

**4. Protocol Guild's $100M annual target**

Protocol Guild's ambition is to have $100M/year passing through its vesting contract to Ethereum core developers. Current run rate is far below this. If major Ethereum L2s (Base, Arbitrum, Polygon) begin donating protocol revenue to Protocol Guild, it would validate the model and become the most consequential public goods funding mechanism in crypto by size.

**5. Vitalik's "open source > public goods" reframe**

The March 2025 essay is the most important recent development in this community's intellectual trajectory. If Ethereum-adjacent funding begins shifting from "public goods" to "open source" as the primary frame, it changes: (a) what projects can credibly apply, (b) how impact is evaluated, and (c) whether the climate wing of ReFi remains associated with the mechanism design wing.

Watch: does RPGF continue using "public goods" framing or does Optimism's documentation converge on "open source infrastructure"?

**6. The climate wing's second act**

KlimaDAO has been rebuilding since 2022. Toucan Protocol has tightened credit quality standards. A second generation of tokenized environmental credits — biodiversity credits, regenerative agriculture credits — is being developed. The question is whether the infrastructure quality has improved enough to avoid the CarbonPlan critique. If a legitimate institutional buyer (a major corporation with credible sustainability commitments) acquires tokenized environmental credits at scale, it would rehabilitate the climate wing's credibility.

---

## Sources

- [Liberal Radicalism: A Flexible Design for Funding Public Goods — Buterin, Hitzig, Weyl (2018/2019, Management Science)](https://scholar.harvard.edu/files/hitzig/files/buterin_hitzig_weyl_draft.pdf)
- [Quadratic Payments: A Primer — Vitalik Buterin (2019)](https://vitalik.eth.limo/general/2019/12/07/quadratic.html)
- [We should talk less about public goods funding and more about open source funding — Vitalik Buterin (March 2025)](https://vitalik.eth.limo/general/2025/03/29/pubos.html)
- [Gitcoin Grants 20: Results & Recap — Gitcoin Blog](https://www.gitcoin.co/blog/gitcoin-grants-20-results-recap)
- [Gitcoin Grants 2025 Strategy — Gitcoin Blog](https://www.gitcoin.co/blog/gitcoin-grants-2025-strategy)
- [Focusing Gitcoin's Future: Sunsetting Grants Stack — Gitcoin Governance](https://gov.gitcoin.co/t/focusing-gitcoins-future-sunsetting-grants-stack-eol-may-2025/20333/2)
- [Ethereum public goods funding protocol Gitcoin winding down its software division — The Block](https://www.theblock.co/post/352055/ethereum-public-goods-funding-protocol-gitcoin-winding-down-its-software-division)
- [Announcing RetroPGF Round 3 Recipients — Optimism Collective](https://optimism.mirror.xyz/37Bgum6MfTJWDuE41CH9RXSH5KBm_RCL5zsSFeRZl4E)
- [RetroPGF Round 6 — Optimism Docs](https://community.optimism.io/citizens-house/rounds/retropgf-6)
- [The Evolution of Retro Funding in 2025 — Optimism Governance Forum](https://gov.optimism.io/t/the-evolution-of-retro-funding-in-2025/9414)
- [Optimism's $3 Billion Retroactive Funding Round Draws Criticism for Name Change — Unchained Crypto](https://unchainedcrypto.com/optimisms-3-billion-retroactive-funding-round-draws-criticism-for-name-change/)
- [Optimism squabbles over public goods funding to VC-backed projects — Blockworks](https://blockworks.co/news/optimism-vc-backed-project-funding)
- [Protocol Guild funds Ethereum core developers using Splits — Splits](https://splits.org/blog/protocol-guild/)
- [Announcing Protocol Guild — stateful.mirror.xyz](https://stateful.mirror.xyz/mEDvFXGCKdDhR-N320KRtsq60Y2OPk8rHcHBCFVryXY)
- [The Next Stage for Public Good Funding in Crypto — CoinDesk (Sept 2024)](https://www.coindesk.com/opinion/2024/09/20/the-next-stage-for-public-good-funding-in-crypto)
- [Zombies on the Blockchain — CarbonPlan](https://carbonplan.org/research/toucan-crypto-offsets)
- [Tokenized carbon credits in voluntary carbon markets: the case of KlimaDAO — Frontiers in Blockchain (2024)](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2024.1474540/full)
- [The ReFi movement in Web3: implications for the Global Commons — Frontiers in Blockchain (2025)](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2025.1564073/full)
- [GreenPilled: How Crypto Can Regenerate the World — Kevin Owocki (2022)](https://www.amazon.com/GreenPilled-How-Crypto-Regenerate-World/dp/1034928163)
- [Gitcoin Co-Founder Kevin Owocki Unveils ReFi Incubator Supermodular — Yahoo Finance / CryptoNews](https://finance.yahoo.com/news/gitcoin-co-founder-kevin-owocki-190102079.html)
- [Hypercerts: A new primitive for public goods funding — Protocol Labs](https://www.protocol.ai/blog/hypercert-new-primitive/)
- [Octant FAQ and How it Works — Octant Docs](https://docs.octant.app/en-EN/faq.html)
- [Announcing Octant — Golem Foundation (August 2023)](https://golem.foundation/2023/08/08/announcing-octant.html)
- [clr.fund: Permissionless Quadratic Funding with MACI](https://blog.clr.fund/clr-fund-explained-pt-1/)
- GreenPill Podcast — Kevin Owocki, ~200 episodes, launched via Bankless Network (2022–present)
- Gitcoin GG24 governance: `gov.gitcoin.co`, October–December 2025 threads
- GTC token price: CoinMarketCap / CoinGecko, February 2026 (~$0.09)
