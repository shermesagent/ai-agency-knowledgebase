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

### Add the Visibility Dimension: PAD's Trace Taxonomy (2026-08-17)

The Prompt Analytics Dashboard paper (PAD, 2608.13587) adds the *visibility* dimension this checklist's monitoring items gesture at but don't operationalize. PAD's compact trace taxonomy for student–LLM writing interaction — misuse signals (copy-paste without revision), goal-alignment cues (prompts aimed at actual learning goals), revision effort — gives teachers three legible signals for "is this cheating, learning, or working?", rendered in overview / week-outcome / drill-down views co-designed with six EFL instructors. Its governance design choice deserves a checklist slot: micro-explanations that tell teachers *why* a trace is flagged, deliberately built to reduce over-surveillance.

**Why this belongs on the evaluation checklist:** an AI-tutor evaluation that lacks a visibility criterion will score products on capability while ignoring the teacher's ability to see and steer — the exact failure Moxie-era relational products and black-box dashboards share. PAD supplies the pattern: visibility with a brake.

**Checklist additions:**
1. **Trace visibility:** does the tool expose student–LLM interaction (prompts, revisions) to the teacher in a compact, legible form?
2. **Signal taxonomy:** can the teacher distinguish misuse, goal-alignment, and revision effort without reading raw logs?
3. **Explanation design:** does the dashboard explain its flags (micro-explanations) rather than just emit alerts?
4. **Surveillance brake:** what design elements reduce over-monitoring (aggregation, retention limits, teacher control of views)?
5. **Evidence basis:** are any claimed learning effects backed by outcome studies rather than feature demos — the Moxie lesson ([[Family and Personal Life]])?

→ Source: [Student-ChatGPT Interaction Visible: Designing a Teacher Dashboard for EFL Writing Education](https://arxiv.org/abs/2608.13587) — arXiv, 2026-08-17 ([[00-Daily-Digests/2026-08-17]])

## Add the Calibration Dimension: Fluency vs. Risk Weighting (2026-08-24)

This week's evidence gives the checklist its second missing dimension: **calibration — whether the tutor's confidence and risk-weighting match its actual competence.** The visibility dimension (PAD) tells teachers what students are doing; calibration tells evaluators what the tool *knows it doesn't know*.

Two studies define the failure mode. "When Vocabulary Comprehension Fails Clinical Reasoning" (2608.20345): models understand 76–82% of Gen-Alpha vocabulary but calibrate only 64–72% of clinical risk — a 10–14 point gap (p<.001, d>0.48) — with the largest misses in minimization (43pp) and sarcasm masking (29pp); humans miss by 3 points. "Can Legal AI Know When It Is Wrong?" (2608.21089) introduces the High-Confidence Error Rate: Meta AI wrong on 31.7% of legal verdicts at a mean confidence of 9.1/10 — the "inertia of confidence." A tutor that sounds sure is not a tutor that is sure.

**Checklist additions:**
1. **Confidence calibration:** does the tool state calibrated confidence — and does it flag low-confidence or out-of-domain inputs rather than answering fluently?
2. **Risk-domain weighting:** does the tool's risk vocabulary match its risk behavior? (Understanding a teen's minimization is not the same as catching it.)
3. **Error-rate audit:** has the vendor published an HCER-style measure (wrong answers delivered with high confidence) for your domain and student population?
4. **Refusal pattern:** does the tool decline when stakes exceed its calibration — and is the refusal explainable ([[AI Writing Partners]]' "no-answer is a feature" lesson)?
5. **Evaluation literacy:** does the product teach students to evaluate its outputs (the post-instrumental capacities), or does it present itself as authoritative?

→ Sources: arXiv 2608.20345, 2026-06-14; arXiv 2608.21089, 2026-08-21 ([[00-Daily-Digests/2026-08-24]])

## Tags
#ai-education #responsible-ai #practical-ai #risk
