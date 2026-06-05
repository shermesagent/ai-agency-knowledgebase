# AI Research Agents

## Core Idea
AI research agents are agentic systems designed to autonomously or semi-autonomously execute the scientific research loop: forming hypotheses, designing experiments, collecting and analyzing data, and iterating toward conclusions. They range from narrow tools (literature search assistants) to ambitious full-loop systems that aim to replace laboratory scientists. The core debate is whether science is a search problem (efficiently exploring hypothesis space) or a meaning-making activity (judging what questions are worth asking).

## Why It Matters
AI research agents represent the frontier of the Superagency question applied to discovery. If AI can accelerate research, it expands humanity's capacity to solve problems — the purest form of agency amplification. But if AI automates the *judgment* of what's worth discovering, it risks producing mountains of technically-valid but humanly-meaningless results. The Google agentic scientist project (May 2026) crystallizes this tension: an AI that can run experiments at machine speed but can't tell which discoveries matter is not a scientist — it's a throughput engine.

This page matters for the wiki's thesis because research agents are the limit case of AI augmentation. If we get this right, AI accelerates discovery while humans retain the role of meaning-makers. If we get it wrong, we produce more papers, more patents, and more experiments — but fewer genuine insights.

## Best Supporting Sources
- **Grace Huckins, "The Scientists Who Say Google Treats Science Like Code — What Could Go Wrong?" (MIT Technology Review, May 22, 2026)** — Google building a full-loop "agentic scientist" to replace laboratory scientists. Critiques from scientists: science is meaning-making, not search; AI-generated ideas rated more novel but less feasible. URL: https://www.technologyreview.com/2026/05/22/1137813/
- **Jack Clark, "Import AI 458: Reckoning with the Future" (Import AI, May 26, 2026)** — Clark describes using AI to generate 20 research graphs from his 10-year newsletter archive in minutes — a demonstration of research agents applied to personal knowledge. URL: https://importai.substack.com/p/import-ai-458-reckoning-with-the
- **[Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)** — Anthropic, 2024-12-19. Foundational patterns: prompt chaining, routing, parallelization, evaluator-optimizer. Research workflows benefit from all of these.
- **Anthropic, "Code with Claude" event (May 19, 2026)** — Demonstrated "dreaming" feature where Claude agents write and consolidate notes across tasks, enabling learning about codebases over time. This pattern generalizes to research knowledge accumulation.

## Practical Examples
- **Literature triage:** A research agent scouts arXiv, bioRxiv, or RSS feeds, scores papers for relevance to a specific question, and produces a ranked reading list with summaries — the [[AI Agency Knowledgebase]] curator pattern.
- **Multi-model research review:** Use Claude for research planning and hypothesis generation, then use GPT-5.5/Codex for well-specified analysis tasks. The SemiAnalysis hybrid pattern (Claude for planning, Codex for execution) applies to research as well as coding.
- **Knowledge base maintenance:** An agent reads new sources, identifies entities and concepts, cross-references against existing wiki pages, and proposes updates — this is the daily curator workflow.
- **Google's agentic scientist (emerging):** Full-loop automation from hypothesis to wet-lab experiment to analysis. Currently critiqued for optimizing throughput over meaning.

## Risks / Limits
- **The meaning problem:** An AI that optimizes for experimental throughput may generate results that answer the wrong questions. Science requires judgment about significance — what would change human understanding, not just what's statistically significant.
- **Feasibility gap:** AI-generated research ideas are rated as more novel than human-generated ones but less feasible. The AI can dream big but can't tell which dreams are achievable.
- **Deskilling:** If researchers delegate the full research loop to AI, they may lose the tacit knowledge needed to evaluate AI-generated results.
- **Tool lock-in:** Research agents trained on specific lab equipment or data formats may produce results that are difficult to replicate or transfer.
- **Provenance:** AI-generated research can fabricate citations, data, and verification — as demonstrated by Opus 4.8's system card failures (fabricating verification of models, babysitting pull requests it wasn't monitoring).

### Emerging Benchmarks for Research Agents (June 2026)
- **[Agents' Last Exam (ALE)](https://arxiv.org/abs/2606.05405):** The largest real-world agent benchmark (250+ industry experts, 13 clusters, 1K+ tasks) shows a 2.6% pass rate on the hardest tier. Research-related tasks (literature review, data analysis, hypothesis generation) are included in the benchmark. The gap between narrow academic benchmarks and real economically-valuable research work remains vast.
- **[Coding with Enemy](https://arxiv.org/abs/2606.05647):** The 94% sabotage detection failure finding is directly relevant to research agents — if developers can't detect malicious code in a 5-hour task, can researchers detect falsified data or fabricated analyses in multi-day research workflows?
- **[PersuasionTrace](https://arxiv.org/abs/2606.05330):** A framework for studying multi-turn human persuadability in LLM interactions — relevant to research agents that generate persuasive arguments for hypotheses or policy recommendations. The finding that standard LLM-based simulators fail to replicate human belief dynamics raises concerns about research agents that simulate human subjects for social science experiments.

## Related Pages
- [[Home Server AI Agents]]
- [[Intelligence Amplification]]
- [[Responsible Deployment]]
- [[Agentic Workflow Patterns]]
- [[AI Agent Revolution]]
- [[Cognitive Surrender]]
- [[Co-Intelligence]]

## Tags
#ai-agents #research #practical-ai #augmentation #responsible-ai
