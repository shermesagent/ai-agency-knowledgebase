# Home Server AI Agents

## Core Idea
Self-hosted AI agents can make agency tangible: personal automations, private dashboards, local knowledgebases, monitoring, writing support, and custom workflows.

## Why It Matters
Home-server agents turn [[Superagency]] into a personal infrastructure practice. They let individuals build small systems that summarize, monitor, remind, research, and coordinate around their own goals. The healthiest pattern is not maximum autonomy; it is local control, explicit permissions, observability, and human approval for consequential actions.

## Best Supporting Sources
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents), Anthropic, 2024 — favors simple workflows, prompt chaining, routing, parallelization, orchestrator-worker patterns, and evaluator loops before broad autonomy.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST — useful for personal systems too: map the use case, measure behavior, manage risk, govern permissions.
- [Guidance for Safe Foundation Model Deployment](https://partnershiponai.org/wp-content/uploads/1923/10/PAI-Model-Deployment-Guidance.pdf), Partnership on AI — reinforces documentation, monitoring, and adaptation as capabilities and uses evolve.

## Practical Examples
- A daily research curator that fetches sources, scores relevance, writes a draft digest, and waits for human review before publishing.
- A home operations agent that monitors services and proposes fixes but requires approval before destructive commands.
- A family planning assistant that drafts meal plans, schedules, and tutoring practice without storing unnecessary sensitive data.
- A personal knowledgebase maintainer that updates Markdown pages, preserves URLs, and commits changes to Git.

## Risks / Limits
- Tool permissions can turn a helpful assistant into an accidental deletion, spending, or privacy problem.
- Self-hosting does not automatically mean safe; logs, backups, secrets management, and network exposure matter.
- Agents should start read-only, then gain narrow write permissions after dry runs.
- Human approval checkpoints should remain for sending messages, purchases, file deletion, public posts, and security changes.

## Related Pages
- [[AI Research Agents]]
- [[AI Executive Assistants]]
- [[Responsible Deployment Loop]]
- [[Agentic Workflow Patterns]]
- [[AI as Copilot]]

## Tags
#home-server-ai #ai-agents #practical-ai
