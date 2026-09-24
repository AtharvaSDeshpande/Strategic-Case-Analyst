# Strategy analysis playbook

A reusable method kit for running structured strategy analysis with an AI assistant. It contains
seven framework skills, a wiki template that lets the assistant accumulate judgment across runs, a
workflow rules file, and three generic prompts.

**No case materials are included.** This repository holds method only: no case studies, no company
or personal names, no analysis outputs, no findings. It was extracted from a private project and
sanitised. Bring your own case material.

## What is here

```
skills/                 seven framework skills, each a SKILL.md with YAML front matter
wiki-template/          the accumulating-memory structure, with empty judgment files
rules/project-rules.md  the end-to-end workflow, including the evidence and audit gates
prompts/prompts.json    bootstrap, lint-wiki, and a build-case prompt with a placeholder
```

The seven skills are industry analysis, internal assessment, competitive strategy, adjacencies,
diversification and corporate strategy, implementation and leadership, and innovation and dynamic
capabilities. Each covers when to use the framework, its steps, how to apply it well, common
pitfalls, quality checks, and the diagram convention practitioners actually use.

## Install

**Claude Code.** The YAML front matter in each `SKILL.md` is already in the expected format. Place
the `skills/` directories where your installation loads skills from, then invoke a skill by name.

**Antigravity.** Place the skill directories wherever your configuration loads skills from, and
point the workflow at `rules/project-rules.md`.

**Any other chat assistant.** Open the relevant `SKILL.md` and paste its text into your project
instructions or custom instructions. The files are written to work as plain prompt text with no
tooling.

To use the accumulating memory, copy `wiki-template/` to a working `wiki/` directory once, then let
the assistant read it at the start of a run and update it at the end. The template ships empty on
purpose: the judgment files have headers and entry formats but no entries.

## Optional dependencies

None of these are required, and none are bundled.

- **Graphviz** for node-link diagrams such as hierarchies and relationship networks.
- **Python with matplotlib** for the fixed-layout framework exhibits: cross layouts, two-by-two
  grids, bubble matrices, value chains.
- **Understand-Anything** (https://github.com/Egonex-AI/Understand-Anything) for knowledge graphs.
  The workflow has a hand-authored fallback if it is unavailable.

## Credits

- The accumulating-wiki pattern comes from Andrej Karpathy's `llm-wiki.md` gist:
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Optional knowledge-graph tooling: https://github.com/Egonex-AI/Understand-Anything

The frameworks themselves are standard strategy tools and are described here in the maintainer's
own words. Nothing in this repository reproduces a textbook, a case study, or any copyrighted
teaching material.

## Scope and honesty note

The method files encode a bias that is worth stating: they push hard toward evidence discipline,
toward marking what the sources do not show rather than filling it in, and toward exhibits that
carry real figures instead of generic labels. That is a deliberate stance, not a neutral one.
