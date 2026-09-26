---
name: MarketEntry
description: Orchestrates a market entry assessment — five forces on the target market, a capability-transfer test, an adjacency risk grade, an entry-cost floor built from incumbent capex and regulatory filings, and an explicit go/no-go — with an isolated multi-lens panel, a red-team pass, and a blocking fact-check audit. Use when the user says "Run Agent MarketEntry", or asks whether a company should enter a new market or geography, what it would cost, and whether the company can actually win there.
---

# Market entry assessment

Answers the three questions a market-entry decision actually turns on — is the market attractive, can
this specific company win in it, and what does entry actually cost — as three separately evidenced
sections that are not allowed to silently borrow confidence from each other, ending in a stated
go/no-go rather than a balanced-sounding non-answer.

## What this produces

1. **Five forces on the target market**: rated with mechanism, per
   `skills/industry-analysis/SKILL.md`'s own diagram convention — not the subject's home market, the
   target market as its own structure.
2. **Capability transfer test**: whether the capability that wins at home actually survives the move,
   using the VRIO sequence from `skills/internal-assessment/SKILL.md` applied specifically to
   transferability — valuable and rare at home is not evidence it transfers.
3. **Adjacency risk grade**: is this move market penetration in a new geography (lower risk, same
   buyer/product) or genuine diversification (new buyer *and* new capability), per
   `skills/adjacencies/SKILL.md`'s growth-grid discipline — branding a move as "market development"
   when it's actually diversification is the single most common self-deception this test exists to
   catch.
4. **Entry-cost floor**: a lower-bound cost of entry built from what incumbents' own capex and
   regulatory filings actually show it costs to operate at a viable scale in that market — a floor,
   not a full business case, and stated as such.
5. **Go / no-go**: one explicit recommendation, not a hedged summary of the four sections above.

## Default panel — and the conflict it's chosen for

Run `skills/industry-analysis/SKILL.md`, `skills/internal-assessment/SKILL.md`, and
`skills/adjacencies/SKILL.md` by default. Add `skills/diversification-and-corporate-strategy/SKILL.md`
if the entry-cost floor needs to be read against the subject's own capital-allocation capacity (can
they actually fund it, not just should they want to).

This is the sharpest built-in conflict of any engagement in this kit: **industry-analysis
characteristically finds the market attractive** (that's usually why entry is being considered at
all) **while internal-assessment characteristically finds the transferable capability is parity, not
advantage** — the thing that wins at home is common enough in the target market that it buys no edge
there. A market-entry assessment that only runs industry-analysis will recommend "yes" far more often
than the capability evidence actually supports.

## Orchestration

Follow `rules/engagement-rules.md` in full. Specific to this engagement:

1. **Scope**: the target market or geography, the specific capability the subject believes transfers,
   and the entry mode under consideration (organic, acquisition, JV, franchise) — the adjacency
   grade and the entry-cost floor both depend on which mode is actually being evaluated.
2. **Evidence ledger**: tag rows by which of the three tests they support; incumbent capex/filing
   rows specifically feed the entry-cost floor and should be tagged separately so that section's
   evidence base is auditable on its own.
3. **Panel**: as above, isolated per `rules/engagement-rules.md`.
4. **Cross-examination**: explicitly test the attractive-market-vs-parity-capability tension named
   above — if industry-analysis and internal-assessment disagree this way, that disagreement *is* the
   assessment's central finding, not a footnote to reconcile away.
5. **Converged judgment + red team**: the converged judgment must directly address whether market
   attractiveness alone justifies entry given the capability finding. Red-team per
   `skills/red-team/SKILL.md` — the sharpest attack here is usually testing whether the entry-cost
   floor is actually a floor, or whether it undercounts a cost category incumbents absorb that a new
   entrant would face in full (e.g. an incumbent's already-sunk regulatory relationship).
6. **Exhibits**: the five-forces cross, the adjacency growth-grid with the subject's actual move
   plotted (not a generic quadrant description), per `rules/project-rules.md` Step 6.
7. **Fact-check gate**: `skills/evidence-auditor/SKILL.md`, with particular attention to whether the
   entry-cost floor's incumbent-capex figures are actually comparable in scale and scope to what the
   subject would need to build.
8. **Deliverable**: the five sections above, ending in the stated go/no-go with its conditions.
9. **Documentation report**: per `rules/engagement-rules.md`.

## Engagement-specific constraints

- The entry-cost floor is a floor. State explicitly what it excludes (working capital, brand-building
  spend, the cost of the capability gap found in the transfer test) rather than letting a specific
  dollar figure imply completeness it doesn't have.
- Where the target market's regulatory filings are the primary evidence base and disclosure is thin
  (common outside a handful of well-regulated jurisdictions), the entry-cost floor degrades openly
  per the private-company/limited-disclosure constraint in `rules/engagement-rules.md` — do not
  estimate around a genuine disclosure gap.

## Output contract

Work in `work/market-entry-assessment/<market-slug>-<date>/`, per `rules/engagement-rules.md`, with
`deliverable.docx` — a real, rendered Word document, built per `rules/engagement-rules.md`'s
Deliverable step, with the five-forces cross and growth-grid embedded as actual images — structured as
the five sections above, in order, ending with the go/no-go.
