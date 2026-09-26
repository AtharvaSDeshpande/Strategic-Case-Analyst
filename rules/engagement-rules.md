# Engagement rules: the shared spine

This file is authoritative for **every** orchestrator skill under `skills/` whose job is to run a
full engagement (competitor teardown, commercial DD screen, market entry assessment, competitive
monitor, decision memo, regulatory impact read, portfolio review, and the academic reflection
paper). Each of those skills specializes this spine for its own deliverable; none of them may skip a
step or invent a different one. `rules/project-rules.md` remains authoritative for the mechanics of
applying a single framework well and for diagram conventions (its Step 6); this file is authoritative
for how an orchestrator assembles several framework passes, a red-team pass, and an audit pass into
one engagement.

## The spine

```
scope → evidence ledger → panel (parallel lenses) → cross-examination
      → converged judgment + strongest counter → exhibits → fact-check gate → deliverable
      → documentation report → human validation gate
```

Every orchestrator skill implements all nine stages. What differs per engagement is which lenses run,
what the exhibits look like, and what the deliverable's sections are — not whether a stage happens.

### 1. Scope

Before anything else, write `scope.md`: the subject (company, market, target, decision), the
question actually being asked, the deliverable recipient, the time horizon, and — critically — what
is explicitly out of scope. An engagement that cannot state its own boundary will drift into research
for its own sake. If the user's request is ambiguous on subject, rivals, market, or decision, ask
before scoping rather than guessing.

### 2. Evidence ledger

Every specific claim (a figure, a named initiative, a dated event, a regulatory provision, a filing
line item) is logged in `evidence-ledger.md` before it is used anywhere else:

`ID | subject | claim | source URL | exact wording (<=25 words) | checked (Y/N)`

Only log a URL actually opened this run. Well-known public facts ("X is a listed FMCG company")
don't need a citation; anything that sounds like inside knowledge does, and must be verified live or
cut. This is unchanged from the single-framework discipline in `rules/project-rules.md` — an
engagement just accumulates many more rows, tagged by which lens or exhibit each row supports.

### 3. Panel — run only the lenses that earn their place

Read `skills/*/SKILL.md` for the seven framework lenses (industry analysis, internal assessment,
competitive strategy, adjacencies, diversification and corporate strategy, implementation and
leadership, innovation and dynamic capabilities). An orchestrator assigns lenses to the engagement;
it does not run all seven by default.

**The panel is only worth its cost when the lenses actually conflict.** Before assigning lenses,
state in `scope.md` which lenses you expect to disagree and why — a prediction you then check against
what the panel actually returns. If a question is simple enough that every assigned lens would agree,
run one or two lenses and say so explicitly in the documentation report, rather than running all
seven to produce seven agreeing memos and a padded bill. Each orchestrator skill states its own
engagement's typical lens set and the specific tension it expects between them; treat that as a
starting point to justify, not a quota to hit.

**Isolation is mandatory whenever more than one lens runs.** Each lens forms its view before anything
is compared or synthesized:

- **If your environment can spawn subagents**: spawn one per assigned lens, in parallel. Give each
  ONLY its own `SKILL.md`, the matching `wiki/frameworks/<slug>.md` page, and the relevant
  `evidence-ledger.md` rows for its subject. No agent sees another lens's notes or conclusions.
- **If your environment cannot spawn subagents**: work through the lenses one at a time, writing
  each independent view into `panel/<lens-slug>.md` and setting it aside before starting the next.
  Do not let one lens's framing leak into the next.
- **Return requirements**: each pass returns which lens, why it genuinely fits this engagement, its
  specific conclusion, the anecdotes or figures behind it, and the ledger IDs — in plain language.

### 4. Cross-examination

This step is new relative to the single-framework workflow and is not optional. After the panel
returns, an orchestrating pass (not any individual lens) compares the independent conclusions and
answers, explicitly, in `cross-examination.md`:

- Where do the lenses actually disagree — not just phrase things differently, but reach a different
  practical conclusion?
- Where does one lens's evidence contradict another lens's conclusion?
- Which disagreement is load-bearing for the final deliverable, and which is cosmetic?

If every lens agrees on every material point, say so plainly; a forced disagreement is worse than an
honest convergence. But check for real tension before declaring convergence — the whole reason to run
more than one lens is to surface exactly this.

### 5. Converged judgment + strongest counter

Write `converged-judgment.md`: the single conclusion the evidence actually supports, naming which
lenses and ledger IDs carry it, and how any cross-examination disagreement was resolved (or why it
couldn't be).

**Red team the converged judgment before it goes anywhere near a deliverable.** Invoke
`skills/red-team/SKILL.md` as a separate pass. The agent or lens that wrote the converged judgment
must not write its own counter-argument — the author of a conclusion is structurally the worst person
to attack it. The red-team pass returns `red-team.md`: the single load-bearing assumption, the
strongest disconfirming evidence available, a falsification condition (what would have to be true to
flip the conclusion), and a robustness grade (robust / narrow / fragile) with reasoning.

### 6. Exhibits

This step is a **build**, not a description. "The matrix would show X" is not an exhibit; a rendered
file that a human can open and look at is. What exhibits a given engagement needs is specified by
that engagement's own skill file; how to build any of them is the same every time:

1. **Research the convention** for this exhibit type before drawing anything, per
   `rules/project-rules.md` Step 6 — a weighted competitive profile matrix, a five-forces cross, a
   growth-share bubble chart, and a value-chain chevron each have a real, checkable standard shape,
   and none of them is a generic box-and-arrow diagram.
2. **Write an actual script**, not a one-off drawing done by hand in the moment. Put plotting/table-
   generation source under `scripts/` and nothing else there; rendered output (PNG at 300+ DPI, or an
   SVG, or a real table) goes under `diagrams/` and nowhere else. Use matplotlib for fixed-layout
   exhibits (crosses, two-by-two grids, bubble matrices, chevrons) and Graphviz for genuine node-link
   structures, per the tool-matching table in `rules/project-rules.md` Step 6. If neither tool is
   installed, say so explicitly and offer `skills/install-visual-tooling/SKILL.md` — do not silently
   fall back to a described-in-prose diagram and call the exhibit done.
3. **Encode this engagement's own numbers**, not generic placeholders — every axis, weight, bubble
   size, and cell must trace to a specific `evidence-ledger.md` row. Where a cell's real number is
   undisclosed, mark it "not disclosed" on the exhibit itself, per the private-company honest
   constraint — never estimate to complete the picture.
4. **Run the script and confirm the output file actually changed on disk.** A clean exit code is not
   proof; check the file's modified time or open it.
5. **Open every rendered file and look at it.** Overlapping labels, text running outside its box, and
   collided axis text are routine failures invisible to an exit code. A diagram that renders without
   error but can't be read is not done — fix it and re-render before it goes into the deliverable.
6. **If rendering fails, stop and report the exact command and error.** Do not write a placeholder
   image or a table that looks rendered but isn't; a visibly missing exhibit is fixable, a fake one
   isn't.

### 7. Fact-check gate

Invoke `skills/evidence-auditor/SKILL.md` as a separate pass, after exhibits exist. This gate is
**blocking**, not advisory: if a cited claim does not match its source on re-check, the deliverable
does not ship until the ledger and the prose are both fixed and the audit is re-run clean. A ledger
row marked `checked: Y` by the pass that logged it is not itself proof; the auditor re-opens the
source independently.

### 8. Deliverable

**The default deliverable format is a professional Word document (`deliverable.docx`), not a markdown
file.** A markdown or plain-text version may exist as a working draft, but what actually ships — the
thing a board, a committee, or a buyer opens — is a real `.docx` with the exhibits embedded as images,
not described in prose. Only skip the docx step if the user explicitly asks for markdown/plain text
instead; do not default to the lighter format because it's less work.

Build it the same way every time, using `python-docx` (or the environment's equivalent):

1. **Merge source text into real paragraphs before writing them into the document.** Never carry over
   a source file's own line-wrapping as if each wrapped line were a separate paragraph — that produces
   artificial mid-sentence breaks and paragraph-spacing gaps in the wrong places. Build each paragraph
   as one continuous block and let Word's own layout engine wrap it to the margin.
2. **Justify body paragraphs** so both edges align cleanly to the margins, and use a plain,
   professional font and consistent, modest heading sizes — this is a working document, not a poster.
3. **Embed every rendered exhibit from `diagrams/` directly in the document**, sized to be legible at
   the page width being used, with a caption directly beneath it stating what the exhibit shows.
4. **Cross-reference every exhibit from the prose**, at the sentence where its content is actually
   being discussed (e.g., "...consistent with the margin gap in the value-chain exhibit (Exhibit 2).")
   — an exhibit with no inline pointer from the text is easy for a reader to miss entirely.
5. **Render the assembled document to PDF and check it** — page count, whether exhibits actually
   embedded (not broken image links), and whether the text visibly wraps to the margin rather than
   breaking oddly. Do this before calling the deliverable done, the same way exhibits get opened and
   looked at in Step 6.
6. **State plainly what the evidence could and could not show.** Do not let a clean-looking exhibit
   imply certainty the underlying disclosure doesn't support.

Each orchestrator's own `SKILL.md` specifies the deliverable's required sections and their order; this
step defines how those sections get assembled into the actual file, not what they say.

### 9. Documentation report

Every engagement produces a second artifact alongside the deliverable: `documentation-report.md`, an
industry-standard methodology note. This is what lets someone who receives the deliverable understand
how it was built without re-deriving it. It always includes:

- **Scope**: subject, question, recipient, time horizon, explicit out-of-scope items.
- **Panel composition**: which lenses ran, why each was assigned, which of the eight were
  deliberately not run and why (including "the question didn't create enough conflict to justify
  more than N lenses").
- **Evidence base**: row count in the ledger, source types (primary filing, press, regulator,
  analyst estimate — flagged as such), and the fact-check audit's result.
- **Cross-examination summary**: where the lenses agreed, where they didn't, and how that was
  resolved.
- **Red-team outcome**: the robustness grade and the falsification condition.
- **Limitations**: what the evidence base could not show, stated as plainly as the deliverable's own
  findings — never buried in a footnote.
- **Validation status**: draft (agent-produced, not yet human-reviewed) or validated (see below).

### Human validation gate

This gate is unchanged by any of the above and does not get lighter for real client work — if
anything it matters more. An agent-drafted conclusion, however well cross-examined and red-teamed,
is not authoritative until a human has reviewed and signed off. Mark every deliverable and every
`documentation-report.md` clearly as **draft — pending human validation** until that happens. Where an
engagement builds on a prior engagement's validated conclusion, check that the prior row is actually
validated before relying on it; a pending row is not authoritative, and drafting the validation
yourself to unblock the gate is not permitted.

## Honest constraints (apply to every engagement)

1. **The panel is only worth its cost when the lenses actually conflict.** See "Panel" above. This
   is a standing instruction, not a suggestion the orchestrator can skip under deadline pressure —
   running two lenses and saying why is a better outcome than running seven for appearances.
2. **Private companies and unlisted targets break the ledger.** The whole discipline rests on primary
   filings and other public, checkable sources. Where the subject (or a rival, or a market
   participant) doesn't disclose, the honest output is "not disclosed" across the affected rows and
   cells of any exhibit — never an estimate dressed up as a figure. Say this plainly in the
   deliverable and in the documentation report's limitations section; do not quietly degrade the
   confidence of a claim without flagging it. If the engagement's whole value depended on data that
   turns out to be undisclosed, say that too, even if it means the deliverable is thinner than what
   was asked for.
3. **The human validation gate stays.** See above.

## Output contract

```
work/<engagement-slug>/<run-slug>/
  scope.md
  evidence-ledger.md
  panel/
    <lens-slug>.md              one file per lens that actually ran
  cross-examination.md
  converged-judgment.md
  red-team.md
  scripts/                      plotting/diagram source, never mixed with output
  diagrams/                     rendered exhibits only
  audit-report.md
  deliverable.docx                the professional Word document — the default; see "Deliverable" above
  deliverable.md                  optional working draft only, never the sole shipped artifact
  documentation-report.md
```

`<engagement-slug>` matches the orchestrator skill that ran (e.g. `competitor-teardown`); `<run-slug>`
identifies this specific run (e.g. the subject and date) so repeated engagements on the same subject
don't overwrite each other.
