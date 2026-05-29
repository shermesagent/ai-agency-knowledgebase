# Agentic Technical Debt

## Core Idea
As agentic AI systems become production infrastructure, they create governance challenges that don't fit traditional software or ML technical debt models. Two new concepts: **Agentic Technical Debt** — the accumulated liability when prompts, memory, tool schemas, orchestration graphs, control policies, and observability routines are patched together faster than they can be validated and governed. **Stochastic Tax** — the recurring operating burden of keeping probabilistic agent behavior within acceptable bounds. The distinction: debt is a STOCK of design and governance liability; tax is a FLOW of operating cost.

## Why It Matters
This framework gives organizations a vocabulary for what they're actually experiencing with agent deployments. "The agent keeps drifting" becomes "our Stochastic Tax is rising." "We have too many ungoverned agent workflows" becomes "we're accumulating Agentic Technical Debt." Making these visible through dashboards creates accountability. Without this framework, organizations accumulate agent fragility silently — the system looks fine right up until it doesn't. This directly extends the "capability masking" concept: Agentic Technical Debt is what accumulates when capability masking goes unaddressed at the organizational level.

## Best Supporting Sources
- **Muhammad Zia Hydari, Raja Iqbal, Narayan Ramasubbu, "Governing Technical Debt in Agentic AI Systems" (arXiv, May 29, 2026)** — The originating paper defining the concepts and outlining lightweight dashboard-based governance controls. https://arxiv.org/abs/2605.29129
- **Wolfgang Rohde, "Short-Term Gain, Long-Term Fragility: AI Labor Substitution and the Erosion of Sustainable Capability" (arXiv, May 28, 2026)** — The capability masking concept that Agentic Technical Debt extends to the organizational level. https://arxiv.org/abs/2605.27399
- **Rohith Nama, "Agentic Literacy Debt" (AI & Ethics, May 28, 2026)** — Complementary concept: Agentic Technical Debt describes organizational liability; Agentic Literacy Debt describes societal liability. https://arxiv.org/abs/2605.27396

## Practical Examples
- **Agentic Technical Debt:** A company deploys 50 agent workflows across departments. Each has custom prompts, tool schemas, and orchestration. None are documented. When the underlying model updates, 12 workflows break silently. The debt from undocumented, unvalidated agents is now a production liability.
- **Stochastic Tax:** A customer service agent has a 2% hallucination rate. Each hallucination requires 15 minutes of human intervention to correct. At 10,000 interactions/day, the Stochastic Tax is 50 hours/day of human correction effort — a recurring operating cost.
- **Dashboard metrics:** Track (1) number of agent workflows in production, (2) last validation date, (3) known failure modes, (4) Stochastic Tax (human intervention hours / agent interactions).

## Risks / Limits
- **Quantifying Stochastic Tax is itself stochastic.** The tax varies by model version, prompt, user behavior, and task type. The dashboard can create an illusion of precision.
- **"Debt" framing implies repayment is possible.** Some Agentic Technical Debt may be structural — you can't "pay it down" without fundamentally redesigning the agent architecture.
- **The dashboard can become theater.** If tracked metrics don't drive decisions, they become another form of capability masking — the appearance of governance without the substance.

## Related Pages
- [[AI Agent Revolution]]
- [[Dissociative Agent Governance]]
- [[Human Review Checkpoints]]
- [[Capability Masking]]
- [[Agentic Business Transformation]]
- [[Responsible Deployment]]

## Tags
#ai-agents #governance #responsible-ai #future-of-work #risk
