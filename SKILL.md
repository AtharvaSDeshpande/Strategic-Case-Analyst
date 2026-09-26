---
name: StrategistAgent
description: Engagement router for a strategy-analyst multi-agent system. Reads a request, picks (or asks which) of eight specialized orchestrator engagements to run — competitor teardown, commercial DD screen, market entry assessment, quarterly competitive monitor, board/IC decision memo, regulatory impact read, portfolio review, or the academic reflection paper — and hands off to that engagement's own SKILL.md, which owns its multi-agent panel, red-team pass, and fact-check gate end to end. Use when the user says "Run Agent" with or without a specific agent name, asks what this repository can do, or describes a strategy task without naming a specific engagement skill.
---

# StrategistAgent

This repository is not a single pipeline that produces one kind of document. It is an **engagement
router** over a shared analytical spine: seven strategy-framework lenses, two enforcement roles that
sit outside the lenses (a red team and an evidence auditor), and eight specialized orchestrator
skills, each of which knows how to run that spine for one real kind of work.

```
scope → evidence ledger → panel (parallel lenses) → cross-examination
      → converged judgment + strongest counter → exhibits → fact-check gate → deliverable
      → documentation report → human validation gate
```

Every orchestrator skill in this repository implements this spine in full. What changes per
engagement is which lenses run, what the exhibits look like, and what the deliverable's sections are
— never whether a stage happens. `rules/engagement-rules.md` is the authoritative, shared definition
of every stage; read it once, then read the specific orchestrator skill for the engagement being run.

## Run an agent

Say **"Run Agent \<name\>"**. Each orchestrator's own `SKILL.md` has a `name:` field matching exactly
what you say:

| Say this | Runs | What it produces |
|---|---|---|
| `Run Agent CompetitorTeardown` | `skills/competitor-teardown/SKILL.md` | A weighted competitive profile matrix, one battlecard per rival, a "where we actually lose" note |
| `Run Agent CommercialDD` | `skills/commercial-dd-screen/SKILL.md` | A four-part DD screen (market, target, peers, risk register) plus what the evidence can't show |
| `Run Agent MarketEntry` | `skills/market-entry-assessment/SKILL.md` | Five forces on the target market, a capability-transfer test, an adjacency risk grade, an entry-cost floor, a go/no-go |
| `Run Agent CompetitiveMonitor` | `skills/competitive-monitor/SKILL.md` | A diff against last quarter's ledger: material moves only, plus which prior judgments are now stale |
| `Run Agent DecisionMemo` | `skills/decision-memo/SKILL.md` | A two-page options table, a weighted decision with visible weights and a sensitivity line, a mandatory red-team section |
| `Run Agent RegulatoryImpact` | `skills/regulatory-impact/SKILL.md` | Each provision of a draft rule mapped to the force it moves, per player, with who gains |
| `Run Agent PortfolioReview` | `skills/portfolio-review/SKILL.md` | A portfolio matrix on disclosed positions, a funding-capacity test, a pipeline check |
| `Run Agent ReflectionPaper` | `skills/reflection-paper/SKILL.md` | The academic 5-6 page concept-silent reflection paper (coursework, not client work) |

If the user asks for something without naming an agent, match the request to the table above by what
it would actually produce, and confirm the match before running a multi-hour engagement on a guess.
If nothing in the table fits, say so rather than force-fitting the nearest one — this router does not
have a ninth, catch-all engagement.

## The panel: seven lenses, two enforcement roles

The seven framework skills are the panel every orchestrator draws from. Each is a `skills/<slug>/
SKILL.md`: `industry-analysis`, `internal-assessment`, `competitive-strategy`, `adjacencies`,
`diversification-and-corporate-strategy`, `implementation-and-leadership`,
`innovation-and-dynamic-capabilities`. They supply method and judgment only — every fact still comes
from a source verified live, never from the skill files themselves.

Two more skills are not lenses and never produce a lens's opinion:

- **`skills/red-team/SKILL.md`** — attacks a converged judgment that a different pass already wrote.
  Never runs on its own author's work.
- **`skills/evidence-auditor/SKILL.md`** — re-opens every cited source and blocks the deliverable if
  a claim doesn't match. Not advisory; a failed audit stops the engagement.

`skills/install-visual-tooling/SKILL.md` is a third supporting skill, for setting up the optional
diagram-rendering dependencies (see the repository README).

## Honest constraints — every orchestrator must apply these

1. **The panel is only worth its cost when the lenses actually conflict.** On a question simple
   enough that every assigned lens would agree, an orchestrator runs one or two lenses and says so —
   not all seven for the appearance of rigor. `rules/engagement-rules.md` and each orchestrator's own
   default-panel section state the expected tension for that engagement; treat that as a hypothesis
   to check, not a quota.
2. **Private companies and thin disclosure break the ledger.** The whole discipline rests on primary,
   public, checkable sources. Where a subject doesn't disclose, the honest output is "not disclosed"
   across the affected cells — never an estimate presented as a figure. `skills/portfolio-review/
   SKILL.md` is the clearest case of this in the kit and should be expected to degrade the most.
3. **The human validation gate stays, and matters more for real work, not less.** Every deliverable
   and every documentation report is marked draft until a human has reviewed it. An agent-drafted
   conclusion, however well cross-examined and red-teamed, is never self-validating.

## Every engagement produces two artifacts, not one

Alongside its deliverable, every orchestrator produces `documentation-report.md`: an industry-standard
methodology note covering scope, panel composition and why each lens was or wasn't run, the evidence
base and audit result, the cross-examination summary, the red-team outcome, explicit limitations, and
validation status. This is what lets the deliverable be trusted in a room where someone will check it
— see `rules/engagement-rules.md`'s "Documentation report" section for the exact template every
orchestrator fills in.

## What's shared vs. what's per-engagement

```
rules/engagement-rules.md      the spine every orchestrator implements (read this first)
rules/project-rules.md         single-framework method + diagram conventions (Step 6), still authoritative
skills/<framework>/SKILL.md    the seven panel lenses
skills/red-team/               attacks a converged judgment; never its own author
skills/evidence-auditor/       re-opens sources; blocks the deliverable on a mismatch
skills/install-visual-tooling/ optional diagram-tooling setup
skills/<engagement>/SKILL.md   the eight orchestrators — each specializes the spine for one deliverable
wiki-template/ → wiki/         accumulating judgment, shared across every engagement and every run
work/<engagement-slug>/<run>/  each run's own scope, ledger, panel notes, exhibits, and deliverable
```

Read `rules/engagement-rules.md` in full before running any orchestrator for the first time in a
session; it is not repeated in full inside each orchestrator skill, only specialized.
