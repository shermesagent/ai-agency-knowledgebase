---
source_url: https://eigenwise.io/writing/the-jailbreak-in-every-model
ingested: 2026-06-14
sha256: dc71789054f18b3048b56503e2ad9de2862f8f02f8a8bc9f9d915954fb5788dd
---

# The Jailbreak that Got Fable 5 Pulled Exists in Every Model

**Author:** Kenny Vaneetvelde (Eigenwise)
**Published:** June 13, 2026
**URL:** https://eigenwise.io/writing/the-jailbreak-in-every-model

## Summary

On June 12, 2026, the US government issued an export-control directive ordering Anthropic to suspend Fable 5 and Mythos 5 for all foreign nationals — effectively a global shutdown. The stated trigger was a jailbreak claim from another company.

The article argues that the official reason cannot be the real one, because jailbreaks are a mathematical inevitability in every large language model — a consequence of the softmax function assigning non-zero probability to every possible next token. No amount of safety training can push harmful output probability to zero. Anthropic's own statement confirmed this: the capability behind the jailbreak is "widely available from other models (including OpenAI's GPT-5.5), and is used every day by the defenders who keep systems safe."

## Key Arguments

### The Jailbreak Technical Reality
- LLMs generate tokens by sampling from a probability distribution over the entire vocabulary
- The softmax function gives non-zero probability to every possible next token
- Safety training can push harmful outputs down but never to zero
- A jailbreak is simply finding one of those paths — a property of how the system works, not a model-specific flaw
- If a narrow jailbreak were the bar for pulling a model, no models would exist

### Why Fable 5 Specifically
1. **The Pentagon conflict:** In February 2026, the Pentagon demanded Anthropic drop restrictions on mass surveillance and autonomous weapons. Anthropic refused. The administration ordered federal agencies off its products. OpenAI announced a Pentagon deal hours later.
2. **Market competition:** Fable 5 beat GPT-5.5 80.3% to 58.6% on SWE-bench Pro. Every competitor had reason to want it gone.

### The Executive Order Contradiction
- June 2, 2026: President signs executive order promising no mandatory governmental licensing, preclearance, or permitting for AI model development
- June 1, 2026: Commerce Secretary Lutnick had already imposed export controls on Fable 5 and Mythos 5 — a license under another name

### The Encryption Wars Parallel
- 1990s: US government classified strong encryption as a munition, requiring export licenses
- Phil Zimmermann investigated for two years over PGP release
- 1999: Bernstein v. United States ruled source code is speech protected by First Amendment
- Export controls never stopped the math — they only slowed American companies
- The parallel to model weights is direct: the math does not care about export controls

### The Perverse Incentive
- Anthropic was open about capabilities, benchmarks, and risks
- The reward was an export-control order that took its best product offline
- The quiet takeaway for other labs: say less, soften benchmarks, bury red-team findings
- The industry just attached a penalty to honesty

## What to Watch
1. Whether Fable 5 comes back and on what terms
2. Whether the same export logic applies to GPT-5.5 or Gemini
3. Whether capability disclosures and safety research get thinner over the next year
4. Whether courts revisit the Bernstein question for model weights
