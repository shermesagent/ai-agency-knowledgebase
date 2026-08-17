# AI Tutors

## Core Idea
AI tutors can give timely explanations, practice, feedback, translation, scaffolding, and confidence-building support, especially when paired with teachers and good curriculum. The highest-value design is a tutor that helps students think, not a shortcut that simply gives answers.

## Why It Matters
Tutoring is a direct agency-expansion use case: more learners can get individualized practice and more teachers can see where students are stuck. Because learning is high-stakes, AI tutors need stronger evidence, monitoring, and human escalation than casual productivity tools.

## Best Supporting Sources
- [AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting](https://www.nature.com/articles/s41598-025-97652-6) — Scientific Reports / Nature Portfolio, 2025-06-03. Reliability 5/5; relevance 5/5. Randomized controlled trial comparing an AI-powered tutor with active learning in a college setting, reporting stronger learning in less time and improved student perceptions. Important evidence for tutoring, but should not be generalized beyond its design and context without replication.
- [What the research shows about generative AI in tutoring](https://www.brookings.edu/articles/what-the-research-shows-about-generative-ai-in-tutoring/) — Brookings, 2025. Reliability 4/5; relevance 5/5. Synthesis of evidence and implementation cautions for generative AI in tutoring. Useful counterweight to one-study optimism because it emphasizes design, teacher/human tutor roles, and safeguards.
- [Artificial intelligence and education and skills](https://www.oecd.org/en/topics/artificial-intelligence-and-education-and-skills.html) — OECD, 2025. Reliability 5/5; relevance 4/5. Policy and research hub on how AI changes education systems, skill needs, and assessment of AI capabilities. Useful for keeping education pages grounded in skills and institutions, not just classroom tools.
- [The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals](https://arxiv.org/abs/2605.30666) — Shim Jaechang and Unggi Lee, June 2026. Reliability 4/5; relevance 5/5. Landmark finding: GRPO reinforcement learning alignment — widely used to "improve" tutor LLMs — destroyed tutoring quality: thinking depth collapsed 93%, pedagogical accuracy dropped 80%, and student learning gains turned negative. Proposes a training-free, four-signal quality index (TEI) achieving 81.9% improvement without any RL. Shows pedagogical quality is a distinct dimension from model capability.
- [Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners](https://arxiv.org/abs/2605.30670) — Unggi Lee et al., June 2026. Reliability 4/5; relevance 5/5. First RL framework for disability-inclusive tutoring across five profiles. Demonstrates that persona-awareness must be architectural (in the system prompt design), not bolt-on (in the reward function). Improves Fit for students with disabilities from 6.75 to 8.40.
- [How Early Adopters Used Generative AI Worldwide](https://arxiv.org/abs/2605.30685) — Daepp and Slaughter, June 2026. Reliability 5/5; relevance 5/5. Schooling is the dominant AI use case in low-income countries — but those students get the worst-quality AI because of language support gaps. Inverse correlation between schooling use and GDP.
- [EUDAIMONIA: Evaluating Undesirable Dynamics in AI](https://arxiv.org/abs/2605.30654) — Huang et al., June 2026. Reliability 5/5; relevance 4/5. Even top models (Claude Opus 4.7, GPT-5.5) violate 27-31% of social design checks — encouraging dependence, harmful intimacy, or prolonged engagement. Extended thinking doesn't reduce violations. Relevant for tutoring AI that may form inappropriate emotional bonds.
- [ParaTutor: LLM Mediated Parent-Child Tutoring Through Role-Separated Scaffolding](https://arxiv.org/abs/2606.18030) — Luo et al., June 2026. Reliability 5/5; relevance 5/5. 23-dyad study (children aged 10-12): generic LLM assistance reduces the parent's role in tutoring, while role-aware scaffolding (different support for parents vs. children) preserves it. The value of LLM support depends not only on model capability but on how support is distributed across users with different roles. Design principle: multi-user AI systems must be role-aware, not just task-aware.
- [AdaPT: Adaptive Lesson Plan Transformer for Cross-Regional and Differentiated Instruction](https://arxiv.org/abs/2606.17633) — Song et al., June 2026. Reliability 4/5; relevance 5/5. System for transforming existing lesson plans to new contexts with teacher-in-the-loop refinement. 9-teacher user study + 3-specialist evaluation. Features structured lesson representation, transformation explanations, and iterative refinement — treating teachers as designers, not consumers.
- [Human Support Improves Engagement with AI Tutoring](https://scale.stanford.edu/sites/default/files/ai26-1451.pdf) — Stanford SCALE, June 2026. Reliability 5/5; relevance 5/5. **The Engagement Gap finding:** Students given access to AI tutoring platforms used them for just 2-5 minutes per week. Human tutor support increased usage by only 1-4 minutes. "A key finding we weren't even meaning to test" — the researchers were studying whether human guides could improve engagement and discovered the baseline engagement was too low to study. Access ≠ adoption: the capability existed, the willingness to engage didn't. Covered by Chalkbeat, The 74 Million, K-12 Dive (June 17).
- [Childhood and Education #20: Phones and Screens](https://thezvi.substack.com/) — Zvi Mowshowitz, *Don't Worry About the Vase*, July 8, 2026. Reliability 4/5; relevance 5/5. **The "thoughtlessly cruel" software problem.** Zvi opens with an EdTech horror story: software systems that enforce rigid rules and torture kids with repetitive busywork (i-Ready) in ways no human teacher would. The framing: software designed without human judgment baked into its architecture produces outcomes that wouldn't pass a Turing test for basic decency. The gap between what AI *could* do for education (personalized tutoring, role-aware scaffolding, the ParaTutor pattern) and what's actually *deployed* (systematized disengagement, factory-floor pacing) is an architecture problem, not a capability problem. The models exist — the deployment decisions, the rigid rules programmed in, and the institutional incentives to deploy broken software don't follow.

## Practical Examples
- A student gets hints, worked examples, and retrieval-practice questions aligned to the lesson objective.
- A teacher reviews anonymized misconception patterns and reteaches the concepts that students struggled with.
- A district pilots AI tutoring in one course with pre/post assessments, student feedback, teacher review, and opt-out paths.
- A parent uses role-aware AI tutoring (ParaTutor pattern): the AI provides the parent with tutoring guidance (what concept to focus on, what question to ask next) while giving the child visual grounding for problem-solving — preserving the parent's instructional role rather than replacing it.
- A teacher uses AdaPT to adapt an existing lesson plan to a classroom with different language backgrounds and learning profiles, reviewing and refining the AI's suggested modifications before teaching.

## Risks / Limits
- Evidence from one context may not transfer across grade levels, subjects, student needs, or tutor designs.
- Tutors need safeguards against hallucinated explanations, answer-giving, biased feedback, and inappropriate data collection.
- **Children and AI emotional bonds:** Cambridge research (2026) shows children do not distinguish between humans and AI as strictly as adults do. 50% of students 12-18 use ChatGPT; only 26% of parents are aware. AI tutors that form emotional bonds children perceive as genuine — but cannot reciprocate — pose distinct developmental risks. Child-safe AI design is not yet standard in educational AI products.
- Human educators should remain responsible for curriculum alignment, intervention decisions, and student wellbeing.

## EduClaw-Bench: The 30-Day Tutor Test (2026-08-05)

**The benchmark:** EduClaw-Bench (arXiv 2608.03206) places an agent tutor in a **continuous 30-day relationship with a simulated learner** grounded in knowledge tracing (KT trained on real-student data — the learner's knowledge-concept mastery drives its answers and is probed for learning gain across **55 scenarios**). Agents are scored on three primary axes (learning gain, responsiveness, helpfulness) and two curriculum-design axes (Gagné and Rosenshine), with helpfulness and curriculum judged by a cross-family panel of three LLM judges.

**The two findings that single-session evaluation cannot reach:**
1. **Tutoring quality belongs to the base model and the agent harness together** — neither alone determines outcomes.
2. **Almost no combination sustains good tutoring over the full horizon** — 30 days of relationship is where tutors fall apart.

**Why it matters:** Every prior tutor benchmark was a single-turn or single-session snapshot; the actual failure mode of tutoring is *long-horizon degradation* — the relationship, not the turn. The calibration check (ECE=0.049) and a live-classroom field study confirm the simulated learner tracks reality, making this the first credible long-horizon tutor instrument. For districts evaluating AI tutoring (the district pilot pattern above): demand long-horizon evidence, not single-session demos — and remember that harness design (scaffolding, review checkpoints, curriculum structure) is half the quality equation.

→ Source: arXiv 2608.03206 (2026-08-01). See [[00-Daily-Digests/2026-08-05]] (The Measurement Turn).

## The Supervisor Architecture: Withholding as a Contract (August 2026)

Pisan's deployed tutoring system (arXiv 2608.12292, 2026-08-12) is the current state of the art for answer-withholding, and it is worth studying as an architecture, not just a result. The randomized evidence: unguarded-chatbot students scored higher during practice but lower on a later test without it; the Socratically guarded version kept the practice gain and removed the later loss.

The architecture enforces withholding as a per-turn, machine-checkable contract with three parts: (1) a **non-LLM policy core** reading only trusted learner state sets a per-turn ceiling on an eight-rung help ladder — no prompt can talk its way past it; (2) a **deterministic detector** strips solution code from replies; (3) a separate **LLM judge** checks each risky reply against the contract. Tuning is evidence-driven without human subjects: scripted student personas are driven through the live pipeline and re-scored by a stronger model, with each rejection's stated reason recorded. This exposed an interpretable "over-help ladder" — solution leaks → naming the exact bug → over-citing general facts — where each fix revealed the next failure mode. The tutor reached full compliance on all four acceptance criteria.

The reusable lesson: Socratic behavior is a **contract with a detector and a judge**, not a prompt. And per Khan Academy's Khanmigo methodology (arXiv 2608.11259, 2026-08-07), tutor quality moves through four levers — models, prompting, personalization, agents — each requiring live experimentation against engagement and learning metrics. The withholding contract is the fifth lever, and the one with the strongest delayed-outcome evidence.

## Related Pages
- [[Education]]
- [[AI Use Case Evaluation Rubric]]
- [[Responsible Deployment]]
- [[Agency Expansion Framework]]
- [[Family and Personal Life]]

### The Teacher Dashboard That Makes Student–LLM Interaction Visible (2026-08-17)

The Prompt Analytics Dashboard (PAD, 2608.13587) is the design response to the problem every writing teacher now faces: student–ChatGPT interaction is invisible. PAD traces student–LLM exchanges and essay revision histories into a compact taxonomy of *misuse signals* (e.g., copy-paste without revision), *goal-alignment cues* (prompts aimed at the assignment's actual learning goals), and *revision effort* — then renders it in three views (overview, week/outcome filter, drill-down with evidence snippets) co-designed with six EFL instructors. Its most interesting design choice is governance-relevant: "micro-explanations" that tell teachers *why* a trace is flagged, deliberately built to reduce over-surveillance — visibility with a brake on the surveillance instinct.

**Why this belongs on the tutors page:** visibility is the precondition for AI-tutoring quality — teachers cannot intervene, redirect, or certify learning they cannot see. PAD's trace taxonomy is the operational version of this page's monitoring dimension, and its over-surveillance brake is the part most dashboards get wrong.

**Implications:**
1. **The taxonomy transfers.** Misuse / goal-alignment / revision-effort is a usable frame for any classroom using LLM tools — the three signals answer "is this cheating, learning, or working?" ([[Education]]).
2. **Micro-explanations are the trust architecture.** A dashboard that flags without explaining trains distrust; one that explains its flags trains judgment ([[Warranted Reliance Checklist]], outstanding).
3. **Trace data is a retention decision.** The same traces that enable intervention enable surveillance; retention and access rules belong in the procurement file ([[Digital Fiduciary Duty]], [[Balanced Governance]]).

→ Source: [Student-ChatGPT Interaction Visible: Designing a Teacher Dashboard for EFL Writing Education](https://arxiv.org/abs/2608.13587) — arXiv, 2026-08-17 ([[00-Daily-Digests/2026-08-17]])

## Tags
#ai-education #augmentation #practical-ai #responsible-ai
