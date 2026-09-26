---
name: DecisionMemo
description: Orchestrates a board or investment-committee decision memo — an options table, a weighted decision with the weights and a sensitivity line both visible, and a mandatory red-team section — built to stand on its own or to summarize a prior engagement (competitor teardown, DD screen, market entry assessment) into the two pages a decision-maker actually reads. Use when the user says "Run Agent DecisionMemo", or asks for a board memo, an IC memo, a decision recommendation with options, or a two-pager to support a specific go/no-go or funding decision.
---

# Board / IC decision memo

Produces the two pages a board or investment committee actually reads, with the one discipline most
such memos skip: the weights behind the recommendation are printed, not implied, and a sensitivity
line shows how much the recommendation would change if a contestable weight or input moved.

## What this produces

- **Options table**: every option actually on the table (including "do nothing"), on the same
  criteria.
- **Weighted decision**: criteria, weights summing to one, a score per option, and the weighted total
  — the same discipline as the weighted competitive profile matrix in
  `skills/diversification-and-corporate-strategy/SKILL.md`, applied to options instead of rivals.
- **Sensitivity line**: which single weight or input, if changed within a defensible range, would
  flip the recommended option — stated as a specific, checkable condition, not a vague caveat.
- **Mandatory red-team section**: the strongest case against the recommended option, visible in the
  memo itself, not filed separately where a reader can skip it.

## Default panel — usually light, and often reused rather than run fresh

This engagement is frequently **downstream of another engagement** rather than a fresh analysis: a
competitor teardown, a commercial DD screen, or a market entry assessment often already produced the
evidence a decision memo needs. Check first whether a relevant prior engagement's
`converged-judgment.md` and `evidence-ledger.md` already exist for this decision; if so, this
orchestrator's job is largely to structure and weight that existing evidence into a decision, not to
re-run a fresh panel.

If no prior engagement exists, assign 1-2 lenses matched to the decision's actual domain — e.g.
`skills/diversification-and-corporate-strategy/SKILL.md` for a capital-allocation decision,
`skills/adjacencies/SKILL.md` for a growth-option decision, `skills/implementation-and-leadership/
SKILL.md` if the real risk is execution rather than the strategic logic itself. Per the honest
constraint in `rules/engagement-rules.md`, do not run the full seven-lens panel for a memo whose
options don't create that much genuine disagreement — a decision memo is, almost by design, the
narrowest-scope engagement in this kit.

## Orchestration

Follow `rules/engagement-rules.md`, with this engagement's specific structure:

1. **Scope**: the decision actually being made, every option genuinely on the table, the criteria and
   their proposed weights (agree these with the user or the requester *before* scoring — weights set
   after seeing scores are not weights, they're a rationalization), and whether this memo draws on a
   prior engagement or starts fresh.
2. **Evidence ledger**: reuse a prior engagement's ledger by reference where one exists; only add new
   rows for anything the memo needs that the prior engagement didn't cover.
3. **Panel**: 0-2 lenses per the rule above, isolated per `rules/engagement-rules.md` if more than
   one runs.
4. **Cross-examination**: only applies if more than one lens ran fresh for this memo; otherwise state
   that the memo is built on a single prior converged judgment and skip this step explicitly.
5. **Converged judgment + red team**: the converged judgment here *is* the weighted decision itself.
   The red-team pass (`skills/red-team/SKILL.md`) is **mandatory and visible in the deliverable** for
   this engagement specifically — unlike other engagements where red-team output feeds the
   documentation report, a decision memo's recipient needs to see the strongest counter-case in the
   memo itself, not in a separate methodology note they may not open.
6. **Exhibits**: the weighted options table as the primary exhibit; a sensitivity chart only if the
   sensitivity finding is itself visual (e.g. a threshold on a single continuous input) rather than a
   one-line statement.
7. **Fact-check gate**: `skills/evidence-auditor/SKILL.md` — even a two-page memo going to a board
   gets the full blocking audit; the stakes are, if anything, the reason this gate matters most here.
8. **Deliverable**: strictly two pages — options table, weighted decision, sensitivity line, and the
   red-team section, in that order. If the honest content doesn't fit two pages, cut supporting prose
   before cutting the red-team section or the sensitivity line.
9. **Documentation report**: per `rules/engagement-rules.md`, separate from the two-page deliverable
   — the memo is what the board reads; the documentation report is what a staffer checks later.

## Engagement-specific constraints

- Weights must be agreed before scoring, not fitted to produce a predetermined answer — if the
  requester wants to change a weight after seeing the result, that's a legitimate request, but it
  must be logged as a new, dated version of the decision, not a silent edit to the first one.
- The red-team section is not optional and not something a rushed run can skip "just this once" —
  this is this engagement's one non-negotiable structural requirement, stated explicitly because
  decision memos are exactly the deliverable most likely to be requested under time pressure.

## Output contract

Work in `work/decision-memo/<decision-slug>-<date>/`, per `rules/engagement-rules.md`, with
`deliverable.docx` — a real, rendered Word document, built per `rules/engagement-rules.md`'s
Deliverable step, with the weighted options table (and sensitivity chart if one was built) embedded as
actual images — as the strict two-page memo, and everything else (full ledger, cross-examination if
run, full audit report) in the supporting files for anyone who wants to check it.
