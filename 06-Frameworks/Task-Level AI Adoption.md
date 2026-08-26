# Task-Level AI Adoption

## Core Idea
Task-level AI adoption means evaluating AI one task at a time instead of asking whether an entire job, course, department, or institution should “use AI.” The practical question is: should this task be automated, augmented, human-only, or prohibited for AI?

## Why It Matters
This framework keeps [[Superagency]] grounded. It avoids both blanket hype and blanket bans by matching AI use to risk, evidence, human value, and accountability.

## Best Supporting Sources
- [The Anthropic Economic Index](https://www.anthropic.com/economic-index) — useful task-level data on collaboration versus delegation patterns.
- [Future of Work with AI Agents](https://futureofwork.saltlab.stanford.edu/) — audits automation and augmentation potential across work tasks.
- [[The Turing Trap]] — warns that substitution and augmentation have different social consequences.
- ["How People Are Really Using AI in 2026"](https://hbr.org/2026/06/how-people-are-really-using-ai-in-2026), Zao-Sanders / HBR, June 2026 — third annual survey: widening range of real-world AI uses; shifts in emphasis rather than stark ruptures; growing anxiety about cognitive surrender. Corporate-specific top-25 use cases added.
- ["AI Assistance for Discretionary Work"](https://arxiv.org/abs/2606.03095), Mahinpei et al., 2026 — RCT: AI drafts increased feedback by 10.8pp. Editable scaffolding as task-level augmentation design pattern.

## Practical Examples
Use four labels during workflow review:
1. **Automate:** low-risk, repetitive, easily checked tasks.
2. **Augment:** tasks where AI drafts, retrieves, critiques, or suggests while a human owns judgment.
3. **Human-only:** tasks where relationship, values, embodied context, or legitimacy are central.
4. **Prohibit AI:** tasks where privacy, safety, law, or dignity make delegation inappropriate.

### Infrastructure Readiness: The Task-Level Agent Gap (July 2026)

A new controlled experiment (arXiv 2607.12056, July 2026) reveals that task-level adoption depends on infrastructure, not just AI capability. Three browser-agent models ran 300 trials on identical website prototypes:

- **Agent-ready websites:** 89.3% strict success rate, 6.49 average steps
- **Human-only websites:** 49.3% strict success rate, 9.31 average steps

The gap is not about AI capability — it's about whether the digital environment is **legible** to the agent. The same agent, same task, same products — only the website's design changed, and success rates nearly doubled.

**Practical implication:** Add a fifth dimension to the task-level classification framework: **infrastructure readiness.** Before labeling a task as "automate" or "augment," ask: does the digital environment support agent access? A task that is technically automatable may fail in practice because the website, API, database, or platform was designed for human interaction only.

**The four agent-readiness audit questions:**
1. Can the agent programmatically discover what it needs (product details, form fields, available actions)?
2. Can the agent reliably navigate multi-step workflows without hitting CAPTCHAs, client-side rendering blocks, or rate limits?
3. Can the agent complete and submit structured transactions (forms, orders, applications)?
4. Does the platform distinguish between "malicious bot" and "user-delegated agent" — or block both indiscriminately?

This connects to the Agent-Ready Websites finding (see [[AI Agent Revolution#Designing Agent-Ready Websites|Designing Agent-Ready Websites]]), the Agent-First Web design principles, and the normative infrastructure gap identified in the agentic web literature. The task-level adoption framework must account for an environment that was not built for the agents now trying to operate within it.

→ Also see: [[AI Agent Revolution]] for the Least Autonomy framework (access control for agentic systems), the Agent Economy Insurance Stack (economic governance), and the Theory of Least Autonomy (security architecture).

### Economic Readiness: When AI Can Do the Task But Shouldn't (July 2026)

The EconEvals framework (arXiv 2607.19375, July 2026) adds a sixth dimension to task-level classification: **economic readiness.** A task can be technically feasible, infrastructure-ready, and user-engaged — and still fail economically. The framework introduces **cost-adjusted performance** — comparing AI output quality against market rates for equivalent human labor — and identifies "economic thresholds" where AI crosses from interesting demo to economically viable substitute.

The economic readiness dimension asks three questions:
1. **Cost-adjusted quality:** At current AI API costs, does the output quality justify deployment relative to the market rate for equivalent human labor?
2. **Reliability premium:** What is the cost of AI errors (human correction time, reputation damage, downstream failures) relative to the cost of human errors for the same task?
3. **Market displacement risk:** If this task is automated/augmented, what happens to the human labor market for this task category? Are there systemic effects (wage compression, skill atrophy, entry-level pathway collapse) that the per-task analysis misses?

**Practical implication:** A task that passes the first five dimensions (automation-appropriate, infrastructure-ready, engagement-verified, technically feasible, risk-acceptable) but fails economic readiness should be classified as "augment" rather than "automate." The economic dimension catches cases where AI CAN do the task but the deployment doesn't justify its costs — the inverse of the engagement barrier, which catches cases where the task is appropriate but no one uses it.

This connects to the [[Future of Work#The Exchange Layer|Exchange Layer]] — the economic dimension completes the task-level framework by asking not just "can AI do this?" and "should AI do this?" but "does AI doing this produce net economic value?"

→ Source: https://arxiv.org/abs/2607.19375

### Economic Readiness Data: MirrorCode (August 2026)

The MirrorCode benchmark (Epoch/METR, July 2026) provides the first cost-adjusted frontier data for agentic coding at realistic repository scale: 22 programs plus scaffold, 132 task instances, 6 languages, drawn from real GitHub repos (examples pkl at 61k LOC, gotree at 16k, qsv_select at 87k).

**Results:**
- **One model (Opus 4.7) solved a task in 14 hours for $251** — vs. an estimated **2–17 human weeks** for the same work
- 17 of 25 targets had at least one perfect run; 4 of 25 near-perfect (≥99%)
- 8 of 25 never solved to 100%; 4 of 25 never even to 99%
- Hardest tasks: `ruff` (Python linter), `giac_subset`, `mailauth`

**What this does to task classification:** For a meaningful slice of real-world coding tasks, agentic AI is now 5–20× cheaper and 100–500× faster than human labor on a per-task basis — while still failing completely on roughly a third of targets. MirrorCode moves the economic-readiness question from "can agents do this?" to "which tasks, at what reliability threshold, under what supervision?" Tasks that pass economic readiness on cost-adjusted performance (large, well-specified, verifiable code changes) now default to "automate — with review," while tasks in the 8/25 failure bucket (linters, legacy toolchains, niche ecosystems) stay "augment" until reliability improves. The 14h/$251 number is the benchmark anchor for the whole category shift: it converts the economic threshold from theory to measurement.

→ Source: [Import AI 466](https://importai.substack.com/p/import-ai-466) (2026-07-27), MirrorCode benchmark coverage

### The Engagement Barrier, Named at Consumer Scale (August 2026)

The June SCALE finding (students used AI tutors 2–5 min/week) showed the engagement barrier inside institutions. In August it was named at consumer scale: Josh Miller (The Browser Company CEO) went viral — and stood by it — for saying "nobody is really using AI Agents… the general public dgaf": "I just have not heard a single person outside of the tech community talk about an agent that they use" (WIRED, 2026-08-06).

**What this adds to the framework:** the engagement dimension already built into task-level classification (per the economic-readiness subsection above, a task must be "user-engaged") now has consumer-scale evidence that engagement failure is the default, not the exception. Two refinements:

1. **Engagement must be verified, not assumed — outside the organization too.** SCALE showed signups ≠ use inside schools; Miller shows demos ≠ adoption in the market. The audit question for any "automate" or "augment" classification: has anyone outside the building used this for a week?
2. **Engagement is a design property, not a user defect.** Miller's own conclusion is that the products don't fit — build what regular consumers want, not what models can do. The engagement dimension therefore belongs upstream of task classification: fit the tool to the task the user already does.

**Counterpoint, fairly stated:** Miller's evidence is anecdotal (his own circle); adoption counters — WIRED's own Meetily piece, the vendor "from asking to doing" cases — show normal people do use AI where it removes friction. The honest version of the finding: engagement is the binding constraint at consumer scale, and product fit is the lever.

→ Source: https://www.wired.com/story/why-normal-people-arent-using-ai-agents/

## Organization-Scale Evidence: Telemetry, Ladders, and Decision Points (August 2026)

Three papers this week moved the task-level picture from case studies to organization-scale measurement.

**Enterprise telemetry (2608.12236, Chatterji, Holtz, Rakholia, Tambe & Weeratunga, 2026-08-12).** Linking ChatGPT Enterprise records to usage, roles, tasks, and financials through March 2026 — 1,500+ organizations, 17M+ messages at the six-month horizon — yields four facts: (1) adoption grew rapidly; (2) it concentrated in larger, R&D-/SG&A-intensive firms; (3) it spread across functions and seniority, with the *highest intensity among early-career workers*; (4) it spans a wide knowledge-work task range — writing, technical, communication, synthesis. The early-career concentration is the one to watch: the people forming their task repertoire inside AI assistance are the ones whose expertise formation is most exposed (cf. 2608.11512 on [[AI and Inequality|junior-task automation]]).

**Technology ladders (2608.11626, Schubert, 2026-08-12).** An instrumented account of how organizational capabilities transfer: a 10pp rise in remote hiring (2021–22) predicted +0.4pp firm-level and +0.7pp occupation-level generative-AI adoption (2023–24); RTO-mandate firms show a larger genAI response. Remote-work infrastructure operated as a ladder rung to AI adoption — organizational practices stack.

**Decision-point autonomy (2608.11241, Ao, Fang & Xu, 2026-07-31).** RecSys Factory ran 78 days across three Tencent recommender business lines on the principle "autonomy at decision points, not over pipelines," discharging an autonomy-determinism-efficiency trilemma: capability confined to a 29-file skill ecosystem (8,971 lines of SKILL.md) whose pitfall tables compile into a 400-entry PitfallStore; zero CPU consumed during the 94% of wall-clock spent waiting on Spark/GPU jobs (no long-running daemon). Onboarding-time compression appeared on two of three lines — reported as case-study observation, not generalization. The task-level lesson: bounding autonomy is what made delegation safe enough to run at scale.

### Adoption Telemetry: Measuring Adoption from Production Signals (August 2026)

Adoption Telemetry (Young, arXiv 2608.23617) adds the measurement layer the task-level framework has been missing: a method for computing change-management stage-progression directly from production usage signals. The contribution is threefold: (1) a framework unifying pre-deployment evaluation gates, production telemetry, and change-management staging into one instrumented system; (2) **NANTE** — a five-stage operationalization with defined telemetry thresholds *published openly so they can be tested and disproven*; (3) an open-source reference implementation that distinguishes a healthy cohort from five characteristic adoption-failure modes on synthetic populations with known ground truth.

**What this adds to task-level classification:** the engagement dimension (SCALE, Miller — "engagement must be verified, not assumed") has been measured by surveys and anecdotes; adoption telemetry makes it continuous and auditable. The five failure modes give organizations names for what the existing telemetry (2608.12236, enterprise ChatGPT records) only showed in aggregate: adoption that looks like usage but is stage-stuck — pilot-only, one-team, reinvention, churn, and nominal-use patterns.

**The honest caveat, stated by the author:** the thresholds are proposed constructs requiring empirical validation against real outcomes, not a calibrated model. The paper is a measurement scaffold, not a verdict. Task-level classification should treat NANTE stages as a diagnostic vocabulary while the thresholds are still being validated — and record which thresholds were used, so the instrument itself can be audited (cf. the no-neutral-harness finding on [[The Judge Problem]]).

→ Source: [Adoption Telemetry](https://arxiv.org/abs/2608.23617)

## Risks / Limits
- Task labels can drift; revisit them as tools, data, and stakes change.
- A low-risk task can become high-risk when connected to sensitive data or consequential decisions.
- Workers and users should be involved in the classification, not merely managed by it.
- **The engagement barrier (June 2026):** Task-level classification assumes people will use the AI if the task is appropriate. Stanford SCALE research (June 2026) found this assumption is wrong — students given access to AI tutors used them for just 2-5 minutes per week. The engagement gap is a distinct barrier from the technical, organizational, and trust barriers already in the framework. A task can be clearly appropriate for augmentation and still generate zero benefit if nobody uses the tool. The practical response: task-level adoption frameworks must add an engagement dimension — before classifying a task as "augment" or "automate," verify that the intended users actually want to use the AI for that task.

## Related Pages
- [[Work]]
- [[AI Use Case Evaluation Rubric]]
- [[Risk-Benefit Matrix]]
- [[Responsible Deployment]]

## Tags
#practical-ai #future-of-work #ai-agents #responsible-ai
