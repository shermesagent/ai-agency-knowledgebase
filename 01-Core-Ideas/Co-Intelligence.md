# Co-Intelligence

## Core Idea
Co-intelligence was Ethan Mollick's practical frame for the chatbot era: invite AI into meaningful work, test it against reality, and keep humans responsible for goals, judgment, taste, and accountability. As of June 2026, Mollick has retired this frame in favor of **Co-Existence** — working with AI agents that are *sometimes, but not always, better than you*. The transition is driven by data: AI now writes 80% of Anthropic's code, coding agents produce 17x more code, and agents complete 50+ step professional workflows. Co-intelligence assumed humans at the center and chatbots as helpers. Co-existence recognizes that AI is now genuinely superior at some tasks — and the skill is knowing which is which.

## Why It Matters
For a [[Superagency]] wiki, the co-intelligence-to-coexistence transition is the framework update that keeps the agency thesis honest. The original co-intelligence frame was appropriate for 2024's chatbot world. In 2026's agent world, where AI writes most of the code that builds AI, pretending the relationship is always collaborative obscures the genuine asymmetry at specific tasks. The Superagency thesis must now answer: what does human agency look like when AI is sometimes, but not always, better than you?

## The Co-Existence Framework (Mollick, June 2026)
- **New book:** *Co-Existence: The Next Phase of AI* (October 20, 2026, pre-order at co-existence.ai)
- **Core shift:** From "AI as helper" to "AI as sometimes-superior collaborator"
- **Mollick's own practice:** He wrote every chapter draft himself ("AI is not a great long-form writer... it has difficulty telling good stories, it has instantly obvious textual tells, and it is kind of dull to read too much of"). He used AI as readers, fact-checkers, and un-stickers. He let Claude Code build his book website in minutes.
- **The em-dash test:** Mollick deliberately used fewer em-dashes in Co-Existence "in a desperate attempt to continue to prove the text was human" — a practical authenticity signal in an AI-saturated writing environment.
- **Key data driving the transition:** Anthropic reports AI writes 80% of its code (each developer shipping 8x more); a separate study found coding agents led to 17x more code; Salesforce standardized on Claude Code with no token limits.

### CollabSkill: Measuring Collaboration Quality (June 2026)
- The CollabSkill benchmark (arXiv 2606.09833) provides the first rigorous empirical test of the Co-Existence thesis: **is "working well with humans" a distinct capability from "working well alone"?** Yes. Across 93 real workers and 386 sessions, agent rankings on collaboration diverge meaningfully from autonomous benchmarks — Claude Code ranks first on collaboration where Codex leads on autonomy.
- **Key finding for Co-Existence:** Practical experience, not technical skill, drives collaboration quality. This validates Mollick's core claim — that the skill of working with AI is learnable, not innate, and benefits from hands-on practice. The benchmark also shows substantial inter-human variability, confirming that Co-Existence is not one-size-fits-all: different humans collaborate differently with the same agent.
- **The bayesian skill model:** By disentangling human and AI contributions, CollabSkill makes visible what Co-Existence implies — that the quality of the output depends on the specific human-agent pairing, not just the agent's capability.

### Human-AI Coordination Zones: The Design Language for Co-Existence (June 2026)
- The Human-AI Coordination Zones framework (arXiv 2606.09848) provides the missing design vocabulary for Co-Existence in practice. Analyzing 60 commercial AI applications, it identifies four zones:
  1. **Done-for-me:** AI executes, human consumes
  2. **Done-under-me:** AI executes, human monitors and approves
  3. **Done-with-me:** AI assists, human leads
  4. **Done-without-me:** Human works independently
- **Practical value for Co-Existence:** The framework makes explicit what is often implicit — who is doing what. The Co-Existence calibration skill (knowing when the AI is better than you) requires knowing which zone you're in. The default drift in AI products is toward "done-for-me" — the framework provides a language to push back and deliberately choose the right zone for each task.
- The framework also includes an **input taxonomy** (prompted, sparked, inferred, layered) and **coordination curves** for mapping how the human-AI relationship changes over the course of a task. This is the practical counterpart to CollabSkill's measurement — one measures how well collaboration works, the other designs how collaboration should work.

## Best Supporting Sources
- [Co-Existence and the End of Co-Intelligence](https://www.oneusefulthing.org/p/co-existence-and-the-end-of-co-intelligence), Ethan Mollick, June 4, 2026 — announces the framework transition and new book, with practical demos of AI's visual evolution.
- [Co-Intelligence: Living and Working with AI](https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/), Ethan Mollick, 2024 — the original practical guide (still relevant for the core practices).
- [Anthropic: Recursive Self-Improvement](https://www.anthropic.com/institute/recursive-self-improvement), June 2026 — AI writes 80% of Anthropic's code.
- [CollabSkill: Evaluating Human-Agent Collaboration on Real-World Tasks](https://arxiv.org/abs/2606.09833), June 2026 — 93 workers, 386 sessions; Claude Code leads collaboration rankings where Codex leads autonomy; practical experience drives collaboration quality.
- [Human-AI Coordination Zones](https://arxiv.org/abs/2606.09848), June 2026 — four-zone design framework (done-for-me, done-under-me, done-with-me, done-without-me) for designing human-in-the-loop agentic AI experiences.
- [[AI as Copilot]] — wiki frame for augmentation over replacement.
- [[AI Agent Revolution]] — the agent paradigm shift that makes Co-Existence necessary.

## Practical Examples
- Ask AI for three drafts, then use human taste and evidence to choose and revise one.
- Use AI as a critique partner: "what am I missing, what evidence would change this, and what could go wrong?"
- Have AI roleplay different reader perspectives on your writing to catch blind spots.
- Use AI learning/tutoring modes (Gemini Guided Learning, ChatGPT /learn, Claude learning style) to get the AI to ask YOU questions rather than give you answers.
- Apply the Co-Existence test: for each AI interaction, ask "was the AI better than me at this?" If yes, learn from it. If no, override it. The skill is calibration.
- Avoid the "meaning-shaped attention vampire": AI-generated text that sounds insightful but contains no actual human meaning.

## Risks / Limits
- Co-intelligence can become overreliance if users stop checking sources and assumptions.
- **Co-Existence risk:** The frame works best for domain experts who can tell when the AI is better. For novices, "sometimes better than you" is a recipe for undetected errors and misplaced trust.
- **Cognitive surrender** (Wharton, 2026): people stop thinking about problems and accept AI output even when wrong. The transition to Co-Existence could accelerate surrender if people default to "the AI is probably better than me."
- **The AI literacy paradox** (Yazan et al., 2026): more AI-literate users report lower trust but are MORE persuaded and MORE reliant on AI advice.
- In consequential settings, collaboration still needs [[Responsible Deployment]] practices.
- The frame works best when the human has enough domain knowledge to notice weak or fabricated output.

## Related Pages
- [[Superagency]]
- [[AI as Copilot]]
- [[AI Agent Revolution]]
- [[Cognitive Surrender]]
- [[Work]]
- [[Human Review Checkpoints]]
- [[Digital Fiduciary Duty]]
- [[Creativity]]

## Tags
#augmentation #practical-ai #human-agency #future-of-work #ai-agents
