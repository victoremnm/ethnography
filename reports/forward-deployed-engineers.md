# Forward Deployed Engineers: An Ethnographic and Analytical Profile

**Audience**: Engineering manager, skeptical of the role's actual value, seeking honest analysis over marketing.
**Method**: Web research, job posting analysis, alumni retrospectives, VC/industry writing, Glassdoor reviews, practitioner blogs.
**Date**: 2026-02-27

---

## Report Metadata

- **Community**: Forward Deployed Engineers (FDEs) — Palantir-origin, now broadly diffused across enterprise AI
- **Analyst**: Research synthesis
- **Key observation mode**: Secondary research, document analysis, practitioner self-reports
- **Narrative momentum**: High (800-1,165% job posting growth in 2025; actively promoted by a16z, Emergence Capital, and Crunchbase as "hottest job in tech")
- **Community cohesion**: Moderate — Palantir alumni form a coherent origin community; the broader FDE label is contested and diluted

---

## Part 1: What FDE Actually Is

### The Official Description vs. Reality

**Official description (Palantir career page, 2024):**
> "FDEs' responsibilities look similar to those of a startup CTO: you'll work in small teams and own end-to-end execution of high-stakes projects... FDSEs focus exclusively on one customer, building production-ready workflows on Palantir's platforms in close collaboration with that organization's teams."

**OpenAI's version (2025 career listing):**
> "Lead complex end-to-end deployments of frontier models in production alongside strategic customers."

**What it actually is, based on practitioner accounts:**

An FDE is a software engineer who spends between 25% and 80% of their time embedded at a customer site, writing production code in that customer's environment, using that customer's tooling, on problems that customer defines. They don't hand off. They don't advise and leave. They stay until it works.

The Pragmatic Engineer summarizes the meaningful functional distinction: "FDEs write code directly on customer infrastructure. Solutions Architects typically build only MVPs or proofs of concept offline, rarely accessing live customer systems." The former is accountable for production outcomes; the latter is accountable for a recommendation.

Nabeel Qureshi, an eight-year Palantir FDE who left in 2024, describes what this looks like in practice:
> "You took disparate sources of data — work orders, missing parts, quality issues — and put them in a nice interface."

Domain fluency was non-negotiable. At a hospital, you needed to know "capacity management" and "patient throughput." At Airbus, "non-conformities." The linguistic immersion wasn't performance — it was the prerequisite for access. Organizations let you into their data only when they believed you spoke their language.

### Comparison to Adjacent Roles

| Role | Writes prod code on client infra? | Stays post-sale? | Quota? | Accountable to outcome? |
|---|---|---|---|---|
| FDE | Yes | Yes | No | Yes |
| Solutions Architect | Rarely | No | Sometimes | No |
| Implementation Engineer | Yes | Yes | No | Sometimes |
| Technical Consultant | Sometimes | Sometimes | No | Rarely (contract-scoped) |
| Solutions Engineer | Sometimes | No | Yes | No |
| Pre-sales SE | MVP/demo only | No | Yes | No |

The core claim of the FDE model is that only end-to-end ownership produces the feedback loop required for a software platform to improve. An FDE who debugs LLM hallucinations in a hospital's discharge workflow at 2am and then feeds that failure mode back into the platform is doing something categorically different from a consultant who writes a recommendation deck and leaves.

Whether that claim is true — and when — is the central contested question about the role.

### What Palantir Invented and Why It Mattered

Palantir did not invent embedded technical delivery. What they invented was the organizational theory that justified making it the dominant staffing model rather than a transitional phase before self-serve.

Until 2016, Palantir employed more FDEs (which it called "Deltas") than software engineers. No product company at scale had done this before. The conventional wisdom — build a product, then hire salespeople to sell it, then hire implementation teams to deploy it — treats the deployment function as cost overhead to be minimized. Palantir inverted this: deployment was intelligence collection, and intelligence collection drove the product.

The Delta-Echo structure reflects this. "Deltas" were the rapid-prototyping technical FDEs. "Echos" were the domain-immersed relationship and strategy layer (closer to deployment strategists or technical product managers). Together they formed a reconnaissance unit, not an installation crew.

From Palantir's own internal framing: customer deployments were proving grounds. What worked got migrated into the core platform. What failed got discarded. The FDE was the sensor network for the product organization. This is what Shyam Sankar — employee #13, inventor of the FDE title — meant when he named it after military "forward deployed forces": the FDE was in the field so the platform team didn't have to be.

---

## Part 2: The Palantir Origins

### Why Palantir Built This Model

Palantir was founded in 2003 to sell software to government intelligence agencies. There was a fundamental bootstrapping problem: the founders didn't know any spies. Even if they did, those people couldn't disclose their actual workflows. You couldn't do a customer discovery interview with the CIA and ask "what's your biggest pain point when analyzing signals intelligence?"

The only path to product-market fit was to get inside, which required building trust, which required demonstrating competence in the customer's own environment. The FDE model was not a go-to-market strategy so much as an epistemic necessity.

This origin explains features of the model that look irrational from a normal software company lens:
- Negative margin pilots were acceptable because they were R&D, not sales
- Talent was expensive (top engineers, not junior analysts) because the work required actual engineering judgment
- Long time-to-value was built into the model because trust at classified environments doesn't compress

By the early 2010s, Palantir had won contracts with the CIA, DIA, NSA, FBI, CDC, NIH, IRS, DHS, ICE, every branch of the military, and municipal police departments. The FDE model was the mechanism for each of those.

### The Karp-Sankar Doctrine

Alex Karp describes Palantir's products as "implementation-orchestration machines" — the framing positions Palantir not as a software vendor but as an entity that is accountable for outcomes. Karp's philosophical influence comes from his background in social theory (Frankfurt School, PhD from Goethe University); he is genuinely committed to the idea that technology vendors should bear moral and operational responsibility for what their software does.

The French restaurant analogy, often attributed to Karp, crystallizes the model: a good French restaurant employs wait staff who are extensions of the kitchen. They don't just take orders — they guide, correct, and opine. If you try to order the wrong wine with the fish, they tell you no. The FDE was this opinionated delivery mechanism: deeply integrated with the product's logic, authorized to push back on customer requests that would produce bad outcomes.

Shyam Sankar is the operational architect. He joined as employee #13 and became Palantir's first FDE in 2006 — he named the role specifically to honor the company's earliest government customers. Sankar's contribution was translating Karp's philosophical stance into an org chart: the Delta-Echo team structure, the feedback loop from field to product, the thesis that complexity at the customer edge should drive platform generalization rather than be hidden behind customization.

### The Recruiting Narrative

Palantir's FDE recruiting is a case study in how a job title can function as a cultural artifact. The term "Forward Deployed" is borrowed directly from military vocabulary — "forward deployed forces" are units positioned close to potential conflict zones, operating with significant autonomy. The recruiting value was obvious: it made a software implementation job sound like a military operation.

This mattered enormously for Palantir's early talent strategy. The company recruited heavily from elite universities (Stanford, MIT, Harvard, Princeton) and from students with military or intelligence community connections or adjacencies. The FDE title carried connotations that "implementation engineer" or "solutions consultant" never could:
- Autonomy and judgment, not just execution
- Mission-critical stakes, not enterprise IT
- Elite peer group, not a services division

The mission framing was real, not just marketing. Early FDEs were in Afghanistan helping intelligence analysts, in hospitals during COVID-19 response. The combination of genuine high-stakes work and impressive branding created a self-reinforcing recruiting loop: the people the title attracted were the kind of people who produced results that justified the title.

One Palantir FDE from the period describes the effect on team cohesion: the "us vs. them" framing — building for the US and its allies — gave people permission to take risks and work hours that would be unreasonable in normal corporate contexts. Whether you agreed with Palantir's politics or not, the mission narrative created activation energy.

### What FDEs Actually Produced

Palantir's entire commercial product line is FDE output at scale. The progression was:

1. FDEs encounter a recurrent manual process at customer sites (e.g., data ingestion, report generation)
2. FDEs build a bespoke solution for that customer
3. Product Development engineers observe the pattern across multiple customer deployments
4. PD engineers generalize the solution into a platform capability
5. That capability becomes part of Foundry/Gotham/AIP

Magritte (data ingestion), Contour (visualization), Workshop (web applications) — these are productized FDE discoveries. Qureshi's retrospective is explicit: "FDEs went to customer sites and did manual work, then PD engineers built tools that automated that work... this eventually drove 50%+ of the company's revenue."

Palantir's 2024 gross margin is approximately 80% — approaching software company levels, not services company levels. This is the proof point for the model's economic validity: if you run FDEs long enough and with enough product discipline, the services costs get absorbed into the platform and the margins compress toward software.

Accenture runs at 32% gross margin. Palantir runs at 80%. The difference is whether the humans are generating IP or just delivering hours.

---

## Part 3: Is FDE a Real Role or Marketing?

### Where FDE Creates Genuine Value

The model works — specifically and narrowly — under the following conditions:

**1. The problem is genuinely novel and domain-specific.** Enterprise data integration in healthcare is not a solved problem. Every hospital has a different EHR system, a different reporting structure, different regulatory constraints. You cannot build a self-serve product for a problem space that varies this much. An FDE who deeply understands both the platform and the domain can navigate this in ways that a general consultant cannot and a self-serve tool cannot.

**2. The contract size justifies the cost.** Palantir's former CFO Colin Anderson, speaking in August 2025, put the arithmetic plainly:
> "A world-class engineer plus their equity dilution is an expensive check. You have to be a capital allocator to pursue this model... Seven-figure contracts can support it; eight or nine figures definitely can."

He describes smaller implementations in the $20,000-$100,000 range as "lighting equity on fire" unless they function as R&D for future productization. This is not a viable engagement model for mid-market.

**3. The FDE feedback loop is connected to the product team.** The model degrades into services consulting when FDE output stops informing product development. If FDEs are customizing forever without productization, you have an Accenture with better recruiting branding.

**4. The platform is meaningfully better with FDE-discovered intelligence.** AI products in 2025 genuinely meet this criterion. LLM integration requires understanding of customer data architecture, security constraints, workflow specifics, and failure modes that no amount of product management research can substitute for. An FDE watching a hospital nurse reject an AI suggestion in real time — and understanding why — is irreplaceable signal.

### Where It Is Consultants Who Can Write Code

The honest answer is: frequently. Thomas Otter, writing in 2025, makes the accounting argument with precision:
> "FDEs performing billable customer work should be classified as COGS under services, not R&D or recurring revenue. Calling it 'Annual Recurring Revenue' when significant FDE resources are deployed represents deluding yourself and your investors."

The FDE model, when executed poorly, is:
- A systems integrator who has internalized SI costs rather than billing them separately
- A way to recognize services revenue as product revenue for valuation purposes
- A sales motion in which "we'll send engineers to help you" substitutes for a product capable of self-serve adoption

The analysis of 1,000 FDE job postings from Bloomberry in 2025 is instructive. Approximately 30% of postings are what they call "Sales Engineer+" roles — supporting pre-sales demos, building POCs, handing off to implementation teams. These are not FDEs in the Palantir sense. They are senior sales engineers with a prestigious new title.

The a16z piece "Trading Margin for Moat" acknowledges this risk directly:
> "Without strong underlying product architecture, companies drift toward 'Accenture for X' — consulting dressed as software with premium valuation but limited competitive moats."

### The "Expensive Body-Shopping" Critique and Whether It's Fair

The critique is fair when applied to the wrong companies, partially unfair when applied to Palantir.

For companies that don't have Palantir's product architecture, FDE teams are expensive systems integration. If you are a startup with a thin platform and a lot of FDEs, you are a services company that raised venture capital at software multiples. This is not uncommon in the 2024-2025 AI deployment wave. Marc Andrusko at a16z notes the risk: "you end up with thousands of bespoke deployments that are impossible to maintain or upgrade."

For Palantir, the critique was valid in 2011 (Dave Kellogg's blog post, which described the company as a services firm masquerading as a software company). It was partially valid through 2016, when they had more FDEs than product engineers. By 2024, with 80% gross margins and Foundry driving over 50% of revenue, the critique had become outdated. They executed the transition.

Most companies attempting to copy the FDE model will not execute that transition. The feedback loop from FDE output to productized platform feature requires organizational discipline that is hard to maintain when FDEs are generating revenue directly and the product team is a cost center.

### Why the Role Has Cultural Cachet Beyond Its Functional Value

The FDE identity is exceptionally well-constructed as a professional brand. It combines:

- **Engineering credibility**: The work requires real engineering skills, not just PowerPoint skills
- **Mission framing**: Palantir's defense and intelligence work attached genuine stakes to the role
- **Autonomy**: FDEs are positioned as startup CTOs, not implementation technicians
- **Outcome ownership**: Unlike most enterprise engineers, FDEs are accountable for whether the thing they built actually got used

This combination is rare in enterprise software careers, which are typically either high-autonomy/low-stakes (startup engineering) or low-autonomy/high-stakes (enterprise IT). The FDE narrative promises both, and for Palantir alumni, it often delivered.

The cachet has now diffused into the broader market to the point where it functions as a brand for "senior engineer willing to talk to customers," which is a much lower bar. This dilution is real and measurable. In 2024-2025, job postings claiming "Forward Deployed Engineer" include roles that are essentially technical account management or post-sale customer success with a coding requirement.

Ted Mabrey, writing critically about FDE imitations:
> "Every replicant I've encountered is a half measure. They are redrawing boundaries around roles and responsibilities, internalizing costs previously outsourced to SIs, or capturing product feedback in a different way. They are not committing to aligning their interests with their customers."

---

## Part 4: The AI Inflection Point

### How AI Is Changing the FDE Model

The 800-1,165% growth in FDE job postings in 2025 is driven by a specific problem: LLM integration is hard in ways that product-led growth cannot address. Every enterprise deployment of a language model requires:

- Data preparation and access provisioning that is unique to that organization
- Prompt engineering and context design that requires domain understanding
- Security and compliance configurations that require detailed enterprise architecture knowledge
- Evaluation frameworks for whether the model is actually doing what the customer wants
- Workflow integration with systems that predate AI by decades

None of this is automated. None of it is self-serve for non-technical buyers. The FDE function — embed, understand, build, validate — is genuinely necessary for production AI deployment in a way that it was not necessary for SaaS deployment (which has largely become self-serve).

This is why the FDE market is growing despite (or because of) AI: the deployment complexity has gone up faster than the deployment automation has.

### Palantir's AI FDE Product

Palantir launched "AI FDE" in late 2025 — an agent that automates Foundry operations through natural language. Per Palantir's documentation, it "translates natural language requests into Foundry operations, allowing you to perform data transformations, manage code repositories, build and maintain your ontology."

This is Palantir making the bet on the long curve: today's FDE work becomes tomorrow's automated capability. The same transition that turned manual data ingestion into Magritte, and manual report building into Contour, will turn manual ontology configuration into AI FDE.

The official position from Palantir is that AI FDE "elevates" human FDEs — "from builders to designers, operators to orchestrators, technicians to strategists." Whether this holds will depend on whether the elevated role commands comparable compensation and headcount, which is not given.

### Whether FDE Grows, Contracts, or Gets Absorbed

The near-term (2025-2027) trajectory is growth, driven by AI deployment complexity. The medium-term (2027-2030) trajectory is contraction or restructuring, as automation absorbs the execution-layer tasks that currently require human FDEs.

The restructuring will not be uniform:
- **Grows**: FDE work in genuinely novel domains (defense AI, life sciences, complex infrastructure) where the problem space changes faster than automation can follow
- **Contracts**: FDE work in repetitive enterprise integration (CRM connection, ERP hooks, standard data pipelines) where AI agents can execute faster and cheaper
- **Gets absorbed**: The FDE title itself, as "AI deployment engineer" or "AI solutions architect" or "implementation engineer for AI systems" captures the same function without the Palantir-specific branding

The a16z framing — "AI models are the gold, forward deployed engineers are the gold miners" — is the current bull case. The bear case is that as AI models become more capable of self-deployment, the mining metaphor breaks down: eventually the gold mines itself.

### The Emerging "AI Deployment Engineer" Category

Job postings in late 2025 and early 2026 show an emerging bifurcation:

**Type A**: Companies using "Forward Deployed Engineer" as a deliberate brand claim, either because they're Palantir-adjacent (defense tech, government) or because they're trying to attract Palantir alumni and the culture they represent.

**Type B**: Companies using "AI Deployment Engineer," "AI Implementation Specialist," or "GenAI Solutions Engineer" for functionally identical work without the brand specificity.

The functional requirements in both are converging: Python (66% of postings), TypeScript (35%), LLM experience (31%), cloud platforms, and domain knowledge in financial services, healthcare, or defense/government. The title is primarily a recruiting signal about company culture and ambition, not a meaningful differentiator in what the person actually does.

---

## Part 5: Where the Puck Is Going

### What Happens to FDEs When LLMs Can Write Integration Code

The execution tasks currently performed by FDEs fall into roughly three categories, with different automation trajectories:

**Automatable within 3-5 years:**
- Writing data pipeline transforms
- Configuring standard integrations (API connections, data schema mapping)
- Building basic dashboards and workflow interfaces
- Documenting system configurations and ontologies

**Automatable within 5-10 years (harder):**
- Domain-specific evaluation of AI output quality (requires ground truth the model may not have)
- Security architecture decisions (requires organizational context)
- Stakeholder management and political navigation
- Novel problem framing (identifying which problem to solve, not just solving it)

**Unlikely to automate:**
- Judgment about which customer requests are actually the problem vs. the symptom
- Relationship management in high-stakes contexts where trust is the commodity
- Escalation decisions: when to say "this is actually not buildable on this platform"
- Discovery of problems the customer doesn't know they have

The roles that survive are those whose value is fundamentally relational and contextual — not execution, but interpretation. The FDE who survives 2030 is not the one who can write the most transforms, but the one who can walk into a dysfunctional enterprise, identify the real blocker (which is rarely technical), and navigate the organization to a solution.

This is a different profile from most current FDEs, who are primarily hired for their coding velocity.

### Companies Doubling Down vs. Replacing with Product

**Doubling down on the model:**
- Palantir (by definition, their entire business model)
- Anduril (defense, genuinely complex environments)
- Scale AI (government defense, data annotation pipelines)
- OpenAI's enterprise team (22 of 311 open roles in enterprise FDE/SE functions as of late 2025)
- Any company selling to government/defense where self-serve is impossible

**Moving toward product-led:**
- Most AI infrastructure companies (LangChain, Weaviate, ChromaDB) — developer tools that assume self-serve adoption
- AI application companies with standard use cases (customer service AI, code assistance, document processing)
- Any company where the customer's technical sophistication is high enough to self-deploy

The honest version of this choice: FDE-heavy go-to-market is a bet that your customer cannot self-serve and that you have a platform valuable enough to justify the cost of making it work. If either condition doesn't hold, you are burning margin.

---

## Part 6: Community and Identity

### How FDEs Self-Identify

LinkedIn is the primary artifact layer. A search for "Forward Deployed Engineer" on LinkedIn currently returns over 136,000 job listings and a dense network of self-identified practitioners, Palantir alumni, and aspirants.

Palantir alumni are the most coherent subgroup. Their LinkedIn profiles cluster around specific signals:
- "Palantir FDSE" or "Forward Deployed Software Engineer" as a title rather than "Software Engineer"
- Deployment stories described in outcome terms, not feature terms ("led deployment of X to Y, resulting in Z operational outcome" rather than "built dashboard using React and Python")
- Client names when not classified, or sector names when classified (e.g., "US Intelligence Community," "NATO partner nation")

The self-presentation is consistent with the internal culture: outcomes-oriented, mission-framed, deliberately vague about classified work in ways that signal rather than reveal. This creates a status signal that is legible within the community but opaque outside it.

Post-Palantir, the role functions as a credential. Alumni from Palantir FDE roles are disproportionately represented in:
- Startups at the founding or early stage (Nabeel Qureshi's observation: "usually more ex-Palantir founders than ex-Googlers in each YC batch")
- VP of Engineering or CTO roles at growth-stage companies
- Other defense tech companies (Anduril, Shield AI, Joby Aviation)
- AI labs' enterprise teams (OpenAI, Anthropic)

### The Prestige Hierarchy of FDE Placements

Within the FDE community, client placement functions as a status signal in the same way that law firm matters, consulting firm case studies, or investment banking deals do. The hierarchy is roughly:

**Tier 1 (maximum prestige):**
- Defense intelligence (CIA, DIA, NSA, JSOC)
- Active military operations support (forward bases, not headquarters)
- Head of state or national security decision-making contexts

**Tier 2:**
- Major defense primes (Lockheed, Boeing, Raytheon programs of record)
- Healthcare crisis response (COVID-19 response, pandemic preparedness)
- Critical infrastructure (energy grids, supply chain disruption)

**Tier 3:**
- Large financial institutions (JPMorgan, Goldman) in high-stakes contexts
- Major pharma (drug discovery, clinical trial optimization)
- US federal civilian agencies

**Tier 4:**
- Fortune 500 commercial deployments
- International government (non-US, non-NATO)

The prestige derives from a combination of genuine stakes (the work matters), exclusivity (few people can get access to these environments), and narrative richness (these deployments make better stories). An FDE who spent time in a classified DoD context will reference this for the rest of their career; an FDE who spent time at a retailer's demand forecasting team will not.

Salesforce CEO Marc Benioff, commenting on Palantir in 2025: the engineer-embedding strategy is "cool," but it was the price list that made him go "whoa." This distinction matters — the prestige is in the model, but the money is in the price. For many customers, both are barriers.

### Burn Rate and Attrition

The FDE role is structurally high-attrition for reasons that have nothing to do with job quality:

**The 2-3 year cliff:** Palantir's internal culture recognized this. The flat hierarchy works on the way up — everyone is an FDE, titles are suppressed, and what matters is the quality of your work and the relationships you build. At around the 2-3 year mark, this starts to invert. The most capable people want more influence over platform direction; the flat structure provides no clear path. People who should be senior staff become flight risks.

Glassdoor reviews are consistent: "close to no career progression (monetary or level) at Palantir with additional responsibility," "politically difficult to navigate at around the 2-3 yr mark," "burnout is evident on every team," and hours ranging from 30-40 per week on some teams to 65-80 on others, with no predictability.

**The travel problem:** FDE roles require 3-4 days per week on-site for at least part of the engagement. This is sustainable for a 25-year-old with no family commitments; it becomes untenable at 30. The role is structurally designed around a particular life stage and burns through people who exit that stage.

**Where FDEs go after Palantir:**
- ~50-60%: transition internally to product engineering, deployment strategy, or technical leadership
- ~20-25%: move to product management or operations roles at external companies
- ~15-20%: start companies (the most celebrated outcome in the community)
- ~5-10%: join other defense/government tech firms

The founder outcome is disproportionately celebrated because the FDE role genuinely develops founding-relevant skills: reading organizational dynamics, rapid context switching, customer discovery under uncertainty, building with incomplete information. Qureshi explicitly attributes the YC overrepresentation to FDEs having developed "instincts for reading rooms, group dynamics, and power" that translate directly to fundraising and hiring.

---

## Synthesis: Honest Assessment for a Skeptical Engineering Manager

The FDE model is genuinely valuable in a narrow set of conditions and genuinely marginal in the much larger set of conditions where companies are now applying it.

**What the model actually solves:** The specific problem of deploying complex software into organizations that cannot self-serve, where the deployment produces intelligence that improves the platform, and where contract values justify the cost structure.

**What the model gets confused with:** A sales motion (send technical people to close deals), a customer success function (keep technical people at accounts to prevent churn), or a systems integration practice (deliver custom software at services margins but software valuations).

**The fundamental accounting question (Thomas Otter's point):** If your FDEs are doing billable work that is primarily in service of a specific customer's specific requirements — not informing your product roadmap — then you have a services business. Calling it software changes your multiple; it doesn't change the economics.

**The signal that distinguishes real FDE from dressed-up consulting:** Does the FDE output systematically route back to the product organization? Is the platform measurably better because of FDE deployments? Are gross margins improving as FDE-discovered capabilities get productized? If none of these are true, you have a services firm.

**For the AI moment specifically:** There is a genuine, temporary spike in demand for people who can bridge the gap between LLM capabilities and enterprise deployment. This is real work that requires real engineering skill and domain judgment. The question is whether "Forward Deployed Engineer" captures this or whether it is one of the many labels being applied to a function that will professionalize under a different name (AI deployment engineer, AI implementation specialist, etc.) as the field matures.

The Palantir model — run it long enough with enough product discipline and the FDE function eventually productizes itself into software — is the only exit ramp from the services trap. Most companies won't run it long enough, won't maintain the product discipline, and will end up with an expensive services organization trading at software multiples until the multiple corrects.

The role is real. The brand is inflated. The value is context-dependent. The future is probably a smaller number of more specialized FDEs doing work that AI cannot yet do, while the current wave of "FDE" hiring produces a lot of implementations that could have been handled by better products.

---

## Sources

- [Pragmatic Engineer: What are Forward Deployed Engineers, and why are they so in demand?](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers)
- [Nabeel Qureshi: Reflections on Palantir](https://nabeelqu.co/reflections-on-palantir)
- [Nabeel Qureshi on Lenny's Podcast: How Palantir built the ultimate founder factory](https://www.lennysnewsletter.com/p/inside-palantir-nabeel-qureshi)
- [Ted Mabrey: Sorry, that isn't an FDE](https://tedmabrey.substack.com/p/sorry-that-isnt-an-fde)
- [Thomas Otter: WTF is a forward-deployed engineer?](https://thomasotter.substack.com/p/wtf-is-a-forward-deployed-engineer)
- [a16z: Trading Margin for Moat (Services-Led Growth)](https://a16z.com/services-led-growth/)
- [Marc Andrusko / a16z: The Palantirization of Everything](https://www.a16z.news/p/the-palantirization-of-everything)
- [SVPG / Marty Cagan: Forward Deployed Engineers](https://www.svpg.com/forward-deployed-engineers/)
- [Bloomberry: What I Learned Analyzing 1,000 Forward Deployed Engineer Jobs](https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/)
- [barry.ooo: Understanding Forward Deployed Engineering](https://www.barry.ooo/posts/fde-culture)
- [Palantir Blog: Dev versus Delta — Demystifying Engineering Roles at Palantir](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87)
- [Palantir Blog: A Day in the Life of a Palantir Deployment Strategist](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96)
- [Benzinga: Satya Nadella Once Praised Palantir's FDE Model, But Ex-CFO Says It's 'Lighting Equity On Fire'](https://www.benzinga.com/markets/tech/25/08/47326410/satya-nadella-once-praised-palantirs-fde-model-but-ex-cfo-says-its-lighting-equity-on-fire-over-20k-contracts)
- [Benzinga: Palantir's Engineer Embedding Strategy Is 'Cool,' Says Salesforce CEO](https://www.benzinga.com/markets/equities/25/08/47404795/palantirs-engineer-embedding-strategy-is-cool-says-salesforce-ceo-but-it-is-their-price-list-that-made-him-go-whoa)
- [Everest Group: Palantir — Inside the Category of One](https://www.everestgrp.com/palantir-inside-the-category-of-one-forward-deployed-software-engineers-blog/)
- [Palantir AI FDE Documentation](https://www.palantir.com/docs/foundry/ai-fde/overview)
- [Scale AI FDE Job Postings](https://scale.com/careers/4549048005)
- [OpenAI FDE Job Postings — NYC](https://openai.com/careers/forward-deployed-engineer-nyc/)
- [Crunchbase: 2025: The Year of the Forward-Deployed Software Engineer](https://news.crunchbase.com/ai/forward-deployed-software-engineer-sales-team-coker-felicis/)
- [Fonzi AI / Medium: Forward-Deployed Engineers — The 800% Growth Role](https://medium.com/fonzi-ai/forward-deployed-engineers-the-800-growth-role-redefining-ai-hiring-69e19d800047)
- [Emergence Capital: AI Models Are The Gold, Forward-Deployed Engineers Are The Gold Miners](https://www.emcap.com/thoughts/ai-models-are-the-gold-forward-deployed-engineers-are-the-gold-miners)
- [Palantir Q4 2024 Earnings](https://investors.palantir.com/news-details/2025/Palantir-Reports-Q4-2024-Revenue-Growth-of-36-YY-U.S.-Revenue-Growth-of-52-YY-Issues-FY-2025-Revenue-Guidance-of-31-YY-Growth-Eviscerating-Consensus-Estimates/)
- [Colossus: The Patriot — Shyam Sankar of Palantir](https://colossus.com/article/the-patriot-shyam-sankar-palantir/)
- [What's In A Name: Forward Deployed](https://embracingemergence.beehiiv.com/p/what-s-in-a-name-forward-deployed)
- [Palantir Glassdoor Reviews — FDSE](https://www.glassdoor.com/Reviews/Palantir-Technologies-Forward-Deployed-Software-Engineer-Reviews-EI_IE236375.0,21_KO22,56.htm)
- [Blind: Is Palantir FDE genuinely bad for your career?](https://www.teamblind.com/post/Is-Palantir-FDE-genuinely-bad-for-your-career-7wGNyjWT)
- [Quora: Where do ex-FDEs at Palantir now work?](https://www.quora.com/Where-do-ex-FDEs-at-Palantir-now-work)
