# Human Review Checkpoints

## Core Idea
Human review checkpoints are explicit stopping points in AI workflows where a person must inspect the work, verify evidence, and approve or revise the next action before the system proceeds.

## Why It Matters
As [[Agentic Workflow Patterns]] become more capable, organizations and individuals will be tempted to let AI move directly from suggestion to action. That can expand agency when the action is low-risk and reversible, but it can reduce agency when systems publish, send, buy, delete, grade, discipline, diagnose, or alter infrastructure without meaningful human ownership.

The checkpoint idea turns [[Responsible Deployment]] into a concrete design rule: increase autonomy only after deciding where humans must retain judgment, context, taste, values, and accountability.

## Best Supporting Sources
- [Agentic AI, explained](https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained), MIT Sloan, 2026 — notes that moving agency from humans to machines increases the importance of governance, infrastructure, and robust metrics.
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents), Anthropic, 2024 — recommends simple workflows, evaluator loops, and controlled tool use before open-ended autonomy.
- [Responsible AI Progress Report](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/documents/ai-responsibility-update-published-february-2025.pdf), Google DeepMind, 2025 — describes governance, evaluation, red teaming, privacy/security controls, provenance, and literacy as operational practices.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST — provides the Map, Measure, Manage, Govern loop that checkpoints can implement at workflow level.

## Practical Examples
- Require approval before an AI agent sends external email, posts publicly, purchases items, deletes files, changes infrastructure, or modifies financial records.
- In schools, require teacher review before AI-generated grades, student interventions, parent communications, or placement recommendations.
- In writing workflows, allow AI to draft and critique but require human approval before publication and before factual claims are treated as verified.
- In home-server automations, start with read-only agents; graduate to write access only after dry runs, logs, rollback plans, and approval gates.

## Risks / Limits
- Checkpoints can become rubber stamps if humans are overloaded or lack the context to review well.
- Too many checkpoints can make low-risk AI use unnecessarily slow; use risk-proportional review.
- A checkpoint is not a substitute for good system design, access control, logging, evaluation, and user training.
- Reviewers need authority to stop the workflow, not merely observe it.

## Related Pages
- [[Agentic Workflow Patterns]]
- [[Responsible Deployment]]
- [[Responsible Deployment]]
- [[AI Use Case Evaluation Rubric]]
- [[Open Questions]]
- [[Home Server AI Agents]]

## Tags
#responsible-ai #ai-agents #practical-ai #governance
