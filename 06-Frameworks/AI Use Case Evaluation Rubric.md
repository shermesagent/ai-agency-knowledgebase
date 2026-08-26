# AI Use Case Evaluation Rubric

## Core Idea
A rubric for judging AI use cases by agency gain, user need, evidence, risk, privacy, operational fit, human oversight, cost, and learning value.

## Why It Matters
Use-case selection is where responsible optimism becomes operational. A strong AI use case should expand human capability, have a clear user need, be measurable in context, and preserve accountability. Weak use cases create adoption theater: impressive demos, hidden review costs, brittle workflows, and avoidable risk.

## Best Supporting Sources
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST, 2023/2024 — supports risk-proportional mapping, measurement, management, and governance.
- [Impact of Generative AI in Software Development](https://services.google.com/fh/files/misc/dora-impact-of-generative-ai-in-software-development.pdf), Google/DORA, 2025 — emphasizes feedback loops, trust, and outcome measurement during AI adoption.
- [Navigating the Jagged Technological Frontier](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf), Dell’Acqua et al., 2023 — shows why every use case needs task-boundary testing: AI can help inside its frontier and hurt outside it.
- [AI Opportunities Action Plan](https://www.gov.uk/government/publications/ai-opportunities-action-plan/ai-opportunities-action-plan), UK Government, 2025 — frames public-sector AI adoption around opportunity, infrastructure, adoption capacity, and safeguards.

## Practical Examples
- Score candidate use cases on agency gain, measurable outcome, data sensitivity, reversibility, human review burden, and learning value.
- Require a baseline before rollout: how is the task done now, how good is it, and what failure modes already exist?
- Start with low-risk augment tasks before high-consequence automation.
- Write a stop condition: when should the AI workflow pause, escalate, or be turned off?

## Risks / Limits
- A use case can be efficient but agency-reducing if it removes human voice, discretion, learning, or appeal.
- ROI claims are often inflated when review time, integration work, privacy risk, and error handling are ignored.
- The rubric should be updated after each pilot; static checklists decay as tools and workflows change.

## Specify the Instrument (August 2026)

The rubric's measurement dimension has a hidden variable: the instrument itself. Two August papers converge on the same lesson — a verdict is a joint property of the system and the measuring stick:

- **2608.21382 (There Is No Neutral Harness):** twelve open-weight models scored 31–89% depending only on which of 26 equally defensible harness configurations was used; config-fragile items carry 95.7% of adjacent-model score gaps; 4 of 12 models reach rank one under some configuration.
- **2608.23641 (instrument vs model):** holding outcomes and models fixed and varying only the prompt-format instrument, measured model preferences shift with the instrument — 15 welfare outcomes × 8 models × 5 instruments × 5 runs.

**Rubric addition — the Instrument Specification clause:** every evaluation record must state the instrument (harness config, prompt format, evaluation protocol, model version) alongside the score. Two use cases with the same score but different instruments are not comparable; a use case whose pilot "failed" under one instrument may be mis-measured, not deficient. Before comparing evaluations across vendors, teams, or quarters, check the instrument is held fixed — if it isn't, the comparison is noise.

This converts the rubric's "measurable in context" criterion from an aspiration into a protocol: measure, and record how you measured.

→ Sources: [There Is No Neutral Harness](https://arxiv.org/abs/2608.21382), [How much of a measured AI preference is the model, and how much is the instrument?](https://arxiv.org/abs/2608.23641)

## Related Pages
- [[Agency Expansion Framework]]
- [[Responsible Deployment]]
- [[Risk-Benefit Matrix]]
- [[AI Field Experiment Evidence]]
- [[Task-Level AI Adoption]]
- [[The Expression Gap]] — score what a system expresses, not what it claims to encode; unexpressed capability is unverifiable

## Tags
#practical-ai #responsible-ai #tools
