---
name: RegulatoryImpact
description: Orchestrates a regulatory impact read — maps each provision of a draft rule or consultation paper to the specific competitive force it moves, for the subject and for each named rival, with who gains and who is exposed — built from the regulatory text itself as primary evidence, with a focused panel, a red-team pass, and a blocking fact-check audit. Use when the user says "Run Agent RegulatoryImpact", or asks what a proposed regulation, consultation paper, or draft rule means for a company or its industry.
---

# Regulatory impact read

Turns a policy team's manual read of a draft rule into a structured mapping: not "here's a summary of
the regulation," but "here is exactly which competitive force each provision moves, for whom, and who
gains from that move" — because a regulation rarely affects every player in an industry equally, and
the differential impact is usually the actual strategic question.

## What this produces

- **A provision-by-provision map**: each material provision of the draft rule or consultation paper,
  the specific force it moves (entry barriers, supplier power, buyer power, substitute threat, or
  rivalry intensity itself), and the direction and magnitude of the move where the text supports one.
- **Per-player read**: for the subject and each named rival, whether that provision is a net
  advantage, disadvantage, or roughly neutral — with the mechanism, not just the verdict.
- **Who gains**: a single, explicit summary naming which player(s) come out ahead once every
  provision is netted out, and why that's not always the player the regulation appears to target.

## Default panel — narrow by design

Run `skills/industry-analysis/SKILL.md` alone by default — this is the one lens built specifically
for force-by-force structural mapping, and a regulatory text is exactly the kind of primary,
public, dense source its method was built to work from. Add `skills/adjacencies/SKILL.md` only if the
regulation plausibly redraws a market boundary (e.g. it defines a new licensed category, or removes
one) rather than just adjusting the terms of competition within an existing one.

Per the honest constraint in `rules/engagement-rules.md`: resist the temptation to run the full panel
just because the source material is rich. A regulatory impact read is a structural-mapping exercise,
not a capability or portfolio question — running internal-assessment or diversification lenses on it
usually produces analysis the regulatory text itself can't actually support, since a consultation
paper rarely discloses anything about any single firm's internal capabilities.

## Orchestration

Follow `rules/engagement-rules.md`, with this engagement's specific structure:

1. **Scope**: the specific regulatory text (draft rule, consultation paper, or enacted provision),
   its jurisdiction and effective/consultation timeline, the subject, and the rival set whose
   exposure matters for this read.
2. **Evidence ledger**: the regulatory text itself is the primary source for every provision-level
   claim — quote the operative language directly (within the ledger's exact-wording limit) rather
   than paraphrasing from a news summary of the text. Secondary commentary (law firm client alerts,
   trade-press analysis) may inform the read but must be tagged as secondary, not cited as the
   provision's own wording.
3. **Panel**: industry-analysis alone, or plus adjacencies, per the rule above, isolated per
   `rules/engagement-rules.md` if both run.
4. **Cross-examination**: only applies if both lenses ran; otherwise skip explicitly.
5. **Converged judgment + red team**: the converged judgment is the "who gains" summary. Red-team it
   per `skills/red-team/SKILL.md` — the sharpest attack here is usually testing whether the "who
   gains" conclusion depends on the regulation actually being enforced as drafted, when consultation-
   stage drafts are routinely watered down before enactment; the red team should state explicitly
   whether the read holds for the draft as written versus a plausible weakened final version.
6. **Exhibits**: the five-forces cross with each moved force annotated by which provision moves it
   and in which direction, per `rules/project-rules.md` Step 6 — this is the engagement where the
   standard force diagram earns its keep most directly, since the annotation *is* the finding.
7. **Fact-check gate**: `skills/evidence-auditor/SKILL.md`, with particular attention to the
   attribution check — regulatory provisions are frequently misquoted or summarized loosely in
   secondary coverage, and this engagement's entire value depends on getting the operative text right.
8. **Deliverable**: the provision-by-provision map, the per-player read, and the who-gains summary.
9. **Documentation report**: per `rules/engagement-rules.md`, explicitly noting the text's stage
   (draft, consultation, enacted) since that materially changes how much weight the read should carry.

## Engagement-specific constraints

- **Draft-stage text is not enacted text.** State the regulatory stage prominently in the deliverable
  itself, not only in the documentation report — a read built on a consultation draft that gets
  substantially amended before enactment is a real risk this engagement's recipient needs to see
  without digging for it.
- Where a rival's actual exposure depends on internal details the regulation's text doesn't disclose
  (e.g. what share of a rival's revenue the newly-regulated activity represents), say "not disclosed"
  for that rival's specific magnitude rather than assuming proportional exposure across all players.

## Output contract

Work in `work/regulatory-impact/<regulation-slug>-<date>/`, per `rules/engagement-rules.md`, with
`deliverable.md` structured as the provision map, the per-player read, and the who-gains summary, in
that order, with the regulatory stage stated at the top.
