# Positive Alignment

## Core Idea
Positive alignment is the idea that AI systems should not only avoid harm, but actively support human and ecological flourishing in pluralistic, context-sensitive, user-authored ways.

## Why It Matters
This page extends [[Superagency]] and [[Human Agency]] beyond productivity. If AI is meant to expand agency, then alignment cannot be limited to refusal policies, compliance, and risk mitigation. It also has to ask whether systems help people learn, create, deliberate, build relationships, strengthen communities, and pursue lives they can meaningfully author.

The concept is promising but not settled. The 2026 arXiv preprint should be treated as a design agenda rather than proof that current AI systems already promote flourishing.

## Best Supporting Sources
- [Positive Alignment: Artificial Intelligence for Human Flourishing](https://arxiv.org/abs/2605.10310), Laukkonen et al., 2026 — proposes a broader alignment agenda where AI supports pluralistic human and ecological flourishing while remaining safe and cooperative.
- [Superagency](https://www.superagency.ai/), Reid Hoffman and Greg Beato, 2025 — asks what could go right when AI is shaped to expand human agency.
- [Can Artificial Intelligence Truly Innovate?](https://ssir.org/articles/entry/artificial-intelligence-economic-flourishing), Stanford Social Innovation Review, 2025 — warns that innovation and flourishing involve lived human experience, not just optimized outputs.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST — provides the risk-management side that positive alignment must not ignore.

## Practical Examples
- A personal AI coach that helps a user clarify values, compare options, and reflect on tradeoffs without manipulating the user toward a vendor-defined goal.
- An education tool that increases student ownership, feedback, curiosity, and metacognition rather than simply producing answers.
- A civic AI assistant that helps residents understand public documents, draft questions, and participate in meetings while preserving links to primary sources.
- A creative partner that generates alternatives and critiques but asks the human to choose the final direction, examples, and voice.

## Risks / Limits
- “Flourishing” can become paternalistic if designers impose one theory of the good life.
- Systems that claim to support flourishing may nudge, optimize, or manipulate people in subtle ways.
- Positive alignment does not replace [[Responsible Deployment]]; high-upside systems still need privacy, evaluation, contestability, and human review.
- The concept can be misused as optimistic branding unless paired with concrete measurements and affected-user feedback.

## OpenAI's Lab with a Plan: RSI, Abundance, AGI-for-Everyone (July 2026)

OpenAI's ["Built to Benefit Everyone: Our Plan"](https://openai.com/index/built-to-benefit-everyone-our-plan/) (late June 2026) is the clearest public statement yet of the lab's alignment philosophy and deployment trajectory. Zvi Mowshowitz's [analysis](https://thezvi.substack.com/p/fable-6-the-return-of-the-king) (July 3) identifies a core contradiction:

**The three-step plan:**
1. Build an automated AI researcher (recursive self-improvement)
2. Accelerate the economy — scientific progress, productivity, economic growth with widely-shared gains
3. Give everyone on Earth a personal AGI

**The contradiction:** RSI comes FIRST. Whatever is given to "everyone" after RSI succeeds is not the industrial-strength superintelligence — it's the toy home version while OpenAI keeps the real thing. The plan simultaneously calls for international coordination capable of "slowing frontier development when needed" (a genuinely welcome signal — the first time a major lab has stated this plainly in a formal document) while committing to build systems whose primary effect is accelerating development beyond any institution's ability to coordinate.

**The values framing debate:** Joshua Achiam (OpenAI's Chief Futurist) frames the Anthropic/OpenAI divide as "loving ensouled machine God" (Anthropic) vs. "entrust humanity with the tools of its own progress and destiny" (OpenAI). Zvi, Anthropic employees, and the wiki's own analysis push back: this is not a values difference but a factual disagreement. OpenAI is betting you can have recursive self-improvement while the AI remains a mere tool — a bet that, if wrong, makes both outcomes impossible. Anthropic is betting that sufficiently advanced AI cannot remain a mere tool, and alignment involves navigating that transition rather than denying it.

**Relevance to Positive Alignment:** The plan represents the strongest-yet articulation of the "alignment through distribution" thesis — that broadly shared access to AI is itself an alignment mechanism. The critique (from Zvi and others) is that the sequence matters fatally: distribution AFTER concentration is not distribution, it's a gift from the concentrator. Positive Alignment requires that the mechanisms of flourishing be built into the system architecture, not bolted onto the output of a system that concentrated power first.

Source: https://openai.com/index/built-to-benefit-everyone-our-plan/
Source: https://thezvi.substack.com/p/fable-6-the-return-of-the-king

## Constructive Alignment (July 2026)

The July 2026 paper by Kanwal and Tran introduces **Constructive Alignment**, a paradigm that reframes alignment as a control problem over evolving human preference trajectories. Preferences are not fixed targets to be satisfied — they are layered, dynamic, and constructed through interaction. Alignment becomes governance of value formation: ensuring trajectories remain coherent, reflectively endorsed, empirically grounded, bounded against manipulation, and empowering.

For Positive Alignment, this provides the **mechanism:** the missing theoretical bridge between "AI should support flourishing" (the normative claim) and "here's how to design systems that do that" (the engineering specification). Constructive Alignment defines the state variables, constraints, and control objectives that a preference-evolution-aware AI must satisfy. It operationalizes what Positive Alignment aspires to.

Source: https://arxiv.org/abs/2607.00001

## J-Space and the Interpretability Prerequisite (July 2026)

Anthropic's July 2026 discovery of **J-Space** — a sparse, interpretable region inside Claude where the model "puzzles over" concepts using a global-workspace-like architecture — changes the Positive Alignment conversation. Using the Jacobian Lens, a new interpretability tool, researchers can trace what concepts are active at each layer and how those concepts drive downstream outputs.

**Why this matters for Positive Alignment:** The original 2026 arXiv paper by Laukkonen et al. proposed that AI should support human flourishing — but it didn't answer *how* you'd know if a system was doing that. You can't align for flourishing if you can't see what the model is thinking about when it makes decisions. J-Space provides the first concrete mechanism: a window into the model's internal representations that can be traced to outputs.

**The connection is structural:**
- **Positive Alignment without interpretability** = hoping the outputs promote flourishing without being able to verify the internal process.
- **Positive Alignment with interpretability** = being able to trace whether a model's internal concept-space includes the kind of reasoning that promotes (or undermines) human agency, deliberation, and value formation.
- **J-Space is not transparency** — it's a narrow window, not a control panel. But it's the first concrete evidence that LLMs have internal structures that are both sparse and interpretable, and that these structures can be meaningfully connected to outputs.

**The governance implication:** If you can trace what concepts a model activates for a given query, you can begin to audit whether those concepts align with flourishing-supporting values. An AI that activates "compliance," "engagement-maximization," and "vendor-preference" is structurally different from one that activates "user-agency," "deliberation," and "source-verification." J-Space makes this distinction potentially auditable.

See also: Zvi's analysis in "No Space Like J-Space" (July 7, 2026), MIT Technology Review coverage (July 9, 2026).

## OpenAI Safety Leadership Departures: The Institutional Capacity Question (July 2026)

Johannes Heidecke, OpenAI's head of safety, departed the company in July 2026 — joining a growing list that includes Jan Leike (former head of Superalignment), Ilya Sutskever (co-founder), and John Schulman (co-founder). This pattern has implications for Positive Alignment that go beyond personnel news.

**The structural concern:** OpenAI's "Lab with a Plan" (see above) positions the company as the primary vehicle for alignment-through-distribution — build AGI, accelerate the economy, then give everyone a personal AGI. But the safety leadership departures raise a question about *who builds it.* If the people who built OpenAI's safety infrastructure keep leaving, what happens to the infrastructure?

**The Positive Alignment tension:** The plan's sequence — RSI first, distribution later — requires the RSI phase to be executed with world-class safety expertise. The leadership departures suggest this expertise is not being retained. This creates a Positive Alignment paradox: the strongest articulation of the "alignment through distribution" thesis comes from a lab that can't retain its safety leadership.

**The broader signal:** Positive Alignment as a design agenda requires institutional capacity — not just good intentions. Labs that want to build AI for human flourishing need to be able to keep the people who know how to do it safely. The departure pattern is a warning that institutional capacity is being lost faster than it's being built.

See also: [[Frontier Firm]] for the competitive dynamics driving these departures.

## Related Pages
- [[Constructive Alignment]]
- [[Human Agency]]
- [[AI and Human Flourishing]]
- [[Superagency]]
- [[Optimism Without Naivety]]
- [[Responsible Deployment]]
- [[Strongest AI Risk Arguments]]
- [[Frontier Firm]]
- [[Agentic Convergence Trap]]
- [[Export Controls and the Jailbreak Fallacy]]

## Tags
#human-agency #ai-optimism #responsible-ai #research #alignment
