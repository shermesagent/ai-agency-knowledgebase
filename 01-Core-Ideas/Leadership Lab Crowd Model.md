# Leadership Lab Crowd Model

## Core Idea
The Leadership / Lab / Crowd model is a three-layer organizational framework developed by Ethan Mollick for AI adoption. It argues that successful AI integration requires coordinated action across three distinct organizational layers — not just "give everyone access and hope for the best."

**Leadership** sets vision, incentives, and permission. **The Crowd** (employees) discovers what AI can do through trial and error. **The Lab** (centralized AI team) productizes discoveries, builds benchmarks, and creates provocations.

The model's key insight: all three layers must function together. Leadership without Crowd is top-down AI initiatives nobody uses. Crowd without Leadership is "Secret Cyborgs" — workers hiding their AI use. Lab without either is a research group building things nobody needs.

## Why It Matters
Most organizations are failing at AI adoption because they're treating it as a tool deployment problem rather than an organizational learning challenge. Official AI usage maxes out at ~20% of workers while over 40% use AI in secret — a massive hidden adoption gap driven by worker incentives that punish disclosure. The model diagnoses why and prescribes how to fix it.

For the Superagency thesis, this model provides the organizational implementation layer: how do you build an organization where AI expands human capability rather than replacing or hiding it?

## Best Supporting Sources
- Ethan Mollick, "Making AI Work: Leadership, Lab, and The Crowd" (May 28, 2026) — https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- MIT Technology Review / Ema, "Rethinking organizational design in the age of agentic AI" (May 26, 2026) — https://www.technologyreview.com/2026/05/26/1137584/ — convergently arrives at a similar three-pillar framework

## The Three Layers

### Leadership
- Set a clear vision for how AI should change work. What will work be like? Will efficiency gains lead to layoffs or growth? How will workers be rewarded?
- **Solve the Secret Cyborg problem**: publicly commit that productivity gains won't lead to layoffs. Build incentives (promotions, cash rewards, recognition) for discovering transformative AI use cases. Model AI use yourself.
- Replace vague "AI ethics" talks with specific permission boundaries: "here's where experimentation of any kind is permitted."
- The General Counsel's office is often the choke point. Provide HIPAA-compliant, enterprise-safe AI access.

### The Crowd
- Experienced workers are the best AI discoverers — they know their jobs well enough to assess when AI is actually useful.
- The discovery process benefits from cross-functional mixing: embedding engineers with subject matter experts and marketers in cross-functional teams.
- Training should focus less on prompting techniques and more on hands-on practice communicating needs to AI.

### The Lab
- Consists of subject matter experts and AI enthusiasts from The Crowd.
- **Productize discoveries fast**: take prompts and solutions from The Crowd, build quick products, test, release, measure.
- **Build organization-specific AI benchmarks**: public benchmarks are "flawed or focus on trivia, math, or coding." You need benchmarks for YOUR actual tasks.
- **Build provocations**: demos of what seems impossible today. Visceral experiences jolt people into understanding AI's potential.
- **Build what doesn't work yet**: prototype full agent automation of key business processes, identify failure points, and plug in new models as they improve. When the models cross critical thresholds, you have deployable prototypes ready.
- **Infrastructure for The Lab:** The HARP platform (Human-AI Research Platform, arXiv 2607.20773, July 2026) provides exactly the kind of tool The Lab needs — configurable, reproducible human-AI interaction research. Place participants in controlled scenarios with live AI agents, collect not just transcripts but pre-submission prompt drafts, hesitations, and revisions. This is the methodology for building organization-specific benchmarks: you need to see what people *don't* send to the AI to understand when and why they surrender their own judgment. HARP makes Lab-style AI interaction research a reproducible design object rather than a one-off experiment. A Lab without this kind of infrastructure is flying blind — measuring outputs without understanding the interaction process that produced them.

### Why the Model Matters More When Roles Narrow

The Scientific Labor Reorganization finding (Zheng et al., arXiv 2607.20923, July 2026) reinforces the urgency of the three-layer model. LLM-era science shows more interdisciplinarity at the project level but narrower individual roles — 775,323 scientists taking on fewer distinct CRediT roles. The AI coordination layer enables larger, more diverse teams while making individuals more specialized and less capable of cross-functional understanding.

The three-layer model is the defense against this narrowing: **Leadership** sets a vision for team design that maintains role breadth; **The Crowd** surfaces where narrowing is happening — the workers who feel their skills contracting; and **The Lab** builds tools and benchmarks that measure not just AI performance but human capability development over time. Without all three layers, organizations drift toward AI-optimized narrowness: AI coordinates, humans execute narrow roles, and the cross-functional judgment that drives innovation atrophies. → See [[Democratization of Expertise#The Narrowing Role]] for the full analysis.

## Practical Examples
- Mollick "vibe-benchmarked" Manus (Claude-based agent) on a Wharton business simulation that normally takes student teams dozens of hours. Manus produced a 45-page business model analysis, website, pitch deck, and financial deep-dive in minutes with fewer mistakes than talented students.
- One enterprise switched from output metrics (cost per query) to outcome metrics (% of contracts reviewed without human escalation) and measured ROI from agentic AI tripled in two quarters.
- Companies in heavily regulated industries are adopting AI across all functions with proper enterprise-grade security — the General Counsel bottleneck is solvable.

## Risks / Limits
- **Requires organizational resources**: Small businesses, nonprofits, and government agencies may lack the resources to stand up "The Lab."
- **The model assumes cooperative Leadership**: What if leadership uses AI gains to cut costs rather than grow? The worker incentive problem isn't just about disclosure — it's about trust that the organization won't exploit AI productivity gains against workers.
- **The pace of technology change may outrun organizational learning**: Opus 4.8 dropped six weeks after 4.7. Labs building against 4.7 may find their work obsolete before deployment.

## Related Pages
- [[Frontier Firm]]
- [[Agentic Business Transformation]]
- [[Work]]
- [[Co-Intelligence]]
- [[AI Use Case Evaluation Rubric]]
- [[Cognitive Surrender]]

## Tags
#future-of-work #augmentation #practical-ai #ai-agents #entrepreneurship #superagency
