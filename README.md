# StrategistAgent

A multi-agent strategy analyst, not a document generator. Say **"Run Agent \<name\>"** and it runs a
full engagement — competitor teardown, due-diligence screen, market entry call, board memo, and five
more — through an isolated panel of framework lenses, a mandatory red-team attack on its own
conclusion, and a fact-check gate that blocks the output if a cited number doesn't check out.

**No case materials are included.** This repository holds method only — no case studies, no company
or personal names, no analysis outputs, no findings. Bring your own subject.

## What you get

- **Eight orchestrator agents**, one per real engagement type (see the table below). Each one is a
  self-contained `SKILL.md` that runs its own multi-agent workflow start to finish — you never have
  to sequence the steps yourself.
- **A seven-lens panel** — industry analysis, internal assessment, competitive strategy, adjacencies,
  diversification and corporate strategy, implementation and leadership, and innovation/dynamic
  capabilities — each a plain-English guide to one strategy framework, reused across every engagement.
- **A red team that never grades its own homework** — every converged conclusion gets attacked by a
  separate pass whose only job is to find the strongest counter-argument, before anything ships.
- **A fact-check gate that blocks, not flags** — every cited claim gets re-opened and re-checked
  against its source; the deliverable does not ship until it passes.
- **Framework visualization** — each lens has a standard, professional diagram convention built in (a
  five-forces cross, a two-by-two grid, a bubble matrix, a value-chain chevron, and so on), so the
  output is a real chart with your subject's own numbers in it, not a generic template.
- **A self-improving wiki** (`wiki-template/`) — after every run, what was learned about applying each
  framework well gets written down, so the tenth engagement starts smarter than the first.
- **An industry-standard documentation report on every run** — alongside the deliverable itself, you
  get a methodology note: scope, which lenses ran and why, the evidence base, the red-team outcome,
  and — always — what the evidence couldn't show.

## Run an agent

Say **"Run Agent \<name\>"**:

| Say this | You get |
|---|---|
| `Run Agent CompetitorTeardown` | A weighted competitive profile matrix, one battlecard per rival, and a "where we actually lose" note |
| `Run Agent CommercialDD` | A four-part due-diligence screen (market, target, peers, risk register) plus what the evidence can't show |
| `Run Agent MarketEntry` | Five forces on the target market, a capability-transfer test, an entry-cost floor, and a go/no-go |
| `Run Agent CompetitiveMonitor` | A quarterly diff: only material moves since last time, plus which prior conclusions are now stale |
| `Run Agent DecisionMemo` | A two-page board/IC memo: options, a weighted decision with visible weights, a sensitivity line, a mandatory counter-case |
| `Run Agent RegulatoryImpact` | A draft regulation mapped provision-by-provision to who it actually helps and hurts |
| `Run Agent PortfolioReview` | A portfolio matrix on disclosed business units, a funding-capacity check, a pipeline read |
| `Run Agent ReflectionPaper` | The academic version: a 5-6 page concept-silent reflection paper on three real companies (coursework, not client work) |

If you're not sure which one fits, just describe what you need — the router in the root `SKILL.md`
will match it to the table above, or tell you if nothing here fits.

## Quick start

1. **Open this folder in your AI assistant** (Claude Code, Antigravity, or any tool that reads skill
   files — see "Using it with other tools" below).
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
4. **Say "Run Agent \<name\>"** from the table above, or describe the task and let the router match
   it.
5. **Review the output.** Every agent produces its deliverable *and* a `documentation-report.md`
   alongside it — read that first if you want to know what ran, what it found, and what it couldn't
   verify. Every conclusion is marked **draft** until a human validates it; nothing in this system
   self-certifies (see `wiki/validated-conclusions.md` once the wiki exists).

## How an engagement actually runs

Every agent in the table above follows the same spine, defined once in `rules/engagement-rules.md`
and specialized by each agent's own `SKILL.md`:

```
scope → evidence ledger → panel (parallel lenses) → cross-examination
      → converged judgment + strongest counter → exhibits → fact-check gate → deliverable
      → documentation report → human validation gate
```

Three rules apply to every single run, no exceptions:

1. **The panel only runs the lenses that actually conflict.** A simple question gets one or two
   lenses and a note explaining why, not all seven run by default for the look of rigor.
2. **Undisclosed data stays undisclosed.** Where a subject doesn't publish a figure, the output says
   "not disclosed" — never an estimate dressed up as a fact. `Run Agent PortfolioReview` is the
   engagement most likely to hit this, and is built to degrade honestly when it does.
3. **A human signs off before anything is final.** Every deliverable and documentation report is
   marked draft until reviewed — the red-team pass and the fact-check gate make the draft more
   trustworthy, they don't replace a human's judgment.

## Using it with other tools

- **Claude Code**: the YAML front matter in each `SKILL.md` is already in the format Claude Code
  expects. Point it at this folder and it will pick up every skill — the eight orchestrators, the
  seven framework lenses, and the red-team/evidence-auditor/install-visual-tooling support skills —
  automatically.
- **Antigravity**: place the `skills/` directories wherever your configuration loads skills from, and
  point the workflow at `rules/engagement-rules.md` (spine) and `rules/project-rules.md`
  (single-framework method and diagram conventions).
- **Any other agentic tool**: open the relevant `SKILL.md` — the root router, or a specific
  engagement's — and paste its text into your project or custom instructions. Every file is written
  to work as plain prompt text, no tooling required, and each engagement's `SKILL.md` is
  self-contained enough to run on its own once pasted in.

## What's in this repository

```
SKILL.md                              the engagement router — start here
rules/
  engagement-rules.md                 the shared spine every orchestrator implements
  project-rules.md                    single-framework method + diagram conventions (Step 6)
skills/
  industry-analysis/                  the seven panel lenses, each a SKILL.md
  internal-assessment/
  competitive-strategy/
  adjacencies/
  diversification-and-corporate-strategy/
  implementation-and-leadership/
  innovation-and-dynamic-capabilities/
  red-team/                           attacks a converged judgment; never its own author
  evidence-auditor/                   re-opens sources; blocks the deliverable on a mismatch
  install-visual-tooling/             checks/installs the optional diagram tools on request
  competitor-teardown/                the eight orchestrator agents — "Run Agent <name>"
  commercial-dd-screen/
  market-entry-assessment/
  competitive-monitor/
  decision-memo/
  regulatory-impact/
  portfolio-review/
  reflection-paper/                   the coursework deliverable, not client work
scripts/                              the optional installer (Windows .ps1 and macOS/Linux .sh)
wiki-template/                        the accumulating-memory structure, with empty judgment files
prompts/prompts.json                  bootstrap, lint-wiki, and a build-case prompt with a placeholder
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
real figures instead of generic labels. That is a deliberate stance, not a neutral one. The red-team
and evidence-auditor roles exist specifically to enforce that bias against the natural pull of any
single pass to round a finding up to sound more finished than the evidence supports.
