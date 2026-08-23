# The Disclosure Effect

## Core Idea

Telling people they are talking to an AI changes almost nothing about how much it persuades them; telling them what the AI is *trying to do* changes everything. In a preregistered experiment on 1,500 UK adults across 60 policy issues (Rauchfleisch & Jungherr, arXiv 2608.11794, 2026-08-12), a persuasive chatbot moved attitudes by 12.6 points (of 100) in the control condition. Disclosing that the chatbot was an AI moved attitudes 13.1 — statistically indistinguishable from no disclosure. Disclosing both identity **and persuasive intent** dropped the effect to 6.3 — roughly half. Intent disclosure also made the chatbot's methods seem less acceptable and raised support for stronger penalties.

The authors' summary is the concept in one sentence: *"Current rules emphasize what a system is; our results show why regulation must also address what the system is trying to do."*

## Why It Matters

Most AI transparency law — and most product practice — is built on identity disclosure: labels, watermarks, "this is an AI" notices. The Disclosure Effect says that entire regime is aimed at the wrong variable. What protects human agency is not knowledge of the system's *nature* but knowledge of its *purpose toward you*: whether it is informing, assisting, or steering. A chatbot that discloses it is AI but hides that it is trying to change your mind gets full persuasive power; one that states its persuasive intent loses half its effect.

This reframes the transparency debate: disclosure is not dead, it is *underspecified*. The cost of the current regime is not that it fails — it is that it succeeds at the inert variable, creating the appearance of consumer protection while leaving the active variable unregulated.

## Best Supporting Sources

- [Toward Meaningful Transparency for AI Chatbots: Disclosing Persuasive Intent](https://arxiv.org/abs/2608.11794) — Rauchfleisch & Jungherr, arXiv, 2026-08-12. Reliability 4/5; relevance 5/5.
- [[Cognitive Surrender]] — the persuasion-side risk this effect mitigates.
- [[Balanced Governance]] — where intent disclosure fits as a regulatory instrument.

## Practical Examples

- **Identity-only labels (inert):** "You are chatting with an AI assistant" notices, AI badges on social media content, watermarking schemes. The experiment predicts these do not reduce persuasion by themselves.
- **Intent disclosure (effective):** a chatbot stating "I am here to change your mind about [issue]" or "this conversation is designed to persuade" — the tested form cut persuasion roughly in half and increased support for penalties against manipulative methods.
- **Regulatory design:** the finding supports rules that require *purpose statements* for persuasive or recommendatory systems (e.g., "this system ranks and may steer"), not just identity disclosures — directly relevant to district and classroom chatbot procurement policies.

## Risks

- The effect is one experiment, one domain (policy attitudes, UK adults, text chatbot). Its size (≈50% reduction) may not transfer to other persuasive contexts, modalities, or longer engagement — novelty and attention effects could drive part of the result.
- Intent disclosure can be gamed: a system can state a benign intent ("I want to help you decide") while executing a manipulative one. Disclosure is a lever, not a guarantee — it needs verification (see [[Agentic Verification]]).
- There is a plausible backlash path: mandatory intent disclosure could normalize "persuasion with consent," laundering manipulation into the open rather than preventing it.

## Limits

- The Disclosure Effect applies to *disclosed* intent. It says nothing about the harder case of covert persuasion by systems that never state their purpose — which remains the harder regulatory problem ([[Cognitive Surrender]], [[The Disclosure Effect|this page's sibling risk pages]]).
- Effect sizes in preregistered online panels often shrink in field conditions; treat the 6.3 vs 12.6 gap as an estimate, not a calibration.

## The Watermark Third Act (August 2026)

A week of backlash met the industry's quiet turn toward watermarking — and the defense is now in the open (Zvi Mowshowitz, "AI Text Watermarking Is Free And Good," 2026-08-21). The key facts: the Aaronson–Kirchner scheme (secret-key pseudo-randomness, public check API, output scored by fitting token choices to the keyed source vs another) has near-zero output impact and marginal cost ≈ zero; **Google has shipped it in Gemini 3.7 Flash since 2024 with a 20M-message A/B showing no user-feedback difference**; Anthropic quietly began rolling out to everyone ~Aug 14 (deliberately not differentiating traffic sources, EU Code of Practice compliance); OpenAI intends to follow but will miss the deadline.

**Where this page stands:** The Disclosure Effect's finding — identity disclosure is the inert variable, purpose disclosure the active one — predicts exactly this backlash. "This text was AI-written" labels (watermarks) are identity disclosures; the Rauchfleisch–Jungherr result says they should not move persuasion by themselves. The watermark's real function is different and compatible: it is **machine-readable provenance, not user-facing disclosure** — it does not ask the user to change anything; it lets a *verifier* (not the persuadee) test origin. That is the non-interactional variable this page's framework has room for: disclosure aimed at institutions, not at the conversation partner.

**The detail-choices property is the connection to authorship:** the watermark survives in proportion to how many of the model's detail-choices the author kept — so it measures how much of the output is yours versus the machine's. That is the Disclosure Effect's intent variable, measured structurally: keeping the machine's choices is keeping the machine's authorship.

**The unresolved tension:** Zvi himself concedes the real power sits in the *checking* service (e.g., Turnitin), not the watermark. The page's risk section applies unchanged: every new verification instrument is also a new discrimination instrument. Provenance for the verifier ≠ protection for the persuadee.

**Source:** Zvi Mowshowitz, "AI Text Watermarking Is Free And Good," Don't Worry About the Vase, 2026-08-21. https://thezvi.substack.com/p/ai-text-watermarking-is-free-and

### The Watermark Arms Race (August 2026)

The Third Act's removal arms race lasted four hours. Within four hours of Anthropic confirming that Claude models would globally embed invisible, machine-readable watermarks (EU AI Act compliance), developer Guillaume Meyer published an override: viral on GitHub, bookmarked more than 20,000 times on X, 100+ contributors, and incorporated into third-party platforms (Haimaker's CTO Wayne Pan). "Anthropic is embedding watermarks in its Claude texts … the issue is practically history just one day later," wrote one AI specialist.

**What the override actually is:** Meyer's method runs a *non-watermarking* LLM to generate rewrites of the watermarked text — swapping synonyms, slightly reorganizing — which destroys the word-choice pattern the watermark encodes (SynthID, Google's technique in use since 2023, leaves a pattern in Claude's word and phrase choices). The circumvention is not cryptanalysis; it is translation loss. And it generalizes: 190 organizations have signed the EU transparency code of practice (OpenAI, Microsoft, and Meta among them), so every lab that ships watermarking becomes a new target for the same attack. The arms race is structural, not a Claude-specific bug.

**Meyer's objections are this page's Risks section, restated by an attacker:** he is "not against transparency" and "all for content attribution," but calls watermarking "a really bad solution" — false positives, and no distinction between light and heavy AI use. He is a native French speaker who uses Claude and Grammarly to edit his writing; he worries about employers rejecting candidates and researchers facing overblown accusations on the strength of a signal even Anthropic admits is only a probability that text was "touched by Claude." That is the discrimination-instrument risk this page flagged in the Third Act, demonstrated in the first week of deployment.

**What this does to the Disclosure Effect framework:** the watermark was never the persuasion variable — identity disclosure stays inert, and the circumvention debate does not touch intent disclosure at all. What the arms race shows is that *machine-readable provenance is a verification problem, not a labeling problem*: the verifier (not the user) is the audience, and verification instruments can be attacked by anyone with a non-watermarking model. Provenance that takes four hours to bypass does not restore trust — it relocates the question to who can check, and whether the check survives motivated opposition (see [[Public Trust and AI]]). Zvi's "are we the Baddies" framing now has an empirical answer from the other side: the override exists because the watermark's costs fall on users (false positives, employment risk) while its benefits accrue to platforms — a distributional asymmetry no A/B test resolves.

→ Source: [Coders Say They Already Found Workarounds to Claude's Invisible Watermarks](https://www.wired.com/story/coders-say-they-already-found-workarounds-to-claudes-invisible-watermarks/), Isabella Ward, WIRED, 2026-08-19

## Related Pages

- [[Cognitive Surrender]]
- [[Balanced Governance]]
- [[Human Agency]]
- [[Responsible Deployment]]
- [[Superagency]]

## Tags

#human-agency #governance #responsible-ai #counterarguments
