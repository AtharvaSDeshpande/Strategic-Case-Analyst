---
name: SMAIPlaybook-public-export-claude
description: End-to-end workflow for producing the individual strategic-management reflection paper — a Word document, strictly 5-6 pages, that applies six approved frameworks across three real companies (one retail, one IT, one FMCG) through concept-silent first-person narrative, backed by an isolated multi-agent research panel, a fact-checked evidence ledger, nine concept-silent diagrams, and a wiki update. Use when asked to build, rebuild, or extend this specific reflection-paper deliverable in this repository, or when asked to fix its formatting, figures, or page budget.
---

# Individual reflection paper: end-to-end workflow

## Objective

Produce an individual reflection paper (Word document, strictly 5-6 pages maximum, simple
formatting) that applies strategic concepts to real companies through anecdote and comparison,
without ever naming or defining the concepts in the prose. One retail, one IT, and one FMCG company
are selected. For every organization chosen:

1. Map out its various capabilities via a capability pie chart and identify its single core
   capability.
2. Examine the organization through two unique strategic frameworks chosen from the approved list of
   eight, driven by that core capability.

Apply 6 unique frameworks across the 3 companies (2 distinct frameworks per company, no duplicates
across the entire paper), with their sharpest insights woven into a single, cohesive first-person
reflective essay — not a report, and not a framework-by-framework survey. The reflections must lean
heavily toward the concrete real-world application of these frameworks.

## Company & framework selection

### 1. Company selection

- Choose one company each from retail, IT, and FMCG.
- Pick companies that are genuinely well-known and whose strategic story is well-documented and easy
  to verify. Obscure or thinly-covered companies defeat the purpose even if a framework fits them
  technically.
- State briefly in your preparatory notes why each was picked over an obvious alternative.

### 2. Approved framework roster (select exactly 6 unique frameworks total)

Each company must have 2 frameworks assigned from this list, with no framework reused across
companies (6 unique frameworks total):

a. Porter's 5 Forces
b. Ansoff Matrix
c. 9-Box GE Matrix
d. BCG Matrix
e. Porter's Value Chain
f. Aghion-Howitt (Schumpeterian Creative Destruction / Growth)
g. Corporate Scope
h. S.E. Model (Strategy & Environment)

### 3. Natural fit (no force-fitting)

- Do not force-fit a model. Choose the frameworks that smoothly and naturally fit into the
  organization's actual strategic context, unit economics, market environment, or operational
  trade-offs.
- Base the analysis on how the organization leverages or defends its identified core capability.

## No hallucination & fact-checking rigor

- **Depth over breadth**: gather a small number of specific, well-documented anecdotes per company,
  not an exhaustive company study.
- **Evidence ledger**: every specific claim (a figure, a named initiative, a dated event, a product
  decision) is logged first in `evidence-ledger.md`:
  `ID | company | claim | source URL | exact wording (<=25 words) | checked (Y/N)`
  Only log a URL you actually opened this run — never build one from memory.
- **Public facts vs. specifics**: common, well-known public facts ("X is one of the largest FMCG
  companies in India") don't need a citation. A specific claim invented to sound like inside
  knowledge does, and must be verified live or cut.
- **Fact-check audit**: before generating any diagram or final draft, re-open every cited source,
  confirm exact match, fix discrepancies, re-run the whole check until clean, and log the result.

## Style rules — no explicit concept naming

- Never name a framework or academic term, and never define one in the essay. Not "this demonstrates
  VRIO," not "applying Porter's Five Forces," not "according to the BCG matrix." Show the underlying
  operational logic through specific, concrete detail instead: what the company actually did, what a
  rival couldn't copy and why, what trade-offs changed, and what it revealed.
  - Wrong: "This is a good example of the resource-based view: the resource was valuable, rare, and
    hard to imitate."
  - Right: "A rival could copy the designs within a week. What it couldn't copy was the factory two
    hours from the design desk."
- **First-person student voice**: write in a natural, first-person reflective voice, not a clinical
  AI-report tone. Weave the logic in naturally, the way a practitioner or thoughtful observer thinks
  about it.
- **Focus on application**: the reflections must center on how these frameworks actually manifest in
  practice — capital allocation, supplier leverage, substitution threats, product cannibalization,
  capability reuse, and competitive dynamics.
- **Honest, qualified comparisons**: state plainly what insight or relevance you found in a
  comparison. Don't force a tidy conclusion where the fit between two companies is only partial.
- **Plain English**: short sentences, one idea each, no stacked qualifiers.
- **Inline figure cross-references**: every figure still gets a pointer in the body text, at the
  sentence where its content is actually being discussed (e.g., "...cut the price by a fifth
  overnight (Figure 1)."). A bare figure reference is a pointer, not a framework name, and does not
  violate the no-naming rule — the caption or a footnote may name the underlying method, but the
  prose sentence around the cross-reference must not. Do not let this become a loophole for writing
  "(see the value chain, Figure 2)" — the parenthetical is a figure number only.

## Delivering a strategic punch — scored, not asserted

Not every true, well-sourced anecdote earns a place in a 5-6 page paper. Before an anecdote or
comparison makes the final draft, it must pass:

- **Non-obvious**: does it reveal something a casual observer of the company wouldn't already see?
- **Concrete**: is it grounded in one specific fact or event, not a generalization about the company?
- **Legible without the label**: does the strategic logic still land if a reader who's never heard of
  the framework reads it, with nothing named?

Log this scoring in `punch-test.md` (private, not part of the submission) for every anecdote
considered, including the ones cut, and why. Don't just assert the final selection is the sharpest
one — show the comparison.

## The panel — multi-agent execution (isolation is mandatory)

Read `skills/*/SKILL.md` (all seven) and `wiki-template/index.md`. For each of the 3 companies,
assign the skills/frameworks that genuinely fit the company's story without force-fitting.

Every assigned skill MUST form its view on its company in isolation from every other skill's view on
that same company, before anything is compared or woven together:

- **If your environment can spawn subagents**: spawn one per assigned `(company, skill)` pair in
  parallel. Give each ONLY its own `SKILL.md`, its matching `wiki-template/frameworks/` page, the
  `evidence-ledger.md` rows for its company, and nothing else — no access to another agent's notes or
  output.
- **If your environment cannot spawn subagents**: work through the `(company, skill)` pairs one at a
  time, writing down and setting aside each independent view in `panel-notes.md` before starting the
  next. Do not let one agent's framing leak into another's read of the same or a different company.
- **Return requirements**: each pass returns which framework, why it genuinely fits this company, the
  specific anecdote it surfaces, and the ledger IDs behind it — in plain language, not framework
  jargon, since this is what later gets rewritten into the essay's voice.

Skills supply method and judgment only; every fact still comes from a verified live source, never
from the skill files.

## Diagram specifications & visual standards

Every company must have:

1. **Capability pie chart** (1 per company): displays the distribution of various organizational
   capabilities, clearly highlighting and isolating the chosen core capability that anchors the
   company's strategic analysis.
2. **Framework diagrams** (2 per company): clear, structured visual models of the two selected
   frameworks for that company (6 framework diagrams total).

Technical & aesthetic requirements:

- **Total visual assets**: exactly 3 capability pie charts + 6 framework diagrams (9 figures total).
- **Light theme exclusively**: clean white or soft neutral background, high contrast, professional
  color palette (e.g., slate, navy, muted teal, subtle warm accents). No dark backgrounds, harsh
  neon colors, or illegible gradients.
- **Crisp & highly professional**: vector-quality rendering (SVG or 300+ DPI PNG), cleanly formatted
  typography, precise alignment, and publication-ready polish. Open every rendered figure and
  visually check it for overlapping text, labels running outside their shape, or collided axis text
  before it goes into the document — a diagram that renders without error but can't be read is not
  done.
- **Rules / project-rules Step 6 compliance**: apply `rules/project-rules.md` Step 6 in full —
  convention research and industry-standard shape/layout; case-specific data encoding (real company
  segments, business units, or metrics); a tool-matching table (`scripts/` vs `diagrams/`);
  output-path verification, fail-loud on render failure, and an open-and-look check.
- **Concept-silent captions**: diagram titles and captions must follow the no-naming rule. Caption
  what the diagram reveals about the business reality, not the textbook framework name (e.g.,
  "Figure 2: Upstream supplier lock-in and margin defense against private labels" instead of
  "Porter's Five Forces Diagram").

## Phases (work in `work/individual-reflection-paper/`)

1. **Phase 1 — Company selection & capability breakdown.** Select 1 Retail, 1 IT, and 1 FMCG
   company. Identify capabilities, isolate the core capability for each, and build
   `evidence-ledger.md` as research proceeds.
2. **Phase 2 — Independent lenses (`panel-notes.md`).** Run per THE PANEL above, one isolated pass
   per assigned `(company, skill)` pair. Assign 2 frameworks per company from the approved
   8-framework list (6 unique frameworks total).
3. **Phase 3 — Score and select (`punch-test.md`) & draft essay (`reflection-paper.md`).** Score
   candidate anecdotes in `punch-test.md`. Draft the essay in first person, focusing on the deep
   application of the models without naming them. At the point in the prose where each figure's
   content is being discussed, add an inline cross-reference to it (e.g., "(Figure 3)"), so every one
   of the 9 figures is pointed to from the body text and not left to the caption alone. Maintain a
   private `concept-map.md` mapping each paragraph to the underlying framework(s) for your own
   reference (never submitted).
4. **Phase 4 — Fact check.** Re-open and audit all cited sources before rendering diagrams or
   finalizing text.
5. **Phase 5 — Diagrams.** Generate 3 capability pie charts and 6 framework diagrams matching all
   visual rules (light theme, crisp, professional, concept-silent captions). Verify output paths and
   visual legibility.
6. **Phase 6 — Update the wiki.** Copy `wiki-template/` to `wiki/` if it doesn't exist yet. For every
   framework applied in Phases 2-3, add a dated entry to its `wiki/frameworks/<slug>.md` detailing
   real-world application learnings. Add one `capability-log.md` entry. Add a
   `reusable-heuristics.md` line only if earned. Leave `validated-conclusions.md` for the human.
7. **Phase 7 — Assemble `Reflection_Paper.docx`.** Real typed text, clean typography, diagrams
   embedded with concept-silent captions. Scan text to ensure zero framework names or academic
   jargon appear in the prose, outside of the inline figure cross-references.
   - **Paragraph flow and line breaks**: build each paragraph as one continuous block of text and let
     Word's own layout engine wrap it to the margin. Do not carry over the source markdown file's own
     line wrapping as if each wrapped line were a separate paragraph — that produces artificial
     mid-sentence breaks and paragraph-spacing gaps in the wrong places. Justify body paragraphs so
     both the left and right edges align cleanly to the margins.
   - **Figure sizing**: render each figure as large as the page and page budget can cleanly
     accommodate. If the person reviewing the draft has already resized any image in the working
     document, treat that size as a floor: never regenerate the document with that figure smaller
     than the size they set, even if the script's own default would otherwise produce a smaller one.
   - **Figure placement**: each figure must sit immediately after the paragraph that discusses it,
     directly under the inline cross-reference added in Phase 3, with its concept-silent caption
     directly beneath the image.
   - **Strict page budget**: the document must be strictly between 5 and 6 pages maximum (cannot
     exceed 6 pages). Render to PDF to verify page count, trimming prose or adjusting figure spacing
     if necessary. If honoring an already-set, larger figure size would itself push the document past
     6 pages, say so explicitly rather than silently shrinking the figure back down — report the
     resulting page count and flag the conflict for a decision, rather than resolving it
     unilaterally in either direction.
8. **Phase 8 — Final report.** Report: companies chosen and why; core capability identified for each;
   the 6 unique frameworks selected and why each smoothly fits; which `(company, skill)` pairs
   contributed and which sat out; `punch-test.md` results including cuts; fact-check audit summary;
   diagrams built; exact page count; and file paths.
