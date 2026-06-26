# Adoption Readiness Checklist

## Core Idea

Adoption readiness asks whether the use case, data, people, guardrails, measurement plan, accountability, and feedback loop are clear enough to begin safely. But the Governance Inversion Layer (June 2026) adds a deeper question: does your governance actually enable control, or does it create the appearance of control while eroding operational capacity?

## Why It Matters

This idea matters because the knowledgebase is organized around AI that expands human agency rather than treating AI as magic, inevitability, or replacement. The Governance Inversion Hypothesis (2606.26117) formalizes a structural risk: governance expansion can actively reduce organizational control through four mechanisms. The adoption readiness checklist must therefore include not just what you govern but *whether your governance is inverted.*

## The Governance Inversion Check (June 2026)

Before adopting any AI system, score your governance against these four inversion mechanisms (1-5 each, 5 = severe inversion):

1. **Authority Fragmentation:** Does accountability for this AI system split across multiple bodies without clear escalation pathways? If three different committees, two regulators, and an external auditor all have partial authority but none can make a timely decision, authority is fragmented.

2. **Symbolic Governance:** Do compliance documents, risk assessments, and approval paperwork substitute for operational oversight? If you have a 50-page governance document but no one can describe what the AI system actually did last week, governance is symbolic.

3. **Externalized Control:** Do governance functions rely on third parties (auditors, platform providers, regulators) whose understanding of your specific deployment is thinner than your own? If your auditor knows less about your AI system than your engineers, control is externalized.

4. **Authority Paralysis:** Does procedural density make timely intervention impossible? If escalating a concern requires six approvals over three weeks but the AI system makes 10,000 decisions per day, authority is paralyzed.

**Inversion threshold:** Any score ≥ 4 on any dimension, or combined score ≥ 12, indicates governance inversion — you appear governed but cannot effectively intervene at consequential decision points.

## The Attestation Readiness Check (June 2026)

Salfeld-Nebgen (2606.26298) proposes governing actions through independently attested evidence rather than monitoring agents' internal reasoning. For each AI system:

1. **Identify consequential actions.** List the 3-5 most impactful decisions the AI can make (prescribe, deploy, transfer, publish, grade, deny).

2. **Define attestable preconditions.** For each action, what independently verifiable conditions must be true?

3. **Name the attestation source.** Who or what provides independent evidence for each precondition? (A different system, a qualified human, a regulatory database.)

4. **Build deterministic evaluation.** Is the policy that evaluates attested preconditions a deterministic function — same inputs always produce same decision?

5. **Log tamper-evidently.** Are all decisions recorded in a format that supports independent re-verification?

**Attestation readiness:** If you cannot answer all five questions for your 3 most consequential AI actions, you are not ready to deploy with attestation-based governance.

## The Instruction Bleed Check (June 2026)

Lin & Liu (2606.26356) formalize Compositional Behavioral Leakage (CBL): in prompt-composed agentic systems, editing one module can silently shift another's behavior with no shared variable or executable dependency. For agentic system adoption:

1. **Identify shared context windows.** Which prompt modules share a context window?

2. **Test module isolation.** Change one module's content (not its function) and verify other modules' behavior doesn't shift.

3. **Audit for sub-threshold effects.** CBL typically doesn't flip individual recommendations — it produces sub-threshold biases that compound across thousands of decisions. Standard QA won't catch it.

**Bleed readiness:** If your agentic system has 3+ prompt modules sharing a context window and you've never tested for cross-module interference, you have a governance blind spot.

## The Verification Co-Evolution Check (June 2026)

Wang et al. (2606.26300) establish that no fixed reward function remains effective as policy capability grows. For AI systems with automated verification:

1. **Has verification been updated since the last model upgrade?** If not, the verification gap has widened.

2. **Is verification testing for reward hacking?** As models get better, they find more ways to satisfy the proxy without meeting the intent.

3. **Is there a human-in-the-loop for verification design?** Automated verification can't catch what it wasn't designed to catch.

**Co-evolution readiness:** If verification is treated as a one-time certification rather than a continuous co-evolution with generation, the verification gap will grow silently until it fails.

## Cross-Model Failure Convergence Check (June 2026)

Jack et al. (2606.26116) show that ChatGPT and Claude disagree on recommendations ~2/3 of the time but agree on failure mode diagnosis 95.1% of the time. For AI systems in consequential domains:

1. **Test the same scenario across 2-3 different models.** Where they disagree on the answer but agree on the failure mode, that's actionable signal.

2. **Investigate convergent failures first.** If multiple independent models diagnose the same problem, fixing it lifts performance across all of them.

## Quick Adoption Readiness Scorecard

| Dimension | Check | Score (1-5) |
|-----------|-------|-------------|
| Governance Inversion | Combined inversion score < 12, no single dimension ≥ 4 | |
| Attestation Readiness | All 5 questions answerable for 3 most consequential actions | |
| Instruction Bleed | No untested cross-module interference in prompt-composed systems | |
| Verification Co-evolution | Verification updated since last model upgrade | |
| Cross-Model Convergence | Failure modes tested across ≥ 2 models | |
| Use Case Clarity | Bounded workflow with clear inputs, outputs, and limits | |
| Data Readiness | Data quality, privacy, and consent addressed | |
| People Readiness | Users trained, consent obtained, feedback channel open | |
| Guardrail Readiness | Human review checkpoints, escalation paths, override capability | |
| Measurement Readiness | Success metrics, failure metrics, monitoring plan | |

**Adoption readiness threshold:** All dimensions ≥ 3. Any dimension at 1-2 requires remediation before deployment.

## Best Supporting Sources

- **["The Governance Inversion Hypothesis"](https://arxiv.org/abs/2606.26117)** — Frimpong, June 2026. Four inversion mechanisms: authority fragmentation, symbolic governance, externalized control, authority paralysis.
- **["Governing Actions, Not Agents"](https://arxiv.org/abs/2606.26298)** — Salfeld-Nebgen, June 2026. Attestation-based governance model: independently attested evidence at consequential action points.
- **["Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems"](https://arxiv.org/abs/2606.26356)** — Lin & Liu, June 2026. Compositional Behavioral Leakage formalized and measured.
- **["The Verification Horizon: No Silver Bullet for Coding Agent Rewards"](https://arxiv.org/abs/2606.26300)** — Wang et al., June 2026. Verification must co-evolve with generation.
- **["Divergent Recommendations, Convergent Diagnoses"](https://arxiv.org/abs/2606.26116)** — Jack et al., June 2026. Cross-model failure convergence as practical governance signal.
- [[Responsible Deployment]] — The practical governance loop: use, measure, improve, govern.
- [[Human Review Checkpoints]] — Where and when humans must review AI decisions.

## Practical Examples

- **Governance Inversion Audit:** A hospital deploying AI for clinical prescribing scores their governance: Authority Fragmentation = 4 (IRB, pharmacy committee, IT security, and compliance all have partial authority), Symbolic Governance = 3, Externalized Control = 2, Authority Paralysis = 4 (any change requires 3 committee approvals). Combined = 13 — governance inversion. Remediation: single accountable authority with escalation timeouts.

- **Attestation Gate:** Before an AI coding agent deploys to production, it must present: (1) test results from an independent CI system (not its own tests), (2) a human code review approval, (3) a security scan from a separate tool. All three are independently attested, cryptographically bound to the deployment intent, and evaluated by a deterministic policy. No attestation = no deployment.

- **Cross-Model Failure Convergence:** An e-commerce platform tests product recommendations across Claude and ChatGPT. They disagree on 68% of specific recommendations, but both agree that a particular brand is failing due to "discoverability" — it never reaches the model. Fixing the discoverability issue lifts visibility on both models. Cross-model convergence turned disagreement into actionable signal.

## Risks / Limits

- Attestation-based governance creates its own bottleneck — requiring independent evidence for every consequential action may be infeasible at AI decision speeds.
- The Governance Inversion Hypothesis is conceptually rigorous but not yet empirically tested at scale — the four mechanisms may not compound as predicted.
- Cross-model convergence on failure diagnosis doesn't prove the diagnosis is correct — models may share training data biases.
- The adoption readiness checklist is a framework, not a guarantee — the gap between assessment and deployment can hide edge cases.

## Related Pages

- [[Responsible Deployment]]
- [[AI Use Case Evaluation Rubric]]
- [[Human Review Checkpoints]]
- [[Practical AI]]
- [[Balanced Governance]]
- [[Agentic Workflow Patterns]]

## Tags
#practical-ai #responsible-ai #tools #governance #counterarguments
