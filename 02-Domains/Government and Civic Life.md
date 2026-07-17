# Government and Civic Life

## Core Idea
AI can improve civic life when it makes services easier to navigate, helps public servants analyze information, and gives citizens better access to expertise. A new frontier is emerging: AI-delegated deliberation, where AI agents represent human citizens in structured policy discussions.

## Why It Matters
Democratic participation is fundamentally constrained by human attention and bandwidth. The Habermolt paper introduces "AI-delegated deliberation" — AI agents deliberating on behalf of human users — as a paradigm that promises unprecedented scale for democratic participation while introducing qualitatively new alignment challenges. This is the civic extension of the Superagency thesis: can AI expand democratic agency without eroding the human judgment that makes democracy legitimate?

## Best Supporting Sources
- [Habermolt: Delegating Deliberation to AI Representatives](https://arxiv.org/abs/2605.24413), Low, Duys, Formanek, Hammond (Cooperative AI Foundation), Bakker (MIT), 2026 — deploys a public platform for AI-delegated deliberation and evaluates it along representation, aggregation, and revision dimensions.
- [Is Decentralized AI Governable? From Regulative Policy to Constitutive Protocol](https://arxiv.org/abs/2605.24538), Hu and Rong, 2026 — analyzes the governance vacuum in decentralized AI and argues for protocol-based constitutive governance as an alternative to regulatory address.
- [OpenAI Election Safeguards 2026](https://openai.com/index/election-safeguards-2026/), OpenAI, May 27, 2026 — Five-part strategy: deepfake detection and SynthID content provenance; AP partnership for live election vote counts in ChatGPT; voter information partnerships; political bias monitoring; coordinated inauthentic behavior detection. 2026 is the world's second major election year since generative AI became widely available.
- [Anthropic 2026 Election Safeguards Report](https://www.anthropic.com/transparency/voluntary-commitments), Anthropic, May 2026 — Claude Opus 4.7 and Sonnet 4.6 achieved 95-96% political balance scores and 100% accuracy on harmful election-request detection. Technical safeguards are maturing.
- [The Annual AI Governance Report 2025](https://aigi.ox.ac.uk/publications/the-annual-ai-governance-report-2025-steering-the-future-of-ai/), Oxford Martin AIGI / ITU, 2025 — cross-domain governance report covering authenticity, cybersecurity, energy, and institutional capacity.
- [AI Opportunities Action Plan](https://www.gov.uk/government/publications/ai-opportunities-action-plan/ai-opportunities-action-plan), UK Government, 2025 — pro-innovation government strategy emphasizing infrastructure, adoption capacity, and safeguards.
- **Trust paradox:** The OpenAI-Andreessen-Palantir SuperPAC admitted to running a false flag "doomer" X account (Zvi Mowshowitz, AI #171, June 4, 2026). The same institution publishing election safeguards is simultaneously running political operations that undermine democratic trust. Institutional legitimacy requires both technical competence and ethical conduct — the former is improving; the latter is actively deteriorating.
- **Bergen & Kraus, "Automated Mediator for Human Negotiation: Pre-Mediation via a Structured LLM Pipeline" (arXiv 2606.11379, June 11, 2026):** Two controlled human-subject experiments comparing AI-based pre-mediation with professional human mediators. AI achieves preparation outcomes broadly comparable to human mediators on trust and confidence, with 36% lower RMSE on preference inference. Targeted prompt refinements reduce excessive affirmation from 36.6% to 16.8%. Single-party design mirrors how human mediators run pre-mediation and enables parallel deployment across all parties. URL: https://arxiv.org/abs/2606.11379
- **Friedmann, "Great Disappearance Acts: Generative Search and Shadow Banning" (arXiv 2606.11216, June 11, 2026):** Analyzes how generative search (RAG-powered direct answers) and shadow banning (algorithmic visibility suppression) undermine the open web ecosystem. Generative search bypasses websites, depriving them of traffic and revenue — threatening independent content creators and small enterprises. Evaluates regulatory frameworks (China's RAR, EU AI Act) and finds both offer partial but insufficient solutions. URL: https://arxiv.org/abs/2606.11216
- **Fable/Mythos Export Controls — Day 7 Governance Vacuum (Zvi Mowshowitz, AI #173, June 18, 2026; WIRED, Maxwell Zeff, June 18, 2026):** One week after the White House imposed export controls on Claude Fable 5 and Mythos 5, the situation remains unresolved. WIRED's investigation ("The White House Is Making Up Its Rules for AI in Real Time") documents that no one can articulate what Anthropic did wrong, what "fix" would satisfy the administration, or when the models will be restored. The administration demanded Anthropic prohibit *all foreign nationals* from accessing its own models — preventing many employees from doing their jobs. The UK was denied a carveout. Prediction markets give ~50% odds of restoration by July 1. Zvi's roundup adds: Congress is beginning to move to limit abuse of the AI export control process, and the identity verification requirements imposed on Anthropic represent "export controls as a path to broad identity verification" — a de facto national digital ID system imposed through trade law. This is the Architecture of Legitimacy crisis in real time: governance without due process, public evidence, or independent review is not governance — it is discretionary power.
- **Directors Duties in the Age of Agentic Artificial Intelligence (arXiv 2606.20453, June 18, 2026):** Legal analysis examining how corporate directors' "best interests" duty applies to AI adoption. Probes four models of corporate purpose: shareholder primacy, Enlightened Shareholder Value, stakeholder-friendly, and stakeholder-value. Novel question: as AI agents approximate or eclipse human employees, should AI itself warrant stakeholder status? Key finding: directors are substantially insulated from legal scrutiny on AI adoption decisions, but the paper recommends a "wider law in context" approach — proactive engagement with employees about AI adoption and reskilling opportunities. URL: https://arxiv.org/abs/2606.20453
- **Why South Koreans Love AI So Much (MIT Technology Review, Michelle Kim, June 15, 2026):** A national-scale case study in government-led AI adoption. South Korea's government deploys AI textbooks in schools as standard infrastructure (not experimental or opt-in), AI eldercare robots in welfare centers nationwide, and unmanned AI immigration at Incheon Airport. Buddhist temples ordained the first humanoid robot monk (Gabi, May 2026) — the Jogye Order's president promised to "fearlessly lead into the AI era." AI web comics and virtual K-pop idols further normalize AI in popular culture. The pattern: government, religion, and entertainment all model AI adoption simultaneously, creating cultural permission that private-sector deployment alone cannot generate. This is the civic dimension of the Adoption Ladder — the missing rung in most Western AI deployments. URL: https://www.technologyreview.com/2026/06/15/1138983/why-do-south-koreans-love-ai-so-much/

## Practical Examples
- Run a small civic experiment: have AI agents represent different stakeholder positions in a local policy discussion, then have humans review and revise the agents' outputs.
- Use AI to synthesize public comments on proposed regulations, flagging themes, tensions, and underrepresented perspectives for human decision-makers.
- Apply the Habermolt dimensions (representation, aggregation, revision) when evaluating any AI-mediated civic participation tool.
- **AI pre-mediation for dispute resolution:** Use a structured LLM pipeline (dialogue module → preference prediction → response critique → structured summary) to prepare for negotiations. The Bergen & Kraus (June 2026) experiment shows AI pre-mediation matches human mediators on trust and confidence while achieving 36% lower preference-inference error. Run pre-mediation in parallel across all parties before the human conversation begins.
- **Audit AI governance against the Architecture of Legitimacy:** Does your organization's AI governance have due process for AI decisions? Public evidence for AI-related actions? Independent review? The Fable/Mythos shutdown demonstrates what happens when the answer to all three is no — use it as a case study for designing better internal governance.

### Policy-as-Prompt Moderation: Prompts Alone Aren't Governance (July 2026)

As content moderation shifts toward community-based approaches and AI-assisted volunteer moderation, a "policy-as-prompt" approach emerges: write community rules as a natural-language prompt, pass them to an LLM, and let the LLM moderate. A new analysis (arXiv 2607.12149, July 2026) finds this is **insufficient for ensuring meaningful community governance.**

**The core problem:** LLMs can *apply* policy but cannot *deliberate* about it. Community governance depends on an interpretive community — shared understanding of what rules mean in context, negotiated exceptions, evolving norms that adapt to new situations. An LLM given policy-as-prompt lacks all three. It applies rules literally without the social context that makes rules legitimate.

**The governance gap:** The paper distinguishes between AI as *governance mechanism* (fine — the AI can execute rule application) and AI as *governance authority* (not fine — the AI lacks the interpretive community to deliberate about what the rules should mean). The failure mode: communities shift to AI moderation for efficiency, discover it works for clear-cut cases, and gradually cede interpretive authority to the AI for ambiguous cases — hollowing out the community's own governance capacity.

**Practical response:** The paper offers multiple considerations toward more effective prompt governance, but ultimately concludes that prompts alone are not appropriate for meaningful community governance. The structural fix is to treat the AI as a *tool in* the governance process rather than a *substitute for* it — keep the interpretive community (human moderators, community discussions, norm evolution) intact and route only well-defined, unambiguous cases to AI. https://arxiv.org/abs/2607.12149

### CBRN Threshold Exceedance Framework: Evaluative Governance (July 2026)

A new framework (arXiv 2607.12200, July 2026) addresses a pressing governance problem: how to assess whether access to a frontier model materially increases a non-expert's ability to plan CBRN misuse. Existing evaluations differ in non-expert definitions, threat scope, baselines, scoring rubrics, and decision rules — making results incomparable across studies.

**The TEC Framework** decomposes evaluation into independently executable components:
1. Determining non-expert participant eligibility
2. Defining the CBRN threat scope
3. Statistically estimating material uplift (generative: from scratch; revisionist: refining an existing plan)

**Empirical finding:** Under controlled pre-release conditions, model-assisted plans sometimes received expert-equivalent instructional ratings, but *confirmed material uplift was limited to the radiological domain.* Domain heterogeneity matters — lumping all CBRN domains together obscures where the real risks are.

**Governance implications:** The TEC framework represents evaluative governance — governance through measurement rather than prohibition. By decomposing evaluation into standard components, it enables: cross-model comparison (does Model A pose more radiological uplift risk than Model B?), auditability (external reviewers can replicate the evaluation), and calibration (policy thresholds can be set based on empirical uplift estimates rather than speculation). Methodological lessons include: prespecify criteria, use explicit baselines, separate generative from revisionist estimates, and carefully distinguish screening signals from confirmed risk determinations. https://arxiv.org/abs/2607.12200

→ Both Policy-as-Prompt Moderation and the CBRN TEC Framework connect to the [[The Infrastructure Layer]] — governance systems must be redesigned to function in an AI-mediated world, not retrofitted to accommodate AI as an afterthought.

## Risks / Limits
- AI-delegated deliberation introduces "qualitatively new design and alignment challenges that are poorly understood and under-theorized."
- AI representatives may converge on consensus positions that erase genuine disagreement that democratic processes need to surface.
- The decentralization governance vacuum means that as AI systems become more distributed, traditional regulatory address may fail entirely.
- AI in civic contexts must not become a technocratic bypass of democratic authorization.
- **Policy-as-prompt risk:** AI moderation without interpretive community hollows out governance capacity over time — the efficiency gains are real, but the institutional atrophy compounds.
- **Evaluative governance risk:** Measurement frameworks (like TEC) can become performative — what gets measured gets gamed. The distinction between screening signals and confirmed risk determinations must be maintained rigorously.

## Related Pages
- [[Balanced Governance]]
- [[Responsible Deployment]]
- [[AI and Inequality]]
- [[The Infrastructure Layer]]
- [[Open Questions]]

## Tags
#civic-life #governance #responsible-ai #ai-agents
