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

## Sim-to-Real Validation Gate (2026-09-23)

[A held-out Upworthy headline A/B-test study](https://arxiv.org/abs/2609.25010) compared a ten-persona LLM panel with a plain no-persona LLM prediction on **399 tests with distinguishable outcomes**. The no-persona baseline did better at ranking variants (Kendall tau 0.361 versus 0.084; top-choice accuracy 49.2% versus 34.6%). It is a preprint about aggregate headline clicks, not a verdict on all persona research or individual preference prediction.

**Add to the rubric:** before buying synthetic-persona or AI-simulation tools, name the real-world outcome, retain a no-persona baseline, preregister a held-out test, and report uncertainty and evaluation-set exclusions. If the elaborate simulation cannot beat the simple baseline on actual behavior, do not use its vivid explanations to stand in for evidence. For creative workflows, pair this with [[Creativity]]'s narrative-ownership check and [[AI Field Experiment Evidence]]'s insistence on observed outcomes.

## Outcome Ownership and Parallelism Gates (2026-10-06)

[Didion, Garaialde and Coyle](https://arxiv.org/abs/2610.03722) report two experiments distinguishing the *feeling* of controlling a computer's immediate action from judgments of responsibility for its later outcome. Their abstract reports no pre-reflective sense of agency over the final effect, even where participants judged they caused a meaningful outcome after a specific instruction. Add to the rubric: identify the person accountable for the final effect, show the sequence from command to consequence, and provide time and means to review or stop before externally visible effects. This is a design implication, not a measured safety improvement for deployed agents; pair with [[Human Review Checkpoints]].

[Jack Clark's Import AI 475](https://importai.substack.com/p/import-ai-475-swarm-scaling-google) summarizes Toby Ord's swarm-scaling analysis: parallel agents can trade higher total token use for lower elapsed time, with coordination costs. Before approving a swarm use case, compare **same-task** elapsed time, total tokens/cost, review time, error duplication and quality against one agent. Do not book a theoretical wall-clock gain as a measured productivity gain. **Why this matters:** a fast workflow that obscures responsibility or consumes more review than it saves is not automatically agency-expanding. See [[The Participation Problem]] and [[00-Daily-Digests/2026-10-06]].

## Whose success does the benchmark measure? (2026-10-15)

[Whose Data, Whose Benchmark?](https://arxiv.org/abs/2610.19268) audits 16 evaluation resources. Its abstract reports that all 16 documented source-user context but none operationalized the intended *target user's* context. In paired scoring experiments, meaning-preserving answer variants changed DROP exact-match accuracy from 100.0% to 33.3% under the tested setup. Those are findings about the studied resources and scoring examples, not a universal drop in model capability.

**Rubric amendment:** name both the people who supplied the benchmark's content and the people the deployment is supposed to serve. Before treating a vendor score as fit-for-purpose, run a small, consented local set of equivalent answers and contexts, with human review for meaning rather than exact string alone. Record the benchmark version, scoring rule, subgroup/context coverage and failures. In schools, do not upload identifiable student responses to a vendor benchmark as a shortcut; use approved, de-identified or purpose-built test items with privacy review. Cross-check [[AI and Inequality]] and [[AI Field Experiment Evidence]].

## Count Escaped Defects, Not Just Minutes (2026-10-28)

[Lijo's preprint](https://arxiv.org/abs/2610.35942) argues that the stopwatch alone misprices AI assistance. Its ledger pairs *time saved* with *excess escaped defects* and asks what defect cost would erase a claimed saving. Reanalysis of public METR developer-study data yields a reported slowdown of 19% or 24% depending on the estimand (34% without adjustment for a chance imbalance). In a small prespecified AI-reviewer experiment on SEC-filing briefs, telling the reviewer that the AI drafter made tenfold fewer errors led it to check seven fewer of nine figures and let a wrong figure through in 22.5% of briefs versus none in the comparison described in the abstract. These are the paper's reported results, not a universal rate for human reviewers or school workflows.

**Rubric amendment:** log drafting, review, correction and post-release repair time separately. Predefine consequential error types, review a blinded sample against source material, and compute the *break-even defect cost* for each workflow. If errors can affect student placement, author reputation or public decisions, do not trade quality for seconds saved. The Macmillan staff accounts in [WIRED](https://www.wired.com/story/macmillan-staff-say-the-publisher-threw-a-party-for-a-workplace-ai-assistant-that-was-later-killed/) are a reason to run this test, not themselves a time-savings estimate. See [[Work]] and [[AI Field Experiment Evidence]].

## Related Pages
- [[Agency Expansion Framework]]
- [[Responsible Deployment]]
- [[Risk-Benefit Matrix]]
- [[AI Field Experiment Evidence]]
- [[Task-Level AI Adoption]]
- [[The Expression Gap]] — score what a system expresses, not what it claims to encode; unexpressed capability is unverifiable

## Tags
#practical-ai #responsible-ai #tools
