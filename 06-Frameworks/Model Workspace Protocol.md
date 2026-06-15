# Model Workspace Protocol (MWP)

## Core Idea
Replace framework-level agent orchestration with filesystem structure. Numbered folders represent sequential stages. Plain markdown files carry the prompts and context that tell a single AI agent what role to play at each step. Local scripts handle mechanical work that doesn't need AI.

Defined in **Interpretable Context Methodology: Folder Structure as Agentic Architecture** (Van Clief & McDermott, arXiv 2603.16021, March 2026).

## Why It Matters
MWP inverts the complexity curve of multi-agent frameworks. Instead of building code abstractions (CrewAI, LangChain, AutoGen) to coordinate agents, you use the filesystem — the most universal interface in computing. Every stage output is a plain file a human can read, edit, or override before the next stage runs. This makes agent workflows:

- **Self-documenting** — the folder structure IS the workflow diagram
- **Human-edit-friendly** — any text editor can modify intermediate artifacts
- **Language-agnostic** — no framework lock-in, stage scripts can be any language
- **Context-efficient** — agents load only the files relevant to the current stage (2k–8k tokens per stage vs 30k–50k in monolithic prompts)

MWP is not a response to multi-agent complexity; it is a deliberate return to Unix philosophy from the 1960s/70s. Programs that do one thing. Output of one becomes input of another. Plain text as universal interface.

## MWP Five-Layer Context Model

| Layer | File | Purpose | Typical Size |
|-------|------|---------|-------------|
| 0 | `CLAUDE.md` or `AGENTS.md` | Identity: where am I? | ~800 tokens |
| 1 | `CONTEXT.md` (workspace root) | Routing: where do I go? | ~300 tokens |
| 2 | `CONTEXT.md` (per stage) | Contract: what do I do? | ~200-500 tokens |
| 3 | `references/`, `_config/`, `shared/`, `skills/` | Reference: what rules apply? | Variable |
| 4 | `output/` | Working artifacts: what am I working with? | Variable |

An agent reads down the layers and stops when it has what it needs. A rendering agent only needs Layers 0-2. A script-writing agent reads to Layer 4 for voice rules (Layer 3) and source material (Layer 4).

## Workspace Structure

```
workspace/
  CONTEXT.md               # Layer 1: task routing
  stages/
    01-research/
      CONTEXT.md            # Layer 2: stage contract
      references/           # Layer 3: reference material
      output/               # Layer 4: working artifacts
    02-script/
      CONTEXT.md
      references/
      output/
    03-production/
      CONTEXT.md
      references/
      output/
  _config/                  # Layer 3: brand, voice, design system
  shared/                   # Layer 3: cross-stage resources
  skills/                   # Layer 3: bundled domain knowledge
  setup/
    questionnaire.md        # One-time onboarding
```

## Design Principles
1. **One stage, one job** — a research stage doesn't write, a writing stage doesn't build (Unix principle)
2. **Plain text as interface** — stages communicate through markdown files. Any tool can participate, any human can inspect
3. **Layered context loading** — agents load only needed context, improving model performance (prevention over compression)
4. **Every output is an edit surface** — human can open, edit, and save intermediate files before the next stage runs
5. **Configure the factory, not the product** — one-time setup for preferences/brand/style, each run produces a new deliverable

## Related Patterns
- [[Agentic Workflow Patterns]] — broader taxonomy of agent coordination approaches
- [[Home Server AI Agents]] — practical implementation context on Hermes Agent infrastructure
- [[file:05-Source-Library/references/ICM-MWP-Paper.pdf]] — full paper PDF

## Tags
#framework #agentic-architecture #mwpf #unix-philosophy
