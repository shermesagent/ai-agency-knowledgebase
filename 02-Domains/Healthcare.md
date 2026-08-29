---
title: Healthcare
created: 2026-06-15
updated: 2026-08-29
type: domain
tags: [healthcare, responsible-ai, human-agency, augmentation, practical-ai, ai-agents, calibration]
confidence: high
---

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

## The Clinician's Veto: Calibrated Autonomy in AI Prescribing (June 2026)

A critical paper from June 25, 2026 establishes minimum architectural requirements for autonomous AI in healthcare — and in doing so, demonstrates that the shaping layer operates through professional gatekeepers who don't reject AI but reshape it around their accountability requirements.

LaRocco et al. (arXiv 2606.25108) surveyed 136 U.S. prescribing clinicians, motivated by the fact that U.S. bill H.R. 238 and Utah's prescription-renewal pilot both authorize AI to prescribe medications in an agentic capacity. The paper argues that current regulatory guidelines — which suggest aggregate model performance metrics for clearance — are insufficient without three minimum architectural requirements:

### Three Minimum Requirements

1. **Calibrated per-prediction confidence for action-gated thresholds.** Clinicians would not permit autonomous prescribing without it. Aggregate performance metrics (e.g., "97% agreement with physicians") hide the variance: the 3% of cases where AI disagrees might be the highest-risk decisions. Calibrated confidence means the AI says "I am 99% confident in this refill recommendation" vs. "I am 60% confident" — and the action threshold gates on confidence level.

2. **Differentiated communication of aleatoric vs. epistemic uncertainty.** When uncertainty arises from genuine clinical ambiguity (aleatoric) — e.g., two reasonable treatment paths with different tradeoffs — clinicians preferred a competing-options summary. When uncertainty arises from model ignorance (epistemic) — e.g., the AI hasn't seen enough similar cases — clinicians shifted to abstention. The distinction matters because it determines what the human does next: weigh options vs. gather more data.

3. **Inferential transparency at the moment of decision enabling liability allocation.** Clinicians were only willing to accept additional liability when they could make a substantive judgment under acknowledged uncertainty. Black-box autonomy that says "prescribe X" without showing its reasoning is not just unsafe — it's uninsurable. Inferential transparency means the AI shows its work: which patient factors drove the recommendation, which evidence sources support it, where the uncertainty lies.

### The Collapse of "Autonomy"

The paper's most striking finding is that a system meeting these three requirements **functions less as an autonomous agent and more as heavily supervised decision support.** The architectural features that make AI safe for autonomous prescribing also strip away what "autonomy" conventionally means. The system proposes; the clinician evaluates confidence, understands the uncertainty type, inspects the reasoning, and decides. This is not AI replacing clinical judgment — it's AI presenting its judgment for clinical review.

### Superagency Connection

The Clinician's Veto is the shaping layer in healthcare: professional gatekeepers don't reject AI — they reshape it. The result is AI that expands clinical agency rather than replacing it. A system with calibrated confidence, uncertainty distinction, and inferential transparency gives clinicians more information, not less; more context for their judgment, not less; more evidence to support their decisions, not less. This is the Superagency pattern in its highest-stakes domain: AI handles the data integration and recommendation generation; humans retain the accountability, the uncertainty navigation, and the final decision.

### Deployment Implications

The gap between "these are good requirements" and "these are deployable in every clinical setting" is the implementation challenge. Calibrated confidence at per-prediction granularity is technically demanding. Aleatoric/epistemic uncertainty decomposition is an active research area. Inferential transparency that is both accurate and readable is a UX challenge. But the paper establishes that these are not optional — they are minimum requirements that clinicians themselves demand before accepting AI autonomy in prescribing. Regulation that sets a lower bar will face professional resistance; regulation that meets this bar will face implementation complexity. The shaping layer is not just about what's possible — it's about what's acceptable to the humans who bear the liability.

Source: https://arxiv.org/abs/2606.25108

### Friction in Clinical Decision-Making (June 2026)
Fischer et al. (2606.14406) investigate what forms of friction actually promote reflection in clinical AI use. In interviews with 7 clinicians, two friction designs were tested: (1) data-driven questions (e.g., \"have you considered X?\") — perceived as unhelpful for reflection but useful as reminders; (2) \"what-if\" hypotheticals — perceived as genuinely useful for improving patient care. Clinicians saw the prototype as a promising training tool for novices. The finding: friction that generates alternatives is more valuable than friction that checks completeness. **Superagency connection:** For healthcare AI to expand agency rather than erode it, the friction must be productive — offering new possibilities, not just second-guessing existing decisions. Source: https://arxiv.org/abs/2606.14406

### SpheriCity: Provenance-First AI for Sustainability Knowledge (June 2026)
Qayyum et al. (2606.13854) built a conversational AI for city-level circularity assessment that foregrounds evidence traceability, structured synthesis, and interaction scaffolds. Expert review with 6 sustainability professionals found that **transparent sourcing, contextual explanation, and alignment with expert workflow** strongly shape expert trust. The provenance-first design pattern — where every claim is traceable to source documents — transfers directly to clinical AI: healthcare professionals need to verify AI recommendations against evidence, not trust model outputs. Source: https://arxiv.org/abs/2606.13854

### NLP in Health Professions Education — The Scoping Review Gap (July 2026)

A July 2026 scoping review (arXiv 2607.21605) is the first to systematically map NLP/AI applications across the full spectrum of health professions education. It identifies **7 application domains** — but only **4 studies on public health education**, revealing a massive research gap at the population-health level. The concentration is in clinical education (medical, nursing); community-facing health education — where Superagency's democratization thesis is most relevant — is barely studied.

**The Superagency connection:** If AI education tools concentrate exclusively on clinical training, the Superagency pattern accrues to clinicians (who are already highly trained) rather than to patients, community health workers, and public health practitioners. The scoping review gap is an implementation gap: we're building AI tutors for doctors before building AI tutors for communities. The shaping layer in healthcare education is currently steering AI toward the already-empowered.

Source: https://arxiv.org/abs/2607.21605

### Co-Design and Overtrust — When Participation Produces Overconfidence (July 2026)

A July 2026 study on LLM-based preference agents (arXiv 2607.21757) found a counterintuitive result: **people who co-designed an LLM-based preference agent rated its results as more accurate, even when they weren't.** Participation — ordinarily a good thing — produced overtrust when not paired with calibration.

This has direct implications for patient-facing healthcare AI. Co-designing a symptom checker with patients increases trust. But if that trust isn't calibrated to the tool's actual accuracy, patients may act on incorrect recommendations with higher confidence than they would have given an off-the-shelf tool. The mechanism: participation creates psychological ownership, and ownership suppresses skepticism.

**The calibration requirement:** Co-design must be paired with calibration feedback — showing users when the tool was wrong, why, and what the consequences were. Without this feedback loop, participatory design becomes a vector for overtrust rather than a safeguard against it. For healthcare AI, this means: involve patients in design, but also show them the error rates.

Source: https://arxiv.org/abs/2607.21757

### Five-Layer Architecture for Healthcare AI

The five-layer agency architecture (developed Week 30, 2026-07-20 through 2026-07-24) maps onto healthcare AI as follows:

| Layer | Healthcare Translation | Evidence in This Page |
|-------|----------------------|----------------------|
| **Abstention** | AI refrains from autonomous decisions where confidence thresholds aren't met. The Clinician's Veto requires abstention when uncertainty is epistemic. Doc In a Box escalates 28% of cases — abstention by design. | Clinician's Veto, calibrated per-prediction confidence thresholds |
| **Development** | Build AI capability systematically: refill automation → diagnostic assistance → treatment recommendation. Each stage earns autonomy through demonstrated reliability. The scoping review gap shows we're under-developing public health AI education. | NLP scoping review, agentic AI for administration |
| **Calibration** | Verify AI outputs against physician judgment. 97% agreement on refills. Distinguish aleatoric from epistemic uncertainty. The co-design finding — participation without calibration produces overtrust — is a calibration failure. | Doc In a Box, co-design/overtrust, ClinicalBERT bias amplification |
| **Exchange** | AI presents recommendations with inferential transparency — showing its work, not just its conclusion. Physicians accept liability only when they can make substantive judgments under acknowledged uncertainty. The provenance-first design pattern (SpheriCity) transfers to clinical AI. | Inferential transparency requirement, SpheriCity provenance pattern |
| **Scaffolding** | Build institutional infrastructure for AI deployment: FDA clearance, clinical evidence, reimbursement codes, liability frameworks. The Midjourney scanner diffusion challenge is a scaffolding problem — the technology exists but the institutional layer doesn't. | Midjourney Medical Scanner, Clinician's Veto liability allocation |

**The healthcare Superagency thesis in five-layer terms:** AI expands clinical agency when it handles the scalable, repeatable work (Development layer), verifies its own outputs against clinician judgment (Calibration), presents reasoning transparently (Exchange), and is embedded in durable institutional frameworks (Scaffolding) — *and* when it knows to abstain where confidence is insufficient (Abstention). The five layers are not optional in healthcare — they are the minimum architecture for deployment that preserves rather than erodes clinical agency.

This page was 32 days stale (filesystem: June 25). Refreshed with NLP scoping review, co-design/overtrust findings, and five-layer architecture integration.

### Clinical Reasoning in Real-World Care: Triage as Sequential Decision Under Asymmetric Loss (August 2026)

The strongest formal statement yet of why medicine is the wrong place for autonomous LLM decisions — and the right place for abstention: arXiv 2607.28677 argues LLMs are **not yet safe for autonomous clinical care**, and explains the structural reason. Safe triage is a **sequential decision under asymmetric loss**: the cost of missing a rare must-not-miss diagnosis (aortic dissection, sepsis, pediatric red flags) vastly exceeds the cost of a false alarm. The correct action is therefore often the *improbable* answer — "this could be X, rule it out" — which is the opposite of most-probable-text continuation, the objective LLMs are optimized for. Most-probable-token reasoning and must-not-miss clinical reasoning are different objectives; the gap is not a prompt-engineering fix, it is a difference in what is being optimized.

**Where this lands in the five-layer architecture:** it is the **Abstention layer's decision-theoretic foundation**. The five layers say AI should abstain where confidence is insufficient; this paper says *why* — under asymmetric loss, the low-probability hypothesis is often the high-value one, and an LLM's probability ranking is the wrong instrument for that decision. Practical consequences:

1. **Widening-net use is sound; autonomous disposition is not.** Using AI to surface improbable must-not-miss candidates (the "could be X" suggestions) expands clinical agency; letting it decide the disposition optimizes the wrong loss function.
2. **The clinician's veto is not a check on AI — it is the decision.** The [[The Clinician's Veto]] logic (human holds escalation authority) is now justified formally: the veto is where the asymmetric-loss function is actually computed, because only the clinician can price the miss.
3. **Calibration gains a new requirement:** verify not just agreement (97% refill agreement) but *coverage of the improbable* — does the AI flag the rare-but-catastrophic hypothesis, or only the common one? Agreement on common cases is precisely the metric that misses the asymmetric-loss point.

**For the agency frame:** this is augmentation with the right division of labor stated precisely. AI widens the net (scale, recall, pattern availability); humans price the misses (judgment, liability, asymmetric loss). The paper is a counterweight to both autonomous-care hype and blanket dismissal: the issue is not that LLMs are dangerous, it is that they optimize the wrong objective for triage — and the fix is architectural (keep the human in the loss function), not a better prompt.

→ Source: https://arxiv.org/abs/2607.28677

## Related Pages
- [[Risk-Benefit Matrix]]
- [[Responsible Deployment]]
- [[Superagency]]
- [[AI as Copilot]]
- [[Open Questions]]

## AMIE and Video Consultations (2026-08)

Google Research's AMIE demonstration (2026-08-11) pushes the clinical-AI frontier toward real-time **video** consultation: a first-of-its-kind multi-agent architecture built on Gemini + Project Astra that hears and sees the patient (speech, intonation, facial expression) rather than parsing text chat. In a randomized simulated-consultation study with patient actors and primary-care physicians, clinical evaluators favored AMIE on history-taking thoroughness, diagnostic accuracy, management appropriateness, and communication quality — and patient actors preferred the video experience over text chat.

**Reading for this page:** the video preference is an augmentation signal — patients chose the interface that preserves more of the clinical encounter, not the one that hides it. That aligns with this page's through-line: the human relationship in the room (physician → patient) is preserved and supported, not replaced; the technology absorbs the documentation, history-taking, and differential-construction load so the clinician can attend to the person. Caveats are material: simulated actors and standardized cases are not clinics, Google flags it as a research system only, and more work is needed before clinical deployment — treat the direction as demonstrated, the deployment as unproven. The multi-agent architecture is also notable for [[Beyond Prompting]] — specialist sub-agents (history, diagnosis, management, communication) coordinated around one patient encounter.

→ Source: Google Research AMIE (2026-08-11); [[00-Daily-Digests/2026-08-15]]

### The AI-Only Threshold in Medicine (2026-08-29)

The strongest "AI alone" claim yet published in a major medical venue — and the sharpest test of this page's Clinician's Veto architecture. **Emanuel, Khosla et al., "Will Autonomous AI Exceed AI-Physicians as the Best Medical Care?"** (JAMA, August 2026; covered by Steven Levy in WIRED, 08-28) reviews all published AI-in-medicine research since January 1, 2024 and argues medicine "is rapidly approaching the transition point at which AI alone will exceed physicians and physician AI-hybrids" at five fundamental tasks: taking medical histories, establishing a diagnosis, identifying needed tests, prescribing treatment, and managing chronic disease. Their policy conclusion is deliberately provocative: clinicians should refrain from meddling because "humans in the loop degrade AI performance." Lead author Emanuel — who spent years dismissing Khosla's "Do We Need Doctors or Algorithms?" hobbyhorse — says the shift began when UCSF's Robert Wachter showed him the "economy class medicine" future.

**The dissent is structural, not rhetorical.** AMA CEO John Whyte: many surveyed studies are simulations, not blind trials, and a February 2026 Nature study found most real patients could not effectively converse with LLMs to access their expertise. Wachter concedes the argument's importance but invokes the **doorman fallacy** — the fear that doormen would vanish once doors opened automatically; instead doormen persist because they perform myriad adjacent tasks (packages, pets, a sympathetic ear). Medicine will find its version: AI may never be as effective as a human at delivering a grim prognosis, and patients may be guided to better paths by a real clinician.

**Where this lands against this page's architecture:** the claim is task-specific, and the resolution is loss asymmetry (see the Clinician's Veto and the asymmetric-loss argument from 2607.28677 above). For symmetric-loss tasks — documentation, history intake, refill triage — the "humans degrade" finding is plausible, and a checkpoint placed there is a design bug. For asymmetric-loss tasks — must-not-miss diagnosis, treatment under uncertainty — the human is not a performance drag; the human is where the loss function is priced. The danger is the paper's sweeping "AI alone" framing licensing removal of humans from exactly the asymmetric tasks where its evidence is weakest. The agency frame stands: AI widens the net; humans price the misses — and the threshold crossing changes *which* tasks belong on which side, not the need for the division.

→ Sources: [WIRED, "AI Has Human Doctors Asking: What's Left for Us?"](https://www.wired.com/story/ai-has-human-doctors-asking-whats-left-for-us/) (2026-08-28); Emanuel & Khosla et al., JAMA (August 2026); [[00-Daily-Digests/2026-08-29]]

## Tags
#responsible-ai #human-agency #augmentation #practical-ai #ai-agents
