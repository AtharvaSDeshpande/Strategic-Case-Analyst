---
name: CompetitiveMonitor
description: Orchestrates a quarterly competitive monitor — re-reads a named set of rivals' latest disclosures, diffs them against last quarter's evidence ledger, and reports only material moves plus which prior judgments are now stale. Deliberately the lightest-panel engagement in this kit, built to compound with the wiki across repeated runs rather than re-analyze from scratch each quarter. Use when the user says "Run Agent CompetitiveMonitor", or asks what changed with a company or its rivals since the last check, or asks for a quarterly/periodic competitive update.
---

# Quarterly competitive monitor

Replaces someone re-reading every rival's filings each quarter from a blank page and writing "what
changed" from memory of last quarter. This is the one engagement in the kit built specifically to get
cheaper and sharper every time it runs, because it depends on a prior run's ledger existing — the
tenth quarter should take a fraction of the effort the first one did.

## What this produces

- A **diff against last quarter's evidence ledger**: new rows only, each tagged as a genuinely
  material move (a filing, a launch, a pricing change, a leadership change with strategic
  consequence) or explicitly excluded as noise.
- A **staleness list**: which rows in `wiki/validated-conclusions.md`, `wiki/reusable-heuristics.md`,
  or a prior engagement's `converged-judgment.md` for this subject are now questionable given what
  changed this quarter — flagged for human re-review, never silently updated.

## Default panel — deliberately minimal

This engagement is the clearest test of the honest constraint that **the panel is only worth its cost
when the lenses actually conflict.** A quarter-over-quarter diff is, by construction, usually a small
set of facts, not a question with multiple genuinely competing strategic readings. Default to **zero
or one lens**:

- **Zero lenses**: if the new disclosures are simple factual updates (a results announcement in line
  with trend, a routine filing), just log them, diff them, and flag staleness. Do not manufacture a
  panel to analyze a quarter that didn't actually change anything.
- **One lens**: if a single new disclosure looks like it could change a specific prior judgment (e.g.
  a rival's new segment disclosure bears directly on a conclusion from a prior
  `skills/competitor-teardown/SKILL.md` run), run only the one lens that judgment depended on, to
  test whether it still holds — not the full panel.

Only escalate to two or more lenses if a single quarter's disclosures are themselves large enough to
constitute a new question (a major acquisition, a strategy reversal, a regulatory action) — at which
point, say explicitly that this quarter has outgrown the monitor and consider running the fuller
engagement it now resembles (competitor teardown, market entry, etc.) instead.

## Orchestration

Follow `rules/engagement-rules.md`, adapted for this engagement's lighter weight:

1. **Scope**: which subject and rival set to monitor, and — required — the prior run's
   `evidence-ledger.md` and `converged-judgment.md` (or the relevant prior engagement's equivalents)
   to diff against. If no prior run exists, say so: this is a first run, not a monitor, and should
   probably start from a fuller engagement instead.
2. **Evidence ledger**: append new rows only; never edit or delete a prior row. A correction to a
   prior row is itself a new, dated row noting the correction.
3. **Panel**: zero, one, or (rarely) more lenses, per the rule above — always state which and why in
   the documentation report, since "why we ran fewer lenses" is this engagement's most important
   honesty check.
4. **Cross-examination**: only applies if more than one lens ran this quarter; otherwise state
   plainly that this step was not needed.
5. **Converged judgment + red team**: the "judgment" here is simply the answer to "does anything from
   this quarter change a standing conclusion?" Red-team per `skills/red-team/SKILL.md` only if the
   answer is yes for at least one prior judgment — there is nothing to attack in "nothing material
   changed."
6. **Exhibits**: usually none. If a tracked metric (e.g. a disclosed segment figure from
   `skills/competitor-teardown/SKILL.md`'s weighted matrix) has a new data point, update that one
   exhibit's underlying data and re-render it rather than building a new one.
7. **Fact-check gate**: `skills/evidence-auditor/SKILL.md` still runs on every new row — this
   engagement's speed comes from running fewer lenses, never from skipping the audit.
8. **Deliverable**: the diff and the staleness list, both short by design. A monitor deliverable that
   reads like a full new engagement has drifted from its purpose.
9. **Documentation report**: per `rules/engagement-rules.md`, with the panel-composition section
   explicitly justifying the zero/one/more lens count for this quarter.

## Engagement-specific constraints

- Never silently mark a `wiki/validated-conclusions.md` row as updated — flag it as stale and require
  a human to re-validate, per the standing human-validation gate. This engagement finds staleness; it
  does not resolve it.
- If a rival has gone quiet (no new disclosure this quarter), say that plainly rather than treating
  silence as "no change confirmed" — a lapse in disclosure is different from a confirmed lack of
  movement, and the difference matters for a private or newly-private rival in particular.

## Output contract

Work in `work/competitive-monitor/<subject-slug>-<quarter>/`, per `rules/engagement-rules.md`
(omitting `panel/` and `cross-examination.md` entirely on quarters where zero or one lens ran, rather
than leaving empty placeholder files), with `deliverable.docx` — still a real rendered Word document
per `rules/engagement-rules.md`'s Deliverable step even though it's usually short — containing the
diff and the staleness list as its two sections. If a tracked exhibit's data changed this quarter,
its updated image is embedded here too, not just described.
