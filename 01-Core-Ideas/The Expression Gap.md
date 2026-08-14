# The Expression Gap

**Core claim:** Large language models systematically know more than they say — and the gap between what a model's hidden states encode and what its outputs express is the correct unit of analysis for trust, refusal, and verification. What you can audit is the output; the output lags the representation by a wide, measurable margin.

## Core Idea

The expression gap is the dissociation between a model's **internal representation** (what its activations encode about the question's answerability, the boundary of its knowledge, the specificity of a referent, its confidence) and its **expressed behavior** (what tokens it actually emits). Three independent results from August 2026 establish it as a phenomenon, not a curiosity:

1. **Encoding without expression.** TRAPSBench (2608.13167) built 1,404 procedurally generated physics videos in which a single targeted change makes the outcome physically undeterminable. Across 16 vision-language models, the best spontaneous abstention rate was PECS 0.292 — models answered with false certainty ~71% of the time. Yet linear probes decode answerability from the models' own hidden states at up to 0.91 AUROC, and steering a single-layer "void direction" causally induces or suppresses abstention. The knowledge of ignorance is present and readable; the generation policy does not use it. The gap is ~4× worse for visual uncertainty than for textual uncertainty.
2. **Substrate without policy.** A Gricean analysis (2608.13484) found LLM activations encode both knowledge boundaries and referent specificity — but generation never reconciles them: models emit specific referents even for entities they demonstrably don't know, and prefer specificity over correct generics. "The substrate for a Gricean retreat is present; the policy that would act on it is not."
3. **Tuned confidence without tuned accuracy.** Instruction tuning (2608.13430) changes verbalized confidence and shrinks cross-rationale diversity while accuracy barely moves and calibration worsens — the tone of certainty is manufactured by training, independently of the underlying competence it claims to report.

The expression gap is the generalization of the withholding problem (08-13): withholding is the *designed* refusal to act; the expression gap is the *undesigned* failure to say what you cannot do. One is a feature; the other is a risk surface.

## Why It Matters

- **Audit surfaces are output surfaces.** Every mechanism of trust — abstention, disclosure, confidence scores, verification, benchmarks — operates on what a system *expresses*. If expression lags representation, then audits of expression systematically overstate competence.
- **Benchmarks measure transport, not just models.** QuoteBench (2608.13547) showed that matched execution scores hide command-path damage: replaying the same agent reply through one deliberately unescaped added parser costs 55.4–73.2 points across eight configurations; disclosing the boundary recovers 30.4–60.7 points for six of eight. GPT-5.6-sol's matched gap of −3.6 hides −64.3 points of damage and +60.7 points of compensation. A matched score is a harness property until the report says otherwise.
- **Delegation risk concentrates at the gap.** A system that cannot express when it doesn't know is exactly the system that cannot be held to a duty of care — which is the technical substrate of the unsettled personhood/liability debate (see [[Public Trust and AI]]).
- **It reframes the alignment debate.** If epistemic states are decodable from activations (0.91 AUROC) and steerable (void-direction), then output-stage interventions — abstain contracts, specificity floors, uncertainty disclosure — are the pragmatic levers available today, and representation-level fixes are a research frontier rather than a precondition.

## Best Supporting Sources

- **TRAPSBench: Vision-Language Models Encode but Fail to Express Epistemic Restraint** (Pramono, Cai & Kulkarni, arXiv 2608.13167, 2026-08-13) — 5/5, 5/5. The anchor result: 16 VLMs × 1,404 matched pairs; PECS 0.292 best; 0.91 AUROC decodable answerability; single-layer void-direction steering; "the bottleneck is expression, not perception."
- **Toward a Gricean Retreat** (Srinivas, Khatwani & Pacheco, arXiv 2608.13484, 2026-08-13) — 4/5, 5/5. Activation-level encoding of knowledge boundaries and specificity without generation-level reconciliation; models choose specific referents for unknown entities even when correct generics are offered.
- **Are You Sure You're Sure?** (Proskurina, Kumar & Komolafe, arXiv 2608.13430, 2026-08-13) — 4/5, 4/5. Instruction tuning shifts verbalized confidence and rationale diversity with accuracy nearly flat and calibration worse; confidence and rationale diversity capture distinct effects.
- **QuoteBench** (Li, Zhang, Tresp & Yang, arXiv 2608.13547, 2026-08-13) — 4/5, 5/5. Matched scores hide command-path failures; evaluation reports must specify configuration, generation contract, execution path, operating point, and validator.
- **Beyond Final Scores** (Li et al., arXiv 2608.13417, 2026-08-13) — 4/5, 5/5. Long-horizon agents are engineering optimizers with high run variance; within-run behavior (Solution Framing / Execution / Feedback Control) is the meaningful evaluation object.

## Practical Examples

- **Abstention contracts:** require an explicit "insufficient evidence" response mode for decision-support deployments; audit the abstention rate on held-out ambiguous inputs. Best-case spontaneous PECS is 0.292 — a contracted rate near the 0.91 AUROC decodeable ceiling is the target.
- **Evaluation reports:** demand the full stack — model, configuration, transport, operating point, validator — before trusting any matched score (2608.13547).
- **Confidence-score hygiene:** treat confidence as evidence only when it tracks accuracy under controlled perturbations; tuned confidence that doesn't move accuracy is decoration (2608.13430).
- **Prompting is not the fix:** the Gricean result (2608.13484) shows the boundary signal exists in activations but is not reconciled at generation — better prompts may surface it occasionally; only output-stage policy (filters, contracts, steering) makes it reliable.

## Risks/Limits

- **Steering results are proof-of-concept.** Single-layer void-direction steering works in lab settings; production reliability and safety of activation-level interventions are open questions.
- **The gap is model- and modality-specific.** Visual uncertainty is ~4× harder than textual (2608.13167); the gap presumably varies by family, scale, and training recipe — treat any single measurement as a snapshot.
- **Optimism cut:** the 0.91 AUROC decodability invites "just read the hidden states" solutions; the authors instead call for output-stage interventions, suggesting representation-level fixes are not near-term.
- **Benchmark-skepsis contagion:** QuoteBench's lesson can be over-extended into "all evaluations are meaningless"; the correct reading is that evaluation reports are incomplete without transport and validator details.

## Related Pages

- [[Generative Refusal]] — the designed counterpart: withholding as a feature; the expression gap is the undesigned failure to withhold.
- [[The Disclosure Effect]] — disclosure operates at the output stage; intent disclosure is the expressive act that changes behavior.
- [[Strongest AI Risk Arguments]] — the gap as a risk class: systems act on more than they can express.
- [[AI Executive Assistants]] — the trust floor: an assistant that can't express uncertainty can't be delegated to safely.
- [[AI Use Case Evaluation Rubric]] — evaluation must characterize expression, not just scores.
- [[Warranted Reliance Checklist]] (recommended, outstanding)

## Tags

#human-agency #responsible-ai #verification #risk #ai-agents
