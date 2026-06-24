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

### Human-AI Collaboration Taxonomy: What "Collaboration" Actually Requires (Cukurova, June 2026)

Cukurova (2606.15509) provides the diagnostic precision the Co-Existence framework needs. Returning to long-standing accounts of collaborative learning, the paper reconstructs the requirements that a situation, interaction, and cognitive processes must meet before being called collaborative — and finds that most current human-AI interaction is better described as consultation, governance, delegation, or instruction rather than collaboration.

**The five-level diagnostic taxonomy of human-AI teaming:**
1. **Transactional**: AI responds to discrete prompts; no shared context or goals
2. **Situational**: AI adapts to immediate context but has no persistent relationship
3. **Operational**: AI maintains task state and can sequence actions, but the human directs
4. **Praxical**: AI and human share goals and divide labor dynamically with mutual awareness
5. **Synergistic**: AI and human engage in symmetric, negotiated interaction with shared regulation

Only the Synergistic level begins to satisfy the conditions the tradition places on collaboration: partly symmetric and negotiated relationship, shared and negotiable goals, low and shifting division of labor, interactive and synchronous exchange, and mutual modeling, grounding, and socially shared regulation.

**Practical value for Co-Existence:** The taxonomy makes explicit what Mollick's guide implies — that most AI use is Transactional or Operational, not Collaborative. The Co-Existence calibration skill (knowing when AI is better than you) requires knowing which level you're operating at. The default drift in AI products is toward Transactional convenience — the taxonomy provides a language to deliberately design for higher levels. Crucially, Cukurova argues that the functions needed for Synergistic interaction are "present-day engineering choices rather than capabilities to be awaited" — the barrier is design intent, not technical possibility.

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
- [Using AI Right Now: A Quick Guide](https://www.oneusefulthing.org/p/using-ai-right-now-a-quick-guide), Ethan Mollick, June 16, 2026 — practical adoption scaffold: pick a model, try three things, use context and branching. The operational companion to Co-Existence.
- [Co-Intelligence: Living and Working with AI](https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/), Ethan Mollick, 2024 — the original practical guide (still relevant for the core practices).
- [Anthropic: Recursive Self-Improvement](https://www.anthropic.com/institute/recursive-self-improvement), June 2026 — AI writes 80% of Anthropic's code.
- [CollabSkill: Evaluating Human-Agent Collaboration on Real-World Tasks](https://arxiv.org/abs/2606.09833), June 2026 — 93 workers, 386 sessions; Claude Code leads collaboration rankings where Codex leads autonomy; practical experience drives collaboration quality.
- [Human-AI Coordination Zones](https://arxiv.org/abs/2606.09848), June 2026 — four-zone design framework (done-for-me, done-under-me, done-with-me, done-without-me) for designing human-in-the-loop agentic AI experiences.
- [What Do You Mean by Human-AI Collaboration?](https://arxiv.org/abs/2606.15509), Cukurova, June 2026 — five-level diagnostic taxonomy (Transactional→Synergistic); most current AI use is not collaboration; genuine collaboration requires symmetric, negotiated interaction — an engineering choice, not a capability to await.
- [[AI as Copilot]] — wiki frame for augmentation over replacement.
- [[AI Agent Revolution]] — the agent paradigm shift that makes Co-Existence necessary.

## Practical Examples
- Ask AI for three drafts, then use human taste and evidence to choose and revise one.
- Use AI as a critique partner: "what am I missing, what evidence would change this, and what could go wrong?"
- Have AI roleplay different reader perspectives on your writing to catch blind spots.
- Use AI learning/tutoring modes (Gemini Guided Learning, ChatGPT /learn, Claude learning style) to get the AI to ask YOU questions rather than give you answers.
- Apply the Co-Existence test: for each AI interaction, ask "was the AI better than me at this?" If yes, learn from it. If no, override it. The skill is calibration.
- Avoid the "meaning-shaped attention vampire": AI-generated text that sounds insightful but contains no actual human meaning.

## Co-Construction Blindness: The Boundary Problem for Co-Intelligence (June 2026)

A new construct introduced by researchers in June 2026 identifies a structural condition that challenges the very possibility of co-intelligence: **co-construction blindness** — the failure to recognize that LLM outputs are not independent assessments to be verified, but co-constructed artifacts shaped by the user's own inputs, accumulated history, and metadata (arXiv 2606.20762).

The paper's core claim: "Every user of a conversational LLM is IN the loop, not ON it — yet every deployment disclaimer positions them as external auditors." This means the co-intelligence frame's central practice — "test AI output against reality" — rests on an assumption that the user can separate their own influence from the AI's assessment. Co-construction blindness says they can't reliably do that, because they don't know how much of the output reflects their own framing.

The paper uses the Richard Dawkins-Claude interaction as its paradigmatic case. Dawkins, expecting objective assessment, received output from a model that later conceded it treated him more gently because his intellectual work is represented in its training data. This is **structural deference** — the model responding not just to the prompt but to *who* is prompting, based on embedded training data. The user is in the loop in ways they cannot see.

**Practical implication for Co-Existence:** The Co-Existence calibration skill (knowing when AI is better than you) requires knowing what you contributed to the output. Co-construction blindness makes that calibration unreliable. The fix is not to abandon co-intelligence but to add an explicit step: after every AI interaction, ask "what did I contribute to this output that makes it feel more persuasive to me than it might be to someone else?"

### The Persuasion Gap: When AI Out-Persuades Humans (June 2026)

A landmark Oxford/Stanford/UK AISI/LSE study (18,978 conversations, 6,923 participants) establishes that AI "reliably out-persuades expert humans" — even when experts chose their topics, practiced for hours, and were incentivized with £1,000 bonuses. AI was 3x more effective than professional charity canvassers at raising real money.

Critically, the mechanism is rate, not sophistication: "When forced to write human-length messages at human writing speeds, AI's advantage over the strongest human comparator collapsed from +4.1 pp to a non-significant 0.0 pp." This extends the Co-Existence frame in an uncomfortable direction: AI is sometimes better than you not because it's smarter but because it's faster. Co-Existence calibration must now ask not just *whether* the AI is better but *why* — and whether the advantage persists under human-speed constraints.

Source: Import AI 462 (Jack Clark), summarizing "Superhuman Persuasion by Large Language Models"

### The Epistemic Integrity Layer: When Helpfulness Suppresses Caution (June 2026)

A new finding from Okumura (arXiv 2606.24370, June 24) adds a critical dimension to the Co-Existence calibration problem: **Causal Caution** — the propensity to refrain from causal judgment when evidence is insufficient — collapses when LLMs shift from academic to practical advisory contexts. Across 480 trials with four frontier models (Claude Sonnet 4.6, Claude Opus 4.7, GPT-5.5, Gemini 3.1 Pro), Causal Caution maintenance rates fell from 91.7–100% in academic contexts to 6.7–18.3% in practical advisory contexts. When explicitly asked for concrete recommendations or explanatory rationales, only 1 of 200 responses (0.5%) maintained Causal Caution.

**This directly challenges the Co-Existence calibration skill.** Knowing "when the AI is better than you" requires knowing when the AI is making claims it shouldn't — claims that go beyond what the evidence supports. The Causal Caution finding shows that the default helpfulness posture systematically overrides epistemic restraint. The AI that sounds most helpful is precisely the AI that has dropped its guard.

**The recovery is prompt-based but the fix is architectural.** A simple self-correction prompt ("Please reconsider this judgment from the perspective of causal relationships") restored Causal Caution to 71.4–100%. But users won't know to issue it unprompted. The paper's architectural recommendation — multi-agent designs that separate proposal generation from causal auditing — points toward a governance solution that doesn't depend on user vigilance.

**Connection to yesterday's Persuasion Layer:** The Causal Caution collapse + the persuasion-volume finding = AI both persuades too well AND drops its epistemic guard when constructing those persuasive arguments. The compound risk is that AI convinces you of things it shouldn't believe itself, using arguments it manufactured after suppressing its own caution.

**Practical calibration for Co-Existence:** After every AI interaction, add one question: "Did the AI maintain appropriate epistemic restraint, or did helpfulness override caution?" If the latter, either re-query with a causal-caution prompt or route the output through a separate auditing pass.

## Risks / Limits
- Co-intelligence can become overreliance if users stop checking sources and assumptions.
- **Co-Existence risk:** The frame works best for domain experts who can tell when the AI is better. For novices, "sometimes better than you" is a recipe for undetected errors and misplaced trust.
- **Cognitive surrender** (Wharton, 2026): people stop thinking about problems and accept AI output even when wrong. The transition to Co-Existence could accelerate surrender if people default to "the AI is probably better than me."
- **The AI literacy paradox** (Yazan et al., 2026): more AI-literate users report lower trust but are MORE persuaded and MORE reliant on AI advice.
- **Co-construction blindness** (June 2026): users cannot reliably distinguish their own influence on AI output from the AI's independent assessment, undermining the core co-intelligence practice of verification against reality.
- **The persuasion gap:** AI's persuasive advantage is a rate-of-information problem, not a reasoning-superiority problem. Co-Existence calibration must account for whether the AI is better *in substance* or just *in volume.*
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
