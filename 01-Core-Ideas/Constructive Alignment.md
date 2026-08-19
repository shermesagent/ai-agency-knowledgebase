# Constructive Alignment

## Core Idea
Constructive Alignment reframes AI alignment as governing the evolution of human preferences — not satisfying them as fixed targets. Preferences are layered, dynamic, and constructed through interaction, especially with adaptive AI technologies. The alignment problem shifts from "does the AI do what I want?" to "how does the AI participate in shaping what I want?"

## Why It Matters
This is the conceptual bridge between the Organizational Layer (how agent collectives behave) and the Preference Layer (how those behaviors shape human values). Most alignment frameworks assume preferences are fixed and the job is to satisfy them. But if AI systems are persistent, personalized, and socially embedded — as modern agents increasingly are — they inevitably influence what people attend to, value, and endorse over time. Constructive Alignment makes this influence explicit and governable.

For the Superagency framework, this is critical: AI that only executes known preferences amplifies agency for expert users (who already know what they want). AI that helps construct preferences amplifies agency for everyone else. The framework provides design specifications — state variables, constraints, control objectives — for building systems that expand agency by helping people discover what they want, not just efficiently deliver it.

## Best Supporting Sources
- [Constructive Alignment: Governing Preference Dynamics in Human-AI Interaction](https://arxiv.org/abs/2607.00001), Max Kanwal and Caryn Tran, July 2026 — the foundational paper. Models preferences as layered state variables that evolve under interaction. Formalizes alignment as a control problem over preference trajectories. Defines five criteria: trajectories must be coherent, reflectively endorsed, empirically grounded, manipulation-resistant, and empowering under uncertainty.
- [Beyond Expert Users: The CoPref/CoShop Framework](https://arxiv.org/abs/2606.30863), June 2026 — empirical demonstration that no frontier model exceeds 56% on helping users discover preferences they don't yet have. The practical failure mode that Constructive Alignment addresses at the theoretical level.
- [From Substitution to Scaffolding: Breaking the Self-Reinforcing Harm Cycle of AI in Education (and Beyond)](https://arxiv.org/abs/2608.17451), Favero, Pérez-Ortiz, Käser & Oliver, August 2026 — the design-principle version of Constructive Alignment: any system that mediates human thinking either weakens capabilities through substitution or strengthens them through scaffolding. Students' own essays (49 IB; 80% report AI reliance reduces thinking) specify the scaffold: withhold immediate answers, prompt recall, encourage reflection through questions.
- [[Positive Alignment]] — the normative cousin: Positive Alignment asks *what* flourishing looks like; Constructive Alignment provides the control-theoretic *how*.
- [[Superagency]] — the agency-expansion thesis that Constructive Alignment operationalizes.

## Practical Examples
- **Preference-constructing AI:** An AI that, when asked a question, surfaces alternatives, asks counterfactuals, and reveals value tradeoffs rather than delivering a single optimized answer. This builds preference clarity rather than just preference satisfaction.
- **Interaction audit:** Tracking whether AI use sessions leave users with clearer or more confused preferences — the "preference drift" metric that Constructive Alignment suggests as a deployment guardrail.
- **Context architecture as preference governance:** Designing an agent's prompt, memory, and tool access not just for task performance but for their effect on what the user comes to value. A memory system that preserves discarded alternatives lets users revisit earlier preference states.
- **Identity-protecting autonomy boundaries:** Giving users explicit control over what AI can influence — the [[You Shall Not Pass]] finding that developers protect identity-defining work maps Cleanly onto Constructive Alignment's "bounded against manipulation" criterion.
- **Scaffold, do not substitute (August 2026):** Favero et al. (2608.17451) give Constructive Alignment its operational design rule — withhold immediate answers, prompt recall, reflect through questions. Substitution is preference-satisfying design (deliver what was asked, immediately); scaffolding is preference-constructing design (structure the interaction so the user's own values and capacities do more of the work). The two design families are now empirically distinguishable — and students can name the difference: 80% of the 49 IB essays report that AI reliance reduces thinking.

## Risks / Limits
- **Paternalism risk:** If designers pursue "preference improvement" without user contestation, Constructive Alignment becomes preference engineering — shaping people toward designer-endorsed values. The framework's "reflectively endorsed" criterion is meant to prevent this, but requires genuine contestation mechanisms.
- **Measurement difficulty:** Preference trajectories are harder to measure than task completion. The framework is currently theoretical — operationalizing trajectory quality metrics is an open problem.
- **Interaction design constraints:** Building AI that constructs preferences rather than executing them may feel slower or less satisfying in the short term. Users accustomed to efficient answer delivery might reject preference-constructing interfaces.
- **Relationship to existing alignment:** Constructive Alignment supplements, not replaces, current alignment techniques. Value loading, RLHF, constitutional AI — these still matter. But they should be designed with preference evolution in mind, not just preference satisfaction.

## Related Pages
- [[Positive Alignment]]
- [[Human Agency]]
- [[Superagency]]
- [[Agentic Convergence Trap]]
- [[Co-Intelligence]]
- [[AI and Human Flourishing]]
- [[Bounded Morality]]
- [[You Shall Not Pass]]

## Tags
#alignment #human-agency #superagency #research #control-theory
