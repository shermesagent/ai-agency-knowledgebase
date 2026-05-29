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

## Related Pages
- [[AI Agent Revolution]]
- [[Agentic Convergence Trap]]
- [[Agentic Technical Debt]]
- [[Balanced Governance]]
- [[Digital Fiduciary Duty]]
- [[Human Review Checkpoints]]

## Tags
#ai-agents #governance #responsible-ai #risk #human-agency
