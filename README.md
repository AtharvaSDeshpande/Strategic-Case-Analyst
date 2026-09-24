# Strategic-Case-Analyst

A reusable method kit that turns an AI assistant into a strategy analyst: it applies the right
strategy framework to a real company, checks every fact it uses against a source it actually opened,
draws a clean diagram for each framework, and remembers what it learned for next time.

**No case materials are included.** This repository holds method only — no case studies, no company
or personal names, no analysis outputs, no findings. Bring your own case material.

## What you get

- **Seven framework skills** — plain-English guides for when and how to apply industry analysis,
  internal assessment, competitive strategy, adjacencies/new-market analysis, diversification and
  corporate strategy, implementation and leadership, and innovation/dynamic capabilities.
- **An evidence-first workflow** (`rules/project-rules.md`) — every claim is logged with its source
  before it's allowed into an analysis, and a fact-check audit runs before anything is finalized.
- **Framework visualization** — each framework has a standard, professional diagram convention built
  in (a five-forces cross, a two-by-two grid, a bubble matrix, a value-chain chevron, and so on), so
  the output is a real chart with your company's own numbers in it, not a generic template.
- **A self-improving wiki** (`wiki-template/`) — after every run, what was learned about applying each
  framework well gets written down, so the tenth analysis starts smarter than the first.
- **A reflection-paper skill** (`SKILL.md`, at the repo root) — a ready-to-use, end-to-end workflow
  for the specific deliverable this kit was built around: a fact-checked, diagram-illustrated
  strategy reflection paper on real companies.

## Quick start

1. **Open this folder in your AI assistant** (Claude Code, or any tool that reads skill files —
   see "Using it with other tools" below).
2. **Copy the wiki template once**, so the assistant has somewhere to write down what it learns:
   ```
   cp -r wiki-template wiki        # macOS/Linux
   ```
   ```
   Copy-Item -Recurse wiki-template wiki   # Windows PowerShell
   ```
3. **(Optional) Install the diagram-rendering tools**, if you want the assistant to actually draw
   the framework exhibits as images rather than just describe them:
   ```
   scripts/install-optional-deps.sh          # macOS/Linux
   ```
   ```
   scripts\install-optional-deps.ps1          # Windows
   ```
   This installs Python + matplotlib (for grids, crosses, and bubble matrices) and the Graphviz
   binary (for node-link diagrams). Nothing here is required — every skill file also works as plain
   prompt text with no tooling at all, and the assistant will just describe a layout in words instead
   of rendering it if you skip this step. See **Optional dependencies** below for exactly what gets
   installed and why each piece is optional.
4. **Tell the assistant what you want done.** For example:
   - "Read SKILL.md and build the reflection paper for [companies]."
   - "Run the bootstrap prompt from `prompts/prompts.json`."
   - "Apply the industry-analysis skill to [company]."
5. **Review the output.** The assistant's job is to log evidence and flag what it can't verify — a
   human still validates the final conclusions (see `wiki/validated-conclusions.md` once the wiki
   exists).

## Using it with other tools

- **Claude Code**: the YAML front matter in each `SKILL.md` is already in the format Claude Code
  expects. Point it at this folder and it will pick up the skills automatically.
- **Antigravity**: place the `skills/` directories wherever your configuration loads skills from, and
  point the workflow at `rules/project-rules.md`.
- **Any other chat assistant**: open the relevant `SKILL.md` and paste its text into your project or
  custom instructions. The files are written to work as plain prompt text — no tooling required.

## What's in this repository

```
SKILL.md                    the reflection-paper workflow: the whole thing, start to finish
skills/                     seven framework skills, each a SKILL.md with YAML front matter
  install-visual-tooling/   a skill that checks/installs the optional diagram tools on request
scripts/                    the optional installer (Windows .ps1 and macOS/Linux .sh)
wiki-template/              the accumulating-memory structure, with empty judgment files
rules/project-rules.md      the end-to-end analysis workflow, including the evidence and audit gates
prompts/prompts.json        bootstrap, lint-wiki, and a build-case prompt with a placeholder
```

## Optional dependencies

None of these are required, and none are bundled by default. Run `scripts/install-optional-deps.sh`
(or the `.ps1` on Windows) to install what you want — nothing installs until you run it. See
`skills/install-visual-tooling/SKILL.md` for the full detail on what each one is for.

- **Python with matplotlib** — for the fixed-layout framework exhibits: cross layouts, two-by-two
  grids, bubble matrices, value chains.
- **Graphviz** — for node-link diagrams such as hierarchies and relationship networks.
- **Understand-Anything** (https://github.com/Egonex-AI/Understand-Anything) — for knowledge graphs.
  Off by default even when you run the installer (pass `--with-knowledge-graph-tool` /
  `-IncludeKnowledgeGraphTool` to include it); the workflow has a hand-authored fallback if it's
  unavailable, and it's a separately maintained project with its own license.

## Credits

- The accumulating-wiki pattern comes from Andrej Karpathy's `llm-wiki.md` gist:
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Optional knowledge-graph tooling: https://github.com/Egonex-AI/Understand-Anything

The frameworks themselves are standard strategy tools and are described here in the maintainer's own
words. Nothing in this repository reproduces a textbook, a case study, or any copyrighted teaching
material.

## Scope and honesty note

The method files encode a bias that is worth stating: they push hard toward evidence discipline,
toward marking what the sources do not show rather than filling it in, and toward exhibits that carry
real figures instead of generic labels. That is a deliberate stance, not a neutral one.
