# AI Coding Agents

## Core Idea
AI coding agents can scaffold projects, debug, write tests, refactor, document, and operate systems when paired with version control and human review.

## Why It Matters
Coding agents are one of the most concrete places to observe augmentation: they can turn intent into tests, scaffolds, refactors, deployment checks, documentation, and debugging hypotheses. But the agency gain depends on whether developers keep architectural judgment, code ownership, review discipline, and learning rather than becoming passive approvers.

## Best Supporting Sources
- [Impact of Generative AI in Software Development](https://services.google.com/fh/files/misc/dora-impact-of-generative-ai-in-software-development.pdf), Google/DORA, 2025 — argues for measuring AI adoption through software-delivery outcomes, developer trust, feedback loops, and long-term improvement rather than assuming instant productivity.
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents), Anthropic, 2024 — provides workflow patterns such as prompt chaining, routing, parallelization, and evaluator loops that can be adapted to coding agents.
- [Navigating the Jagged Technological Frontier](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf), Dell'Acqua et al., 2023 — reminds coding teams that AI can help strongly inside its frontier and mislead outside it.
- [Using AI to Write Better Code More Slowly](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/), Nolan Lawson, 2026 — practitioner argument for using multiple AI models as independent code reviewers to find bugs and improve quality rather than speed; multi-model review with near-zero false positive rate.

## Practical Examples
- Use agents to create failing tests first, propose a patch, run checks, and summarize the diff for human review.
- Route low-risk maintenance tasks to AI workflows while keeping architecture, security, data migration, and user-impact decisions human-led.
- Track cycle time, escaped defects, review burden, developer learning, and rollback frequency rather than only lines of code or tickets closed.
- Use Offloading Score methodology to measure how much cognitive effort is being delegated vs. amplified.
- Audit for the maternity-leave AI gap: ensure returning team members have structured AI-literacy onboarding rather than being left to self-train.

## Risks / Limits
- Avoid treating one positive case study as universal proof.
- Watch for overreliance, privacy risks, bias, deskilling, labor displacement, and concentration of power.
- Update this section whenever strong counterarguments appear.
- Agents with shell, network, or production access need least privilege, logs, dry runs, and explicit approval gates.

## Related Pages
- [[Home Server AI Agents]]
- [[Responsible Deployment]]
- [[AI Use Case Evaluation Rubric]]
- [[Agentic Workflow Patterns]]
- [[Entry-Level Work Crisis]]
- [[Agentic Technical Debt]]

## Tags
#ai-agents #augmentation #practical-ai #tools
