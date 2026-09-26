---
name: CommercialDD
description: Orchestrates a commercial due-diligence screen — market attractiveness, target position, peer benchmark, and a severity-graded red-flag register, plus an explicit "what the evidence cannot show" section, built entirely from public evidence with an isolated multi-lens panel, a red-team pass, and a blocking fact-check audit. Use when the user says "Run Agent CommercialDD", or asks for a commercial due-diligence screen, a first-pass DD read, or a quick market/target/peer/risk assessment ahead of a deal.
---

# Commercial DD screen

Compresses what a commercial due-diligence team spends roughly two weeks on into a four-part screen,
with one deliberate addition most DD reports bury or omit: an explicit, prominent statement of what
the public evidence base cannot show. That section is not a disclaimer appended at the end — it is as
load-bearing as the findings themselves, because the recipient is about to make a capital decision
partly on the strength of this screen.

## What this produces

1. **Market attractiveness**: structure, growth, and the forces actually moving it.
2. **Target position**: where the target sits in that structure, and whether its position is
   genuinely defensible or merely current.
3. **Peer benchmark**: the target set against comparable peers on the same basis.
4. **Red-flag register**: every material concern found, each with a stated severity (critical / high
   / medium / low) and the specific evidence behind it — not a generic risk list.
5. **What the evidence cannot show**: named gaps — e.g. no visibility into customer concentration,
   contract terms, churn, or unit economics for a private target — stated as plainly as the findings.

## Default panel — and the conflict it's chosen for

Run `skills/industry-analysis/SKILL.md` (market attractiveness), `skills/internal-assessment/SKILL.md`
(target position — is the target's apparent strength actually rare and inimitable, or parity dressed
up as an advantage in the data room), and `skills/competitive-strategy/SKILL.md` (peer benchmark,
via the generic-position and value-chain reads). Add `skills/implementation-and-leadership/SKILL.md`
if the deal's real risk is organizational (a founder-dependent business, a key-person clause, a
system that can't show whether the target's stated strategy is working) rather than purely
competitive.

The characteristic conflict: industry-analysis says the market is attractive; internal-assessment
finds the target's specific edge inside it doesn't clear the rarity or inimitability gate. That gap —
attractive market, unproven target-specific advantage — is usually the single most useful sentence in
a DD screen, and a screen that only reports market attractiveness will miss it entirely.

## Orchestration

Follow `rules/engagement-rules.md` in full. Specific to this engagement:

1. **Scope**: the target, the deal thesis being tested (what would have to be true for this to be a
   good deal), the peer set, and — critically — whether the target is listed (full ledger discipline
   applies) or private (see constraints below).
2. **Evidence ledger**: tag every row by which of the four screen sections it supports, so a gap in
   one section (e.g. peer benchmark) doesn't silently borrow confidence from a well-evidenced section
   (e.g. market attractiveness).
3. **Panel**: as above, isolated per `rules/engagement-rules.md`.
4. **Cross-examination**: explicitly test the deal thesis from scope against each lens's independent
   read — does industry-analysis's attractiveness finding actually depend on assumptions
   internal-assessment's target-position finding contradicts?
5. **Converged judgment + red team**: the converged judgment is a view on the deal thesis, not just a
   restatement of the four sections. Red-team it per `skills/red-team/SKILL.md` — the red team's job
   here is specifically to construct the strongest case the deal thesis is wrong using only the
   evidence already gathered.
6. **Exhibits**: an industry force-diagram, a target value-chain exhibit, and the peer benchmark as a
   weighted competitive profile matrix (per `skills/diversification-and-corporate-strategy/SKILL.md`),
   per `rules/project-rules.md` Step 6.
7. **Fact-check gate**: `skills/evidence-auditor/SKILL.md`, with particular attention to the
   private-subject check — DD targets are disproportionately likely to be private or newly listed.
8. **Deliverable**: the four sections plus the red-flag register, each red flag traced to a ledger ID.
9. **Documentation report**: per `rules/engagement-rules.md`. The limitations section here is not
   optional boilerplate — it is one of the five required deliverable sections in its own right.

## Engagement-specific constraints

- **If the target is private or thinly disclosed**, say so at the top of the scope and expect most of
  the target-position and peer-benchmark sections to read "not disclosed" rather than estimated —
  this is the private-company constraint from `rules/engagement-rules.md` in its sharpest form for
  this engagement. A DD screen that quietly estimates target-specific financials to fill the table is
  worse than useless: it will be relied on by someone about to commit capital.
- Severity grades in the red-flag register must be justified by the mechanism, not the emotional
  weight of the word used to describe it — "critical" means the deal thesis fails if the flag is
  real, not merely that the flag sounds alarming.

## Output contract

Work in `work/commercial-dd-screen/<target-slug>-<date>/`, per `rules/engagement-rules.md`, with
`deliverable.md` structured as the four screen sections plus the red-flag register as a fifth,
explicitly-labeled section.
