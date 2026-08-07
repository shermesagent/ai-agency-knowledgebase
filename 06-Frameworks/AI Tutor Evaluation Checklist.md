# AI Tutor Evaluation Checklist

## Core Idea
An AI tutor evaluation checklist helps schools and educators decide whether a tutoring tool actually supports learning, protects students, and fits instructional goals before procurement or classroom rollout.

## Why It Matters
[[AI Tutors]] are a promising agency-expansion use case, but education requires more caution than casual productivity tools. A tutor can expand feedback and practice, but it can also give wrong explanations, collect sensitive data, or train students to outsource thinking.

## Best Supporting Sources
- [Artificial Intelligence and the Future of Teaching and Learning](https://www.ed.gov/sites/ed/files/documents/ai-report/ai-report.pdf), U.S. Department of Education, 2023 — emphasizes teacher judgment, equity, privacy, and instructional goals.
- [Brave New Words](https://www.penguinrandomhouse.com/books/740806/brave-new-words-by-salman-khan/), Salman Khan, 2024 — optimistic practitioner case for AI tutoring.
- [The Tutoring Effectiveness Index](https://arxiv.org/abs/2605.30666), Shim and Lee, June 2026 — four-signal evaluation (keyword ratio, step density, question rate, reasoning depth) that achieves 81.9% accuracy without training. Demonstrates that standard RL alignment can destroy tutoring quality.
- [Special-R1: RL for Special Education](https://arxiv.org/abs/2605.30670), Lee et al., June 2026 — disability-inclusive design must be structural, not bolt-on. Five disability profiles with persona-aware prompting and Thinking Rewards.
- [EUDAIMONIA: Social AI Design Code](https://arxiv.org/abs/2605.30654), Huang et al., June 2026 — even frontier models violate 27-31% of social design checks. Use for evaluating tutor dependence/intimacy risks.
- [Evaluating and Improving Pedagogical Fit in LLM-Based AI Tutors](https://arxiv.org/abs/2608.05411), Barlog, Craig, and Peng, 2026-08-05 — introduces the Pedagogical Suitability Index (PSI; 0.557–0.638 for a weak baseline). Correctness is not pedagogy: a tutor can be accurate yet misaligned with a learner's foundation, pacing, or course sequence. PSI-driven feedback improved 82.3% of 62 weak tutor cases.
- [Teaching Intro AI When the Tools Can Do the Homework](https://arxiv.org/abs/2608.05175), Pisan, 2026-06-26 — UW Bothell CSS 382 redesign: in-class exercises, reflective writing, defended projects, and a Student Bill of Rights negotiated with students. Assessment rebuilt for a world where the tool completes the old homework.
- [[Responsible Deployment]] — deployment pattern for pilots and review.

## Practical Examples
Before approving a tutor, check:
- **Learning fit:** aligned to curriculum, standards, and teacher goals.
- **Pedagogy:** gives hints, scaffolds reasoning, and encourages metacognition instead of answer dumping.
- **Signal-based quality:** measure thinking depth (reasoning:answer word ratio ≥ 3:1), step density, question rate (≥ 2-3 questions per interaction), and reasoning depth. Use internal signals as quality gates before expensive RL training — see TEI framework.
- **Disability-inclusive design:** does the tutor adapt its teaching style for different learner profiles? Persona-awareness must be architectural (in system design), not bolt-on. Test with at least 2-3 disability profiles.
- **Social design safety:** does the tutor encourage independence or dependence? Does it know when to escalate? Check for harmful intimacy, engagement-maximizing behaviors, or emotional bonding that serves the platform rather than the student — use EUDAIMONIA-style design checks.
- **Accuracy:** handles misconceptions, uncertainty, and citations transparently.
- **Privacy:** minimizes student data, clarifies retention, and supports district requirements.
- **Equity:** works for multilingual learners, students with disabilities, and varied reading levels.
- **Human escalation:** tells students when to ask a teacher or adult.
- **Evidence:** includes pilot data, pre/post measures, teacher feedback, and incident review.
- **Pedagogical fit before accuracy:** score candidate tutors with the PSI dimensions against your actual curriculum — does it adapt to where the learner is, not just answer correctly? Weak-fit tutors are fixable: PSI feedback improved 82.3% of weak cases in the evaluation study (2608.05411).
- **Assume the homework is done:** if the tool completes your old assignments, evaluation must move to in-class performance, defended work, and reflective writing; a negotiated Student Bill of Rights gives students a legible contract for what is and isn't theirs (2608.05175).

## Risks / Limits
- A checklist is not proof of effectiveness; it is a gate for safer pilots.
- Student outcomes should be measured over time and compared with realistic alternatives.
- Teachers should be part of tool selection, prompt design, and ongoing review.

## Related Pages
- [[AI Tutors]]
- [[Education]]
- [[AI for School Districts]]
- [[Responsible Deployment]]

## Tags
#ai-education #responsible-ai #practical-ai #risk
