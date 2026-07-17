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

## Practical Examples
- Redesign one recurring process as a [[Frontier Firm]] workflow: AI drafts or routes the work, humans set goals and inspect exceptions, and the team measures whether quality and agency improve.
- Use [[Task-Level AI Adoption]] to label tasks as augment, automate, preserve-human, or prohibit-AI.
- Build internal learning ladders so junior workers use AI to learn faster rather than merely skipping practice.

## Risks / Limits
- Avoid treating one positive case study as universal proof.
- Watch for overreliance, privacy risks, bias, deskilling, labor displacement, and concentration of power.
- Update this section whenever strong counterarguments appear.
- “AI-operated” can imply worker displacement or managerial surveillance unless organizations explicitly protect human judgment, voice, and development.

## Related Pages
- [[Work]]
- [[AI Executive Assistants]]
- [[Open Questions]]
- [[Frontier Firm]]
- [[AI Field Experiment Evidence]]

## Tags
#future-of-work #augmentation #risk
