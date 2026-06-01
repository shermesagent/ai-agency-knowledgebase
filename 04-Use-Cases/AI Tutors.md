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

## Practical Examples
- A student gets hints, worked examples, and retrieval-practice questions aligned to the lesson objective.
- A teacher reviews anonymized misconception patterns and reteaches the concepts that students struggled with.
- A district pilots AI tutoring in one course with pre/post assessments, student feedback, teacher review, and opt-out paths.

## Risks / Limits
- Evidence from one context may not transfer across grade levels, subjects, student needs, or tutor designs.
- Tutors need safeguards against hallucinated explanations, answer-giving, biased feedback, and inappropriate data collection.
- Human educators should remain responsible for curriculum alignment, intervention decisions, and student wellbeing.

## Related Pages
- [[Education]]
- [[AI Use Case Evaluation Rubric]]
- [[Responsible Deployment]]
- [[Agency Expansion Framework]]

## Tags
#ai-education #augmentation #practical-ai #responsible-ai
