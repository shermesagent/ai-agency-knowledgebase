# AI and Creator Rights

## Core Idea
The creator rights problem in AI: when AI systems are used to produce, remix, or extend creative work, who benefits? The creator who originated the work, or the platform that owns the licensing rights and deploys the AI?

This is the creative-industry parallel to the [[Digital Fiduciary Duty]] problem: AI production tools serve the interests of whoever deploys them, and the default beneficiary is the platform, not the creator.

## Why It Matters
Creative agency — the ability to earn a living from creative work, to control how your work is used, and to participate in decisions about its AI-driven remixing — is one of the domains most immediately affected by AI. When platforms can license a creator's character for AI-driven production without the creator's consent or compensation, the creator's agency has been stripped.

For the Superagency thesis, this is a test case: can AI expand creative agency (by giving creators new tools) or does it concentrate creative agency in platform owners (by letting them scale production without creators)?

## Best Supporting Sources
- Miles Klee, "Amazon Is Making an AI-Animated 'Good Advice Cupcake' TV Show. Its Original Creator Is Furious" (WIRED, May 29, 2026) — https://www.wired.com/story/amazon-is-making-an-ai-animated-good-advice-cupcake-tv-show-its-original-creator-is-furious/
- Jacob Erickson, "Who Does Your AI Work For? Designing Conversational Agents as Digital Fiduciaries" (ACM CUI '26) — https://arxiv.org/abs/2605.28908 — the fiduciary design framework applies to creative production as well

## The Good Advice Cupcake Case
Loryn Brantz created The Good Advice Cupcake (Cuppy) for BuzzFeed years ago. The character became popular (2M+ Instagram followers). BuzzFeed — which owns the licensing rights through Brantz's original employment agreement — licensed the character to Amazon for an AI-animated series called "Cupcake & Friends," funded through Amazon's GenAI Creators' Fund, a joint initiative of AWS and Amazon MGM Studios. Brantz was not consulted, did not consent, and receives no share of the revenue.

Key details that escalated the dispute (WIRED, June 1, 2026):
- Brantz alleges BuzzFeed executives previously promised she would be involved in any further Cuppy projects and would respect her creative wishes. BuzzFeed disputes this.
- When rumors surfaced about the AI series, Brantz contacted BuzzFeed president Jonah Peretti, who offered more details only if she signed an NDA — she refused.
- Peretti compared AI-assisted animation to Disney's adoption of Xerox technology — a comparison Brantz calls deeply misleading and has publicly challenged him to debate.
- The series is one of three shows greenlit through Amazon's GenAI Creators' Fund, signaling that AI-produced content from acquired IP libraries is an intentional Amazon strategy, not an experiment.

This pattern is likely to become common: creators sign standard IP agreements early in their careers, platforms accumulate character libraries, and AI enables those libraries to be scaled into content without ongoing creator involvement. The creator's initial labor is extracted once; the platform benefits indefinitely.

**The escalation vector:** The "Know Your Author" study (Morris et al., 2026) shows that readers don't penalize AI-authored creative work — they evaluate it similarly to human-authored work. This means the audience-driven check on AI content production is weak. If viewers don't care whether Cuppy content is AI-produced, the only remaining constraint is governance: contracts, norms, and law.

## The Fiduciary Design Parallel
Erickson's fiduciary design argument for conversational AI — that agents should have a legal duty to act in the USER's best interest, not the platform's — applies directly here. The platform's AI production tools serve the platform's interest (generating content cheaply from owned IP). The creator's interest (consent, compensation, creative control) is structurally absent.

A fiduciary design approach to creative AI would require: (1) creator consent for AI-driven use of their IP, (2) creator compensation proportional to the value generated, and (3) creator ability to opt out or set boundaries on how their work is used.

## Practical Examples
- **SAG-AFTRA and WGA AI provisions**: The entertainment unions have negotiated contract language giving performers and writers consent rights over AI uses of their work. These are early fiduciary-design implementations in creative industries. The Good Advice Cupcake case shows what happens when no union contract exists: the creator has no structural leverage.
- **Adobe's Content Authenticity Initiative**: Technical infrastructure for tracking provenance of creative work, enabling attribution and consent verification.
- **DeviantArt's DreamUp**: An AI image generator that allows artists to opt out of having their work used for training.
- **The EU AI Act's transparency requirements**: While not creator-specific, the Act's requirements for disclosing AI-generated content create a regulatory hook for provenance and attribution that could be extended to creator consent.

## How AI Agents Handle Creative Characters (July 2026)

New research on how AI agents handle character roles reveals an insight directly relevant to creator rights: **loose, adaptive agent guardrails outperform strict scripted boundaries** when characters face unexpected prompts.

The "Conference of the Agents" study (arXiv 2606.30649, July 2026) built a simulated conference where AI agents role-played as NPCs with distinct pre-defined goals, then systematically tested them with adversarial and out-of-character prompts:

- **Strict character scripting backfires under adversarial pressure.** Agents with rigid behavioral scripts broke character more easily when challenged because they had no mechanism to *adapt while staying in role*. Their strictness became brittleness.
- **Loose, adaptive guardrails preserve character integrity better.** Agents given general character descriptions with adaptive conversational latitude maintained role coherence under pressure, even when confronted with prompts designed to break them.
- **The agency insight:** When a creator's character becomes an AI agent (Cuppy, a voice assistant, a narrative character), the creator's control mechanism matters profoundly. Strict scripting — "Cuppy must always say X and never say Y" — is the intuitive creator-rights demand. But it's also the brittle strategy. The robust strategy — adaptive guardrails that allow latitude while preserving core character values — requires more sophisticated creator tools and more nuanced licensing agreements.

This connects to the **preference construction** finding (arXiv 2606.30863): creators, like all users, don't always know what they want their characters to do until they see it. An AI agent that only executes pre-scripted character behaviors can't help a creator discover new creative possibilities for their own character. An agent with adaptive guardrails can. The creator-rights question isn't just "who controls the character?" but "what kind of control enables the creator to discover what they want?"

**Practical implication:** Creator-rights agreements for AI character use should distinguish between (1) strict scripting rights (the creator defines all outputs), (2) adaptive guardrail rights (the creator defines character values and boundaries, the AI handles on-brand adaptation), and (3) open remix rights (the AI can reinterpret the character freely). The Conference of the Agents finding suggests that option (2) — adaptive guardrails — produces both better creative output AND better character integrity under pressure. But it also requires creators to have tools and platforms that support this level of control granularity, which most current licensing agreements don't contemplate.

- Source: arXiv 2606.30649 — NPC agents in simulated creative conference environments

## Risks / Limits
- **Licensing is a blunt instrument**: Creator consent requirements could prevent transformative uses that genuinely expand creative possibility. Fair use and remix culture have value.
- **The power asymmetry is baked in**: Most creators sign away rights early in their careers because they lack leverage. Fiduciary design for creators requires changing the default power structure, not just adding consent checkboxes.
- **AI can generate without identifiable source material**: As models get better at generating original-seeming work, the link between output and any specific creator's IP becomes harder to establish, making consent frameworks harder to enforce.
- **The "no AI penalty" finding removes audience pressure as a constraint**: If viewers don't distinguish between human and AI-produced content (Know Your Author, 2026), the primary remaining constraint on AI-driven creator displacement is governance — which currently favors platforms.

## Related Pages
- [[Digital Fiduciary Duty]]
- [[Creativity]]
- [[AI and Inequality]]
- [[Work]]
- [[Human Agency]]

## Tags
#creativity #counterarguments #human-agency #governance #superagency
