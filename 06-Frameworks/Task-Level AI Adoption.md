# Task-Level AI Adoption

## Core Idea
Task-level AI adoption means evaluating AI one task at a time instead of asking whether an entire job, course, department, or institution should “use AI.” The practical question is: should this task be automated, augmented, human-only, or prohibited for AI?

## Why It Matters
This framework keeps [[Superagency]] grounded. It avoids both blanket hype and blanket bans by matching AI use to risk, evidence, human value, and accountability.

## Best Supporting Sources
- [The Anthropic Economic Index](https://www.anthropic.com/economic-index) — useful task-level data on collaboration versus delegation patterns.
- [Future of Work with AI Agents](https://futureofwork.saltlab.stanford.edu/) — audits automation and augmentation potential across work tasks.
- [[The Turing Trap]] — warns that substitution and augmentation have different social consequences.
- ["How People Are Really Using AI in 2026"](https://hbr.org/2026/06/how-people-are-really-using-ai-in-2026), Zao-Sanders / HBR, June 2026 — third annual survey: widening range of real-world AI uses; shifts in emphasis rather than stark ruptures; growing anxiety about cognitive surrender. Corporate-specific top-25 use cases added.
- ["AI Assistance for Discretionary Work"](https://arxiv.org/abs/2606.03095), Mahinpei et al., 2026 — RCT: AI drafts increased feedback by 10.8pp. Editable scaffolding as task-level augmentation design pattern.

## Practical Examples
Use four labels during workflow review:
1. **Automate:** low-risk, repetitive, easily checked tasks.
2. **Augment:** tasks where AI drafts, retrieves, critiques, or suggests while a human owns judgment.
3. **Human-only:** tasks where relationship, values, embodied context, or legitimacy are central.
4. **Prohibit AI:** tasks where privacy, safety, law, or dignity make delegation inappropriate.

### Infrastructure Readiness: The Task-Level Agent Gap (July 2026)

A new controlled experiment (arXiv 2607.12056, July 2026) reveals that task-level adoption depends on infrastructure, not just AI capability. Three browser-agent models ran 300 trials on identical website prototypes:

- **Agent-ready websites:** 89.3% strict success rate, 6.49 average steps
- **Human-only websites:** 49.3% strict success rate, 9.31 average steps

The gap is not about AI capability — it's about whether the digital environment is **legible** to the agent. The same agent, same task, same products — only the website's design changed, and success rates nearly doubled.

**Practical implication:** Add a fifth dimension to the task-level classification framework: **infrastructure readiness.** Before labeling a task as "automate" or "augment," ask: does the digital environment support agent access? A task that is technically automatable may fail in practice because the website, API, database, or platform was designed for human interaction only.

**The four agent-readiness audit questions:**
1. Can the agent programmatically discover what it needs (product details, form fields, available actions)?
2. Can the agent reliably navigate multi-step workflows without hitting CAPTCHAs, client-side rendering blocks, or rate limits?
3. Can the agent complete and submit structured transactions (forms, orders, applications)?
4. Does the platform distinguish between "malicious bot" and "user-delegated agent" — or block both indiscriminately?

This connects to the Agent-Ready Websites finding (see [[AI Agent Revolution#Designing Agent-Ready Websites|Designing Agent-Ready Websites]]), the Agent-First Web design principles, and the normative infrastructure gap identified in the agentic web literature. The task-level adoption framework must account for an environment that was not built for the agents now trying to operate within it.

→ Also see: [[AI Agent Revolution]] for the Least Autonomy framework (access control for agentic systems), the Agent Economy Insurance Stack (economic governance), and the Theory of Least Autonomy (security architecture).

## Risks / Limits
- Task labels can drift; revisit them as tools, data, and stakes change.
- A low-risk task can become high-risk when connected to sensitive data or consequential decisions.
- Workers and users should be involved in the classification, not merely managed by it.
- **The engagement barrier (June 2026):** Task-level classification assumes people will use the AI if the task is appropriate. Stanford SCALE research (June 2026) found this assumption is wrong — students given access to AI tutors used them for just 2-5 minutes per week. The engagement gap is a distinct barrier from the technical, organizational, and trust barriers already in the framework. A task can be clearly appropriate for augmentation and still generate zero benefit if nobody uses the tool. The practical response: task-level adoption frameworks must add an engagement dimension — before classifying a task as "augment" or "automate," verify that the intended users actually want to use the AI for that task.

## Related Pages
- [[Work]]
- [[AI Use Case Evaluation Rubric]]
- [[Risk-Benefit Matrix]]
- [[Responsible Deployment]]

## Tags
#practical-ai #future-of-work #ai-agents #responsible-ai
