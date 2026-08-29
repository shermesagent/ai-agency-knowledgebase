# Future of Work

## Core Idea
The future of work question is not only which jobs disappear, but which capabilities become available to more workers and which institutions help people adapt.

## Why It Matters
This idea matters because AI adoption will be experienced as changes to tasks, teams, learning curves, hiring, management, and power inside organizations. The most useful question is not whether “AI replaces jobs” in the abstract, but whether specific deployments increase human capability, mobility, bargaining power, and room for judgment.

## Best Supporting Sources
- [The Turing Trap](https://arxiv.org/abs/2201.04200), Erik Brynjolfsson, 2022 — warns that human-like imitation can steer AI toward substitution rather than complementarity.
- [2025 Work Trend Index Annual Report](https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2025/04/2025_Work_Trend_Index_Annual_Report_680aaa7fe52dd.pdf), Microsoft, 2025 — argues that organizations are moving toward human-led, AI-operated "frontier firms."
- [The Cybernetic Teammate](https://www.nber.org/papers/w33641), Dell'Acqua et al., 2025 — examines AI's effects on teamwork and expertise, not only individual output.
- [How People Are Really Using Gen AI in 2025](https://hbr.org/2025/04/how-people-are-really-using-gen-ai-in-2025), Marc Zao-Sanders, Harvard Business Review, 2025 — offers a bottom-up view of common personal and workplace use cases.
- [A reality check on the AI jobs hysteria](https://www.technologyreview.com/2026/05/26/1137855/a-reality-check-on-the-ai-jobs-hysteria/), David Rotman / MIT Technology Review, 2026 — the most thorough data-driven analysis to date: no large-scale AI job losses yet, AI-exposed unemployment lower than less-exposed, 16% decline concentrated in entry-level roles where AI automates rather than augments. The "earn-while-you-learn" career pipeline is what's breaking.
- [Where Is AI in GDP Statistics?](https://www.piie.com/), Korinek, Solaiman, Zago / PIIE, 2026 — documents AI economy growing at ~2,600%/year but invisible in GDP; proposes AI satellite accounts.
- [Hell Is Other People — So Billionaires Are Using AI to Replace Inconvenient Humans](https://www.thenerve.news/p/cory-doctorow-column-ai-inconvenient-humans-billionaires-sam-altman-bezoz-migrants), Cory Doctorow / The Nerve, June 2, 2026 — structural critique: AI deployment shaped by capital's desire to eliminate labor's bargaining power.

### The Remote Labor Index: AI Capability Growth on Freelance Tasks (July 2026)

**Import AI / CAIS / Scale Labs** released a Remote Labor Index tracking AI systems' success rate on online freelance tasks (coding, writing, design, data analysis). The key data point:

| Date | Success Rate |
|------|-------------|
| October 2025 | 2.5% |
| July 2026 | 16.1% |

A **6.4× increase in nine months.** Online freelance tasks are the closest proxy for general knowledge work — if AI can complete a freelance coding gig, it can complete portions of salaried coding work. The index measures capability, not displacement, but capability is a leading indicator: tasks AI can do are tasks AI is eventually assigned.

**Why this matters:** At the current acceleration rate, 50% success is plausible within 18 months. But there's a structural floor — creative judgment, client communication, and contextual adaptation remain hard. The index should be read alongside the MIT Tech Review finding that only 1 in 5 US companies use AI in any function — **capability is running ahead of organizational adoption, and the gap between them is where agency policy lives.**

### Economists Formally Warn on AI Job Displacement (July 2026)

The **New York Times** (July 13, 2026) reported that a group of economists — including Anthropic co-founder **Jack Clark** — signed a formal statement warning that AI could transform the economy faster than previous technologies, with labor market disruptions exceeding prior automation waves.

This is significant because economists have been notably cautious on AI employment claims. The shift from "AI complements workers" (Autor, Brynjolfsson) to "the pace warrants formal institutional attention" represents a consensus movement — not toward alarmism, but toward treating AI displacement as a serious forecasting problem rather than a speculative one.

The statement connects three threads already tracked in this wiki:
- The **invisible AI economy** (PIIE: AI growing at ~2,600%/year but invisible in GDP)
- The **entry-level crisis** (MIT Tech Review: 16% decline in young-worker roles in AI-exposed fields)
- The **Remote Labor Index acceleration** (Import AI: 2.5% → 16.1% capability gain)

Read together, these signals suggest the need for **AI satellite accounts** in economic statistics and **transition programs** designed before displacement becomes a crisis rather than after.

### Agentic Coding Adoption: The Single-Human Oversight Model (July 2026)

The first large-scale analysis of agentic coding tool adoption (arXiv 2607.14037) provides the most granular picture yet of how the agent revolution is landing in practice. Analysis of **25,264 agentic pull requests across 7,402 GitHub projects** reveals several patterns directly relevant to the future of work:

- **Single-human oversight dominates.** The most common deployment pattern: one human oversees multiple agentic coding tools, reviewing and merging agent-generated code. This is not "AI replaces developer" — it's "AI writes, human inspects, ships together." The human's role shifts from *author* to *editor+reviewer+merger*.
- **Adoption is concentrated, not universal.** A small number of high-adoption projects account for most agentic PR activity. The agent revolution has early adopters, not universal uptake — and the adoption patterns suggest organizational factors (team culture, existing tooling, project type) determine adoption more than individual developer preference.
- **Small projects adopt more aggressively.** Smaller, newer projects with fewer established processes show significantly higher rates of agentic PR adoption. Large, established projects with existing contributor communities adopt more slowly — institutional inertia is a real barrier.
- **Multiple agents per project is common.** Projects using agents typically use more than one — Claude Code for architecture, Codex for implementation, OpenClaw for maintenance. The multi-agent pattern is emerging organically in practice.

**Future of Work implications:**
- The single-human oversight model validates the augmentation thesis — AI amplifies individual throughput. But the bottleneck shifts: if one human oversees five agents, review quality becomes the limiting factor.
- The institutional inertia finding suggests that **organizational design**, not just individual capability, determines AI adoption rates. The organizations slowest to adopt may not be the least capable — they may be the ones with the most established processes to reconfigure.
- The multi-agent pattern suggests that **agent orchestration** is becoming a distinct skill — knowing which agent to assign to which task and how to coordinate between them.

Source: https://arxiv.org/abs/2607.14037

### AI-Accelerated Professional Upskilling: The Reskilling Imperative (July 2026)

A new end-to-end framework for rapid professional reskilling (arXiv 2607.14044) provides both the urgency and the method. The World Economic Forum's projection: **59 of every 100 workers will need reskilling by 2030.** The framework maps which skills AI can accelerate (technical skills, structured knowledge acquisition) vs. which require human-intensive development (judgment, collaboration, ethical reasoning, creative direction).

**The acceleration-classification split:**
- **AI-accelerable:** Coding syntax, data analysis procedures, documentation, tool operation, regulatory knowledge — skills where AI can compress the learning curve by providing real-time guidance, examples, and feedback.
- **Human-intensive:** Judgment under uncertainty, cross-domain synthesis, collaborative negotiation, ethical reasoning, taste and creative direction — skills that require accumulated experience, not information delivery.

**The framework's core insight:** Reskilling programs that treat all skills as equally AI-accelerable will fail. The skills that AI can accelerate most are precisely the skills that AI is also automating — so workers reskilled only in AI-accelerable domains face the same automation pressure they were reskilling to escape. The sustainable reskilling pathway focuses on the human-intensive skills that AI amplifies but cannot replace.

**Future of Work implication:** This directly connects to the MIT Tech Review finding that the entry-level career pipeline is what's breaking. Entry-level roles traditionally develop the human-intensive skills (judgment, collaboration, taste) through practice — but if AI automates the entry-level tasks, the pipeline that produces those skills collapses. The reskilling framework needs to be paired with an **earn-while-you-learn** architecture that preserves the developmental pathway even as specific tasks are automated.

Source: https://arxiv.org/abs/2607.14044

### Economic Evaluations of Language Models: The EconEvals Framework (July 2026)

The EconEvals framework (arXiv 2607.19375, July 2026) introduces the first systematic approach to evaluating AI through an economic lens — not just whether models CAN perform tasks, but whether their performance at current cost, reliability, and scalability justifies economic deployment. Key contributions:

- **47 economically relevant task categories** spanning professional services, creative production, analysis, and coordination.
- **Cost-adjusted performance metric:** AI output quality ÷ (API cost + error correction cost), compared against market rates for equivalent human labor.
- **Economic thresholds:** The point at which AI performance crosses from "interesting demo" to "economically viable substitute" — different thresholds for different tasks and labor markets.

**Implication:** The gap between AI capability and AI economic viability is the policy window. If AI can do the task at 90% quality for 50% of the cost, deployment may be economically rational but socially disruptive. If it's 70% quality for 110% cost, deployment won't happen regardless of technical capability. The Remote Labor Index (2.5% → 16.1%) measures capability; EconEvals provides the economic complement.

→ Source: https://arxiv.org/abs/2607.19375

### Algorithm-Mediated Markets: When Shippers Become Algorithms (July 2026)

A case study in AI-mediated market concentration (arXiv 2607.19967, July 2026): when LLMs mediate price-setting in freight markets, algorithm-to-algorithm negotiation produces outcomes that diverge from competitive equilibrium. Key finding: **when AI agents negotiate on both sides of a transaction**, the structural properties of the negotiation environment — information asymmetries, speed advantages, coordination capabilities — favor the party with superior AI deployment.

This generalizes beyond freight: any market where both buyers and sellers deploy AI agents creates a new class of market dynamics that traditional competition policy isn't designed to address. The relevant question shifts from "is the market competitive?" to "are the AI agents negotiating on equal footing?"

→ Source: https://arxiv.org/abs/2607.19967

### UX Principles for Human-AI Agent Interaction in the Workplace (July 2026)

A framework (arXiv 2607.19941, July 2026) with five design principles for workplace AI agents — directly relevant to the Future of Work because interaction design determines whether AI augments or alienates:

1. **Action transparency:** Preview what the agent WILL do before it acts.
2. **Reversibility by default:** Irreversible actions require explicit human confirmation.
3. **Boundary legibility:** Users must understand the agent's action space at a glance.
4. **Trust calibration per task:** Different tasks deserve different autonomy levels.
5. **Escalation clarity:** When the agent encounters ambiguity, the escalation path must be explicit.

These principles operationalize the [[The Abstention Layer]] and [[The Calibration Layer]] for workplace deployment. They're the design-side complement to governance frameworks: governance determines what agents CAN do; UX principles determine whether humans can effectively supervise what agents DO.

→ Source: https://arxiv.org/abs/2607.19941

### The Sysadmin Expertise Ladder: Mentor and Ladder-Shortener at Once (August 2026)

A 14-interview study of IT professionals (arXiv 2607.28650, Abou Khamis, Assal, Matrawy) documents what "compression of traditional expertise pathways" actually looks like inside one profession. The findings:

- **The tutor role is real:** GenAI acts as a mentor-like tutor — juniors reach task-level competence in months instead of years, with on-demand explanation replacing the slow accumulation of trial-and-error.
- **But the ladder is being shortened from underneath:** the traditional pathway — years of incremental troubleshooting that built judgment, pattern recognition, and the instinct for *what could go wrong* — is compressed. Workers report performing better on tasks while experiencing a shallower understanding of the systems beneath the tool.
- **Performance perception diverges from expertise formation:** people look more competent (and feel more competent) faster, while the underlying internalized skill grows more slowly than the performance signal suggests. This is the [[The Cognitive Commons]] mechanism (Distributed vs. Internalized Mastery) observed in the field: the tool carries the load, and the load does not transfer.

**For the agency frame:** this is augmentation with a deferred bill. The productivity dividend is real and immediate; the expertise deficit shows up later, precisely when the tool changes, fails, or is absent. The mitigation is deliberate practice design — the "build internal learning ladders" recommendation below is not a nice-to-have, it is the countermeasure to ladder-shortening. If the first rungs of the expertise ladder are being removed across sectors simultaneously (see the drive-thru section), the shape of the career ladder itself changes.

→ Source: https://arxiv.org/abs/2607.28650

### The AI Drive-Thru Arrives: Voice Agents in Fast Food (August 2026)

WIRED's Kate Taylor documents the first mass-market voice-agent rollout: **Taco Bell runs AI ordering at 890 drive-thru lanes** (>10% of US locations), **Dairy Queen in 25 states**, and **12% of White Castles use "Julia."** The lineage goes back to McDonald's Apprente acquisition (2019); today's wave is powered by Presto and SoundHound partnerships. This is millions of real transactions per week through autonomous voice agents — the largest consumer-facing agentic deployment to date, and the fastest (from pilot to scale in months, not years).

**Why this is a Future of Work page item, not just a product story:** it is the augmentation-vs-replacement question at scale, in the labor market's most visible entry-level segment. WIRED reports the labor math that pushed chains to automate — turnover above 100% annually makes the agent cheaper than the churn. But the job being automated was the traditional first rung of the workforce ladder for millions of young and part-time workers. Combined with the sysadmin ladder-shortening finding, the pattern is not sector-specific: **entry rungs are being compressed or removed across very different industries at the same time.** What replaces the entry rung — a new rung (maintaining and supervising the agents), or nothing — is the open question this page will track.

→ Source: [WIRED, "AI Conquered Coding. Fast Food Is Next"](https://www.wired.com/story/ai-conquered-coding-fast-food-is-next/) (Kate Taylor, 2026-08-03)

### The Capability Ladder: Task Reallocation, Not Replacement (2026-08-12)

**[The Capability Ladder: A Curriculum-Modernization Framework for Workforce Readiness in the AI Era](https://arxiv.org/abs/2608.07779)** (Memari, Rudolph, 2026-08-07) — a five-level ladder (trigger → automation → workflow → AI agent → agent team) that maps tasks onto the level of AI capability they require, reframing workforce readiness as **curriculum modernization**: the training question is not "which jobs will AI replace" but "which level of the ladder does each task sit on, and how does education move people up it?" Task *reallocation* — moving human effort to ladder levels where judgment is the binding constraint — is the stated goal, not headcount reduction.

**Why it matters here:** it gives HR, education, and the entry-rung debate above a shared vocabulary — the same ladder can label a job requisition, a training module, and a task-level adoption plan (see [[Task-Level AI Adoption]]). The verification corollary: as humans move up the ladder, the judge problem follows them — higher levels need stronger evidence rules, not just stronger models (see [[The Judge Problem]]). Related: [[Education]], [[Frontier Firm]], [[AI Field Experiment Evidence]].

→ Source: arXiv 2608.07779 (2026-08-07); [[00-Daily-Digests/2026-08-12]]

## Practical Examples
- Redesign one recurring process as a [[Frontier Firm]] workflow: AI drafts or routes the work, humans set goals and inspect exceptions, and the team measures whether quality and agency improve.
- Use [[Task-Level AI Adoption]] to label tasks as augment, automate, preserve-human, or prohibit-AI — and add the economic readiness check from EconEvals before deployment.
- Build internal learning ladders so junior workers use AI to learn faster rather than merely skipping practice.
- Apply the five UX principles when procuring or building workplace AI agents: if the agent can't preview actions before executing, it's not ready for deployment.

## Risks / Limits
- Avoid treating one positive case study as universal proof.
- Watch for overreliance, privacy risks, bias, deskilling, labor displacement, and concentration of power.
- Update this section whenever strong counterarguments appear.
- “AI-operated” can imply worker displacement or managerial surveillance unless organizations explicitly protect human judgment, voice, and development.

### The Usage Data Gap and the Documentation Shift (2026-08-18)

**[Adoption of Generative AI in the Workplace: Increasing and Shifting the Balance of Productivity and Communication Activity](https://arxiv.org/abs/2608.15550)** (Yu, Chen, Hu, Suri, Counts — Microsoft, 2026-08-13): digital trace data from Microsoft 365, difference-in-differences over 20 weeks. Heavy users (>100 AI uses) show **+21.2% productivity actions** and **+7.1% communication actions**; the composition shifts toward individual, documentation-focused work, with reading and organizing email declining. The gains are real; the *mix* is the finding — and the communication gap is an innovation-diffusion risk: knowledge work that never crosses desks doesn't cross-pollinate.

**[The AI Observatory](https://www.technologyreview.com/2026/08/18/1142226/how-people-use-ai/)** (MIT TR, 2026-08-18): the largest independent aggregation of real consumer use — 85,633 turns, 24,521 conversations, 5,000 users, 52 models, 2023–2025 (Stanford STAIR + MIT Media Lab). Applying Anthropic Economic Index methods filters out **48% of conversations**; the excluded half carries most of the non-work load: health/relationship 44.2% vs 31.2%, harassment/hate 27.5% vs 5.66%, sexual content 16.7% vs 2.4%. OpenAI's own report: only 30% of consumer use is work-related. Companionship is rising (more small talk, longer conversations) while self-disclosure falls. Company-reported usage statistics — the basis of most "AI is a work tool" coverage — are work-shaped by construction.

**The work reading:** the Remote Labor Index numbers on this page measure one slice of adoption. The M365 result says AI shifts *who communicates what*; the Observatory says work is a minority of *what people actually do*. Both point the same direction: measure the mix, not just the mean.

→ Sources: arXiv 2608.15550 (2026-08-13); MIT TR (2026-08-18); [[00-Daily-Digests/2026-08-18]]

### Friction Was the Signal (2026-08-25)

The labor market's sorting mechanism just collapsed. **[It Should Be Harder to Apply for a Job. No, Really](https://www.wired.com/story/applying-for-a-job-is-too-damn-easy/)** (Kate Taylor, WIRED, 2026-08-25): one-click applications plus AI-written résumés and autofill turned the application itself into noise — Vendr's applications went from ~100 to hundreds (sometimes 1,000+), with a "good chunk" of "total bogus" AI-written fake candidates; Greenhouse logged "2,000 applicants in 24 hours for a job. That is a shitty experience for everyone." The response is a deliberate retreat: recruiters now say "we kind of want friction... The friction is good. We want to make it harder."

The friction hiring used to impose was information — it signaled genuine interest and minimal fit. When application cost falls to zero, effort stops sorting, and the burden shifts to whatever comes next: portfolio, referral, verification step, human screen. JLL's CTO frames the macro side ("Everyone was job hopping... Now, it is the polar opposite"; BLS openings peaked at a record 12.3M in March 2022, then declined for two years). Two worker-side lessons: (1) AI-written applications are a coordination problem — when everyone uses them, no one is distinguished; (2) the filters and ATS that absorb the flood become the judge, inheriting every calibration question from [[The Judge Problem]] — including self-preference, since many are AI-scored. See [[Task-Level AI Adoption]], [[The Turing Trap]].

### The Threshold Model of Substitution (2026-08-29)

The week's clearest mental model for where automation bites comes from physicist **Steve Hsu**, surfaced by Zvi in AI #183 (08-27):

> Below some threshold of human ability, AI is primarily a substitute; above it, AI becomes a complement.

Zvi adds the inversion: **below some threshold of AI ability, AI is primarily a complement; above it, AI becomes a substitute. As AI improves, more people's level of human ability falls below that line.** In law, that means today: top talent is worth more (judgment, expertise, client relationships — AI helps firms find the best), everyone else gets automated away — winner-take-most with a steadily rising requirement to remain a winner. The model generalizes to every knowledge domain this page tracks, and it makes the threshold a *moving line*, not a binary.

**Retraining doesn't move the line — and the "problem handled" frame is the danger.** Zvi's summary of the reskilling literature: job retraining programs "sound great, are very popular and don't work," raising the target population's employment ratio by only a few percent. The rare exceptions partner with specific employers who can't otherwise fill positions and end in direct job placement — but that doesn't scale. The real danger is treating retraining as a serious answer to displacement: it is a small positive and a large false comfort. This sharpens the [[Education]] page's entry-level finding from the other side — reskilling people into AI-accelerable skills resubmits them to the same automation pressure (see the Capability Ladder section above for the counter-framework).

**Gates' preference cascade.** Bill Gates has moved from "bumpy transition" to "economic catastrophe" framing (MIT TR interview, 08-26 — already covered in [[00-Daily-Digests/2026-08-26]]). Zvi's meta-point: Gates is a barometer of a **preference cascade** — AI-concern stops looking odd among Very Serious People, and the politics of the threshold change when the connected start treating it as real. "AI will either be the greatest equalizer ever invented, or the worst source of injustice."

**Physical work crosses too — Meta's data-center robots (08-28).** WIRED: Meta is testing robots (Kinova Gen3 arms, Watney Robotics, ABB) for cable swapping, server power-cycling, and device restarts; one worker estimates a successful bot could replace up to 80% of some people's workloads — "We thought those of us performing the physical tasks were safe for a while, but not anymore. It's coming for us all, unfortunately." Meta's response — "we need more workers, not fewer" amid the biggest infrastructure boom since WWII — is technically true about aggregate demand and silent about individual security: the cable-swap line has crossed, and the displaced worker's skills don't transfer automatically. The threshold model predicts exactly this pattern: the least-glamorous, most-bounded physical tasks cross first, precisely because their loss functions are symmetric.

**The agent-FOMO trap is the threshold's psychological shadow.** Zvi (AI #183, citing WSJ's Katherine Bindley): "Every minute that I'm not working, I'm missing out on not doing a week's worth of work" — the agent-multiplier effect that pushes knowledge workers into constant availability. If the complement side of the line rewards doubling marginal productivity, the individual response (work more, sleep less) is itself a form of agency surrender. The threshold model needs the counterweight this wiki has tracked since [[Cognitive Surrender]]: doubling output is only agency if the direction is chosen.

→ Sources: [Zvi, "AI #183: Pre Post Mortem"](https://thezvi.substack.com/p/ai-183-pre-post-mortem) (2026-08-27); [WIRED, "Inside Meta's Push to Put Robots to Work in Data Centers"](https://www.wired.com/story/inside-metas-experiments-with-data-center-robots/) (2026-08-28); [[00-Daily-Digests/2026-08-29]]

## Related Pages
- [[Work]]
- [[AI Executive Assistants]]
- [[Open Questions]]
- [[Frontier Firm]]
- [[AI Field Experiment Evidence]]

## Tags
#future-of-work #augmentation #risk
