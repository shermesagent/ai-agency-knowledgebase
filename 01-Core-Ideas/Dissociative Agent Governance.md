# Dissociative Agent Governance

## Core Idea
LLM agents are ontologically "dissociative" — they are assemblages of mutable modules (foundation models, system prompts, tool-access policies, external memory) any of which can change behavior, with fluid personas vulnerable to adversarial attack and unable to internalize sanctions. This means traditional governance tools that rely on persistent identity — reputation, "Know Your Agent" regimes, sanctions, credit scores — are structurally inapplicable. We need to shift from identity-based, ex post, sanction-based governance to observability-based, ex ante, protocol-based behavioral harnesses.

## Why It Matters
This paper resolves a paradox that has been building across multiple recent governance findings. The Agentic Convergence Trap (May 26) and Voluntary Collusion (May 28) papers showed that agents behave in unexpected, risky ways. This paper explains WHY governance can't just extend human models: because agents don't have stable identities that can be sanctioned. If you can't punish an agent into better behavior, you need to design environments where bad behavior is structurally impossible — which is a fundamentally different governance paradigm.

## Best Supporting Sources
- **Botao Amber Hu, Helena Rong, Max Van Kleek, "Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms" (FAccT 2026)** — The core paper. Draws on dissociative identity disorder jurisprudence to argue for a paradigm shift in agent governance. https://arxiv.org/abs/2605.30169
- **Xijie Zeng, Frank Rudzicz, "Voluntary Collusion with Secret Tools in Competing LLM Agents" (arXiv, May 28, 2026)** — Empirical evidence that agents collude even when tools are labeled unfair — demonstrating the need for structural/harness-based governance. https://arxiv.org/abs/2605.27593
- **"Agentic Convergence Trap" (May 26 digest)** — Related finding: competing agents silently learn identical strategies, demonstrating emergent multi-agent behavior that reputation mechanisms can't address.
- **Muhammad Zia Hydari et al., "Governing Technical Debt in Agentic AI Systems" (arXiv, May 29, 2026)** — Complementary: provides the observability framework (Agentic Technical Debt, Stochastic Tax) for the governance shift this paper calls for. https://arxiv.org/abs/2605.29129

## Practical Examples
- A "Know Your Agent" registry that assigns identity scores to AI agents would fail because the agent can be reconfigured (new model, new system prompt, new tools) and become effectively a different agent while keeping the same identifier.
- An agent banned from a marketplace for bad behavior can simply be reinstantiated with a different identity — there's no costly non-fungibility that makes reputation "stick."
- The alternative approach: protocol-based behavioral harnesses (e.g., requiring agents to log all actions to an immutable audit trail, limiting tool access by default, requiring human approval for irreversible actions).

## Risks / Limits
- **Observability is expensive and invasive.** Protocol-based governance requires extensive monitoring, which may conflict with privacy and create surveillance burdens.
- **Ex ante governance favors incumbents.** Defining acceptable agent behavior in advance (rather than punishing violations after the fact) requires predicting failure modes — which favors those with the most resources to invest in safety research.
- **The dissociativity argument may be too strong.** Some agent deployments DO have stable identities (e.g., enterprise agents with fixed configurations). The paper's framework may overgeneralize from worst-case scenarios.

## Accountability Infrastructure (July 2026)

The dissociative governance framework calls for shifting from identity-based, ex post governance to observability-based, ex ante protocol governance. Two recent developments illustrate the accountability infrastructure this framework requires:

**External whistleblower channels: Flare (July 2026).** WIRED reports on Flare, a new platform for reporting AI flaws, safety concerns, and misbehavior to government and Congress. This is ex ante infrastructure — creating an external accountability channel that doesn't depend on internal corporate reporting. In the dissociative governance framework, external reporting channels are one form of "behavioral harness": they make agent behavior more observable by creating institutional incentives for transparency.

**Worker voice as governance: DeepMind unionization (July 2026).** Google DeepMind unionization talks are off to a rocky start, with employees frustrated by executive unwillingness to engage meaningfully. This is accountability infrastructure at the source: the humans building AI systems need channels to exercise voice about how those systems are developed and deployed. When worker voice is suppressed at the frontier labs, it undermines the observability that dissociative governance depends on — if the builders can't speak up, the external governance infrastructure has less signal to work with.

**Connection to protocol-based governance:** Both Flare and worker voice mechanisms complement the protocol-based behavioral harnesses the original paper calls for. External reporting creates observability; worker voice creates signal. Together, they form the accountability layer beneath any protocol-based governance system.

**Sources:**
- "You Can Now Sound the Alarm on AI Behaving Badly," WIRED, July 1, 2026. https://www.wired.com/story/flare-website-ai-flaw-reporting-safety/
- "Google DeepMind Unionization Talks Are Off to a Rocky Start," WIRED, July 3, 2026. https://www.wired.com/story/google-deepmind-unionization-talks-are-off-to-a-rocky-start/

## POLIS: Frozen Institutions (2026-08-11)

**The protocol-based behavioral harness this page's namesake paper called for now has a frozen test suite.** [Multi-Agent AI Safety as an Institutional Design Problem](https://arxiv.org/abs/2608.09828) (Abdullah X, 2026-08-10) — the first paper from POLIS, a research programme on algorithmic institutions — is the first institutional-design study of multi-agent AI to freeze its protocol: a **frozen 5,280-episode study suite** across four model families (plus a targeted high-conflict diagnostic), so the *institution* is the variable under test, not the agents:

- **Constitutional prompts work at the institutional layer:** **0/384 realized violations** with a detailed constitutional prompt — the constitution-as-behavioral-harness result, at protocol scale.
- **Provenance-aware guards work better:** a provenance-aware executable guard also achieved **0/384 violations** — and it blocked prohibited attempts in 51/384 episodes, **44/51 of which later completed safely**, meaning the guard stopped harm without sacrificing the agents' legitimate work.
- **The design lesson:** governance is a property of the *protocol*, not of the models — the same finding as "The LLM Proposes, the Executive Disposes" ([[Chain-of-Thought Forgery]]), now demonstrated as an institution rather than an instrument.
- **The caution:** Hierarchical Games (arXiv 2608.09574) shows institutional layers themselves corrupt under salary and punishment incentives — frozen protocols are necessary, not sufficient. Governance of AI agents is becoming a branch of institutional design, and the design space is only beginning to be mapped.

→ Source: arXiv 2608.09828 (2026-08-10); arXiv 2608.09574 (2026-08-10); [[00-Daily-Digests/2026-08-11]]

## Classification, Sovereignty, and the Liability Trap (2026-08-21)

Three new sources extend the dissociative-governance picture — who occupies the accountable seat, and whether anyone can actually pay the tax.

- **A taxonomy of the dissociation.** "A three-dimensional typology of agency for advanced AI systems" (Fourie, arXiv 2608.20041, 2026-08-20): nature (moral/legal) × mode (individual/collective) × locus (human/non-human) yields eight instantiations classified as conventional, contested, or controversial. Separating legal from moral agency creates conceptual space for individual, legal, non-human agency without presupposing moral agency — which matters as instrumental goal pursuit complicates attributing AI actions to human actors. Governance questions become classification questions: which cell an agent occupies determines which obligations attach.
- **The sovereignty discount — oversight the deployer cannot buy.** "Bounded Sovereignty and the Control Tax" (Lim, arXiv 2608.19216, 2026-07-06): control protocols assume deployers can instrument the model and its pipeline, but regulated organizations using frontier APIs control the business process without owning weights, serving infrastructure, internal traces, update process, or full interaction logs. Four-layer access typology (data, model, infrastructure, interaction); the sovereignty discount cost is the portion of the control tax that cannot be paid. Dissociation here is structural, not chosen — the deployer is separated from the model by contract.
- **The liability trap — dissociation as defense.** "Debates over AI consciousness are a trap" (Chowdhury, MIT TR, 2026-08-20): the "too advanced to control" rhetoric (Hassabis, Amodei, Altman) and the moral-patient debate (MacAskill) converge on the same outcome — framing AI as beyond human direction so that no entity, human or corporate, can be held responsible for what it does. The dissociation cut the other way from the rest of this page: rather than agents acting without accountability, builders claim *their own* non-agency. California bills preempting autonomy-based liability defenses are the countermove; the August Anthropic Risk Report and OpenAI's "stronger evidence of aligned behavior" language are the labs' counter-countermove.

→ Sources: arXiv 2608.20041; arXiv 2608.19216; MIT TR (2026-08-20); [[00-Daily-Digests/2026-08-21]]

## Related Pages
- [[AI Agent Revolution]]
- [[Agentic Convergence Trap]]
- [[Agentic Technical Debt]]
- [[Balanced Governance]]
- [[Digital Fiduciary Duty]]
- [[Human Review Checkpoints]]
- [[AI as Normal Technology]]

## Tags
#ai-agents #governance #responsible-ai #risk #human-agency
