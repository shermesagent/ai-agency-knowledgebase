# AI Agency Knowledgebase Schema

## Domain
This wiki tracks AI optimism, human agency, responsible acceleration, practical adoption, augmentation over replacement, techno-humanism, and “what could go right” thinking in the spirit of *Superagency*.

This is **not** a random AI news archive. It is a curated, cross-linked knowledgebase about how AI can expand individual, organizational, civic, educational, creative, and economic agency while preserving thoughtful risk analysis.

## Folder Structure
- `/Home.md` — front door and navigation
- `/00-Daily-Digests/` — daily curated research digests
- `/01-Core-Ideas/` — durable concepts and mental models
- `/02-Domains/` — adoption domains such as education, work, civic life, family life, and home-server agents
- `/03-Arguments/` — pro/con arguments, risk debates, governance, inequality, flourishing
- `/04-Use-Cases/` — concrete workflows, roles, tools, and examples
- `/05-Source-Library/` — accepted source indexes by type
- `/06-Frameworks/` — reusable decision frameworks and rubrics
- `/07-Open-Questions/` — unresolved questions worth revisiting
- `/raw/` — immutable source notes or extracted text, kept separate from polished wiki pages
- `/sources/` — structured metadata such as JSONL source records

## Naming Conventions
- Use the user-specified page names with spaces for reader-facing wiki pages.
- Use double-bracket wikilinks for internal links, e.g. link to the exact reader-facing page title.
- Every concept/domain/argument/use-case/framework page should follow the page template unless it is an index or source library.
- Daily digest files use `YYYY-MM-DD.md`.
- Source metadata records preserve original URLs and cite sources; do not plagiarize.

## Required Page Template
Every concept page should use this format:

```markdown
# Page Title

## Core Idea
Explain the idea in plain language.

## Why It Matters
Explain why this idea matters for human agency and AI adoption.

## Best Supporting Sources
List sources with links and short summaries.

## Practical Examples
Give real-world examples.

## Risks / Limits
Explain what could go wrong or where the idea becomes too simplistic.

## Related Pages
Link to related wiki pages.

## Tags
Add relevant tags.
```

## Daily Digest Requirements
Daily digests must include:
1. Executive Summary
2. Best Sources Found
3. Superagency Connections
4. Tensions / Counterarguments
5. Practical Applications
6. Pages to Create or Update
7. Tags
8. Top Insight of the Day
9. Practical Experiment to Try

## Source Filtering Rules
Accept sources only when they are relevant, thoughtful, credible enough to cite, and add a useful idea, framework, case study, warning, or practical application.

Reject shallow SEO posts, generic hype, duplicate coverage without a distinct angle, pure product marketing without a usable workflow/case study, and alarmism with no practical insight.

## Scoring
- Reliability score: 1–5
- Relevance score: 1–5
- Prefer sources with both scores >= 4 for the digest.
- Include thoughtful criticism even when it challenges AI optimism.

## Tag Taxonomy
Allowed tags:
- #superagency
- #human-agency
- #ai-education
- #ai-agents
- #augmentation
- #governance
- #responsible-ai
- #ai-optimism
- #future-of-work
- #practical-ai
- #creativity
- #entrepreneurship
- #civic-life
- #family-life
- #home-server-ai
- #risk
- #counterarguments
- #tools
- #research
- #source-library

## Update Policy
Each daily run must:
1. Save the daily digest.
2. Update at least 3 existing wiki pages.
3. Recommend 1–3 new pages.
4. Add accepted sources to `/sources/sources.jsonl` and to the relevant `/05-Source-Library/` page.
5. Create a “Top Insight of the Day.”
6. Create a “Practical Experiment to Try.”
7. Commit changes to Git with message `Daily AI agency knowledgebase update — YYYY-MM-DD`.

## Provenance and Ethics
- Preserve URLs.
- Separate facts from interpretation.
- Keep direct quotes short and cite clearly.
- Summarize in original language; do not copy article text.
- Never treat one optimistic source as proof.
- Always include thoughtful risks and counterarguments.
