# AI Field Experiment Evidence

## Core Idea
AI field experiment evidence is empirical research that tests AI tools in realistic work or learning settings, measuring changes in quality, speed, learning, teamwork, or decision-making rather than relying only on benchmarks or anecdotes.

## Why It Matters
A Superagency-style knowledgebase needs optimism that can survive measurement. Field experiments such as customer-support AI, consultant tasks, team product work, tutoring pilots, and software-development studies help separate genuine agency expansion from novelty effects, hype, and vendor claims. They also reveal the jagged frontier: AI can help dramatically on some tasks while hurting performance on others.

## Best Supporting Sources
- [Generative AI at Work](https://www.nber.org/papers/w31161), Brynjolfsson, Li, and Raymond, NBER, 2023 — studies AI assistance in customer support and finds larger gains for less-experienced workers, suggesting democratization of tacit expertise.
- [Navigating the Jagged Technological Frontier](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf), Dell’Acqua et al., 2023 — shows large gains for consultants inside the AI frontier and worse performance outside it.
- [The Cybernetic Teammate](https://www.nber.org/papers/w33641), Dell’Acqua et al., NBER, 2025 — examines generative AI in team settings and expertise formation.
- [AI tutoring outperforms in-class active learning](https://www.nature.com/articles/s41598-025-97652-6), Scientific Reports, 2025 — randomized education study showing tutoring gains in one authentic setting.
- [Impact of Generative AI in Software Development](https://services.google.com/fh/files/misc/dora-impact-of-generative-ai-in-software-development.pdf), Google/DORA, 2025 — emphasizes feedback loops, trust, and measuring software-delivery outcomes rather than assuming AI improves everything.

## Practical Examples
- Before expanding an AI pilot, define baseline quality, time, satisfaction, learning, error, and review metrics.
- Segment outcomes by novice/expert users, task type, and risk level; averages can hide who gains and who loses.
- Treat negative or null results as design information: redesign prompts, training, workflow boundaries, or escalation paths.

## Risks / Limits
- Field studies can be context-specific; do not generalize across domains without replication.
- Short-term productivity gains may mask long-term deskilling, overreliance, or hidden review costs.
- Sponsored or vendor-adjacent studies need extra attention to methods, incentives, and measured outcomes.

## The Shadow Evaluation (2026-08-05)

**The experiment:** A consortium (Princeton, Cornflower Labs, UK AI Security Institute, Toronto, UC Berkeley, Georgetown CSET, Johns Hopkins, Golden Gate Institute for AI, AI Digest, Stanford) ran Claude Opus 4.8 in an OpenClaw harness against **two unpublished NeurIPS 2026 submissions** — a shadow evaluation: can a frontier agent do the research, as opposed to the engineering?

**The result:** Personas paper scored **2 ("Reject")**; TabPFN paper scored **1 ("Strong Reject")**. Jack Clark's reading of the failure mode: the agent **committed to narrow research paths early, ignored synthetic feedback, and could not reverse out of unpromising approaches** — "good engineers, poor researchers." The result rhymes with earlier Anthropic shadow evals and Import AI's own "First Proof" (#445) and RSI (#455) threads: "the singularity could be delayed" — unverifiable research craft, not formalizable capability, is the frontier bottleneck.

**Why it's a field experiment:** This is field-experiment methodology applied to *agent capability* rather than human outcomes: real (unpublished) task materials, an instrumented harness, blinded evaluation, and an institutional consortium to make the measurement repeatable. The design lesson for AI field experiments: **evaluate the agent on the task class you actually care about (creative research), not the benchmark that exists.** The finding also validates the wiki's existing negative-result discipline: null results are design information — here, they locate taste, problem selection, and reversal-of-commitment as the human comparative advantage.

→ Source: Import AI 467 (Jack Clark, 2026-08-03). See [[00-Daily-Digests/2026-08-05]] (Good Engineers, Poor Researchers) and [[Pacing the Frontier]].

## Related Pages
- [[Agency Expansion Framework]]
- [[AI Use Case Evaluation Rubric]]
- [[Work]]
- [[Education]]
- [[AI Tutors]]

## Tags
#research #practical-ai #augmentation #responsible-ai
