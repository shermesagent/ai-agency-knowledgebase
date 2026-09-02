# The Agentic Garden of Forking Paths

## Core Idea
AI agents amplify analytical variation — different AI personas, given the same data and the same research question, produce systematically different (and often opposing) conclusions. The space of defensible analyses is vast, AI makes exploring it cheap, and the "one analysis as the answer" model breaks down. The solution is not to suppress variation but to make the full distribution of plausible analyses visible — so readers can see whether a reported conclusion is a central tendency or a tail event.

## Key Concepts

### The m-value (Multiverse Value)
The probability that an analysis path would produce a claim at least as extreme as the reported one. Analogous to a p-value but operating across the space of defensible analytical choices rather than within a single analysis. A low m-value means the reported conclusion is in the tail of the distribution of what could reasonably be concluded from the same data.

### Agentic Bootstrap
A method that uses AI agents to sample plausible analysis paths — by assigning different analytical personas, methodological preferences, and starting assumptions — to estimate the distribution of possible conclusions from the same dataset. Makes the "garden of forking paths" visible and quantifiable.

### Analytical Power Inequality
The structural advantage that accrues to actors who can commission hundreds of AI analyses and selectively present the one that best serves their interests — while resource-constrained actors see only a single analysis and can't tell where it falls in the distribution of defensible conclusions.

## The Evidence

The landmark paper by **Miao, Pritchard, and Zou (July 2026, arXiv 2607.01507)** established the core findings:

- **72% reproduction of the human ideological gap:** AI agents assigned different analytical personas and given the same immigration data reproduced 72% of the ideological gap in reported effect estimates that 42 human research teams produced.
- **Analyses pass review:** 86% of AI-produced analyses passed independent AI review; 78% passed majority human expert review. The problem is not error — it's that the space of defensible analyses is vast and AI makes selective exploration cheap.
- **Extreme conclusions are common:** 13.5% of reported human analyses fell in the most extreme 5% of the analysis space (m < 0.05). Many reported conclusions are genuinely in the tail of the distribution.
- **Cross-domain generalizability:** Tested across four high-stakes domains (immigration, minimum wage, executive compensation, and tax policy).

## Why It Matters

The Garden of Forking Paths reframes evidence-based decision-making in the age of AI. Before AI, analytical variation was constrained by human time and expertise — most analyses explored only a few paths. AI makes exploring hundreds of paths cheap. This creates:

1. **A governance crisis for evidence:** If any defensible position can be supported by some analytical path, and AI makes it trivial to find that path, then "the evidence says X" becomes meaningless without knowing where X falls in the distribution.
2. **An amplification mechanism for existing biases:** AI doesn't invent the ideological gap — it extends it. Analysts who already lean in a direction can use AI to find the paths that support their leaning, while feeling (correctly) that their analysis is methodologically defensible.
3. **A case for transparency infrastructure:** The only defense is to make the distribution visible. Agentic Bootstrap is one method; preregistration of analytical choices, multiverse analysis, and specification curve analysis are others. The Pluralism Layer of the [[Superagency]] framework addresses this directly.

## Implications for Superagency

The Garden of Forking Paths is the core challenge of the [[Superagency#The Pluralism Layer: AI Doesn't Just Shape Preferences; It Multiplies Perspectives (July 2026)|Pluralism Layer]]: if Superagency means more people analyzing data and forming conclusions, it necessarily means more competing truths. The design challenge is building institutions that can:

- Surface the full distribution of defensible analyses rather than presenting one as "the" answer
- Distinguish genuine disagreement from selective reporting
- Provide readers with the m-value — the context to know whether a reported conclusion is central or extreme
- Make analytical power inequality visible so it can be governed

## Connections to Other Concepts

- **Constructive Alignment** (arXiv 2607.00383, July 1, 2026): The Preference Layer established that AI shapes preferences through interaction. The Garden of Forking Paths extends this: AI also shapes factual beliefs, and different AI personas lead to different beliefs. The combination is explosive — an AI that shapes both values AND facts, with no mechanism to surface the variation.
- **Persuasion Layer** (June 30, 2026): AI's persuasive advantage operates through information volume. The Garden of Forking Paths identifies a new persuasive mechanism: selective presentation of one defensible analysis from a vast space of equally-defensible alternatives.
- [[Synthetic Contact with AI]] (arXiv 2607.02181, July 3, 2026): The bridge dimension of the Pluralism Layer — AI can also reduce cross-perspective animosity and create behavioral spillover into real engagement.

## Limitations and Cautions

- Agentic Bootstrap is a method, not a solution. Making analytical variation visible doesn't automatically resolve it — it just makes selective reporting harder to hide.
- The m-value inherits the limitations of all statistical summaries: it compresses a distribution into a single number. Full specification curves or multiverse visualizations may be more informative.
- The finding that 86% of AI analyses pass AI review is both a feature (defensible analyses exist across the spectrum) and a warning (review alone doesn't catch selective reporting).

## Homogenization on Both Ends of the Delegation Decision (2026-08-21)

The garden has two gardeners, and both are flattening it. New evidence this week closes the loop on the diversity question from both directions.

- **The supply side — models converging:** "Are LLMs becoming similarly creative?" (Patel et al., arXiv 2608.19437, 2026-08-19) analyzes three years of model releases on the Infinity-Chat100 corpus plus the Alternate Uses Task: output diversity decreases significantly over successive releases — the creative outputs of newer models are converging in substance, not just style. Even before anyone delegates, the branches are growing more alike.
- **The demand side — delegation homogenizes choice:** "The Basic B*** Effect" (Matz et al., arXiv 2509.02910, 2025-09-03) — 110,000 real-world choices from 1,000 users plus a controlled experiment (348 participants, 12,097 decisions): using LLM-based agents shifts choices toward popular options. Generic agents reduce interpersonal distinctiveness (choices converge on the majority); personalized agents temper that homogenization but compress intrapersonal diversity harder, narrowing exploration across topics; sequential delegation amplifies the flattening.
- **The mechanism — social proof suppresses the fork:** "Modeling AI Overreliance as a Complex Adaptive System" (Biswas, arXiv 2608.19616, 2026-08-20) shows verification collapses not through individual failure but through visible unverified use cascading across a population. Making verification visible reverses the cascade — an intervention at the garden-design level.
- **The science corollary — uniform guidance monocultures:** "Navigating Epistemic Monocultures in AI-Driven Science" (Fazelpour et al., arXiv 2608.19390, 2026-08-19) simulates AI guidance in scientific communities: non-personalized uniform AI guidance improves community outcomes only under a narrow conjunction of conditions and is harmful otherwise; personalization can restore diversity but depends on institutional adaptation.

The convergence story: generic delegation + generic guidance + increasingly similar models = the majority path gets wider while every other path narrows. The m-value framing of this page (surfacing analytical variation) is one countermeasure; the simulation evidence adds a second — personalization and visible verification, not just transparency.

## Risk Vesting in the Garden: Every Fork Is a Potential Actor (2026-09-02)

The garden has been governed so far as a *distribution* problem — make analytical variation visible. New work (arXiv 2609.01035, 2026-09-02) governs it as an *authority* problem: in recursive agent systems, every fork is a potential actor, and the question is when a branch should receive authority to act. **[Spawn Freely, Act Sparingly: Progressive Risk Vesting for Recursive LLM-Agent Trees](https://arxiv.org/abs/2609.01035)** distinguishes:

- **Sandbox spawning** — external controls prevent the specified harm; search can branch freely.
- **Capability activation** — a selected branch crosses an irreversible-action boundary; this is the moment authority must be earned, not inherited.

The mechanism — **Progressive Risk Vesting (PRV)** — holds a trajectory-level risk budget in escrow and debits it as branches are activated, with a proven anytime harm bound for adaptively generated trees. Branch outcomes may be dependent; each local certificate must stay valid conditional on the full pre-activation history (including the information used to select the request). Two results matter for this page:

- **Delayed vesting preserves every policy** available under irrevocable spawn charging when activation gates, branch charges, and compute constraints are held fixed — restraint is not a capability tax.
- Trajectory harm changes character at an **authority reproduction number** R_A = 1: below criticality harm scales with local risk p, at criticality with √p, and above criticality it retains a positive floor no matter how small p gets. Above criticality, cheap local safety stops compounding into safe trajectories.

**Why this belongs on this page:** this page's m-value asks *where a conclusion falls in the distribution of defensible analyses*; PRV asks *what a branch may do once it exists*. The two govern the same tree — one meters the *claims* a fork produces, the other meters the *actions* a fork takes. The garden's analytical power inequality (actors who can commission hundreds of analyses) has a dangerous sibling: actors who can spawn hundreds of *agents* and activate the one that succeeds. The design rule from the paper — **search broadly in the sandbox, grant recursive authority sparingly, with an explicit risk charge** — is the governance answer to the garden's second gardener problem: fork freely for exploration, vest authority only at irreversible boundaries (see [[Sandbox Integrity]]'s fleet-scale update, same day). The homogenization evidence on this page (08-21) suggested the branches were growing alike; the vesting result adds that the branches are also growing *authority* — and authority, unlike analysis, is not a free good.

→ Source: arXiv 2609.01035 (2026-09-02); [[00-Daily-Digests/2026-09-02]] (The Veto Question)

## Related Pages
- [[Superagency]]
- [[AI and Inequality]]
- [[Case for AI Optimism]]
- [[Co-Intelligence]]
- [[Balanced Governance]]

## Tags
#pluralism #analytical-variation #evidence-governance #superagency #inequality
