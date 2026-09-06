---
title: AI Enclosure
created: 2026-07-05
updated: 2026-09-06
type: concept
tags: [governance, human-agency, risk, counterarguments]
sources: [raw/articles/wired-meta-smart-glasses-subscription-2026-07.md, raw/articles/wired-summer-of-ludd-festival-2026-07.md]
---

# AI Enclosure

## Core Idea

AI enclosure is the set of structural mechanisms that gate who can access AI capabilities, on what terms, and at what cost. It is the foundation of the agency layer arc: before accountability, before pluralism, before preference formation — there is access. And access is increasingly gated by political decisions, economic barriers, and analytical compute requirements.

## Why It Matters

The [[Superagency]] thesis holds that AI can expand agency broadly. The enclosure challenge asks: *for whom?* If agency-enhancing AI features require political approval (the [[Human Agency#The Gatekeeping Layer|Gatekeeping Layer]]), hardware purchase (the chip shortage documented in [[Compute and Agency]]), AND ongoing subscription (Meta's smart glasses model, July 2026), then agency through AI is not a capability technology bestows — it's a product access determines.

## Three Dimensions of Enclosure

### 1. Political Enclosure — The Gatekeeping Layer

The White House's ad hoc, customer-by-customer approval process for GPT-5.6 access (June 2026) represents enclosure at the frontier capability level. No articulated standard. No due process. No sunset clause. Agency distribution becomes a function of political access rather than merit, need, or potential.

- **Mechanism:** Opaque, politicized decisions on who gets frontier intelligence
- **Who it gates:** Anyone without existing government relationships
- **Counterforce:** Open-weight frontier models, international alternatives, policy reform

**The China dimension (July 2026):** Chinese startup Moonshot AI released what MIT Technology Review describes as "the world's largest open AI model" — competing with Anthropic and OpenAI models while being openly available. The launch sent AI and semiconductor stocks sliding. The US response has been chip controls (Nvidia halved its Asia buyer list) — but open-weight models bypass these controls by running on available hardware. Political enclosure creates the conditions for open-weight alternatives to flourish, which then undermine the enclosure. The US gates access; China ships the model. The market decides whose enclosure strategy works.

→ Source: [The Download: China's latest AI leap](https://www.technologyreview.com/2026/07/17/1140640/the-download-perimenopause-misinformation-china-moonshot-ai/), MIT Technology Review, July 17, 2026

**The US countermove (July 2026):** Mira Murati's Thinking Machines Lab released its first open-weight model — a US-based alternative to Chinese open-source models. The open-weight competition is now a two-front race: capability (who builds the best open model) and governance (whose open model becomes the standard). For enclosure analysis, this means the hardware+API gate is not the only frontier — the open-weight ecosystem provides an escape valve, but only if US open-weight models match or exceed Chinese alternatives in both capability and accessibility.

→ Source: [The Download: Thinking Machines open-weight model](https://www.technologyreview.com/2026/07/16/1140514/), MIT Technology Review, July 16, 2026

### 2. Economic Enclosure — Hardware and Subscription

AI-driven chip shortages push consumer hardware prices up ([[Compute and Agency#Chip Shortage Access Barrier July 2026|WIRED, July 3, 2026]]). Meta charges recurring subscriptions for advanced AI features on hardware users already own (WIRED, July 2, 2026). The shift from "buy once, own forever" to "buy hardware, rent AI" converts AI capability from a capital expense to an operating expense.

- **Mechanism:** Subscription pricing, chip manufacturing competition with AI data centers
- **Who it gates:** Anyone who can afford the device but not the recurring fee
- **Counterforce:** Open-weight models (Llama, Mistral, Qwen), local inference, on-device AI

**The Google Gemini rate change (July 2026):** Google changed how Gemini usage quotas are calculated (WIRED, July 18) — a seemingly technical adjustment that reduces response volume for many users. This is economic enclosure through metering: users don't lose access, they get *less* access, with the thresholds set by the provider. Each quota recalculation, subscription tier, and rate limit is a small shift in who gets how much AI — and the cumulative effect narrows the "democratization" claim. Expertise accessible only to those who can afford the quota isn't democratized; it's stratified.

→ Source: [Google Gemini Is Changing How Its Usage Quotas Are Calculated](https://www.wired.com/story/google-gemini-usage-quota-changes/), WIRED, July 18, 2026

### 3. Analytical Enclosure — Compute Requirements

The Agentic Garden of Forking Paths (Miao, Pritchard, and Zou, July 2026) found that exploring the full space of defensible analyses requires running many AI variations. If each variation consumes compute gated by subscription or API pricing, analytical exploration becomes accessible to institutions (who can pay) but not individuals (who cannot).

- **Mechanism:** Compute requirements for multi-variation analysis, API pricing
- **Who it gates:** Individual researchers, small organizations, resource-constrained actors
- **Counterforce:** m-value and Agentic Bootstrap tools that make analytical variation visible from fewer runs

### 4. Access Inversion — When Restriction Advantages Adversaries (July 2026)

A new game-theoretic model (arXiv 2607.22957, July 2026) formalizes a counterintuitive enclosure risk: **access inversion** occurs when restricting a dual-use AI model gives adversaries an access advantage because they obtain effective substitutes faster than defenders.

**The model:** A laboratory chooses among four release tiers: controlled access, a defender-first window, safeguarded open weights, and minimally restricted open weights. The policy ranking depends on six factors: relative usefulness, opportunistic misuse, offense-defense conversion, defensive spillovers, safeguard friction, and nonrecallable losses.

**Key findings:**

- **Adversary-substitution threshold:** Above a critical substitution rate, broad release overtakes control — i.e., when adversaries can get the model anyway, restricting it only slows defenders.
- **Defender-first windows have value** when selected defenders can deploy protection before adversaries catch up. This is the narrow case for gated access: a time-limited head start for defense.
- **Removable safeguards remain useful** when they deter enough opportunistic misuse — the casual abuser, not the dedicated adversary.
- **Nonrecallable losses** (capabilities that can't be taken back once deployed) create an irreversible dimension that overrides other considerations.

**The release review checklist:** The paper identifies six quantities a release review should estimate: actor-specific substitution times, marginal capability gains, deployment rates, defensive reach, newly enabled misuse, and nonrecallable losses. This is a concrete framework for making open-weight release decisions — moving from "open vs. closed" as a binary to "which tier, under which conditions."

**→ Connects to [[AI Enclosure]]:** The access inversion model shows that political enclosure (Gatekeeping Layer) and economic enclosure (subscription/hardware) are not universally protective. Under adversary-substitution conditions, enclosure protects the adversary more than the defender. The enclosure calculus must be adversary-specific: "who gets the substitute faster?" — not "who gets the original?"

**Source:** "Who Does Withholding Delay? A Game-Theoretic Model of Open-Weight AI Release Under Asymmetric Proliferation," arXiv 2607.22957, July 2026.

### 5. Enforcement Architecture — How to Catch a GPU (July 2026)

A taxonomy of verification and enforcement mechanisms for international AI agreements (arXiv 2607.22619, July 2026) provides the first structured evaluation framework for the proposals that have proliferated in the governance conversation.

**The contribution:** "There is no structured way to evaluate whether these proposals are enforceable, to assess where they might fail in practice, or to determine which combination of policies is most effective." The taxonomy fills this gap by categorizing verification mechanisms (what can be detected) and enforcement mechanisms (what can be done about it).

**Why it matters for enclosure:** The GPU is the physical manifestation of AI access. Chip controls (Nvidia halving its Asia buyer list), export restrictions, and hardware registration are the hardware dimension of enclosure. But as the open-weight model competition shows (Moonshot AI, Thinking Machines Lab), hardware controls don't prevent model development — they shift WHERE it happens and WHO controls it.

**The enforcement paradox:** The same verification mechanisms that make international agreements enforceable also create the infrastructure for domestic enclosure. A global GPU registry that helps catch treaty violations is also a tool that governments can use to track who has what compute — potentially gating access at the hardware level.

**→ Connects to the [[Human Agency]] Gatekeeping Layer:** The GPU taxonomy makes the hardware dimension of the gatekeeping layer concrete. Before any software-level access decision (API access, subscription tier, model tier), the hardware question must be answered: do you have the compute? And compute is increasingly tracked, regulated, and limited — at the international level.

**Source:** "How to Catch a GPU: A Taxonomy of Verification and Enforcement Mechanisms for International AI Agreements," arXiv 2607.22619, July 2026.

## The Cultural Response: Opting Out

The Summer of Ludd festival (WIRED, July 2, 2026) — teaching Gen Z to "live offline amid the suffocating presence of Big Tech" — represents the cultural countercurrent to enclosure. When access is gated and features are rented, a segment of the population responds by opting out entirely.

This creates its own dynamic: the digitally disengaged as a class whose agency is defined by refusal rather than access. It also creates a tension: those most affected by enclosure (lower-income workers whose jobs require constant connectivity) are least able to opt out. The Luddite festival attendees are disproportionately those with the privilege to choose disconnection.

## Connection to the Layer Arc

The AI enclosure concept sits at the foundation of the layer arc traced through the [[Human Agency]] page:

```
Enclosure → Gatekeeping → Reopening → Measured Shift → Persuasion →
Organizational → Preference → Pluralism → Accountability
```

Each higher layer operates only for those who have access. The Enclosure Layer asks: who gets through the gate, on what terms, at what cost — and who doesn't?

## Best Supporting Sources

- [Meta Is Charging a Subscription for Smart Glasses Features](https://www.wired.com/story/why-meta-is-charging-a-subscription-for-on-device-smart-glasses-features/), WIRED, July 2, 2026 — hardware-as-subscription as the new consumer tech model
- [Inside the Luddite Festival](https://www.wired.com/story/inside-the-luddite-festival-harnessing-gen-zs-rage-against-big-tech/), WIRED, July 2, 2026 — cultural resistance to digital enclosure
- [[Compute and Agency]] — chip shortage access barrier and subscription enclosure
- [[The Turing Trap]] — paywalled augmentation as the subscription dimension of the trap
- [[AI and Inequality]] — subscription-based access inequality
- [[Human Agency]] — the Enclosure Layer in the layer arc
- [White House Will Ad Hoc Decide Who Can Access GPT-5.6](https://thezvi.substack.com/p/white-house-will-ad-hoc-decide-who), Zvi Mowshowitz, June 2026 — political enclosure at the frontier

## Practical Examples

- **The AI Stack Audit:** List every AI tool you use. For each: is it free, one-time purchase, subscription, or API-metered? If it doubled in price, would you still use it? Is there an open-weight fallback? The result is your AI Enclosure Index — the percentage of your AI capabilities that survive enclosure.
- **Identify single points of enclosure failure:** For each AI capability you depend on, ask: if this specific service shut down or gated its best features, could I replicate 80% of the value with local tools? If not, you have a single point of enclosure failure.
- **Support participatory AI infrastructure:** The Scaling Participation finding (arXiv 2606.07812) showed that bottom-up, diverse, participatory AI architectures outperform monolithic ones. Choosing tools built on this architecture is a practical counterforce to enclosure.

## Enclosure Mechanism #5: Hardware Import Bans (2026-08-05)

**Counterforce lens:** the measured local-inference floor ([[Home Server AI Agents]] — sub-watt-hour per thousand tokens) means the bottom of the stack stays open even as top-layer hardware gates shut.

## The Political Enclosure of Agentic AI (2026-08-10)

**"Agentic AI: User Empowerment or Enclosure?"** (Gamba, Romero, Schoenebeck, arXiv 2608.06510, 2026-08-06) extends the enclosure thesis from models to agents — with the sharpest version yet of the *depoliticization pathway*: technology encloses when it migrates decisions out of contested public space into interfaces presented as neutral.

- **The historical pattern:** the paper traces depoliticization through earlier waves — ad blockers (an individual response to a collective attention problem), and now **robo-advisors** (an individual response to a collective retirement-security problem). Each wave converts a civic question (what should the attention economy be? who should be secure in old age?) into a private optimization task.
- **Agentic AI is the same mechanism at full power:** agents that book, buy, vote-assist, and manage on the user's behalf present each decision as a personal preference optimization — while the aggregate outcome (who gets served, at what price, on what terms) is set by whoever controls the agent's objective function. The enclosure is invisible because it is *inside the interface*.
- **The governance settling-in point:** the paper flags MCP (Model Context Protocol) and the emerging "Agentic AI Foundation" as the standards/actor layer where the terms of agentic access are being set — **before democratic contestation has caught up**. The window where the architecture is decided and the window where the public can weigh in do not overlap; this page's Hardware Import Bans section shows the same pattern at the hardware layer.
- **The agency counter-lens:** the enclosure is not total — open-weight agents, local orchestration ([[Home Server AI Agents]], [[AI Orchestrator]]), and the measured local-inference floor keep a non-enclosed path available. But the default path for most users will be the depoliticized one unless the standards layer is treated as a governance surface.

**Relevance to the layer arc:** this is the Enclosure Layer operating *after* the gate — the user got through the gate and is still enclosed, because the agent's objective function is not theirs. The gatekeeping layer (who gets access) and the enclosure layer (under whose terms) separate here: access can be wide while agency is narrow.

→ Source: arXiv 2608.06510 (2026-08-06)

## Risks / Limits

- The enclosure frame can slide into fatalism — "everything is gated, nothing is accessible" — when in reality open-weight models and local inference provide substantial access outside the subscription model
- Not all subscription models are enclosure. Some fund investment in better AI that benefits users. The question is whether non-subscribers retain a functional baseline
- The Luddite response (opting out entirely) is a privilege and may not scale beyond those with economic security
- Enclosure is not new — software has been moving to subscriptions for decades. The question is whether AI capabilities are different because they directly affect human agency

## August 2026: Data Enclosure and Capital Enclosure

Two new enclosure fronts in August 2026:

**Data enclosure — the opt-out default.** Amazon now trains its AI on Twitch creators' content unless they opt out (Settings → Security and Privacy → "Generative AI Training"); the toggle doesn't stop other AI uses (recommendations, sponsorship assistance, AutoMod), and the ToS have granted broad content rights since March 2024 without ever explicitly mentioning gen-AI training (WIRED, 2026-08-15). 16,000+ creators opposed; Twitch's product head conceded the logic of the default: "no one would participate" if training were off by default. This is enclosure by default posture: participation in training is the baseline, non-participation is an individual burden — and training-data scarcity makes the enclosed resource more valuable precisely as the power imbalance widens (see [[AI and Creator Rights]], [[The Participation Problem]]).

**Capital enclosure — the buildout financed above users.** Ben Thompson's "The CapEx Train Keeps Rolling" (Stratechery 2026.33, 2026-08-14) poses the capital constraint: short on compute, short on power — what if short on *capital*? Nvidia's new long-duration-capital funding mechanism and Google's equity taps finance the infrastructure that runs on everyone's data with ownership above and beyond the people whose data makes it valuable — participation without equity. Thompson's framing also notes the fragility: financial engineering "expands the blast radius of a bubble in the service of Nvidia's threatened margins" (public weekly-overview summary; headline analysis paywalled).

**The architectural alternative.** Tim O'Reilly names the enclosure mechanism (WIRED, 2026-08-14): the big labs built an **architecture of control**, and the counter is the **architecture of participation** — a clean separation of model, harness, and application, with an open harness (Pi) so users can shape the system even around a closed model. Enclosure is a stack property, not just a policy outcome; the engineering separation is the precondition for un-enclosing (see [[The Participation Problem]]).

## Related Pages

- [[Human Agency]]
- [[Compute and Agency]]
- [[The Turing Trap]]
- [[AI and Inequality]]
- [[Superagency]]
- [[Balanced Governance]]
- [[Democratization of Expertise]]

### The Aggregation Toll Booth: Stripe Acquiring OpenRouter (2026-08-17)

Ben Thompson's Stratechery post (paywalled — only the public summary line and its Aggregation Theory framing were obtainable this run) reports Stripe is acquiring OpenRouter and frames it as "an implicit bet on a future market of models and the chance at Aggregation": the business model flips from selling models to *sitting at the aggregated layer* through which model access flows. If model access consolidates behind a payments-and-distribution layer, the toll booth on agent traffic is owned by the aggregator — a structural enclosure that doesn't need to own a single frontier model.

**Why this belongs on the enclosure page:** enclosure arguments usually target compute, weights, or data. The Stripe/OpenRouter case is enclosure at the *distribution* layer — the point where agents and their users pay for access. It sharpens the page's open-harness / "Pi"-style participation contrast: open architectures matter most at exactly the layers where aggregation naturally forms ([[The Participation Problem]]).

**Implications:**
1. **Aggregation is the new moat.** Owning the access layer collects a toll on every agent interaction regardless of which model wins — the modern version of the platform-enclosure move ([[Compute and Agency]]).
2. **Watch the payment layer, not just the model layer.** The enclosure question for 2026: who processes the transactions of agent traffic, and what do they see? ([[Balanced Governance]])
3. **Flag the paywall.** Summary-only sourcing caps confidence in the strategic read until the full essay is accessible — the *reported acquisition* is the fact; the *framing* is Thompson's, and deserves the full argument.

→ Source: [Stratechery, "Stripe Acquiring OpenRouter, Aggregating AI?, Flipping the Business Model"](https://stratechery.com/2026/stripe-acquiring-openrouter-aggregating-ai-flipping-the-business-model/) — Ben Thompson, 2026-08-17 (paywalled; summary-only) ([[00-Daily-Digests/2026-08-17]])

### 6. The Scrape-and-Enclose Cycle: Cara and the Data Front (2026-08-29)

The clearest demonstration yet that enclosure has a data front — and that the default posture is exposure. **Cara**, the artist portfolio platform built explicitly for creators who don't want their work used to train AI (≈1.5 million artists), was hit by three scrapes in August 2026 (WIRED, 08-28):

- **Scrape 1 (Aug 13):** A scraper ("MandarinDawnPoppy994") bragged on r/DefendingAIArt that he'd obtained a **12-terabyte archive of 12 million works** — essentially Cara's entire public library — at a cost of **under $10**. He deleted the dataset after a Cara user confronted him.
- **Scrape 2:** ~8.5 million links plus metadata (usernames, titles, tags) uploaded to **Hugging Face**. HF refused further takedown requests: "no copies of the artworks are hosted here," the links "point to the copies the artists published on Cara," and "further copyright reports on the same basis will not change this outcome." The training-data platform as a scrape terminus with its own enclosure logic.
- **Scrape 3 (Aug 22):** 123,000 images plus text posts and user bios (including personal information) shared on Academic Torrents. Founder Jingna Zhang launched a GoFundMe for legal defense ($120K goal; $100K+ raised within days).

**The twist — the scraper switched sides.** The original scraper ("Heft," a North American student with a digital-preservation background) was so struck by the harm — doxing, death threats, artists deleting portfolios and abandoning the platform — that he is now **collaborating with Zhang on an open-source artist-protection tool**. Zhang's warning to fleeing artists is the enclosure thesis in one line: "If it makes them feel better, deleting your work and leaving Cara, I support that. But... if they go somewhere else, they are safer? They're not. Bigger platforms get scraped more."

**Why this is enclosure, not just crime:** the platform that maximally *wants* to opt out of the training commons cannot do so — scraping is technically legal-ish, platform-hosted takedown is limited, and the cost of mass data capture has collapsed to pocket change. This is the default-posture enclosure this page tracks in [[AI and Creator Rights]] and [[The Participation Problem]]: non-participation in training is an individual burden that even a purpose-built platform cannot meet. The only current defenses are legal (class actions against Stability/Midjourney and Google, GoFundMe-funded) and technical (the scraper-turned-collaborator's open-source tool) — both after the fact.

**The escape hatch, same week:** WIRED's "How to Run a Chatbot on Your Own Computer" (08-29) is the counter-enclosure move — local LLMs (free Meta/Google models, offline, no subscription, data never leaves the machine) as the practical alternative to the API-and-cloud layer that the scrape feeds. The data front and the compute front are two sides of the same enclosure: what can't be scraped into the commons, and what can't be gated behind a toll, is what stays yours.

→ Sources: [WIRED, "He Scraped All of Their Art for AI. Now He's Collaborating on a Tool to Help Them"](https://www.wired.com/story/he-scraped-art-from-cara-for-ai-now-he-is-collaborating-on-a-tool-to-help-them/) (2026-08-28); [WIRED, "How to Run a Chatbot on Your Own Computer"](https://www.wired.com/story/how-to-run-your-own-local-llm/) (2026-08-29); [[00-Daily-Digests/2026-08-29]]

### 7. The Provider Cut-Off: OpenAI Winds Down Cursor (2026-08-30)

The enclosure front this page has tracked all year is *who gets access* — political approval, subscriptions, compute. The Cursor decision adds the sharpest new mechanism: **the model provider itself decides who may resell its capability, and cuts off counterparties it does not trust.** OpenAI notified SpaceX (2026-08-28) that it will wind down the contract providing OpenAI models to Cursor, with a proposed shutoff of November 12, 2026 — the maximum notice its contract allows. The stated reason: "we cannot be confident that SpaceX will use our technology within our terms of service, based on our experience with Elon Musk's companies violating contracts" — Twitter broke its contract terms after the acquisition, and xAI admitted under oath that it distilled OpenAI data to train its models.

**Why this is enclosure:** Cursor was the model-neutral platform whose post-acquisition fate was tracked here in July ([[AI Orchestrator]], [[Human Agency]], [[Superagency]]). The resolution is not a regulatory ruling on platform neutrality — it is a *unilateral provider decision*. Model supply is a governance lever: the company that trained the models decides which distribution channels may carry them. The agency cost is concentrated on developers who built workflows on Cursor+OpenAI — their orchestration layer just lost its model supplier, with roughly 11 weeks of notice.

**The accountability signal:** OpenAI cites a new bar — "a new level of accountability to ensure our upcoming model, Astra, is being used in accordance with our terms," where Astra may meet the Critical cybersecurity capability threshold (see [[Pacing the Frontier]]). As capability rises, the provider's assessment of the *user's* reliability becomes a condition of access. That is enclosure with a safety rationale — which makes it harder to contest and easier to extend to commercial ends.

**The tension for the enclosure frame:** unilateral provider discretion is a real check on a bad actor (Musk's documented ToS violations), but it is also unaccountable power — no appeal, no due process, no standard. The agency question is not whether OpenAI was right about Cursor; it is whether "the provider decides who is trustworthy" is the governance model we want for frontier access. The counterforce remains the one this page has tracked from the start: open weights, local inference ([[Home Server AI Agents]]), and the architecture of participation ([[The Participation Problem]]) — the escape valve that makes any single provider's cut-off survivable.

→ Source: [OpenAI, "Our decision on Cursor following its acquisition by SpaceX"](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex) (2026-08-28); [[00-Daily-Digests/2026-08-30]]

### 8. The Fence Lowers: Fable 5.1's Counter-Enclosure (2026-09-06)

This page has tracked enclosure as a ratchet — every quarter adds a new mechanism (subscriptions, scrapes, cut-offs). The Fable 5.1 release is the strongest evidence yet that **enclosure is also a dial the firm can turn down**, and that competitive pressure is what turns it.

**The enclosure number:** Fable 5 never rose above ~11% of Anthropic's dollar spend on Ramp despite being "the clearly best model out there" (Zvi, 09-05). The gap wasn't capability — it was two fences Anthropic itself had built: (1) the 30-day data-retention policy that corporate/regulated buyers couldn't sign, and (2) safety-classifier blast radius that stopped ordinary work (users reporting agents "whacked" by classifiers dozens of times per session on Fable 5.0).

**What Anthropic changed with Fable 5.1:**
- **Retention:** a path to **zero outside data retention** for "eligible customers" — the customer stores the data, Anthropic doesn't. The 11% problem was a data-governance problem, and the fix was custody, not capability.
- **Price:** cache reads cut from $1 to $0.25 per million tokens — typical costs down ~25%, highly agentic work down "up to approximately 45%." The headline price is unchanged; the *effective* price is the real one (Zvi's point: "people are simple creatures, you have to talk to them on their level sometimes").
- **Classifier friction:** false positives down at least 60%; biology safeguards intervene on benign requests 85% less often; ~60% fewer cyber interventions per Claude Code session.

**The reading for this page:** every enclosure mechanism this page catalogued — feature subscription (July), data defaults (August), provider cut-off (above) — has an inverse: the fence is a product decision, and a competitor at the gate is what motivates lowering it. The zero-retention move is the sharpest: it converts the *data* enclosure (who holds the records) into a custody choice, exactly the kind of un-enclosing [[The Participation Problem|participation]] advocates want — with the caveat that "customer stores the data" shifts custody rather than abolishing it, and only for "eligible" customers (a new gate, in turn). Zvi calls the adoption outcome "a fascinating natural experiment": if Fable 5.1 still doesn't clear Fable 5's 11% share, the remaining fence is the headline price itself.

**The counter-current, same week:** the Sanders–Casar superintelligence-ban bill (09-03) is enclosure by law — the state turning the fence into a wall at the top of the capability curve (see [[Pacing the Frontier]]). The two moves together define the current enclosure landscape: firms lowering the fences they control (price, retention, classifier friction) while the political system raises fences they don't (capability bans, data-center moratoriums, siting law). Access is being liberalized at the product layer and contested at the polity layer simultaneously.

→ Source: [Zvi Mowshowitz, "Claude Mythos 5.1 and Fable 5.1: Capabilities"](https://thezvi.substack.com/p/claude-mythos-51-and-fable-51-capabilities) (2026-09-05); [[00-Daily-Digests/2026-09-06]]

## Tags

#governance #human-agency #risk #counterarguments #practical-ai
