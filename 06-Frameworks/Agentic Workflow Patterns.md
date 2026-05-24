# Agentic Workflow Patterns

## Core Idea
Agentic workflow patterns are repeatable ways to combine LLM calls, tools, memory, evaluation, and human review so AI can accomplish useful work without pretending that every task needs a fully autonomous agent.

## Why It Matters
The practical path to [[Superagency]] is not “let an agent do everything.” It is to identify bounded work where AI can draft, search, route, critique, or coordinate while humans retain goals, context, taste, and accountability. Anthropic’s guidance on building effective agents argues for starting with simple workflows and adding autonomy only when the task demands it.

## Best Supporting Sources
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents), Anthropic, 2024-12-19 — distinguishes predictable workflows from more open-ended agents and describes patterns such as prompt chaining, routing, parallelization, orchestrator-worker, and evaluator-optimizer loops.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST, 2023/2024 — provides the Map, Measure, Manage, Govern loop that should wrap higher-impact agent workflows.
- [Co-Intelligence](https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/), Ethan Mollick, 2024 — reinforces that practical gains come from repeated human-AI collaboration, not blind delegation.

## Practical Examples
- **Prompt chain:** Research question → source list → source scoring → synthesis → human edit. Useful for [[AI Research Agents]].
- **Routing:** Classify incoming email, tickets, or documents, then send each to a specialized prompt or human queue.
- **Parallelization:** Ask several agents to scout sources, critique a plan, or generate alternatives, then compare outputs.
- **Evaluator-optimizer:** Generate a draft, score it against a rubric, revise, and surface remaining uncertainties.
- **Orchestrator-worker:** A planning agent decomposes a task into small subtasks, delegates them, and assembles a result for human review.
- **Human checkpoint:** Stop before publishing, sending, purchasing, deleting, grading, disciplining, or making any high-consequence decision.

## Risks / Limits
- Agentic systems can compound errors when they act on unverified intermediate outputs.
- Tool access can create privacy, security, or financial risks if permissions are too broad.
- More autonomy increases observability needs: logs, dry runs, approval gates, rollback plans, and incident records.
- Many “agent” tasks are better solved with a simple checklist, script, or deterministic workflow.

## Related Pages
- [[Home Server AI Agents]]
- [[AI Research Agents]]
- [[Responsible Deployment Loop]]
- [[AI Use Case Evaluation Rubric]]
- [[AI as Copilot]]

## Tags
#ai-agents #practical-ai #augmentation #responsible-ai #tools
