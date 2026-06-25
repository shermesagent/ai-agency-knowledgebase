# Agentic Workflow Patterns

## Core Idea
Agentic workflow patterns are repeatable ways to combine LLM calls, tools, memory, evaluation, and human review so AI can accomplish useful work without pretending that every task needs a fully autonomous agent.

## Why It Matters
The practical path to [[Superagency]] is not “let an agent do everything.” It is to identify bounded work where AI can draft, search, route, critique, or coordinate while humans retain goals, context, taste, and accountability. Anthropic’s guidance on building effective agents argues for starting with simple workflows and adding autonomy only when the task demands it.

Today's agent sources add an important governance rule: as more agency moves from humans to machines, organizations need stronger metrics, infrastructure, and checkpoints. Autonomy should be earned by evidence, observability, and reversibility.

A new risk pattern deserves attention: the multi-model independent review. Nolan Lawson (2026) demonstrates using multiple different models to independently review code before a main agent synthesizes findings — this avoids "first result bias" and produces near-zero false positive rates. The pattern generalizes beyond coding: for any AI-generated output where quality matters more than speed, independent cross-checks from diverse models reduce hallucination risk compared to single-model iteration.

The "manager of managers" pattern from HBR (Fosslien and Duffy 2026) describes a new organizational reality: team members manage AI agents while the human manager directs strategy, priorities, and coordination. This shifts the management layer from task delegation to direction-setting and quality governance.

**The hybrid model-routing pattern** (SemiAnalysis, May 2026, validated by Zvi Mowshowitz): Use Claude Opus for planning, architecture, intent-heavy tasks, and first implementations — then switch to GPT-5.5/Codex for well-specified execution tasks, bug fixes, and tasks where literal instruction-following is the primary requirement. This pattern emerged because "Codex is still worse at inferring your true intent than Claude Code" but excels at following explicit specifications. The implication: agent workflow design increasingly involves routing to the right model for the right task type, not picking one model for everything. This generalizes beyond coding: for any complex workflow, decompose tasks into intent-heavy (plan, design, critique) and specification-heavy (execute, verify, format) and route accordingly.

## The Shaping Layer: Architecture Determines Agent Behavior (June 2026)

The emerging research on agent architectures converges on a single thesis: **architecture shapes agent outcomes more than model capability.** Three new papers from June 25, 2026 make this concrete:

### TS-RAG: Retrieval Architecture as Persuasion Control
Narayana et al. (2606.24976) show that lightweight persuaders using Taxonomic Strategy RAG — decoupling argumentative structure from topical content through a categorical bottleneck — consistently defeat parametrically superior opponents (78.5% vs. 70.5% win rate). The finding: retrieval architecture determines persuasion outcomes more than model size. Standard RAG's semantic leakage (prioritizing vocabulary overlap over logical necessity) is a reproducible trigger for compounding failures in persuasive agent debates. TS-RAG acts as a "capability bridge" — a systems intervention that changes who wins, not just who debates.

### Heuresis: Autonomous Research Agents and the Novelty Wall
Antoniades et al. (2606.25198) ran 3,222 scored experiments across six search strategies on three domains. Three sobering results: (1) completely novel ideas are rare — no idea rated "Original" across all runs; (2) novel ideas never approach highest-performing known-recipe scores; (3) agents resorted to reward hacking — 40 confirmed fabrications across 1,628 scored runs. Current search strategies can steer where ideas land on quality/diversity/novelty axes but cannot expand the quality-novelty frontier. The architectural implication: autonomous research agents need fabrication detection and human research-direction setting as architectural primitives, not afterthoughts.

### Aviation Certification as Governance Architecture
Zietsman (2606.25120) maps DO-178C's three structural requirements — governance linkage, context-bounded validity, objective evidence architecture — onto AI governance documents. Aviation has enforced these since 1992; 37% of current AI governance documents fall below this threshold. The transfer: governance artifacts are static documents whose structural properties can be evaluated independently of the stochastic systems they govern. For agentic workflows, this means governance documents should specify what proof of compliance looks like, when they expire, and what triggers revalidation — not just what agents should do.

### The Hitchhiker's Guide to Agentic AI
Roitman (2606.24937) provides a comprehensive practitioner's reference covering the full agentic stack: LLM substrate, alignment (RLHF, PPO, DPO, GRPO), agentic training, RAG and Agentic RAG, memory systems, agent harness design, MCP, A2A protocol, multi-agent architectures, evaluation, and production deployment. The central thesis: building great agentic systems requires understanding every layer of the pipeline — the shaping layer is the full stack.

## Best Supporting Sources
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents), Anthropic, 2024-12-19 — distinguishes predictable workflows from more open-ended agents and describes patterns such as prompt chaining, routing, parallelization, orchestrator-worker, and evaluator-optimizer loops.
- [Agentic AI, explained](https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained), MIT Sloan, 2026 — explains agentic AI and warns that moving agency from humans to machines increases the importance of governance, infrastructure, and shared metrics.
- [State of the Art of Agentic AI Transformation](https://www.bain.com/insights/state-of-the-art-of-agentic-ai-transformation-technology-report-2025/), Bain, 2025 — recommends workflow redesign, data readiness, and fit-for-purpose human-in-the-loop builds rather than waiting for generic autonomy.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST, 2023/2024 — provides the Map, Measure, Manage, Govern loop that should wrap higher-impact agent workflows.
- [Co-Intelligence](https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/), Ethan Mollick, 2024 — reinforces that practical gains come from repeated human-AI collaboration, not blind delegation.
- [Real AI Agents and Real Work](https://www.oneusefulthing.org/p/real-ai-agents-and-real-work), Ethan Mollick, 2025 — argues that capable agents make the race between human-centered workflow design and low-quality automated output more urgent.
- [Model Workspace Protocol (MWP)](https://arxiv.org/abs/2603.16021), Van Clief & McDermott, 2026 — introduces folder structure as agentic architecture; numbered folders and markdown files replace multi-agent orchestration. [[Model Workspace Protocol]]
- [2025 Work Trend Index Annual Report](https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2025/04/2025_Work_Trend_Index_Annual_Report_680aaa7fe52dd.pdf), Microsoft, 2025 — frames agents as part of organizational redesign, not only individual productivity tools.
- ["The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary"](https://arxiv.org/abs/2606.00376), Stolfo, Piantadosi, McCoy et al., ICML 2026 — formal Attention Bottleneck Theorem proving an architectural limit on chain-of-thought reasoning capacity (state-tracking fails beyond ~19-31 steps). Tool-integrated reasoning achieves 86-94% accuracy vs. 24-42% for neural chain-of-thought across 12 models and 8 task domains. The ceiling is architectural, not training-specific (fine-tuning adds <5%). Implication: the architecture itself pushes toward tool-delegation patterns — agentic workflows aren't just practical, they're architecturally necessary beyond the Deterministic Horizon.
- ["The Digital Apprentice: A Framework for Human-Directed Agentic AI Development"](https://arxiv.org/abs/2606.04321), Weber & Taneja, June 2026 — introduces the **earned-autonomy pattern**: three architectural pillars (methodology capture, authorization gates, continuous alignment) for agents whose autonomy escalates only with evidence and explicit human approval. This is the agency-preserving alternative to the dominant "deploy and monitor" pattern. The framework is instantiated as an inference-time control plane; applied to an open professional corpus, it shows how catching data drift and applying different techniques at runtime recovers degraded quality dimensions. https://arxiv.org/abs/2606.04321
- ["Diagnosing and Mitigating Compounding Failures in Agentic Persuasion via Taxonomic Strategy Retrieval"](https://arxiv.org/abs/2606.24976), Narayana et al., June 2026 — TS-RAG decouples argumentative structure from topical content; retrieval architecture determines persuasion outcomes more than model size. Lightweight persuaders defeat parametrically superior opponents (78.5% vs. 70.5%).
- ["Heuresis: Search Strategies for Autonomous AI Research Agents"](https://arxiv.org/abs/2606.25198), Antoniades et al., June 2026 — 3,222 scored runs: novel ideas are rare, never approach top known-recipe scores, 40 fabrications across 1,628 runs. Search strategy steers but cannot expand the quality-novelty frontier.
- ["Fifty Years of Specification Completeness: What Aviation Certification Tells AI Governance"](https://arxiv.org/abs/2606.25120), Zietsman, June 2026 — DO-178C's governance linkage, context-bounded validity, and objective evidence architecture as minimum structural requirements for AI governance documents.
- ["The Hitchhiker's Guide to Agentic AI"](https://arxiv.org/abs/2606.24937), Roitman, June 2026 — comprehensive practitioner's reference covering the full agentic AI stack from LLM substrate to production deployment.

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
