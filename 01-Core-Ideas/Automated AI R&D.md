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
