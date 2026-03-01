# Netnography — Research Methods

Netnography is ethnography adapted for online communities: you participate in, observe, and analyze digital cultures using the same rigor applied to fieldwork. The foundational text is Robert Kozinets, *Netnography: Doing Ethnographic Research Online* (2010, updated 2019).

**This repo uses netnography as its primary method.** The `communities/` directory is the fieldwork. The `theory/` directory is the analytical framework. The `sources/` directory is the triangulation layer.

## Sources
- Netnography overview: https://en.wikipedia.org/wiki/Netnography
- Digital ethnography (Decision Lab): https://thedecisionlab.com/reference-guide/anthropology/digital-ethnography
- Academic overview: https://pmc.ncbi.nlm.nih.gov/articles/PMC10280005/

---

## Core Practices

### 1. Participant Observation

Lurk before posting. Understand the community's:
- Status hierarchy (who has authority, how it is earned)
- Language and shibboleths (vocabulary that signals membership)
- Rituals (gm/gn, daily posting patterns, event coordination)
- Identity formation (how members perform community belonging)

In crypto/AI communities, *posting* is the participation. Watching CT without posting is field observation. Responding to CT is field participation. Distinguish these clearly in your notes.

### 2. Trace Data Capture

Online communities leave recoverable traces. Collect systematically:
- Archived Twitter threads (use Nitter mirrors or archive.org)
- Discord server histories (where accessible)
- On-chain behavioral data (Dune, Nansen, DeFiLlama)
- Publication timestamps (when did this narrative emerge?)

**The on-chain layer is unique to crypto netnography.** Wallet behavior is public, pseudonymous, and timestamped. Token purchases, DAO votes, and liquidity provision are behavioral traces with no equivalent in other online communities.

### 3. Coding and Memoing

Assign conceptual codes to field observations:
- **Community codes:** Language, status signal, ritual, initiation, boundary-marking
- **Philosophical codes:** Which thread does this activate? (Reference `theory/philosophical-roots.md`)
- **Temporal codes:** Emerging / established / declining narrative

Write memos after each observation session — brief notes connecting a specific observation to a broader pattern. These become the raw material for community profile updates.

### 4. Triangulation

No single source is sufficient. For each claim in a community profile:
1. Primary source (what the community says about itself)
2. External analysis (what outside researchers say)
3. Behavioral trace (what the data shows)

When these three diverge, that divergence is the most interesting finding. A community that *says* it is decentralized but has whale-dominated governance (behavioral trace) is more interesting than either fact alone.

### 5. Reflexivity

Document your own position. For this research: the analyst is a Stanford MS&E grad / engineering manager approaching these communities as an educated outsider with VC-adjacent professional ambitions. This position:
- Enables: structural analysis that insiders can't see
- Limits: embodied community knowledge that only comes from deep participation
- Biases: toward strategic/intelligence framing over pure anthropological observation

State your analytical position when your position might affect the reading.

---

## The "Adversarial Fact-Checking" Protocol

To prevent echo-chamber analysis, every community deep-dive must undergo a **"Refute/Contest"** stress test.

### 1. Identify the "Success Narrative"
Isolate the primary claim the community makes about itself.
- *Example:* "AI Agents are sovereign economic actors."
- *Example:* "Prediction markets are unbiased truth machines."

### 2. Seek the "Counter-Signal"
Find the data point that contradicts the narrative.
- *Technique:* **On-Chain Forensics.** If the narrative is "volume," check unique wallet count. (e.g., OpinionLabs: $8B volume but <3% of transactions = wash trading).
- *Technique:* **Infrastructure Audit.** If the narrative is "sovereignty," check the dependencies. (e.g., Agents rely on centralized APIs = "API Tether" risk).

### 3. Narrative-as-a-Judge
Use trusted critical voices to evaluate the claim.
- *Action:* Cross-reference community claims with skeptics outside the consensus (e.g., Zvi Mowshowitz for prediction markets, Molly White for crypto).
- *Output:* A dedicated "Contested Views" section in every research document.

---

## The Summarize CLI in Research Workflow

The `summarize` tool (`npm i -g @steipete/summarize`) is the primary method for source ingestion. It accepts URLs, YouTube videos, Substacks, and PDFs.

**Standard research workflow:**

```bash
# Single source
summarize "https://example.com/article" --length xl --plain

# YouTube (with slides for visual content)
summarize "https://youtube.com/watch?v=..." --slides --plain

# Force specific model (for cross-model reproducibility)
summarize "https://..." --model cli/claude --length xl --plain
summarize "https://..." --model cli/gemini --length xl --plain
```

After summarizing, use `/ethnography-ingest` to map output to threads and format for `sources/canonical-texts.md`.

**When to summarize vs. read in full:**
- Summarize first: news articles, Substack posts, conference talks, long reports
- Read in full: founding texts that anchor a philosophical thread; artifacts requiring close reading

---

## Source Credibility Tiers

When evaluating any source, assign a tier:

| Tier | Description | Examples |
|------|-------------|---------|
| **Primary source** | The ideology itself; founding documents | Andreessen Manifesto, Bitcoin whitepaper, Balaji's *Network State* |
| **Analysis** | External research with methodology | Life Itself web3 guide, academic papers, Messari research |
| **Counter-analysis** | Steelman critique | Other Internet essays, Kate Crawford, Zeynep Tufekci |
| **Signal** | Real-time behavioral intelligence | Dune dashboards, Nansen wallet data, Kaito mindshare |
| **Community artifact** | Content from within the community | CT threads, Discord discussions, Telegram channels |

Credibility is **tier-specific, not absolute.** A community artifact has low credibility as objective fact but high credibility as evidence of what a community believes. A Dune dashboard has high credibility as behavioral evidence but zero credibility as explanation of that behavior.

---

## Research Debt Tracker

Known gaps — address via `/ethnography-ingest` or new community profiles:

**Missing community profiles:**
- [ ] Farcaster / Warpcast — crypto-native social layer
- [ ] DeSci — decentralized science (EA + longtermism + crypto)
- [ ] Open-source AI — Hugging Face, open-weights culture
- [ ] RWA / Stablecoin ecosystem — institutional crypto on-chain
- [ ] Regulatory layer — a16z policy team, Coinbase Institute

**Missing theory documents:**
- [ ] `theory/temporal-map.md` — emergence/peak/cooling timeline for each community
- [x] `theory/argument-map.md` — fault lines and active debates

**Missing source entries in canonical-texts.md:**
- [ ] Thread 2 (EA/Longtermism) — no entries yet
- [ ] Thread 4 (Prediction Markets) — no entries yet
- [ ] Thread 7 (Performativity) — no entries yet
- [ ] Thread 8 (Status/Desire Theory) — no entries yet
- [ ] 6 seed list URLs pending from sources/seed-lists.md
