---
name: CompetitorTeardown
description: Orchestrates a full competitor teardown — a weighted competitive profile matrix, one battlecard per named rival, and an explicit "where we actually lose" note, built from public filings and verified live sources, with an isolated multi-lens panel, a red-team pass, and a blocking fact-check audit. Use when the user says "Run Agent CompetitorTeardown", or asks to compare a company against 3-5 named rivals, build battlecards, or find where a company is structurally losing rather than just behind on scale.
---

# Competitor teardown

Replaces days of manually pulling rivals' filings into a mismatched-period comparison sheet. The
value isn't the table — it's finding the specific point where the lenses disagree about *why* the
subject is losing, because that's usually not the point a scale-only comparison would surface.

## What this produces

- A **weighted competitive profile matrix**: criteria as rows, weights summing to one, a score per
  firm, a weighted total, printed on the exhibit so the weighting is checkable, not asserted (this is
  the exact tool `skills/diversification-and-corporate-strategy/SKILL.md` specifies for comparing
  several rivals inside one industry — reuse it, don't invent a different shape).
- **One battlecard per named rival**: their position, what they can do that the subject can't (and
  why), what the subject can do that they can't, and the single most current, checkable fact a
  salesperson or strategist would actually need in the room.
- A **"where we actually lose" note**: not a summary of weaknesses, but the specific mechanism —
  named, evidenced — behind the sharpest loss, distinguished explicitly from mere scale disadvantage.

## Default panel — and the conflict it's chosen for

Run `skills/internal-assessment/SKILL.md`, `skills/competitive-strategy/SKILL.md`, and
`skills/adjacencies/SKILL.md` by default. These three are chosen because they characteristically
disagree about the same facts in a genuinely useful way:

- **Internal assessment** tends to find that a lot of apparent scale advantage is actually **parity**
  (VRIO's most under-used verdict) — everyone in the set can buy the same inputs.
- **Competitive strategy** tends to find the real gap sits in **margin**, via one activity in the
  value chain done structurally differently, not in scale at all.
- **Adjacencies** tends to find a rival holds an entire **quadrant** (a market or product move) the
  subject has never entered, which neither of the other two lenses would surface.

Add `skills/industry-analysis/SKILL.md` only if the rivalry itself (not any one rival) is the live
question — e.g. the subject is asking whether to compete on price at all. Per the honest constraint
in `rules/engagement-rules.md`: if, after scoping, these three lenses would obviously agree (e.g. the
rivals are trivially similar and undifferentiated), say so and run fewer.

## Orchestration

Follow `rules/engagement-rules.md` in full. Specific to this engagement:

1. **Scope**: the subject, the named rival set (3-5; more dilutes the matrix), and the weighting
   criteria for the profile matrix — agree these with the user before scoring, since the weights
   drive the whole exhibit and must not be chosen after seeing how they'd make the subject look.
2. **Evidence ledger**: one row set per rival, tagged by rival, so a stale or wrong rival's data
   doesn't block the whole matrix — see the competitive-monitor engagement for re-running this later.
3. **Panel**: as above, isolated per `rules/engagement-rules.md`.
4. **Cross-examination**: this is the step that actually produces the teardown's value. Explicitly
   check whether the three lenses' rival-by-rival reads agree on *who the subject's most dangerous
   rival actually is* — it is common for the lens focused on scale to name a different rival than the
   lens focused on activity-level margin or the lens focused on category-quadrant coverage.
5. **Converged judgment + red team**: the converged judgment must name the single sharpest loss
   mechanism, not list all findings. Red-team it per `skills/red-team/SKILL.md` — the most useful
   attack here is usually "is this loss actually about scale, and the activity-level story a
   post-hoc rationalization?"
6. **Exhibits**: the weighted competitive profile matrix (table), one value-chain exhibit for the
   subject and its sharpest rival if internal-assessment/competitive-strategy disagree materially,
   per `rules/project-rules.md` Step 6 conventions.
7. **Fact-check gate**: `skills/evidence-auditor/SKILL.md`. Rival financials are frequently
   mismatched-period or non-comparable-currency — the auditor must confirm every cross-rival
   comparison uses the same period and, where currencies differ, states the conversion basis rather
   than silently normalizing it.
8. **Deliverable**: the matrix, the battlecards, the "where we actually lose" note, each clearly
   labeled with the weighting basis and evidence dates.
9. **Documentation report**: per `rules/engagement-rules.md`, plus explicitly state which rival(s), if
   any, had materially weaker public disclosure than the rest, since that alone can distort a
   weighted matrix without the reader noticing.

## Engagement-specific constraints

- A rival with materially less disclosure than the others degrades that rival's row to "not
  disclosed" cells rather than an estimated score — do not let one well-disclosed rival's complete
  row make a thinly-disclosed rival's incomplete row look like a real, comparable score.
- Do not let scale (revenue, headcount, store count) stand in for competitive strength on its own —
  `skills/internal-assessment/SKILL.md`'s own guidance is explicit that being large is not rare, and
  a large rival is often parity, not advantage.

## Output contract

Work in `work/competitor-teardown/<subject-slug>-<date>/`, per the structure in
`rules/engagement-rules.md`, with `deliverable.md` (or `.docx` if the user wants a client-ready
document) containing the matrix, battlecards, and loss note as its three sections.
