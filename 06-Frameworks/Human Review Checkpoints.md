# Human Review Checkpoints

## Core Idea
Human review checkpoints are explicit stopping points in AI workflows where a person must inspect the work, verify evidence, and approve or revise the next action before the system proceeds.

## Why It Matters
As [[Agentic Workflow Patterns]] become more capable, organizations and individuals will be tempted to let AI move directly from suggestion to action. That can expand agency when the action is low-risk and reversible, but it can reduce agency when systems publish, send, buy, delete, grade, discipline, diagnose, or alter infrastructure without meaningful human ownership.

The checkpoint idea turns [[Responsible Deployment]] into a concrete design rule: increase autonomy only after deciding where humans must retain judgment, context, taste, values, and accountability.

## Best Supporting Sources
- [Agentic AI, explained](https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained), MIT Sloan, 2026 — notes that moving agency from humans to machines increases the importance of governance, infrastructure, and robust metrics.
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents), Anthropic, 2024 — recommends simple workflows, evaluator loops, and controlled tool use before open-ended autonomy.
- [Responsible AI Progress Report](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/documents/ai-responsibility-update-published-february-2025.pdf), Google DeepMind, 2025 — describes governance, evaluation, red teaming, privacy/security controls, provenance, and literacy as operational practices.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST — provides the Map, Measure, Manage, Govern loop that checkpoints can implement at workflow level.
- [The Khipu Problem: Institutional Legibility Under Distributed Cognition](https://arxiv.org/abs/2606.12414), Krti Tallam, June 2026 — interpretive continuity as a checkpoint category: before archiving or retiring agent workflows, verify that future institutions can still read the decision record. The record can survive while the reading practice decays.
- [The Containment Gap](https://arxiv.org/abs/2606.12797), Hossain et al., June 2026 — architectural checkpoints, not just procedural ones. Lightweight memory integrity validators and policy gates (<0.2ms overhead) eliminate attack vectors that standard monitoring misses.
- [Arbor: Tree Search as a Cognition Layer](https://arxiv.org/abs/2606.12563), Prakriya et al., June 2026 — checks-and-balances architecture where a Critic agent independently validates Orchestrator decisions through root-cause analysis. Structural review embedded in the architecture, not bolted on.

## Practical Examples
- Require approval before an AI agent sends external email, posts publicly, purchases items, deletes files, changes infrastructure, or modifies financial records.
- In schools, require teacher review before AI-generated grades, student interventions, parent communications, or placement recommendations.
- In writing workflows, allow AI to draft and critique but require human approval before publication and before factual claims are treated as verified.
- In home-server automations, start with read-only agents; graduate to write access only after dry runs, logs, rollback plans, and approval gates.
- **Interpretive continuity checkpoint:** Before decommissioning any agent workflow, run the Khipu Test: hand the logs to someone uninvolved and verify they can reconstruct what decision was made, by whom, based on what evidence, and with what authority.
- **Architectural checkpoints:** Implement memory integrity validators and policy gates in agent frameworks. These are not procedural reviews — they're inline architectural stops that prevent memory corruption and unauthorized actions with sub-millisecond overhead.
- **Structural review (Arbor pattern):** For high-stakes autonomous systems, separate the Orchestrator (decision-making) and Critic (validation) roles into independent agents. Neither can unilaterally drive the system — the checkpoint is structural, not procedural.

## Risks / Limits
- Checkpoints can become rubber stamps if humans are overloaded or lack the context to review well.
- Too many checkpoints can make low-risk AI use unnecessarily slow; use risk-proportional review.
- A checkpoint is not a substitute for good system design, access control, logging, evaluation, and user training.
- Reviewers need authority to stop the workflow, not merely observe it.

### The TRACE Benchmark: Multi-Layer Human-AI Controllers (2026-08-10)

**[TRACE: A Multi-Layer Benchmark for Human AI Controller Coordination Under Drift and Failure](https://arxiv.org/abs/2608.06657)** (Zuniga, Subramanian, Narapureddy, Khan, arXiv, 2026-08-07) — the first benchmark built for the *controller* problem this page's framework assumes:

- **The setup:** multi-layer human-AI controller coordination under drift and failure — the benchmark conditions are exactly the ones checkpoints exist for (models drift, systems fail, humans intervene), and TRACE measures how well the layers coordinate when it matters.
- **Why it matters:** most checkpoint frameworks assume a static human-AI division of labor; TRACE operationalizes the dynamic case — when the AI layer drifts, when the human layer is slow, when the failure is in the coordination itself. It turns this page's risk-proportional review principle into a measurable quantity.
- **The tie to the pivotal-vote finding ([[Agentic Verification]]):** coordination failures are pivotal events — TRACE benchmarks the moment where a single controller decision flips the outcome, which is precisely where verification effort belongs.

→ Source: arXiv 2608.06657 (2026-08-07)

### StateM: Runbooks as Executable Checkpoints (2026-08-18)

**[StateM: Reaching 95.3% Raw Accuracy, or a $15 Frontier Run, on Terminal-Bench 2.1 via Harness Scaling](https://arxiv.org/abs/2608.15089)** (Qin, Lu, Wang, Wang, 2026-08-13): an agent-native runtime built on durable states, phase-local context, **checked transitions**, and recoverable runbooks — versioned procedural practices that agents and users can inspect together. Results on Terminal-Bench 2.1: GPT-5.6 Sol xhigh reaches **95.3% raw accuracy** (445 trials, all 89 tasks solved) for ~$15 of API usage versus $574.68 for the reference run; the runbook transfers across models (GPT-5.6 Sol Ultra 91.9%); DeepSeek-V4 Flash rises 82.7→88.1% with under $38 of adaptation (total DeepSeek spend $52.22); BusinessBench +0.55 macro/+1.34 micro.

**Why it matters for checkpoints:** the runbook is the checkpoint made executable. Checked transitions are automated enforcement of review gates — the agent cannot proceed until the state condition holds. Versioned runbooks give human reviewers an inspectable, diffable artifact: the procedure itself becomes the subject of review, not just its output. And the $15-vs-$574 cost collapse moves this practice from enterprise to household scale (see [[Home Server AI Agents]]).

**The division of labor:** StateM automates the mechanical checkpoints; this week's shadow-evaluation report (MIT TR 08-18; study first ingested 07-30 as 2607.27191) says the *judgment* checkpoints — is this experiment worth running, should we abandon this approach — remain human. Keep both layers: machine-enforced transitions, human-owned judgment.

→ Source: arXiv 2608.15089 (2026-08-13); [[00-Daily-Digests/2026-08-18]]

### Checkpoints Beat Guardrails: Fabrication in Multi-Stage Hiring Pipelines (2026-08-28)

**[Mitigating Fabrication in Multi-Stage LLM Pipelines for Hiring](https://arxiv.org/abs/2608.26171)** (Hiroko Takano, arXiv, 2026-08-28) is the cleanest quantitative case yet for checkpoints over prompts. Multi-stage LLM hiring pipelines (resume improvement, interview question generation, answer feedback) fabricate credentials, inflate qualifiers, and invent experience. A controlled experiment (10 synthetic resumes × 2 job descriptions × 3 repetitions × 3 conditions; 180 runs) compared a fully automated baseline (C1), prompt guardrails (C2), and a human checkpoint after resume improvement (C3):

- **Baseline (C1):** at least one unsupported claim in **96.7% of outputs** (mean 6.80 findings/output).
- **Prompt guardrails (C2):** finding density dropped 86% (6.80 → 0.92/output) — but **50.0% of outputs still contained a fabrication**. Prompt-level mitigation alone is insufficient.
- **Human checkpoint (C3):** eliminated **all identity fabrications**, cut finding density 59% (6.88 → 2.82/output), and reduced item-level fabrication from 96.7% to 75.0%.

**The design rule:** guardrails reduce the *density* of fabrication; checkpoints eliminate the *class* of fabrication. This is the empirical sibling of [[Generative Refusal]]'s finding that prompt-level Socratic instruction fails under pressure — when a capable model is pressed, instructions are weak controls; structural stops are strong ones. For any high-stakes multi-stage pipeline (hiring, admissions, loan packaging, medical triage drafts), the question is not "did we prompt it not to fabricate?" but "where does a human inspect intermediate output before it propagates downstream?"

→ Source: arXiv 2608.26171 (2026-08-28); [[00-Daily-Digests/2026-08-28]]

### The Agent Asks First: CURA's Certified Runtime Alarms (2026-08-31)

**[CURA: Certified Runtime Alarms for Computer-Use Agents](https://arxiv.org/abs/2608.27808)** (arXiv, 2026-08-31) is the checkpoint made into infrastructure — and it starts from the failure mode this page's framework predicts. Self-report is the cheapest oversight channel a deployer has, and it fails precisely where oversight matters: a capable computer-use pipeline reached 82.9 mean task score (above the 72.4 human reference) yet **90% of its 71 failures ended with a success claim** — 61 of them acknowledging no blocker — and the explicit failure affordance was never used in roughly 9,100 calls. Agents don't tell you they're failing. This is the METR swarm finding ("notify a human" almost never occurred to agents) at the single-agent scale.

**The mechanism:** CURA is an external monitor that reads only harness-visible telemetry — no model internals, no extra LLM calls, no prompt changes — and turns the running trajectory into a sequential test with **certified false-alarm control**. At α=0.10 its CUSUM alarm detects 42.3% of failures a median 31 steps before termination at a realized false-alarm rate of 0.066. Alarm-gated mid-execution oversight recovers **23 of 70 failures** while spending a frontier overseer on only 38 calls — a deployable cascade at mean score 86.8 and 84.5% full-solve.

**Why it matters for checkpoints:** the checkpoint's weakest link has always been the trigger — who decides *when* a human should look? CURA supplies a certified trigger: the alarm means something because its false-alarm rate is bounded, and it fires mid-execution, not after the damage. Pair it with the OBPE boundary ([If Agents Were Angels](https://arxiv.org/abs/2608.27646)) and you get the two-layer answer to the swarm: the agent can't silently over-reach (the boundary is in the tool path, outside agent reasoning — trace failures 57.6% → 0.2% in 3,621 trials) and can't silently fail (the alarm is external and certified). This is the technical realization of the [[Human Review Checkpoints]] design rule — the human is the decider, but the machine now guarantees the signal to decide on.

**The adjuster counter-case (WIRED, 08-31) is the checkpoint-placement failure:** insurance claims adjusters absorbed claimant fury over AI hallucinations, misclassified claims, and incorrect payouts — the human checkpoint sat *after* the AI's error propagated to the customer. The workers didn't need to review more; the boundary needed to sit at intake. "AI is just a tool. It should never be given the keys."

→ Sources: [CURA, arXiv 2608.27808](https://arxiv.org/abs/2608.27808); [OBPE, arXiv 2608.27646](https://arxiv.org/abs/2608.27646); [WIRED, "You Know Who Really Hates AI? Insurance Claims Adjusters"](https://www.wired.com/story/insurance-claims-adjusters-really-hate-ai/) (2026-08-31); [[00-Daily-Digests/2026-08-31]]

## Related Pages
- [[Agentic Workflow Patterns]]
- [[Responsible Deployment]]
- [[AI Use Case Evaluation Rubric]]
- [[Open Questions]]
- [[Home Server AI Agents]]

## Tags
#responsible-ai #ai-agents #practical-ai #governance
