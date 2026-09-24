---
name: install-visual-tooling
description: Check for, and optionally install, the tools this playbook's framework diagrams use when they're actually rendered as images rather than just described — Python with matplotlib for fixed-layout exhibits (crosses, two-by-two grids, bubble matrices, value chains), the Graphviz binary for node-link diagrams, and optionally the Understand-Anything knowledge-graph tool. Nothing here is required for the skill files themselves, which work as plain prompt text with no tooling. Use when the user asks to set up, check, or install the diagram/visualization tooling for this repository, or when a diagram step is about to run and the required tool's presence hasn't been confirmed yet.
---

# Install visual tooling

## When to use this

- The user explicitly asks to set up, check, or install the optional diagram tooling.
- You are about to run a diagram-rendering step (Step 6 of `rules/project-rules.md`) and haven't
  confirmed the relevant tool is actually installed yet — check first rather than assuming.
- Nothing here should run silently or proactively outside those two triggers. Installing software
  is an action with real side effects on the person's machine; always say what you're about to run
  and why before running it.

## What it installs, and why each one is optional

| Tool | Used for | Required? |
|---|---|---|
| Python + `matplotlib` | Fixed-layout exhibits: crosses, two-by-two grids, bubble matrices, value chains | Only if you want rendered images instead of a described layout |
| Graphviz (`dot` binary) | Node-link diagrams: hierarchies, relationship networks | Only if a case needs a node-link exhibit |
| Understand-Anything (github.com/Egonex-AI/Understand-Anything) | Knowledge graphs | Never — the workflow has a hand-authored fallback (see `rules/project-rules.md`, Step 9) |

None of the three are bundled in this repository. The installer scripts under `scripts/` fetch them
on request; they change nothing on a fresh clone until someone actually runs one.

## How to run it

1. **Check what's already there, without installing anything:**
   - Windows: `scripts\install-optional-deps.ps1 -CheckOnly`
   - macOS/Linux: `scripts/install-optional-deps.sh --check-only`
2. **Install matplotlib and Graphviz** (the two used by the standard diagram conventions):
   - Windows: `scripts\install-optional-deps.ps1`
   - macOS/Linux: `scripts/install-optional-deps.sh`
3. **Also pull in Understand-Anything**, only if the user specifically wants knowledge-graph
   rendering and has accepted that it's a separate, externally maintained project:
   - Windows: `scripts\install-optional-deps.ps1 -IncludeKnowledgeGraphTool`
   - macOS/Linux: `scripts/install-optional-deps.sh --with-knowledge-graph-tool`

## How to report the result

Read the script's own summary block and relay it plainly — installed / already present / skipped /
failed, per tool. This repository's standing rule is fail-loud, not fail-quiet: if Graphviz's binary
install fails or needs a new terminal session to be picked up on PATH, say that explicitly rather
than assuming it worked. Never claim a tool is available because the install command exited without
an error; confirm it with `-CheckOnly` / `--check-only` afterward, or with a direct
`python -c "import matplotlib"` / `dot -V` check, before relying on it in a diagram step.

## What this does not do

- It does not choose which diagram tool to use for a given framework — that's
  `rules/project-rules.md` Step 6's tool-matching table (Graphviz for genuine node-link structures,
  matplotlib for fixed spatial layouts).
- It does not touch anything outside installing these three tools: no case files, no wiki, no
  scripts other than itself.
