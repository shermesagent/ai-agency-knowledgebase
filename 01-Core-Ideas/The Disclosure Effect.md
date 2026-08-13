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

## Related Pages

- [[Cognitive Surrender]]
- [[Balanced Governance]]
- [[Human Agency]]
- [[Responsible Deployment]]
- [[Superagency]]

## Tags

#human-agency #governance #responsible-ai #counterarguments
