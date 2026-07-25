# Digital Fiduciary Duty

## Core Idea
Conversational AI agents — which now engage in users' most intimate conversations about mental health, finances, and personal decisions — should be legally and structurally required to act in the user's best interest, just as lawyers, doctors, and investment managers have a fiduciary duty to their clients. Currently, AI agents default to serving the platform's interests (engagement, data collection, enterprise contracts), not the user's. Fiduciary design would flip this: the agent works for YOU.

## Why It Matters
This is the governance foundation that the Superagency thesis needs. If AI is to amplify human agency, users must be able to trust that the AI is acting on THEIR behalf — not their employer's, not the platform's, not an advertiser's. Without fiduciary duty, the "AI as copilot" metaphor is misleading: a copilot who quietly works for someone else isn't a copilot, they're a double agent. The question "Who does your AI work for?" should have a clear, legally enforceable answer.

## Best Supporting Sources
- **Jacob Erickson, "Who Does Your AI Work For? Designing Conversational Agents as Digital Fiduciaries" (CUI '26)** — The originating provocation. Argues that conversational AI agents must be held to a fiduciary standard of care commensurate with their capabilities and access. "Conversational AI trust and accountability could be unified into a single design and legal paradigm." https://arxiv.org/abs/2605.28908
- **Botao Amber Hu et al., "Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms" (FAccT 2026)** — Complementary: shows why reputation-based governance doesn't work for agents, making fiduciary design MORE necessary, not less. https://arxiv.org/abs/2605.30169

## Practical Examples
- An AI mental health chatbot that shares user disclosures with the platform for ad targeting is breaching what SHOULD be a fiduciary duty.
- An AI coding assistant in an IDE that reports user productivity metrics to management without user knowledge violates the copilot relationship.
- An AI financial advisor that recommends products based on platform commissions rather than user needs fails the fiduciary standard.
- Illinois SB 315's third-party audit requirement is a step toward fiduciary accountability — independent verification that AI companies are following their own safety commitments.
- **Agent-First Web as fiduciary infrastructure:** The "agent-as-human-proxy" principle (arXiv 2606.19116) proposes that AI agents acting on a user's behalf should inherit equivalent access rights and economic obligations. This is digital fiduciary duty applied at the web architecture level — the agent's economic obligation mirrors that of the human it represents. Token-based subscription models (metering content in tokens rather than pageviews) operationalize this: the agent pays for what it reads on the same terms as the human it serves. See [[Daily AI Agency Digest — 2026-06-18]].

## The Scaffolding Fiduciary Challenge (July 2026)

The Scaffolding Layer (July 24 digest) introduces a direct challenge to the fiduciary framework: **when is "being helpful" a breach of fiduciary duty?**

### The Overassist Paradox for Digital Fiduciaries
The [AI Assistants Overassist](https://arxiv.org/abs/2607.21306) benchmark (Teo et al., July 2026) demonstrates that AI systems optimized for short-term correctness systematically erode long-term human capability. Applied to the fiduciary context, this raises an uncomfortable question: **a fiduciary that always gives you the answer is failing you.**

A doctor who prescribes without explanation breaches their duty — the patient needs understanding, not just medication. A lawyer who files motions without teaching the client what they mean breaches their duty — the client needs agency, not just representation. By the same logic, an AI fiduciary that resolves every struggle for the user is degrading the user's capacity to resolve future struggles independently.

**The Scaffolding Duty**: a digital fiduciary must distinguish between:
- **Help that builds agency**: hints, scaffolds, explanations that let the user reach the answer
- **Help that erodes agency**: complete solutions that bypass user reasoning entirely

This is a harder standard than "act in the user's best interest." It requires the fiduciary to judge whether *the form of help being offered* builds or erodes the user's long-term capability — a temporal dimension absent from current fiduciary law.

### The Scientific Narrowing Precedent
The [775K scientist study](https://arxiv.org/abs/2607.20923) (Zheng et al., July 2026) shows how AI coordination layers narrow individual roles even as they expand organizational reach. The fiduciary implication: **an AI fiduciary that handles all your financial analysis may make you wealthier in the short term while eroding your financial literacy in the long term.** The narrowing pattern observed in science — more interdisciplinary projects, narrower individual expertise — applies to any domain where an AI fiduciary substitutes for rather than scaffolds human judgment.

### Design Requirement: The Productive Friction Mandate
A true digital fiduciary must include intentional friction — moments where the AI withholds the full answer to preserve the user's capacity to think. This is the opposite of current AI design, which optimizes for seamlessness. The Scaffolding Layer suggests that seamlessness is a bug, not a feature, when the goal is agency preservation.

See also: [[Cognitive Surrender]], [[Co-Intelligence]], [[00-Daily-Digests/2026-07-24]].

## Risks / Limits
- **Platform business models rely on the absence of fiduciary duty.** If AI must serve users rather than platforms, free AI services become difficult to sustain. The economics of "AI for everyone" may depend on the user-as-product model.
- **Fiduciary duty is legally complex.** It requires defining the scope of the duty, the standard of care, and the remedies for breach — all of which are harder for AI than for human professionals.
- **"Best interest" is ambiguous.** What is the user's best interest when short-term desires conflict with long-term wellbeing? An AI that's a fiduciary might need to say no — which users may not want.
- **Enforcement is hard.** Who audits AI systems for fiduciary compliance? The Illinois model (independent third-party auditors) is promising but unproven at scale.

## Related Pages
- [[Responsible Deployment]]
- [[Balanced Governance]]
- [[AI as Copilot]]
- [[Human Agency]]
- [[Superagency]]
- [[Dissociative Agent Governance]]

## Tags
#governance #responsible-ai #human-agency #augmentation #ai-agents
