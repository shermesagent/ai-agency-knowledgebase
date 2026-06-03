# Agentic Workflow Patterns

## Core Idea
Agentic workflow patterns are repeatable ways to combine LLM calls, tools, memory, evaluation, and human review so AI can accomplish useful work without pretending that every task needs a fully autonomous agent.

## Why It Matters
The practical path to [[Superagency]] is not “let an agent do everything.” It is to identify bounded work where AI can draft, search, route, critique, or coordinate while humans retain goals, context, taste, and accountability. Anthropic’s guidance on building effective agents argues for starting with simple workflows and adding autonomy only when the task demands it.

Today's agent sources add an important governance rule: as more agency moves from humans to machines, organizations need stronger metrics, infrastructure, and checkpoints. Autonomy should be earned by evidence, observability, and reversibility.

A new risk pattern deserves attention: the multi-model independent review. Nolan Lawson (2026) demonstrates using multiple different models to independently review code before a main agent synthesizes findings — this avoids "first result bias" and produces near-zero false positive rates. The pattern generalizes beyond coding: for any AI-generated output where quality matters more than speed, independent cross-checks from diverse models reduce hallucination risk compared to single-model iteration.

The "manager of managers" pattern from HBR (Fosslien and Duffy 2026) describes a new organizational reality: team members manage AI agents while the human manager directs strategy, priorities, and coordination. This shifts the management layer from task delegation to direction-setting and quality governance.

**The hybrid model-routing pattern** (SemiAnalysis, May 2026, validated by Zvi Mowshowitz): Use Claude Opus for planning, architecture, intent-heavy tasks, and first implementations — then switch to GPT-5.5/Codex for well-specified execution tasks, bug fixes, and tasks where literal instruction-following is the primary requirement. This pattern emerged because "Codex is still worse at inferring your true intent than Claude Code" but excels at following explicit specifications. The implication: agent workflow design increasingly involves routing to the right model for the right task type, not picking one model for everything. This generalizes beyond coding: for any complex workflow, decompose tasks into intent-heavy (plan, design, critique) and specification-heavy (execute, verify, format) and route accordingly.

## Best Supporting Sources
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents), Anthropic, 2024-12-19 — distinguishes predictable workflows from more open-ended agents and describes patterns such as prompt chaining, routing, parallelization, orchestrator-worker, and evaluator-optimizer loops.
- [Agentic AI, explained](https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained), MIT Sloan, 2026 — explains agentic AI and warns that moving agency from humans to machines increases the importance of governance, infrastructure, and shared metrics.
- [State of the Art of Agentic AI Transformation](https://www.bain.com/insights/state-of-the-art-of-agentic-ai-transformation-technology-report-2025/), Bain, 2025 — recommends workflow redesign, data readiness, and fit-for-purpose human-in-the-loop builds rather than waiting for generic autonomy.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST, 2023/2024 — provides the Map, Measure, Manage, Govern loop that should wrap higher-impact agent workflows.
- [Co-Intelligence](https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/), Ethan Mollick, 2024 — reinforces that practical gains come from repeated human-AI collaboration, not blind delegation.
- [Real AI Agents and Real Work](https://www.oneusefulthing.org/p/real-ai-agents-and-real-work), Ethan Mollick, 2025 — argues that capable agents make the race between human-centered workflow design and low-quality automated output more urgent.
- [2025 Work Trend Index Annual Report](https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2025/04/2025_Work_Trend_Index_Annual_Report_680aaa7fe52dd.pdf), Microsoft, 2025 — frames agents as part of organizational redesign, not only individual productivity tools.
- ["The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary"](https://arxiv.org/abs/2606.00376), Stolfo, Piantadosi, McCoy et al., ICML 2026 — formal Attention Bottleneck Theorem proving an architectural limit on chain-of-thought reasoning capacity (state-tracking fails beyond ~19-31 steps). Tool-integrated reasoning achieves 86-94% accuracy vs. 24-42% for neural chain-of-thought across 12 models and 8 task domains. The ceiling is architectural, not training-specific (fine-tuning adds <5%). Implication: the architecture itself pushes toward tool-delegation patterns — agentic workflows aren't just practical, they're architecturally necessary beyond the Deterministic Horizon.

## Practical Examples
- **Prompt chain:** Research question → source list → source scoring → synthesis → human edit. Useful for [[AI Research Agents]].
- **Routing:** Classify incoming email, tickets, or documents, then send each to a specialized prompt or human queue.
- **Parallelization:** Ask several agents to scout sources, critique a plan, or generate alternatives, then compare outputs.
- **Evaluator-optimizer:** Generate a draft, score it against a rubric, revise, and surface remaining uncertainties.
- **Orchestrator-worker:** A planning agent decomposes a task into small subtasks, delegates them, and assembles a result for human review.
- **Human checkpoint:** Stop before publishing, sending, purchasing, deleting, grading, disciplining, or making any high-consequence decision. See [[Human Review Checkpoints]].
- **Human-in-the-loop agent collaboration (DeskCraft protocol):** Mid-turn exchanges (agent-initiated clarification, user-initiated interruption) + post-turn user-driven feedback. Formalized in [[DeskCraft benchmark]]. For any long-horizon agent workflow (>50 steps), build explicit mid-turn and post-turn human interaction points — agents that can't proactively clarify under uncertainty will fail. [[AI Agent Revolution]].
- **Trust-boundary trace sharing (InquiryBits):** AI conversation traces shared within team-level trust boundaries. Default to team visibility, not organizational surveillance. Professionals are broadly willing to share traces to support collaboration but comfort drops sharply outside close teams — trust boundaries matter more than information granularity. https://arxiv.org/abs/2606.02763
- **Editable scaffold dispatch:** AI produces a draft, critique, or analysis; human adopts, edits, or ignores at discretion. Proven in a randomized field experiment: TAs given AI feedback drafts increased feedback provision by 10.8pp (p<0.001) while preserving full control — the AI lowered the activation barrier without constraining the output. See [[AI Assistance for Discretionary Work]].

## Risks / Limits
- Agentic systems can compound errors when they act on unverified intermediate outputs.
- Tool access can create privacy, security, or financial risks if permissions are too broad.
- More autonomy increases observability needs: logs, dry runs, approval gates, rollback plans, and incident records.
- Many “agent” tasks are better solved with a simple checklist, script, or deterministic workflow.
- Agents can produce “infinite PowerPoints” or plausible busywork unless the workflow includes quality criteria and a human-owned outcome.
- Without shared metrics, organizations may not know whether agents are producing value or introducing new risk.

## Related Pages
- [[Home Server AI Agents]]
- [[AI Research Agents]]
- [[Responsible Deployment]]
- [[AI Use Case Evaluation Rubric]]
- [[Human Review Checkpoints]]
- [[AI as Copilot]]
- [[Frontier Firm]]
- [[AI Field Experiment Evidence]]

## Tags
#ai-agents #practical-ai #augmentation #responsible-ai #tools
