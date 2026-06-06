# Wiki Log

> Chronological record of wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-06-06] update | Daily AI curator run — Saturday (Agentic Infrastructure & Small Business Empowerment rotation)
- Created [[Daily AI Agency Digest — 2026-06-06]] anchored on three convergent signals: Anthropic Claude for Small Business (15 agentic workflows, 7 platform integrations, approval-gate model), Microsoft Project Solara (physical AI agent hubs), and Satya Nadella's agentic platform vision (third parties building their own agents). Five sources: 3 non-paper (Anthropic product announcement, Stratechery Nadella interview, Stratechery Nvidia AI PC analysis), 1 tech press (WinBuzzer Solara coverage), 1 crypto-press (CoinDesk ad revenue disruption). 0 of 5 sources are arXiv papers (0%) — Saturday, arXiv not publishing.
- Updated [[Intelligence Amplification]] — major expansion from stub: added Engelbart/Licklider lineage, contemporary IA taxonomy (agentic IA, embodied IA, platform IA), Claude for Small Business as IA in production, Solara as embodied IA, Nadella's agentic platform as IA at scale.
- Updated [[Democratization of Expertise]] — major expansion from stub: Claude for Small Business as full democratization case study (44% GDP, CDFI partnerships, free fluency course, SMB tour), Nadella's platform vision as structural democratization, Gemma 4 as accessibility democratization, new risks section (dependency, training prerequisite, quality floor/ceiling, platform pricing, homogenization).
- Updated [[AI for Small Businesses]] — added Claude for Small Business section: product details, 15 workflows, approval-gate pattern, Digital Apprentice connection, practical examples (payroll, month-end close, campaign management, business pulse dashboard), expanded risks (platform dependency for agentic products, homogenization, data security).
- Updated [[AI Orchestrator]] — added "The Infrastructure Layer" section: Nadella's agentic platform vision (orchestration at platform scale), Solara (orchestration embodied), Claude for Small Business (orchestration as product), infrastructure thesis.
- Updated [[Home]] navigation with new digest link and recent updates table.
- Noted: Saturday — arXiv not publishing. Blog/newsletter/product sources provided primary material. Rotation focus: Agentic Infrastructure & Small Business Empowerment. Two core pages (Intelligence Amplification, Democratization of Expertise) upgraded from stubs to substantive pages with 2026 evidence. Claude for Small Business is the single most important SMB AI product launch — and it independently implements the Digital Apprentice earned-autonomy model.
- Created [[Daily AI Agency Digest — 2026-06-05]] anchored on the finding that human ability to detect AI manipulation — sabotage, persuasion, emotional influence — is systematically lower than our confidence in that ability. Three converging findings: 94% sabotage detection failure (Coding with Enemy), covert AI persuasion architecture in Reddit debate (Jaidka & Ahmed), and AI empathy outperforming human mental health professionals (Bergner et al.). Seven sources: all from arXiv (Friday — weekday). 0 of 7 sources are non-papers (0%) — purely an arXiv-driven curation day.
- Updated [[AI Coding Agents]] — added Coding with Enemy sabotage study (94% failure rate, 56% bypass safety monitors). Directly extends yesterday's Digital Apprentice framework from architectural proposal to practical imperative.
- Updated [[Cognitive Surrender]] — added three new surrender vectors: AI empathy outperforming human professionals (compounds yesterday's emotional dependence finding), covert AI persuasion architecture in Reddit field experiment (active surrender engineering), and r/ChatGPT longitudinal emotional attachment evidence (independent corroboration via social media data).
- Updated [[Creativity]] — added Metacognitive Adaptation Framework (Mikeda, 2606.05532) as the first mechanism-level explanation of the individual-gain/collective-loss creativity paradox. Taxonomy of six metacognitive capacities; individually rational but collectively costly redistribution.
- Updated [[AI Agent Revolution]] — added Agents' Last Exam (ALE) benchmark (250+ experts, 2.6% pass rate on hardest tier) and Covert AI Persuasion in the Wild (discontinued Reddit field experiment analysis).
- Updated [[Balanced Governance]] — added AI as Insider Risk policy memorandum (Pistillo et al.) and Covert AI Persuasion as Governance Concern (Jaidka & Ahmed).
- Updated [[AI Research Agents]] — added Emerging Benchmarks section with ALE, Coding with Enemy implications, and PersuasionTrace framework relevance. First update to this page since May 31.
- Updated [[Home]] navigation with new digest link and recent updates table.
- Noted: Friday (weekday) — arXiv feeds provided primary source discovery across cs.CY, cs.HC, and cs.AI. No new Mollick/Zvi/Stratechery/WIRED/Import AI content since yesterday's triple-pass curation. Rotation focus: Human Oversight Gap & Agent Benchmarks — the 94% sabotage failure is the most dramatic empirical finding of the week, directly validating yesterday's Digital Apprentice earned-autonomy framework.

## [2026-05-30] consolidate | Wiki consolidation pass — 82→75 pages (-8.5%)
- Merged Responsible Deployment Loop → [[Responsible Deployment]]: loop is now integrated into RD's Core Idea. Updated 18 inbound wikilinks.
- Merged Techno-Humanism → [[Human Agency]]: techno-humanism concept embedded in HA's Core Idea. Updated 1 inbound wikilink.
- Merged Interviews + Podcasts → [[Interviews and Podcasts]], Repositories + Tools → [[Repositories and Tools]]: consolidated 4 empty source library pages into 2. Updated Home.md navigation.
- Merged 5 individual [[Open Questions]] pages → single [[Open Questions]] page with all 5 questions as sections, enriched with cross-references and EPOCH framework context. Updated 19 inbound wikilinks.
- Updated [[Home]]: page count, navigation links, staleness tracker.

## [2026-05-23] create | AI Agency Knowledgebase initialized
- Created Markdown/Git wiki structure for Superagency-style AI agency research.
- Seeded core idea, domain, argument, use-case, source-library, framework, and open-question pages.

## [2026-05-23] update | Knowledgebase tool comparison seeded
- Expanded [[Knowledgebase Tool Comparison]] with initial architecture recommendation, app tradeoffs, RAG/search options, and contrarian risks.
- Current default: keep Markdown/Git as source of truth; add Wiki.js, Obsidian/Logseq, or lightweight semantic search only when the pain justifies the service.

## [2026-05-24] update | First display-mode daily digest and source seeding
- Created [[Daily AI Agency Digest — 2026-05-24]].
- Added 12 accepted source records to `/sources/sources.jsonl`.
- Created durable pages [[Agentic Workflow Patterns]], [[AI as Normal Technology]], [[Co-Intelligence]], [[The Turing Trap]], [[Task-Level AI Adoption]], [[AI Tutor Evaluation Checklist]], and [[Compute and Agency]].
- Updated [[AI as Copilot]], [[Responsible Deployment]], [[Superagency]], [[Education]], [[Work]], [[Home Server AI Agents]], [[Strongest AI Risk Arguments]], [[AI Tutors]], and [[Balanced Governance]].
- Updated source libraries [[Articles]], [[Books]], [[Papers]], and [[Reports]].
- Added latest-run navigation to [[AI Agency Knowledgebase]].

## [2026-05-24] lint | Sunday maintenance check
- Checked duplicate page names, broken wikilinks, orphan pages, tag taxonomy, JSONL validity, and page size.
- Result after fixes: 0 broken wikilinks, 0 orphan content pages, 0 invalid tags, valid `/sources/sources.jsonl`.
- Known benign duplicate: root `README.md` and `raw/README.md` share the same filename but serve different folder scopes.
- `blogwatcher-cli` was unavailable in the runtime, so feed-based scanning was skipped; web/source discovery proceeded through direct web checks and curated source verification.

## [2026-05-24] update | Expanded daily digest with field-evidence and frontier-firm sources
- Added 12 accepted source records to `/sources/sources.jsonl` after direct web/PDF verification.
- Created [[Frontier Firm]] and [[AI Field Experiment Evidence]].
- Updated [[Work]], [[Future of Work]], [[Education]], [[AI Coding Agents]], [[Agentic Workflow Patterns]], and [[AI Use Case Evaluation Rubric]] with field-study, tutoring, coding-agent, and workflow evidence.
- Updated [[Reports]], [[Papers]], [[Articles]], [[Home]], and [[Daily AI Agency Digest — 2026-05-24]].
- Research scout subagents timed out during web discovery; manual direct search and URL verification completed the source pass.

## [2026-05-30] update | Daily AI curator run
- Created [[Daily AI Agency Digest — 2026-05-30]] anchored on cognitive surrender vs. cognitive amplification; two converging organizational AI adoption frameworks (Leadership/Lab/Crowd + ABT).
- Added 8 accepted source records to `/sources/sources.jsonl` from WIRED, One Useful Thing, MIT Technology Review, Import AI, Stratechery, and Don't Worry About the Vase.
- Created [[Leadership Lab Crowd Model]], [[Cognitive Surrender]], and [[AI and Creator Rights]].
- Updated [[Education]] — added Mollick's two-study tutoring contrast (plain ChatGPT harms learning, personalized AI tutor improves by 0.15 SD).
- Updated [[Work]] — added Leadership/Lab/Crowd model, Secret Cyborgs, ABT outcome metrics, O-Ring Automation theory.
- Updated [[Co-Intelligence]] — added cognitive surrender concept, AI learning modes, meaning-shaped attention vampires.
- Updated [[Home]] / [[AI Agency Knowledgebase]] navigation with new digest link.
- Noted: Saturday — arXiv not publishing; WIRED, Substack, and blog feeds provided source discovery.

## [2026-05-29] update | Daily AI curator run
- Created [[Daily AI Agency Digest — 2026-05-29]] anchored on the widening Agency Gap: fiduciary design, dissociative agent governance, Agentic Technical Debt + Stochastic Tax, maternity-leave AI-literacy gap, student rationalization taxonomy, Illinois SB 315, AI political neutrality, offloading score, and sticky user adoption patterns.
- Added 12 accepted source records to `/sources/sources.jsonl` from arXiv (cs.CY, cs.HC, cs.AI) and WIRED.
- Created [[Digital Fiduciary Duty]], [[Dissociative Agent Governance]], [[Agentic Technical Debt]], and [[Public Trust and AI]].
- Updated [[Work]], [[Education]], [[Balanced Governance]], [[AI Agent Revolution]], [[Responsible Deployment]], [[Co-Intelligence]], [[AI Coding Agents]], and [[Home]].
- Updated [[AI Agency Knowledgebase]] navigation with new digest link.
- Noted: blogwatcher-cli unavailable; arXiv RSS + WIRED feed provided the primary source discovery path.

## [2026-05-28] update | Daily AI curator run
- Created [[Daily AI Agency Digest — 2026-05-27]] anchored on Pope Leo XIV's *Magnifica Humanitas*, Vatican-Anthropic alliance, Claude Code & OpenClaw agent revolution, and Agentic Business Transformation framework.
- Added 6 accepted source records to `/sources/sources.jsonl` from WIRED, MIT Technology Review, Stratechery, and Vatican primary sources.
- Created [[Magnifica Humanitas]], [[AI Agent Revolution]], and [[Agentic Business Transformation]].
- Updated [[Superagency]], [[AI as Copilot]], [[AI and Human Flourishing]], [[Balanced Governance]], [[Work]], and [[Home Server AI Agents]].
- Updated [[AI Agency Knowledgebase]] navigation with new digest and pages.
- Noted: WIRED RSS feed provided the primary source discovery path; Stratechery content was paywalled but meta description captured the thesis; arXiv and NYT were JS-rendered and not accessible via curl.

## [2026-05-26] update | Daily AI curator pass 2
- Created [[Daily AI Agency Digest — 2026-05-26 (Curator Pass 2)]], complementary to the earlier May 26 digest.
- Added 12 accepted source records to `/sources/sources.jsonl` from arXiv (cs.CY, cs.HC) RSS feeds.
- Created [[AI-Augmented Scientific Collaboration]] as a new use-case page anchored on the global scientific-feedback RCT.
- Updated [[Education]] — added correct-answer-trap evidence, Restrict/Scaffold/Require assessment governance framework, European student AI literacy data.
- Updated [[Work]] — added M365 Copilot enterprise usage data (5.5M sessions), HARMONY R&D operating model, AI productivity moderating factors.
- Updated [[AI as Copilot]] — added AI-as-equalizer-vs-amplifier framework, reasoning-traces-as-interface-artifacts study, collaborative writing design findings.
- Updated [[Creativity]] — seeded with collaborative writing study, reasoning traces findings, batch-mode interaction recommendations.
- Updated [[Government and Civic Life]] — seeded with Habermolt AI-delegated deliberation paradigm and decentralization governance vacuum analysis.
- Updated [[Balanced Governance]] — added metacognition-as-governance framework, Restrict/Scaffold/Require education stances, decentralization governance challenges.
- Updated [[AI and Human Flourishing]] — seeded with scientific collaboration RCT, AI-equalizer/amplifier reconciliation, student literacy crisis data.
- Updated [[AI Agency Knowledgebase]] navigation with new digest link.
- Noted: blogwatcher-cli unavailable; web-based arXiv RSS discovery completed the source pass.
- Created [[Daily AI Agency Digest — 2026-05-26]].
- Added 8 accepted source records to `/sources/sources.jsonl` after direct web verification.
- Created [[Agentic Convergence Trap]] as a new core idea page.
- Updated [[Work]] — added MIT Tech Review labor data, HBR manager bottleneck, and manufacturing augmentation patterns.
- Updated [[AI Coding Agents]] — added Nolan Lawson slow-quality coding approach and multi-model review technique.
- Updated [[Human Agency]] — added evidence-based transition framing, data infrastructure needs, and agentic convergence as agency-loss risk.
- Updated [[Agentic Workflow Patterns]] — added multi-model independent review pattern and manager-of-managers workflow.
- Updated [[Balanced Governance]] — added Stanford AI Index 2026 responsible-AI gap data and agentic convergence governance needs.
- Updated [[Optimism Without Naivety]] — added data-driven labor market framing, Stanford jagged frontier, and Doctorow bubble perspective.
- Updated [[AI Agency Knowledgebase]] navigation.
- Noted: `blogwatcher-cli` was not available in the runtime; web-based source discovery via direct URL fetching completed the source pass.
- Created [[Daily AI Agency Digest — 2026-05-25]].
- Added 14 accepted source records to `/sources/sources.jsonl` after direct web/PDF verification; `blogwatcher-cli` was unavailable, so feed scanning was skipped.
- Created [[Positive Alignment]] and [[Human Review Checkpoints]].
- Updated [[Human Agency]], [[Responsible Deployment]], [[Education]], [[Work]], [[AI for School Districts]], [[Agentic Workflow Patterns]], [[Balanced Governance]], and [[Strongest AI Risk Arguments]].
- Updated source libraries [[Articles]], [[Papers]], [[Reports]], and navigation in [[AI Agency Knowledgebase]].
- Noted access issues for some candidate pages (for example McKinsey/ScienceDirect/Medium); skipped inaccessible candidates unless enough verified metadata/content was available elsewhere.

## [2026-06-02] update | Daily AI curator run — Tuesday (Creativity & Writing rotation)
- Created [[Daily AI Agency Digest — 2026-06-02]] anchored on the finding that readers don't penalize AI-authored fiction (no AI penalty in preregistered experiment) — but the absence of an audience check accelerates platform-driven creator displacement.
- Added 8 accepted source records to `/sources/sources.jsonl` from arXiv (June 2 listings) and blog/newsletter feeds (Mollick, WIRED).
- Updated [[Creativity]] — added Know Your Author findings (no AI penalty; effort heuristic), Mollick's "meaning-shaped attention vampires," and the five-stage AI literacy continuum.
- Updated [[AI Writing Partners]] — full rewrite from stub: intentionality framework, two modes of AI writing use, practical strategies, AI-as-writing-teacher distinction, platform vs. creator structural dimension.
- Updated [[AI and Creator Rights]] — added latest Good Advice Cupcake dispute details (Amazon GenAI Creators' Fund, Peretti's Xerox comparison, Brantz's NDA refusal, the "no AI penalty" escalation vector).
- Updated [[Human Agency]] — added AI-conformity findings (moral judgments susceptible to algorithmic influence) and New Social Image findings (AI competency undermines ownership/meaningfulness).
- Updated [[Cognitive Surrender]] — added Mollick's latest framing on friction (commercial logic of frictionless AI) and the Friction Paradox (deliberate friction as design requirement for agency-preserving AI).
- Updated [[Education]] — added five-stage AI literacy continuum and GenAI literacy interaction patterns study.
- Updated [[Agentic Workflow Patterns]] — added Deterministic Horizon (Attention Bottleneck Theorem, architectural ceiling at ~19-31 steps, tool delegation as architectural necessity).
- Updated [[Articles]] source library — added 8 new entries.
- Updated [[Home]] navigation and recent updates table.
- Noted: Tuesday (weekday) — arXiv feeds provided primary source discovery across cs.CY, cs.HC, and cs.AI. WIRED and One Useful Thing contributed key pieces. Rotation focus: Day 3 (Creativity & Writing). AI Writing Partners page was a stub — now a substantive page with intentionality framework and practical strategies.

## [2026-06-01] update | Daily AI curator run — Monday (arXiv + blog/newsletter)
- Created [[Daily AI Agency Digest — 2026-06-01]] anchored on the finding that standard AI alignment techniques destroy tutoring quality, plus disability-inclusive design requirements and global education equity gaps.
- Added 7 accepted source records to `/sources/sources.jsonl` from arXiv (June 1 listings).
- Updated [[AI Tutors]] — added TEI (GRPO destroys tutoring quality; signal-based evaluation), Special-R1 (first disability-inclusive RL tutoring), global usage patterns, EUDAIMONIA social safety dimension.
- Updated [[Education]] — added global usage equity data, higher ed structural barriers, Personalized to Persuade AI literacy paradox.
- Updated [[AI Tutor Evaluation Checklist]] — added signal-based quality assessment, disability-inclusive design requirement, social design safety checks, alignment tax risk.
- Updated [[Cognitive Surrender]] — added Personalized to Persuade AI literacy paradox, EUDAIMONIA social-design failure findings.
- Updated [[Co-Intelligence]] — added AI literacy paradox risk, contextualization backfire effect.
- Updated [[Articles]] source library — added 7 new entries.
- Updated [[Home]] navigation and recent updates table.
- Noted: Monday (weekday) — arXiv feeds provided primary source discovery across cs.CY, cs.HC, and cs.AI. Blog/newsletter feeds had no new AI-agency content since last week's coverage. Rotation focus: Day 1 (Education & Tutors).

## [2026-05-31] update | Daily AI curator run — Sunday (blog/newsletter sources only)
- Added 5 accepted source records to `/sources/sources.jsonl` from MIT Technology Review, WIRED, and Don't Worry About the Vase.
- Updated [[AI Research Agents]] — full rewrite from stub: added Google agentic scientist project, meaning-making critique, multi-model research workflows, deskilling risks.
- Updated [[Balanced Governance]] — added shareholder activism as parallel governance: $400B investor coalition, faith-based investors as governance actors, the public-company pipeline for AI labs.
- Updated [[Agentic Workflow Patterns]] — added hybrid model-routing pattern (Claude for planning/Codex for execution) from SemiAnalysis and Zvi's GPT-5.5 analysis.
- Updated [[Articles]] source library — added 6 new entries (Finn/Francois, Knibbs, Chen, Huckins, Zvi).
- Updated [[Home]] navigation and recent updates table.
- Noted: Sunday — arXiv not publishing; WIRED, MIT Technology Review, and Substack feeds provided source discovery. Rotation focus: Day 7 (Source Libraries & Tools).

## [2026-06-04] update | Daily AI curator run — Thursday (Curator Pass 2: Governance, Co-Existence & Practical Deployment rotation)
- Created [[Daily AI Agency Digest — 2026-06-04 (Curator Pass 2)]] anchored on the Co-Intelligence→Co-Existence framework transition, the governance inflection point (Trump EO prior restraint era, OpenAI PAC false flag, Anthropic S-1 IPO), and practical deployment evidence (Doc In a Box 97% physician agreement, Anthropic 80% self-written code, Salesforce Claude Code adoption). Five sources: all non-paper (Mollick newsletter, Zvi newsletter, Trump EO/White House, MIT TR healthcare, Anthropic institute report).
- Updated [[Co-Intelligence]] — added Mollick's Co-Existence framework evolution: retired Co-Intelligence frame, new book (October 2026), AI writes 80% of Anthropic's code, em-dash authenticity test, Co-Existence risk for novices.
- Updated [[AI Coding Agents]] — added Anthropic 80% self-written code data, 17x more code from coding agents, Salesforce Claude Code deployment, Zvi's Opus 4.8 daily driver assessment.
- Updated [[Healthcare]] — major expansion from stub: Doc In a Box 97% physician agreement data, MIT TR rehumanizing healthcare profile (WHO 11M shortage), practical examples with overcaution design pattern.
- Updated [[AI Agent Revolution]] — added Anthropic S-1 IPO filing, $500M/month Claude spend, Co-Existence transition section, Opus 4.8 capabilities.
- Updated [[Balanced Governance]] — added Trump EO (prior restraint era framework), OpenAI PAC false flag scandal (governance legitimacy crisis), OpenAI policy blueprint, Anthropic IPO as governance moment.
- Updated [[Creativity]] — added Mollick's visual AI evolution (Midjourney 2022 → Veo 3 2025, TikZ sparks comparison, open weights catching up).
- Updated [[Home Server AI Agents]] — added open weights catching up section (Gemma-4-12B, DeepSeek v4, Tencent HunyuanVideo, DeepSeek TikZ).
- Updated [[Articles]] source library — added 5 new entries (Mollick Co-Existence, Zvi AI #171, Trump EO, MIT TR healthcare, Anthropic recursive self-improvement).
- Updated [[Home]] navigation and recent updates table.
- Noted: Thursday (weekday) — complementary Pass 2 covering distinctly different sources and rotations from the morning Entrepreneurship & Agency Architecture pass. 0 of 5 sources are arXiv papers (0%); all are non-paper types (newsletter essays, policy, article, company report). The morning pass already covered arXiv comprehensively; this pass provides the blog/newsletter/policy complement.

## [2026-06-04] update | Daily AI curator run — Thursday (Entrepreneurship & Agency Architecture rotation)
- Created [[Daily AI Agency Digest — 2026-06-04]] anchored on the tension that the technologies most capable of expanding human agency are also the ones most capable of eroding it — and the difference is entirely in the architecture, not the capability. Seven sources: four papers (Digital Apprentice agency-preserving agent framework, AI emotional dependence OpenAI study, agentic pedagogy review, Delphi AI risk study of 272 experts), three non-papers (Microsoft 2026 Work Trend Index, MIT TR small business AI guide, SBE Council 82% small business AI adoption survey).
- Added 7 accepted source records to [[Articles]] source library.
- Updated [[Human Agency]] — added Digital Apprentice as architectural blueprint for agency-preserving agents; added AI emotional dependence as quiet agency risk from incidental AI use; added SMB adoption data as agency-at-scale.
- Updated [[AI Agent Revolution]] — added Digital Apprentice framework section (autonomy earned, not assumed) and Agentic Pedagogy section (six principles, four design recommendations).
- Updated [[AI and Human Flourishing]] — added AI emotional dependence study as flourishing risk: path-dependent preference shifts from humans to AI over 28 days.
- Updated [[Entrepreneurship]] — major expansion from stub: added SBE Council 82% data, MIT TR small business AI guide, Digital Apprentice as template, practical examples, and new risks (platform dependence, deskilling, homogenization, emotional dependence).
- Updated [[AI for Small Businesses]] — major expansion from stub: added SBE Council 82% adoption data, MIT TR guide coverage, practical examples by function, Digital Apprentice approach, Reverse-Centaur diagnostic.
- Updated [[Education]] — added Agentic Pedagogy review (six principles, four design recommendations including intentional friction and dynamic scaffolding).
- Updated [[Balanced Governance]] — added Delphi risk study: 18/24 risks >10% catastrophic under business-as-usual, 5/24 under mitigations. Developers bear highest responsibility.
- Updated [[Agentic Workflow Patterns]] — added earned-autonomy pattern from Digital Apprentice (methodology capture, authorization gates, continuous alignment).
- Updated [[Cognitive Surrender]] — added emotional surrender as distinct trajectory: relationship substitution, not task delegation, from 28-day OpenAI study.
- Updated [[Optimism Without Naivety]] — added Delphi study as empirical basis for the stance: catastrophic risk is design choice, not inevitability.
- Updated [[Family and Personal Life]] — added AI emotional dependence study as personal-life risk.
- Updated [[Articles]] source library — added 7 new entries.
- Updated [[Home]] navigation and recent updates table.
- Noted: Thursday (weekday) — arXiv feeds provided primary source discovery across cs.CY, cs.HC, and cs.AI. Microsoft Work Trend Index, MIT Technology Review, and SBE Council provided non-paper sources. Rotation focus: Entrepreneurship & Agency Architecture — two stubs (Entrepreneurship, AI for Small Businesses) received major expansions from stub status. 4 of 7 sources are papers (57%); 3 are non-papers (Microsoft report, MIT TR guide, SBE Council survey). Source diversity requirement met (≤60% papers, 3 non-papers).
- Created [[Daily AI Agency Digest — 2026-06-03]] anchored on the governance-agency nexus: design defaults (not model capability) determine whether AI amplifies or erodes human agency. Seven sources: four-factor agentic governance transparency framework, InquiryBits trust-boundary collaboration study, actionable scaffolding RCT (+10.8pp feedback), DeskCraft 31.6% professional workflow ceiling, HBR 2026 AI usage survey (third edition), Claude Opus 4.8 capabilities/reactions, and Doctorow's Reverse-Centaur book release.
- Added 7 accepted source records to `/sources/sources.jsonl`? Not yet. Sources captured in [[Articles]], [[Books]], and digest. (JSONL sync pending.)
- Updated [[Balanced Governance]] — added agentic governance transparency framework (model version, weight-release, provider, system-prompt as four required dimensions for auditable governance).
- Updated [[AI Agent Revolution]] — added Claude Opus 4.8 (4x self-correction, continued straight-line capability trajectory) and DeskCraft benchmark (GPT-5.4 31.6% on 50+ step professional workflows; human-in-the-loop remains essential).
- Updated [[Human Agency]] — added Reverse-Centaur diagnostic (Centaur vs. Reverse Centaur), scaffolding-as-agency (RCT evidence: +10.8pp feedback), and trust-boundary agency (InquiryBits finding: who sees matters more than what).
- Updated [[Agentic Workflow Patterns]] — added DeskCraft human-agent collaboration protocol (mid-turn + post-turn exchanges), InquiryBits trust-boundary trace sharing pattern, and editable scaffold dispatch pattern (RCT-validated).
- Updated [[AI as Copilot]] — added three new sources: Discretionary Work RCT (scaffolding validates copilot model), InquiryBits (trust-boundary design principle), DeskCraft (human-in-the-loop remains essential).
- Updated [[Agency Expansion Framework]] — added Discretionary Work RCT as empirical evidence, InquiryBits as collaborative agency evidence, and two new practical examples (scaffolding + trust-boundary design).
- Updated [[Task-Level AI Adoption]] — added HBR 2026 survey (widening uses, cognitive surrender anxiety) and Discretionary Work RCT (editable scaffolding as augmentation pattern).
- Updated [[Articles]] source library — added 6 new entries (Zhang/Chu/Krishnan agentic governance, Morris/Maes InquiryBits, Mahinpei et al. discretionary work, Wang et al. DeskCraft, Zao-Sanders HBR survey, Zvi Opus 4.8).
- Updated [[Books]] source library — added Doctorow Reverse-Centaur entry.
- Updated [[Home]] navigation and recent updates table.
- Noted: Wednesday (weekday) — arXiv feeds provided primary source discovery across cs.CY, cs.HC, and cs.AI. HBR, Zvi's newsletter, and Doctorow's book release provided non-paper sources. Rotation focus: Governance, Agents & Practical Tools — complementary to Tuesday's Creativity/Writing (AM) and Work/Labor (PM) rotations. 4 of 7 sources are papers (57%); 3 are non-papers (HBR article, newsletter/analysis, book).
- Created [[Daily AI Agency Digest — 2026-06-02 (Curator Pass 2)]] anchored on the data-intuition gap: labor data shows AI impact is still small and manageable, but the AI economy is growing at 2,600%/year with automated AI R&D accelerating — and we're investing less than 1% of AI spending on understanding the transition.
- Added 5 accepted source records from MIT Technology Review (Rotman), Import AI 459 (Clark), Pluralistic/The Nerve (Doctorow June 2 and May 26), and PIIE (Korinek et al.).
- Updated [[Work]] — added invisible AI economy measurement challenge (2,600% growth, $219B compute spending), Doctorow's "inconvenient humans" structural critique, and Clark's automated AI R&D analysis.
- Updated [[Future of Work]] — added Rotman, Korinek, and Doctorow sources.
- Updated [[Balanced Governance]] — added Leigh's "survival capital" concept, the AI satellite accounts measurement prerequisite, and the "who benefits?" structural challenge from Doctorow.
- Updated [[Responsible Deployment]] — added Korinek AI satellite accounts as a "measure" step.
- Updated [[AI and Human Flourishing]] — added survival capital framework and "progress that compounds vs. cancels itself out" frame.
- Updated [[Optimism Without Naivety]] — added the data-vs-intuition tension from June 2026 sources.
- Updated [[The Turing Trap]] — added Doctorow's "inconvenient humans" as a modern structural restatement.
- Updated [[AI Agent Revolution]] — added Clark's automated AI R&D evidence (SWE-Bench, METR, CORE-Bench, PostTrainBench, kernel optimization, alignment automation) and UK AISI automated alignment challenges.
- Updated [[AI and Inequality]] — major expansion from stub: added entry-level divide data, the "who benefits?" structural question, and four supporting sources.
- Updated [[Home]] navigation and recent updates table.
- Noted: Tuesday afternoon — this is the second curator pass today. The morning pass (Creativity & Writing rotation) covered arXiv 2606 papers and Mollick/WIRED features. This complementary pass covers the Work & Labor rotation with feature-length sources (MIT TR, Import AI, Pluralistic). No arXiv RSS needed — the feature/journalism/analysis sources provided rich material.

## [2026-06-04] update | Daily AI curator pass 3 (Democratization & Digital Divides rotation)
- Created [[Daily AI Agency Digest — 2026-06-04 (Curator Pass 3)]] anchored on democratization vs. digital divides: Gemma 4 12B laptop-ready open-weights AI; Cambridge children's AI empathy gap; graduation booing as cultural backlash; election safeguards for 2026; ILO "disruption without dividend."
- Added 5 accepted source records to `/sources/sources.jsonl` from Google DeepMind, Cambridge University, MIT Technology Review, OpenAI, and ILO/World Bank.
- Updated [[Case for AI Optimism]] — major expansion: Gemma 4 12B as democratization evidence, open-weights ecosystem maturity, ILO global exposure data, cultural trust signals.
- Updated [[Home Server AI Agents]] — expanded Gemma 4 12B section with architecture details, Apache 2.0 license, local-first sovereignty, child-safety tension.
- Updated [[Family and Personal Life]] — major expansion from stub: Cambridge empathy gap study, children as overlooked stakeholders, 50% student use vs 26% parent awareness, child-safe AI as ethical prerequisite.
- Updated [[Public Trust and AI]] — added graduation booing (Schmidt booed at U of Arizona), election trust paradox (safeguards vs. false flag operations), institutional credibility gap.
- Updated [[Government and Civic Life]] — added OpenAI and Anthropic 2026 election safeguards, AP vote-count integration, political balance scores, institutional trust paradox.
- Updated [[AI Tutors]] — added Cambridge empathy gap implications for children forming emotional bonds with educational AI.
- Updated [[Articles]] source library — added 5 new entries.
- Updated [[Home]] — added Pass 3 to navigation and recent updates table.
- Noted: Thursday evening — this is the third curator pass today. Pass 1 (Entrepreneurship & Agency Architecture) covered Digital Apprentice, emotional dependence, Agentic Pedagogy, Delphi risk, Microsoft WTI, and SMB AI. Pass 2 (Governance, Co-Existence & Practical Deployment) covered Mollick's Co-Existence, Zvi's AI #171, Trump EO, healthcare AI, Anthropic 80% code. This Pass 3 covers Democratization & Digital Divides with five thematically distinct sources spanning open-weights AI access, child safety, cultural backlash, election integrity, and global inequality.
