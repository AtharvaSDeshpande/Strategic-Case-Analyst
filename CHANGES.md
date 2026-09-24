# Changes made during sanitisation

This repository was extracted from a private project. Every change made to the source material on
the way out is listed here.

## Scope

Nothing from any case was copied. The following were excluded in full and never read into the
export: the case library, every per-case folder and its sources, analyses, diagrams and knowledge
graphs, every per-case reflection and summary, the course outline file, version control metadata,
agent configuration, all PDFs, and anything resembling a credentials file.

## rules/project-rules.md

Generalised from the private workflow file. Changes:

1. **Identity.** "Session agent" became "case analysis agent" throughout. Every "session N" became
   "case <slug>" or simply "the run".
2. **Paths.** `sessions/session-N/` became `cases/<slug>/`. The shared wiki path became `wiki/`,
   supplied by copying `wiki-template/`. The per-session `wiki.md` became `summary.md` to avoid
   confusion with the shared wiki.
3. **Course-outline dependence removed.** All reads of the course outline JSON were replaced with a
   generic "run configuration" or "case brief" that the user supplies. References to
   `topicName`, `caseStudyTitle`, `linkedObjectiveIds`, `courseObjectives` and `learningGoals` were
   dropped.
4. **Human validation gate generalised.** The gate previously keyed on a `conclusion` field in the
   course outline. It now keys on a human-written row in `wiki/validated-conclusions.md`. The
   substance is unchanged: an agent-drafted conclusion does not satisfy the gate, and execution
   stops rather than proceeding.
5. **Local paths and machine-specific workarounds removed.** A block describing a specific machine's
   two conflicting Graphviz installations and an absolute Windows path to one of them was deleted.
   The transferable lesson, that a script must resolve its output path from its own location and
   that a clean exit is not proof the intended file changed, was kept and rewritten without the
   local detail.
6. **Environment references generalised.** Named references to one specific assistant environment
   became "your environment".
7. **Understand-Anything kept as optional, by URL.** It is no longer described as a required
   bootstrap dependency. It is not vendored. The hand-authored fallback was kept.
8. **Reflection step generalised.** The instruction to apply the concept to a named business in one
   specific country became "a different, named organisation".
9. **Diagram table generalised.** Framework names were kept; the table is unchanged in substance.
   "BCG Matrix" and "GE/McKinsey Matrix" became "growth-share matrix" and "nine-box matrix" for
   consistency with the skills.
10. **Wiki writing rule added.** A new instruction requires framework pages to record transferable
    rules rather than case findings, which is what makes the wiki safe to share.
11. **Length.** The file was condensed. No gate, guardrail or quality rule was dropped; repeated
    explanations of the same rule were merged.

## wiki-template/

12. **`_schema.md`** kept the credit to Karpathy's gist by URL. Its description of the three layers
    was generalised away from the course structure, and a writing rule for framework pages was
    added.
13. **`index.md`** was reset: it links the framework pages and judgment files, with no run history.
14. **Four judgment files** were reduced to headers plus a suggested entry format. All entries were
    removed.
15. **Framework pages** were rewritten as case-free playbooks. For each page, the transferable "how
    to apply this well" rules were kept and the case name, run number, date and conclusion were
    dropped. Pages now also carry a short "signals that the application is weak" section.
16. **Two duplicate page pairs were merged.** The source had both a short and a long page for the
    five forces, and for blue ocean strategy. Each pair became one page.

## skills/

17. **Written fresh** from the framework method notes and the transferable wiki rules. No case
    material, no organisation names, no figures. Nothing was copied from a textbook.
18. **Two suggested groups were not created**, because the source project had no built material for
    them. See REVIEW.md.

## prompts/prompts.json

19. **Only three entries kept**: bootstrap, lint-wiki, and a single build-case prompt with a
    `{{CASE}}` placeholder. Every per-case build prompt was removed, along with the two
    cross-case prompts that referenced case numbers.
20. **The metadata block** was rewritten to remove the environment-specific invocation phrasing.

## Verification

A leak scanner was run over the whole export for the confidential-term blocklist, session
references, case-ID patterns, local paths, email addresses, URLs, sensitive-keyword patterns,
and forbidden file types. See REVIEW.md for the result.
