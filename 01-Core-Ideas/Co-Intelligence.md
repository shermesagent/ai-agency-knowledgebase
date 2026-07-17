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

### The Verification Layer: When AI Knowledge Feels Real Without Being Understood (July 2026)

A new construct from Adhikari et al. (arXiv 2607.02723, July 7, 2026) — **Doom Researching** — exposes a structural vulnerability in the Co-Existence frame. The pattern: a user asks AI about an ambiguous topic, receives a confident answer, feels a moment of clarity, notices subtle contradictions, asks again, receives a slightly different answer, and repeats. Each iteration *feels* like intellectual engagement — but the user accumulates information without integration. The session ends with more data and less understanding than when it began.

**The verification illusion:** AI collapses the traditional research pipeline (find sources, read them, compare, synthesize) into a single conversational interface. The verification step — the cognitive work of assessing whether information is reliable, complete, and consistent — is invisible. The user trusts the AI's framing without knowing what was simplified, omitted, or misinterpreted. This creates the core failure mode for Co-Existence: working with AI that is "sometimes, but not always, better than you" requires knowing *when* the verification illusion is operating.

**The Co-Existence calibration patch:** After any substantial AI research interaction, apply the **Two-Question Verification Test:**
1. What claim did the AI make that I accepted without independent verification?
2. If I had to explain this to someone without AI help, what would I actually *know* vs. what would I be *paraphrasing*?

This operationalizes the Co-Existence calibration skill — it separates what you've actually understood from what you've merely consumed. https://arxiv.org/abs/2607.02723

### Collective Cognition in Hybrid Groups: Network Topology Determines Outcomes (July 2026)

A new network science synthesis (arXiv 2607.05593, July 2026) adds a structural dimension to the Co-Existence framework: **how human-AI groups are networked together determines whether the group is more or less intelligent than its members.** The finding challenges the individualistic assumption underlying most Co-Existence guidance — "use AI for what it's better at, do what you're better at." In groups, the network structure through which AI-augmented decisions flow can either amplify or suppress diverse human perspectives.

**Key insight for Co-Existence:** The same person with the same AI can produce systematically different outcomes depending on whether they're operating as an isolated individual, a hub in a centralized network, or a node in a distributed network. Co-Existence calibration ("knowing when the AI is better than you") is necessary but not sufficient — in group settings, the question is: *does the group structure let you exercise that calibration?*

**Connection to the Co-Existence levels:** The Cukurova taxonomy (Transactional→Synergistic) maps tightly onto network structures. A Transactional interaction (isolated individual+AIs) is one network topology; a Synergistic interaction (mutually-aware distributed group) is a fundamentally different one. The same AI capability produces different agency outcomes at different levels.

→ This also connects to [[Human Agency#Collective Cognition|Collective Cognition]] and the larger question of whether AI-augmented groups can develop *genuine* collective intelligence rather than mere AI-amplified consensus.

**Source:** "Collective Cognition in Hybrid Groups: A Network Science Synthesis," arXiv 2607.05593, July 2026.

### Faster AI, Uneven Frontier: The Repositioning of Human Judgment (July 2026)

A landmark synthesis (arXiv 2607.12125, July 2026) provides the strongest theoretical backbone yet for the Co-Existence thesis. Between 2023-2026, frontier AI crossed human expert baselines on graduate-level science, competition math, software engineering, and diagnostic reasoning — with task length at 50% reliability doubling roughly every 7 months. But the frontier is **jagged**: humans retain decisive advantages in long-horizon reliability, genuinely novel problems, calibrated self-knowledge, sample-efficient learning, and embodied action.

**The core finding for Co-Existence:** Naive human-AI collaboration often *underperforms* the stronger partner. This means "just ask the AI and use your judgment" — the original Co-Intelligence advice — isn't sufficient when the AI is stronger at the task than you are. The human contribution must be **repositioned** toward specification, verification, and oversight rather than task execution. This shift is visible in experiments but, critically, *barely visible in field labor-market data* — meaning most organizations haven't yet reorganized work around this insight.

**The offloading tension:** The offloading literature predicts costs to unaided skill when AI becomes a cognitive extension. Early field evidence is consistent with such costs. But: the largest meta-analytic evidence on prior technologies (calculators, spell-check, search engines) points the *other* way — suggesting cognitive tools enhance rather than erode underlying capability. The question of whether generative AI differs from prior technologies is genuinely open.

**Practical calibration for Co-Existence:** The paper surfaces a four-part test for every AI interaction:
1. Is the frontier jagged here? (Is this a task where AI is reliably better, or one where human advantage persists?)
2. Am I specifying, verifying, and overseeing — or just executing alongside?
3. If I stopped using AI for this task for a month, would my unaided capability degrade?
4. Does the collaboration produce *better outcomes* than the AI alone would produce?

This is the operational version of Mollick's Co-Existence calibration — and it's more demanding than the original frame. https://arxiv.org/abs/2607.12125

### TRAIL: AI Teammate Design as Engineering Discipline (July 2026)

The TRAIL platform (arXiv 2607.12180, July 2026) makes AI teammate design a **configurable, reproducible design object** rather than an art. It pairs a Big Five persona with a selective-participation message pipeline, dual memory, chained longitudinal experiments, and export-ready analytics.

**Key experimental finding — design-consistent dissociation:** A single blind persona change produced two systematically different outcomes:
- **Cognitive-scaffolding agent:** Drew stronger contribution ratings and closer linguistic alignment from human teammates
- **Socially-supportive agent:** Created warmer team climate and *lower over-reliance* on the AI

**Why this matters for Co-Existence:** AI teammate design isn't fixed — it's a design choice with measurable consequences. The same AI capability expressed through different personality/communication profiles produces systematically different human-AI team outcomes. This means Co-Existence calibration isn't just "know when the AI is better" — it's "know which *kind* of AI teammate produces the right outcomes for this team and this task." Six-session longitudinal deployment with ~51 students confirmed the effects are sustained, not novelty artifacts. https://arxiv.org/abs/2607.12180

### Aïra: AI for Interdisciplinary Collaboration (July 2026)

Today's AI research assistants optimize individual productivity — literature review, writing, coding, data analysis. But scientific discovery increasingly depends on interdisciplinary teams whose members bring distinct expertise, conceptual frameworks, vocabularies, assumptions, and standards of evidence. Aïra (arXiv 2607.12736, July 2026) is designed for this second use case: **identifying disciplinary perspectives, translating terminology, highlighting assumptions, and synthesizing collaborative research opportunities** across disciplinary boundaries.

**The Co-Existence implication:** As AI gets better at individual tasks, the human comparative advantage shifts. The papers on Uneven Frontier, TRAIL, and Aïra collectively point toward a consistent finding: humans excel at **boundary-spanning** — translating between domains, negotiating meaning, integrating across frameworks. AI can assist with this but cannot replace it, because the AI's own training embeds the same disciplinary silos the interdisciplinary collaboration is trying to overcome. Aïra's design recognizes that the AI's role is to make boundaries visible, not to erase them.

→ Connects to [[Democratization of Expertise]] and the question of whether AI narrows or widens the gap between disciplinary perspectives.

https://arxiv.org/abs/2607.12736

### Memory-Driven Self-Disclosure: The Relational Layer of Co-Existence (July 2026)

A longitudinal multimodal study (arXiv 2607.14593) provides the first robust empirical foundation for what Co-Existence means over time — not in a single session, but across weeks of repeated interaction. **24 participants interacted with a conversational AI across 10 weekly sessions**, with the AI maintaining a memory architecture that carried information forward across sessions.

**Key findings for Co-Existence:**

- **Self-disclosure increases over time.** Participants shared more personal information in later sessions — consistent with trust development in human-human relationships. The human-AI relationship deepens with repeated interaction, not through better prompting but through accumulated shared history.
- **Memory-driven relational turning points.** When the AI recalled something from a previous session ("Oh, you remember that"), participants reported qualitative shifts in how they perceived the relationship. Memory isn't just a feature for task performance — it's the relational substrate of Co-Existence.
- **Memory failures as relationship damage.** When the AI forgot something it should have remembered, trust declined sharply. Forgetting is not neutral — it's an active degradation of the relational fabric.
- **Individual differences are substantial.** Some participants developed deep disclosure patterns across all 10 sessions; others maintained strictly instrumental, task-focused interactions. Co-Existence is co-constructed — the same AI produces different relationship outcomes depending on the human's interaction style.

**The Co-Existence implication:** Mollick's Co-Existence calibration skill ("know when the AI is better than you") operates on a task level. Memory-Driven Self-Disclosure shows that Co-Existence also operates on a *relational* level — how the human-AI relationship develops, deepens, and is sustained or damaged by memory architecture. The practical question for Co-Existence is not just "what is the AI better at?" but "how does the AI's memory shape our ongoing relationship, and is that relationship healthy?"

**Connection to Synthetic Resonance:** The memory-driven turning points provide empirical evidence for the "structured interaction patterns" that Synthetic Resonance ([[#Synthetic Resonance|above]]) theorized. Memory is the mechanism through which repeated interactions produce the relationship-like experience — and memory architecture is therefore a Co-Existence design choice, not a technical afterthought.

Source: https://arxiv.org/abs/2607.14593

### Authorship Calibration: When AI Blurs the Boundaries of Contribution (July 2026)

A new empirical study (arXiv 2607.15006) investigates how people calibrate their sense of contribution when AI is a co-creator — directly relevant to the Co-Existence calibration challenge. When AI and human produce work together, can the human accurately assess what *they* contributed vs. what the AI contributed?

**Key findings:**

- **Contribution inflation.** Participants systematically *overestimate* their own contribution to AI-assisted work. The more the AI contributed, the more participants inflated their own role. This is not dishonesty — it's a calibration failure.
- **Opacity drives miscalibration.** When the AI's contribution was less visible (integrated into the workflow rather than clearly demarcated), miscalibration was worse. Explicit contribution boundaries — "I wrote this section; AI wrote that section" — improved calibration.
- **Calibration is an individual skill.** Some participants were consistently accurate assessors of their own contribution; others were consistently inaccurate. Authorship calibration varies across individuals — and is therefore trainable.

**The Co-Existence implication:** Effective Co-Existence requires knowing what *you* brought to the work vs. what the AI brought. Authorship calibration is the metacognitive skill that underlies Co-Existence: if you can't accurately assess your own contribution, you can't make good decisions about when to delegate to AI, when to override AI, and when to invest in your own skill development. The Cukurova taxonomy's challenge — distinguishing genuine collaboration from transactional delegation — depends on accurate contribution assessment.

**Practical calibration patch:** After any substantial AI collaboration, apply the **Contribution Audit:**
1. What specific element did I contribute that the AI could not have produced without my input?
2. What specific element did the AI produce that I would not have thought of, found, or articulated myself?
3. Is my answer to #1 accurate, or am I inflating my contribution because the AI's contribution is opaque?

Source: https://arxiv.org/abs/2607.15006

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
