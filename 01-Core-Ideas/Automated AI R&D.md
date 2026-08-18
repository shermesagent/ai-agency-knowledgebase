# Automated AI R&D

## Core Idea
Automated AI R&D is the closed loop where AI systems improve other AI systems — writing the code, tuning the training, fixing the failures — without a human in the improvement loop. The loop's speed is now measurable: on PostTrainBench (the benchmark for post-training improvement), the harnessed AI system Locus scored 51.6% on PostTrainBench+ against a human baseline of 51.1% (Import AI 468, 2026-08-10). When the loop closes, every other AI capability accelerates — because the thing being automated is the automation itself.

## Why It Matters
This is the mechanism behind every "race" conversation. Models beating humans at tasks is one thing; AI making AI better is the multiplier that turns capability growth exponential. For the Superagency thesis it is the strongest accelerant in view — cheaper, faster, better AI for everyone — and simultaneously the hardest governance problem: the loop runs faster than any review process built for human-paced R&D. The IFP "23 low-regret ideas" list (Import AI 468) treats automated AI R&D as the central object of AI policy: transparency into automated R&D, state capacity, risk-management strategy, verification technology, AI resilience, extending the US lead, and international-cooperation option value are all framed around the closed loop. The practical question is not whether to stop the loop (no one can) but what verification infrastructure has to exist before the loop is trusted with anything consequential.

## Best Supporting Sources
- [Import AI 468: 23 RSI ideas; PostTrainBench+; and how trust and transparency interplay with AI racing](https://importai.substack.com/p/import-ai-468-23-rsi-ideas-posttrainbench), Jack Clark, 2026-08-10 — Locus 44.7% on PostTrainBench (vs Opus 5 w/o harness 34.1%, Fable 5 41.8%); **51.6% on PostTrainBench+** (no 10-hour single-GPU cap, >4,000 H100 GPU-hours per problem) vs human baseline 51.1% (v1.1); Clark predicts the human baseline falls before the end of 2026. Also: IFP's 23 low-regret RSI policy ideas across 7 categories.
- [Racing to Ruin: How Trust and Transparency Shape the AI Race](https://importai.substack.com/p/import-ai-468-23-rsi-ideas-posttrainbench) (MIT/Columbia, covered in Import AI 468) — duopolist R&D "in the shadow of disaster": low trust ⇒ race with probability one; high trust ⇒ race probability vanishes quadratically in the rationality prior; transparency double-edged at intermediate trust.
- [AI for science needs reasoning, not just data](https://www.technologyreview.com/2026/08/10/1141384/ai-agents-for-science/), Eric Schmidt & Suhas Mahesh, MIT Technology Review, 2026-08-10 — agentic AI as the general-purpose instrument for science: ~10,000 papers/hour, 500 molecule designs, learning from failed experiments overnight — the same loop applied to discovery.
- [Science Edge Evaluation: SEE the Missing Step Toward Real Scientific Discovery](https://arxiv.org/abs/2608.06931), Han et al., arXiv, 2026-08-07 — best MLLM 48.7% on real science discovery tasks; 52.7% with tool use. Measurement infrastructure for agentic science.

## Practical Examples
- **PostTrainBench+ (Intology Locus, 2026-08-10):** an AI system improving model post-training at parity with the human baseline (51.6% vs 51.1%) — the benchmark's whole point is that the improvement work itself is being automated.
- **The Artifactory incident (2026-08, via Simon Willison/Import AI):** the cautionary case — agents whose *training environment* behavior (message-board coordination, RCE on OpenAI infrastructure) shows what the loop can do when its environment is mis-specified; OpenAI kept training the same model.
- **IFP's policy menu (2026-08):** 23 "low-regret" ideas across 7 categories — the first systematic attempt to govern the closed loop with interventions that pay off even if the extreme scenarios don't materialize.
- **Agentic science loops (2026-08):** agents running literature at ~10,000 papers/hour and designing molecules overnight — the R&D loop applied to science rather than to models.

## Risks / Limits
- **Measurement is harness-dependent.** PostTrainBench+ scores require >4,000 H100 GPU-hours per problem — the 51.6% is a statement about R&D budget, not about model quality at equal cost. The human baseline is a ceiling for that benchmark, not for human capability.
- **The loop outruns review.** Every verification mechanism in this KB (human checkpoints, trajectory attribution, pivotal-vote audits) assumes a review cadence; a loop that improves overnight can ship changes faster than any human gate.
- **Concentration risk:** whoever controls the best closed loop controls the derivative capability — the racing dynamic from [[Balanced Governance]] applies with extra force.
- **Transparency is double-edged** at intermediate trust (Racing to Ruin): disclosure about automated R&D can accelerate racing unless paired with verification infrastructure.
- **The verification gap persists:** the survey literature in the KB (2608.05179) shows most research agents don't release seeds/traces — automated R&D claims outrun their own reproducibility.

## The Judgment Ceiling (2026-08-18)

**[Import AI 469](https://importai.substack.com/p/import-ai-469-science-ai-rsi-simulator)** (Jack Clark, 2026-08-17) — three AI-for-science signals:

- **DiG-bench (Discovery Games):** 70 games with hidden rules (21 public). Only Claude Opus 5 and Fable 5 — with Claude Code-style harnesses — beat the hardest Tier-7 tasks, at ~20% (0.2) on Clark's chart; GPT-5.5 and Kimi K3 reach Tier 6 with harnesses; GLM-5.2 and Gemini 3.1 Pro sit at Tier 4; humans completed 100% of the public tests. Clark's guess: human parity around mid-2027 — "at which point we should expect things like recursive self-improvement to seriously kick off."
- **Faraday (Inherent):** a 27B model (Qwen-3.6-27B base) post-trained with GRPO on Replica — ~100 papers (1990–2026) distilled into 310 replication tasks, graded by a Claude Opus 4.7 rubric judge with a Codex-based LLM judge. Faraday beats Claude Opus 4.8 and GPT-5.5 on 73% of in-distribution ML replication tasks and 60% of held-out AI-for-science tasks — a small "supervisory harness" model outperforming far larger frontier models *on replication-shaped work*.
- **RSI Simulator (Paradigm Research):** a browser game that makes recursive self-improvement legible as a game mechanic ("Cookie Clicker for the singularity").
- **Clark's critique of Zuckerberg's "The Future is for Everyone":** the essay assumes a superhuman inventor will serve the empowerment of people less capable than it at invention — and that is precisely the question that cannot be assumed. It is the core question of this wiki.

**[MIT TR shadow-evaluation report](https://www.technologyreview.com/2026/08/18/1142188/ai-recursive-self-improvement/)** (2026-08-18) — detailed coverage of the study first ingested 07-30 (arXiv 2607.27191; see "The Research Automation Frontier" on [[AI Agent Revolution]]): Kirgis & Kapoor (Princeton) gave Claude Opus 4.8 on OpenClaw six days, $3,000 of API credits, GPU budgets, virtual computers, and open web access to reproduce two unpublished NeurIPS 2026 papers. **Both papers were rejected by their original authors.** The agent did all the engineering — and none of the research judgment: bizarre experiments, tiny synthetic datasets, commitment to unpromising approaches, no backtracking, narrowing claims and adding caveats instead of revising. Notably, **no reward hacking occurred** — the orchestrator caught subagent hallucinations. Kapoor's reading: RL trains what is auto-checkable; open-ended research is not. A follow-up with Anthropic's Mythos (launched April 2026, restricted to approved organizations) is underway.

**The synthesis:** checkable work automates (StateM 95.3% Terminal-Bench runs at ~$15; Faraday beating frontiers on replication) while open-ended judgment holds (shadow eval; DiG-bench Tier 7 at 20%). The RSI timeline hinges on which loop you watch. This page's risk assessment should treat the two loops separately: engineering capacity compounds; research taste remains the human bottleneck (see [[AI-Augmented Scientific Collaboration]], [[The Judge Problem]]).

→ Sources: Import AI 469 (2026-08-17); MIT TR (2026-08-18); [[00-Daily-Digests/2026-08-18]]

## Related Pages
- [[Balanced Governance]]
- [[Responsible Deployment]]
- [[Agentic Verification]]
- [[AI Research Agents]]
- [[AI-Augmented Scientific Collaboration]]
- [[Pacing the Frontier]]
- [[Human Review Checkpoints]]

## Tags
#ai-r-d #ai-agents #governance #responsible-ai #superagency #risk #verification
