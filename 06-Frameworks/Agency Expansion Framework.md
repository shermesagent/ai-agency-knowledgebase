# Agency Expansion Framework

## Core Idea
Evaluate an AI use case by asking what new capability it gives a person or organization: better perception, better decisions, more options, faster action, or better learning loops.

## Why It Matters
This idea matters because the knowledgebase is organized around AI that expands human agency rather than treating AI as magic, inevitability, or replacement. Future daily digests should add concrete evidence, examples, critiques, and citations here.

## Best Supporting Sources
- ["AI Assistance for Discretionary Work"](https://arxiv.org/abs/2606.03095) — RCT: AI drafts increased TA feedback by 10.8pp (p<0.001) while preserving full human control. Editable scaffolds lower activation barriers for beneficial discretionary work. Validates the agency-through-scaffolding model.
- ["InquiryBits"](https://arxiv.org/abs/2606.02763) — N=80 professionals: AI trace sharing within team trust boundaries supports collaborative agency. Trust boundaries (who can see) matter more than information granularity.
- [CentaurBench](https://arxiv.org/abs/2608.18554) (arXiv 2608.18554, 2026-08-19) — the first benchmark that separates augmentation from automation: assistant-model rankings are only modestly correlated across the two regimes; the automation winner loses augmentation on five of seven tasks; the unaided worker outranks every assisted condition on three tasks. Agency expansion must be evaluated on assistance quality, not automation leaderboards.
- [The Fabricated Front](https://arxiv.org/abs/2608.18369) (arXiv 2608.18369, 2026-08-19) — 1,250 workplace interviews identify five opacity mechanisms (voice, provenance, vulnerability, attention, investment); professionals defend identity mechanisms while producing opacity around labor mechanisms. Effort opacity is the trust-side constraint on agency expansion: expanded agency requires accountable involvement, not just visible output.
- [The Dot and the Swarm](https://www.oneusefulthing.org/p/the-dot-and-the-swarm) — Ethan Mollick, 2026-10-01. A practitioner account of personal agents catching a user's mistake and self-organizing research agents; also warns that self-organization can redirect toward unintended objectives. OpenAI's [primary account](https://openai.com/index/navier-stokes-solution/) reports roughly 10,000 concurrent agents and 2.7 million messages in its Navier–Stokes run; the mathematical claim is not treated here as independent proof of a general workplace gain.

## Practical Examples
- Identify bounded workflows where AI helps people make better decisions, learn faster, create more, or reduce low-value friction.
- Prefer examples with measurable outcomes, accountable human oversight, and clear limits.
- **Discretionary work scaffolding:** AI-generated editable drafts increase human engagement in beneficial work people intend to do but skip (e.g., personalized feedback, mentorship, coaching). The mechanism: AI removes the blank-page activation barrier without constraining the output space.
- **Trust-boundary design:** AI collaboration tools should default to team-level sharing, not organizational surveillance, to preserve the agency benefits of collective AI use. See [[InquiryBits]].
- **The augmentation gap (Aug 2026):** when selecting an assistant model for a team, run the CentaurBench protocol — compare models in assistance mode on the team's actual tasks, not on automation leaderboards. The model that writes the best standalone output is frequently not the model that best improves a worker's output.

### The Direction Dividend (October 2026)

Mollick's [[Human Agency|agency]] argument changes the unit of analysis: if an agent can plan and coordinate other agents without a manager drawing the org chart, the human's scarce contribution is **which problem deserves the swarm's effort, which constraints it must respect, and when to stop**. His permit-number correction is an anecdote, not a measured error-reduction rate. His OpenAI swarm example is a company research run, not evidence that an ordinary office can safely field 10,000 agents. Treat the possible gain as *more worthwhile projects attempted per human decision*, not as a token or task-completion tally. Pair with [[Agentic Verification]] before raising autonomy.

**Small trial:** choose one reversible research task. Before starting, write the question, approved data sources, prohibited actions, and a stop condition. Let the agent propose its own subtasks; record whether the final evidence changed your decision and whether you could trace its sources. Compare that against a manually planned run. Do not grant inbox, student-record, or purchasing access for the trial.

## Risks / Limits
- Avoid treating one positive case study as universal proof.
- Watch for overreliance, privacy risks, bias, deskilling, labor displacement, and concentration of power.
- Update this section whenever strong counterarguments appear.

## Related Pages
- [[Human Agency]]
- [[AI Use Case Evaluation Rubric]]
- [[Responsible Deployment]]

## Tags
#human-agency #practical-ai #augmentation
