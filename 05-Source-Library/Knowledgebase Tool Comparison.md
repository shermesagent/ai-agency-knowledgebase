# Knowledgebase Tool Comparison

## Core Idea
This page evaluates display, editing, search, and AI/RAG layers for the Markdown/Git AI Agency Knowledgebase.

The current source of truth is the Git repository at `/home/writingtired/src/ai-agency-knowledgebase`. The best technical setup should preserve that portability while making the wiki easy to browse, search, edit, back up, and connect to AI tools.

## Working Recommendation
Start with **Markdown files in Git as the durable source of truth**. Add a display/search layer only when it clearly reduces friction.

Recommended path:
1. **Now:** Keep the repo as plain Markdown + Git. This is already agent-friendly, backup-friendly, and easy to inspect.
2. **Best web display candidate:** **Wiki.js** if Git-backed Markdown web publishing becomes useful.
3. **Best human editing clients:** **Obsidian + Git** or **Logseq + Git** for local/desktop editing.
4. **Best lightweight AI search path:** start with file search + Git + curated links; later add **Khoj**, **sqlite-vec**, **Chroma**, or **LanceDB** only if semantic search becomes necessary.
5. **Avoid early overbuild:** Do not add a full RAG stack, OAuth-heavy app, or database-first wiki until there is a clear use case.

## App Comparison

### Wiki.js
- **URL:** https://js.wiki/
- **Docker support:** Strong.
- **Markdown support:** Strong.
- **Git sync:** Strong; this is its main advantage for this wiki.
- **Search quality:** Good; can be extended with external search.
- **Ease of editing:** Good web editor.
- **AI/RAG friendliness:** Strong because Markdown/Git remains accessible.
- **Backup simplicity:** Good, though database/config backups still matter.
- **Mobile usability:** Usable web/PWA experience, not a native notes app.
- **Home-server complexity:** Moderate: more moving parts than plain Git, less than many collaboration suites.
- **Fit:** Best candidate if a browser-accessible self-hosted wiki is needed.

### Obsidian synced through Git
- **URL:** https://obsidian.md/
- **Docker support:** Not a server app.
- **Markdown support:** Excellent.
- **Git sync:** Excellent through normal Git workflow or plugins.
- **Search quality:** Excellent local search and plugin ecosystem.
- **Ease of editing:** Excellent for a technical or semi-technical owner.
- **AI/RAG friendliness:** Excellent because files stay plain Markdown.
- **Backup simplicity:** Excellent through Git.
- **Mobile usability:** Good with Obsidian mobile, but Git-based mobile sync can add friction.
- **Home-server complexity:** Very low; not a web display layer.
- **Fit:** Best personal editing environment; not enough by itself if a web wiki is desired.

### Logseq
- **URL:** https://logseq.com/
- **Docker support:** Community/server options exist, but it is mainly a local app.
- **Markdown support:** Strong; outline/block-based Markdown.
- **Git sync:** Strong because files are local.
- **Search quality:** Good, especially for backlinks and daily notes.
- **Ease of editing:** Excellent if the outliner model fits; awkward if long-form pages are preferred.
- **AI/RAG friendliness:** Strong; block-level notes can be useful for retrieval.
- **Backup simplicity:** Strong through Git.
- **Mobile usability:** Good, but sync choices matter.
- **Home-server complexity:** Low to moderate.
- **Fit:** Strong if the daily digest/outliner workflow feels natural.

### DokuWiki
- **URL:** https://www.dokuwiki.org/
- **Docker support:** Good through community images.
- **Markdown support:** Weak by default; uses DokuWiki syntax.
- **Git sync:** Not native, but flat files are easy to back up/version.
- **Search quality:** Basic but serviceable.
- **Ease of editing:** Simple web editing.
- **AI/RAG friendliness:** Moderate; files are readable, but not Markdown.
- **Backup simplicity:** Excellent because it is flat-file and database-free.
- **Mobile usability:** Serviceable with responsive themes.
- **Home-server complexity:** Very low.
- **Fit:** Good contrarian choice if web editing and minimal ops matter more than Markdown purity.

### BookStack
- **URL:** https://www.bookstackapp.com/
- **Docker support:** Strong.
- **Markdown support:** Available, but content is database-centered.
- **Git sync:** Weak/no native fit.
- **Search quality:** Good.
- **Ease of editing:** Strong, especially for non-technical users.
- **AI/RAG friendliness:** Weaker than Markdown/Git because extraction depends on API/database/export.
- **Backup simplicity:** Requires database backups.
- **Mobile usability:** Good responsive web.
- **Home-server complexity:** Moderate.
- **Fit:** Good human wiki, weaker fit for an agent-maintained Markdown/Git knowledgebase.

### Outline
- **URL:** https://www.getoutline.com/
- **Docker support:** Available but can involve several services and auth pieces.
- **Markdown support:** Excellent editing experience.
- **Git sync:** Weak/no native fit.
- **Search quality:** Strong.
- **Ease of editing:** Excellent.
- **AI/RAG friendliness:** Moderate via API/export, not file-native.
- **Backup simplicity:** Requires database/object storage backup discipline.
- **Mobile usability:** Good web experience.
- **Home-server complexity:** Higher than needed for this project.
- **Fit:** Beautiful but likely overbuilt and not aligned with Git-as-source-of-truth.

### MediaWiki
- **URL:** https://www.mediawiki.org/
- **Docker support:** Strong.
- **Markdown support:** Weak by default; uses wikitext.
- **Git sync:** Weak/no native fit.
- **Search quality:** Strong at scale with the right extensions.
- **Ease of editing:** Powerful but heavier learning curve.
- **AI/RAG friendliness:** Moderate through API/dumps.
- **Backup simplicity:** Requires database/files backup.
- **Mobile usability:** Good.
- **Home-server complexity:** High relative to need.
- **Fit:** Overkill unless Wikipedia-style collaboration and scale are required.

### Joplin Server
- **URL:** https://joplinapp.org/
- **Docker support:** Strong.
- **Markdown support:** Strong in clients.
- **Git sync:** Weak; uses Joplin sync model.
- **Search quality:** Good in clients.
- **Ease of editing:** Good.
- **AI/RAG friendliness:** Moderate/weak because content is not simply the repo.
- **Backup simplicity:** Requires server/database backup or export process.
- **Mobile usability:** Excellent native clients.
- **Home-server complexity:** Moderate.
- **Fit:** Good notes app, not ideal for this Git wiki.

### Anytype
- **URL:** https://anytype.io/
- **Docker support:** Not the cleanest fit for simple self-hosted Markdown wiki use.
- **Markdown support:** Export/import oriented rather than Markdown-as-source.
- **Git sync:** Weak/no fit.
- **Search quality:** Good object search.
- **Ease of editing:** Good block/object editor.
- **AI/RAG friendliness:** Weak because storage is not plain Markdown.
- **Backup simplicity:** More complex than plain Git.
- **Mobile usability:** Strong.
- **Home-server complexity:** Higher than justified.
- **Fit:** Not recommended for this project.

## AI/RAG and Search Options

### Khoj
- **URL:** https://khoj.dev/ and https://github.com/khoj-ai/khoj
- **Fit:** Strong candidate if semantic search over Markdown becomes important. Designed as an AI second brain and can work with local files.
- **Caution:** Adds another service and indexing pipeline.

### AnythingLLM
- **URL:** https://anythingllm.com/ and https://github.com/Mintplex-Labs/anything-llm
- **Fit:** Good all-in-one RAG workspace option.
- **Caution:** More application surface than a simple wiki needs.

### Open WebUI Knowledge/RAG
- **URL:** https://github.com/open-webui/open-webui
- **Fit:** Useful because Open WebUI is already on the server; can provide chat-over-docs workflows.
- **Caution:** Uploaded knowledge collections should not become the source of truth; keep Markdown/Git primary.

### Dify
- **URL:** https://dify.ai/ and https://github.com/langgenius/dify
- **Fit:** Powerful for building AI workflows and knowledge apps.
- **Caution:** Likely too heavy for the initial daily-curated wiki.

### LlamaIndex / LangChain
- **URLs:** https://www.llamaindex.ai/ and https://www.langchain.com/
- **Fit:** Good if a custom RAG API is needed later.
- **Caution:** Custom pipelines create maintenance burden: chunking, embeddings, vector stores, model updates, and evaluation.

### Lightweight vector/search tools
- **sqlite-vec:** https://github.com/asg017/sqlite-vec — promising minimal vector search in SQLite.
- **Chroma:** https://www.trychroma.com/ — easy Python-native vector store.
- **LanceDB:** https://lancedb.com/ — local/on-disk vector database option.
- **Qdrant:** https://qdrant.tech/ — robust Docker-friendly vector database.
- **txtai:** https://github.com/neuml/txtai — embeddings search/RAG toolkit.
- **Meilisearch:** https://www.meilisearch.com/ — fast typo-tolerant full-text search.
- **Typesense:** https://typesense.org/ — fast full-text/search API.

## Contrarian Risks
- **Editing friction:** Markdown/Git is perfect for agents and technical users, but can be awkward on mobile or for non-technical collaborators.
- **RAG complexity:** Semantic search requires a pipeline: file watcher, chunker, embedder, vector store, retriever, evaluation loop.
- **Merge conflicts:** Concurrent edits to long Markdown pages can conflict.
- **Mobile capture:** Quick capture from a phone may need Obsidian Sync, Logseq Sync, a web UI, or a separate inbox workflow.
- **Overbuilding:** A database-first wiki or full RAG stack can undermine the simplicity of the Markdown/Git source of truth.
- **Tool lock-in:** Even “open” RAG pipelines can become bespoke systems that are hard to migrate.

## Decision Rule
Use the simplest layer that solves the current pain:
- Need durable agent-maintained knowledge? **Markdown/Git only.**
- Need better personal editing? **Obsidian + Git** or **Logseq + Git.**
- Need browser-readable wiki? **Wiki.js.**
- Need non-technical web editing with minimal ops and no Markdown purity? **DokuWiki.**
- Need semantic Q&A? Start with **Khoj** or **sqlite-vec/Chroma + a small script**, not a full platform.

## Related Pages
- [[Home Server AI Agents]]
- [[AI Research Agents]]
- [[Responsible Deployment]]
- [[Practical AI]]

## Tags
#tools #home-server-ai #practical-ai #source-library #ai-agents
