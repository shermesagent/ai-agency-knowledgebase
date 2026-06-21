# Healthcare

## Core Idea
Healthcare AI can expand access to information, coordination, documentation support, triage, and decision aids — and when designed well, it can "rehumanize" care by handling the administrative burden so humans can focus on patients. The evidence is crossing a reliability threshold: AI medical refill systems achieve 97% physician agreement, agentic AI is being deployed to address the WHO's projected 11 million healthcare worker shortage, and the framing has shifted from "AI replacing doctors" to "AI making doctors more human."

## Why It Matters
Healthcare is a domain where the Superagency thesis faces its hardest test. The stakes are life and death. The evidence requirements are higher than any other domain. The risks of overreliance, bias, and deskilling are acute. But the opportunity is equally enormous: healthcare systems worldwide are strained beyond capacity, and the choice is increasingly not "AI vs. human" but "AI-augmented human vs. overwhelmed human." When Doc In a Box achieves 97% physician agreement on refill recommendations, and when agentic AI automates complex administrative tasks so clinicians can spend more time with patients, healthcare AI demonstrates the Superagency pattern: AI handles the scalable, repeatable work; humans handle the relational, empathetic, judgment-intensive work.

## Best Supporting Sources
- [Rehumanizing Global Health Care with Agentic AI](https://www.technologyreview.com/2026/06/02/1137827/rehumanizing-global-health-care-with-agentic-ai/), MIT Technology Review, June 2, 2026 — agentic AI addressing the WHO-projected 11M healthcare worker shortage by automating administrative and clinical tasks so humans can focus on patient care.
- [Doc In a Box: Utah Outcomes](https://commerce.utah.gov/wp-content/uploads/2026/05/Doctronic-Outcomes-May-2026.pdf), Utah Department of Commerce, May 2026 — AI medical refill system achieves 97% physician agreement on recommended refills; 69% of physician-reviewed escalations were appropriate; 31% were "overly cautious" (safe design).
- [AI #171: False Flag](https://thezvi.substack.com/p/ai-171-false-flag), Zvi Mowshowitz, June 4, 2026 — analysis of Doc In a Box outcomes: 97% physician agreement on refill recommendations is "very good" and likely exceeds physician-physician agreement rates.
- [Midjourney Medical Scanner Announcement](https://digg.com/tech/6mpkkvze) — Digg / Droids / Midjourney, June 2026. Full-body ultrasonic CT scanner: ~500,000 transducers, 60-second scans, zero radiation, AI medical image segmentation. First target: body composition mapping. Aspirational: cancer screening at 98.7% accuracy. Deployment: 2027, SF spa pilot.
- [Preliminary Thoughts On The Midjourney Scanner](https://www.astralcodexten.com/p/preliminary-thoughts-on-the-midjourney) — Scott Alexander, Astral Codex Ten, June 19, 2026. Analysis of the scanner as a diffusion challenge: technology exists, but clinical/social infrastructure (FDA, evidence, reimbursement, adoption) does not. Raises incidental-finding concerns from the 2000s full-body CT fad.
- [AI Medical Tools Match and Surpass Doctors in Clinical Studies](https://www.crescendo.ai/news/ai-in-healthcare-news) — Crescendo.ai, June 18, 2026. Reliability 4/5; relevance 5/5. Multiple peer-reviewed studies show AI diagnostic tools matching or surpassing board-certified physicians on diagnostic accuracy and treatment recommendation quality. The language has shifted from "AI shows promise" to "AI matches or exceeds physician performance" — a structural validation milestone, not a single-study result.
- [This Month in Healthcare AI (June 2026)](https://www.linkedin.com/pulse/month-healthcare-ai-june-2026-gary-monk-hswoe) — Gary Monk, LinkedIn, June 15, 2026. Reliability 4/5; relevance 4/5. Monthly roundup across Prediction & Diagnosis, Treatment & Care, Generative AI, and Adoption & Governance. Flags AI-powered MRI analysis predicting future diabetes and cardiovascular disease from routine scans — predictive medicine from existing infrastructure. The consistent four-category framework tracks healthcare AI's maturation: Prediction & Diagnosis leads, Adoption & Governance lags.

## Practical Examples

- **Doc In a Box (Utah):** AI reviews prescription refill requests. In 72% of cases, AI recommends a refill — at least one of two physicians agreed in 97% of those cases. In 28% of cases, AI escalates to a human physician. The system is designed for overcaution: false positives (unnecessary escalations) are cheap; false negatives (missed problems) are expensive.
- **Agentic AI for healthcare administration:** AI agents handle scheduling, insurance coding, prior authorization, clinical documentation, and preliminary assessments — freeing clinicians for patient-facing work. This is the domain-specific Superagency pattern: AI as infrastructure that makes human care more human.
- **AI-assisted diagnosis and triage:** Bounded workflows where AI provides preliminary assessments with documented confidence levels, requires human confirmation for consequential decisions, and tracks disagreement rates as a primary safety metric.

### Midjourney Medical Scanner (June 2026)

Midjourney — the AI image generation company — is spinning out **Midjourney Medical**, a dedicated division building a full-body ultrasonic CT scanner. Key details:

- **Technology:** ~500,000 ultrasound transducers in a water tank. AI-powered medical image segmentation labels every pixel by tissue type. Produces MRI-quality 3D body maps in ~60 seconds with zero ionizing radiation.
- **First application:** Body composition mapping — repeatable scans showing changes in muscle, fat, and tissue over time. This is the initial commercial target.
- **Aspirational application:** Cancer screening — specialized algorithms achieve 98.7% accuracy for lung cancer detection and consistently outperform humans.
- **Deployment plan:** SF "spa" pilot in 2027. Consumer-facing walk-in scanning. FDA clearance required.
- **Scott Alexander's analysis (June 19):** The scanner is a diffusion challenge as much as a technical one. Population-level screening raises hard questions: who gets scanned? What do we do with the data? Does finding things earlier actually improve outcomes, or does it produce a flood of incidental findings that trigger expensive, anxiety-producing follow-ups? Full-body CT scans for healthy people were a 2000s fad that faded when evidence showed more harm than benefit. Midjourney eliminates radiation but doesn't eliminate the incidental-finding problem.
- **Superagency connection:** This is democratization of diagnostic imaging — taking body scanning from the hospital to the consumer. If Midjourney delivers, millions gain access to data previously available only to elite athletes and the medically wealthy. But the diffusion layer (FDA clearance, clinical evidence, reimbursement codes, physician adoption) is years from completion. See [[Democratization of Expertise]] and [[00-Daily-Digests/2026-06-20]].

## Risks / Limits
- Healthcare AI requires unusually strong evidence, privacy protections, and accountability mechanisms. 97% agreement on refills is impressive but refills are a bounded task — diagnostic accuracy, treatment recommendations, and end-of-life decisions are far harder.
- Overcaution is the right design for safety but means the system hasn't yet demonstrated cost savings or throughput improvements at scale.
- The "rehumanizing" framing is compelling but needs deployment data — does AI administration genuinely increase patient-facing time, or does it just add another technology layer?
- Watch for overreliance, privacy risks, bias, deskilling, labor displacement, and concentration of power.
- In consequential settings, AI recommendations must be contestable and auditable.
- **Clinical language model bias amplification (June 2026):** Soetan (2606.14460) audits ClinicalBERT — a model pretrained on MIMIC-III discharge summaries — and finds that **65.6% of statistically significant bias findings contradict observed corpus distributions, rising to 80% for Black patients and 87.5% for agency attribution.** The model amplifies bias rather than inheriting it. This is critical for healthcare AI deployment: a model that appears to reflect training data distributions may actually be amplifying demographic associations through internal representation rather than mirroring real clinical patterns. Source: https://arxiv.org/abs/2606.14460

## Design Research: Friction and Trust

### Friction in Clinical Decision-Making (June 2026)
Fischer et al. (2606.14406) investigate what forms of friction actually promote reflection in clinical AI use. In interviews with 7 clinicians, two friction designs were tested: (1) data-driven questions (e.g., \"have you considered X?\") — perceived as unhelpful for reflection but useful as reminders; (2) \"what-if\" hypotheticals — perceived as genuinely useful for improving patient care. Clinicians saw the prototype as a promising training tool for novices. The finding: friction that generates alternatives is more valuable than friction that checks completeness. **Superagency connection:** For healthcare AI to expand agency rather than erode it, the friction must be productive — offering new possibilities, not just second-guessing existing decisions. Source: https://arxiv.org/abs/2606.14406

### SpheriCity: Provenance-First AI for Sustainability Knowledge (June 2026)
Qayyum et al. (2606.13854) built a conversational AI for city-level circularity assessment that foregrounds evidence traceability, structured synthesis, and interaction scaffolds. Expert review with 6 sustainability professionals found that **transparent sourcing, contextual explanation, and alignment with expert workflow** strongly shape expert trust. The provenance-first design pattern — where every claim is traceable to source documents — transfers directly to clinical AI: healthcare professionals need to verify AI recommendations against evidence, not trust model outputs. Source: https://arxiv.org/abs/2606.13854

## Related Pages
- [[Risk-Benefit Matrix]]
- [[Responsible Deployment]]
- [[Superagency]]
- [[AI as Copilot]]
- [[Open Questions]]

## Tags
#responsible-ai #human-agency #augmentation #practical-ai #ai-agents
