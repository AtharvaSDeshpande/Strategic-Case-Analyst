---
name: PortfolioReview
description: Orchestrates a portfolio / capital allocation review — a portfolio matrix on disclosed business-unit positions, a funding-capacity test, and a pipeline check on whether today's question marks can plausibly become tomorrow's cash cows — built from disclosed segment data with an isolated panel, a red-team pass, and a blocking fact-check audit. Explicitly the weakest-fit engagement in this kit, because it needs internal data that is rarely public — the honest constraint is central here, not incidental. Use when the user says "Run Agent PortfolioReview", or asks which business units or segments a company should keep funding, harvest, or exit.
---

# Portfolio / capital allocation review

Answers which of a company's disclosed businesses should be funded, harvested, or exited — but this
is the one engagement in the kit that should be run with the clearest expectations set up front: it
needs internal, unit-level data (segment margins, capital employed by unit, cross-subsidy flows) that
most companies do not disclose at the resolution this question really wants. Where other engagements
in this kit degrade gracefully to "not disclosed" on a few cells, this one frequently degrades on
most of the table — and that is the honest, correct outcome, not a failure of the engagement.

## What this produces

- **Portfolio matrix**: each disclosed unit plotted on growth and relative position (or, where a
  relative-share figure isn't disclosed, on growth against a stated, disclosed proxy — never an
  estimated share), per `skills/diversification-and-corporate-strategy/SKILL.md`'s growth-share
  convention or, where the units sit in genuinely different industries requiring a third axis, its
  nine-box variant.
- **Funding-capacity test**: whether the company's disclosed capacity to invest (cash generation,
  leverage headroom) is actually being *used* — falling leverage alongside falling return on capital
  is a specific, disclosed pattern worth surfacing on its own.
- **Pipeline check**: whether the units in the "question mark" quadrant have any disclosed evidence
  of the specific capital or capability being deployed toward them that would let them mature into
  cash cows — not just that management says they're a priority.

## Default panel

Run `skills/diversification-and-corporate-strategy/SKILL.md` as the primary lens — this is the
skill whose entire method this engagement is built on. Add
`skills/implementation-and-leadership/SKILL.md` only if the funding-capacity test surfaces a mismatch
between stated strategy and disclosed capital allocation, since that lens is the one built to
diagnose *why* a strategy and the system funding it might be misaligned. This engagement rarely
justifies a third lens — the questions it asks are inherently about capital allocation, not
competitive position or capability transfer, so pulling in unrelated lenses tends to manufacture
disagreement rather than surface real tension. Per `rules/engagement-rules.md`, state explicitly if
one lens alone is sufficient for a given company's disclosure level.

## Orchestration

Follow `rules/engagement-rules.md`, with this engagement's specific structure:

1. **Scope**: the company, the specific units or segments in question, and — before doing anything
   else — an honest check of what that company's actual segment reporting discloses. If it reports
   only 2-3 broad segments with no sub-unit detail, say so in scope before promising a fine-grained
   matrix the disclosure can't support.
2. **Evidence ledger**: every plotted position and every bubble size must trace to a disclosed
   figure, per `skills/diversification-and-corporate-strategy/SKILL.md`'s own rule — an estimated
   bubble is indistinguishable from a measured one once drawn, which makes this the exhibit where an
   unverified number does the most damage.
3. **Panel**: as above, isolated per `rules/engagement-rules.md` if both lenses run.
4. **Cross-examination**: only applies if both lenses ran; otherwise skip explicitly.
5. **Converged judgment + red team**: the converged judgment is the fund/harvest/exit call per unit.
   Red-team it per `skills/red-team/SKILL.md` — the sharpest attack here is usually whether a
   "harvest" call is actually correct or whether it's an artifact of thin disclosure making a unit
   look like a cash cow when its real trajectory isn't visible from outside.
6. **Exhibits**: the portfolio matrix (growth-share or nine-box, per which convention actually fits
   the disclosed industries involved), per `rules/project-rules.md` Step 6.
7. **Fact-check gate**: `skills/evidence-auditor/SKILL.md`, with the private-subject / limited-
   disclosure check doing most of the work in this engagement specifically.
8. **Deliverable**: the matrix, the funding-capacity finding, and the pipeline check, each stating
   plainly which cells are evidenced and which are marked not disclosed.
9. **Documentation report**: per `rules/engagement-rules.md` — the limitations section here should be
   expected to be the longest of any engagement in this kit, and that length is itself a correct
   signal to the reader, not a sign the engagement underperformed.

## Engagement-specific constraints (this is the central discipline of this engagement)

- **This is explicitly the weakest-fit engagement in the kit.** Say that to the requester up front if
  the target company's disclosure is thin — a portfolio review promised at unit-level resolution and
  delivered at segment-level resolution because that's all that's disclosed is not a failed
  engagement; a portfolio review that quietly estimates unit-level figures to look complete is.
- Never infer a cross-subsidy between units from group-level capital expenditure alone — per
  `skills/diversification-and-corporate-strategy/SKILL.md`'s own guidance, that requires a traceable,
  disclosed transfer, not just co-occurring numbers.
- If the company being reviewed is private, expect this engagement to degrade further than any other
  in the kit — most of the matrix may read "not disclosed," and the honest deliverable is a short,
  clearly-limited read rather than a padded one.

## Output contract

Work in `work/portfolio-review/<company-slug>-<date>/`, per `rules/engagement-rules.md`, with
`deliverable.docx` — a real, rendered Word document, built per `rules/engagement-rules.md`'s
Deliverable step, with the portfolio matrix embedded as an actual image — structured as the matrix,
the funding-capacity finding, and the pipeline check, with a disclosure-coverage note at the top
stating plainly how much of the intended matrix the company's actual reporting could support.
