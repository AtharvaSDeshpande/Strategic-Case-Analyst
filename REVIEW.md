# Review gate

Nothing here has been published. This file is the checklist for the human review that has to happen
before it is.

## Every file in the export

### Root

| File | What it is |
|---|---|
| `README.md` | What the kit is, install notes for three environments, optional dependencies, credits, and the statement that no case material is included. |
| `CHANGES.md` | Every change made during sanitisation, numbered, including what was removed from the workflow file and why. |
| `REVIEW.md` | This file. |

### skills/

Seven method skills. Each has YAML front matter (`name`, `description`) and the same six sections:
when to use it, the framework steps, how to apply it well, common pitfalls, quality checks, and the
standard diagram convention.

| File | What it covers |
|---|---|
| `skills/industry-analysis/SKILL.md` | Macro scan, five forces, and the structure-conduct-performance chain. Boundary definition, rating with mechanism, segmenting before generalising. |
| `skills/internal-assessment/SKILL.md` | Resource-based view and the VRIO sequence as a filter. Emphasis on parity verdicts and the unrealised-advantage diagnosis. |
| `skills/competitive-strategy/SKILL.md` | Generic positions, the value chain, and the gap between an intended and a realised position. Includes the two-limb test for cost leadership. |
| `skills/adjacencies/SKILL.md` | Growth grid as a risk map, and a strict structural test for claims of uncontested market space. |
| `skills/diversification-and-corporate-strategy/SKILL.md` | Related and unrelated diversification, the portfolio matrix, and institutional theory including the premium-to-discount reversal. |
| `skills/implementation-and-leadership/SKILL.md` | Seven-element alignment diagnosis and the stakeholder power/interest grid, with explicit handling of elements that disclosure cannot reach. |
| `skills/innovation-and-dynamic-capabilities/SKILL.md` | Sensing, seizing, transforming, and ambidexterity, with the announced-versus-executed distinction. |

### wiki-template/

| File | What it is |
|---|---|
| `_schema.md` | How the wiki works, the three layers, the three operations, and the rule that framework pages record transferable method. Credits Karpathy's gist by URL. |
| `index.md` | Entry point linking all framework pages and judgment files. No run history. |
| `capability-log.md` | Header plus suggested entry shape. Empty. |
| `reusable-heuristics.md` | Header plus entry shape including provenance, confidence and validation status. Empty. |
| `open-threads.md` | Header plus entry shape. Empty. |
| `validated-conclusions.md` | Header, the explanation of why human validation matters, and an empty table. |
| `frameworks/pestel.md` | Method for the macro scan. |
| `frameworks/five-forces.md` | Method for industry structure. Merged from two source pages. |
| `frameworks/scp.md` | Method for tracing structure through conduct to performance. |
| `frameworks/vrio.md` | Method for the resource filter, including the context-dependence of the organisation test. |
| `frameworks/value-chain.md` | Method for activity decomposition, linkages, and encoding evidence in the exhibit. |
| `frameworks/generic-strategies.md` | Method for placing a competitive position. |
| `frameworks/ansoff-matrix.md` | Method for mapping and risk-rating growth moves. |
| `frameworks/blue-ocean-strategy.md` | Method for testing uncontested-space claims. Merged from two source pages. |
| `frameworks/bcg-matrix.md` | Method for portfolio and capital allocation. |
| `frameworks/institutional-theory.md` | Method for reading strategy against institutional conditions. |
| `frameworks/dynamic-capabilities.md` | Method for assessing renewal capability. |
| `frameworks/mckinsey-7s.md` | Method for diagnosing execution friction. |
| `frameworks/stakeholder-map.md` | Method for the power/interest grid, emphasising movement between quadrants. |

Each framework page carries a "how to apply this well" section and a short "signals that the
application is weak" section. None names an organisation, a person, a date or a conclusion.

### rules/ and prompts/

| File | What it is |
|---|---|
| `rules/project-rules.md` | The end-to-end workflow, generalised. Keeps the evidence-first architecture, the quality bar, the human validation gate, the evidence and scope audit, the diagram sourcing rules, and the wiki ingest and lint operations. |
| `prompts/prompts.json` | Three entries: `bootstrap`, `lint-wiki`, and `build-case` with a `{{CASE}}` placeholder. |

## Left out, and why

1. **Two of the suggested skill groups were not created.** `governance-and-sustainability` and
   `integration-and-synthesis` have no source material: the directories for those topics in the
   private project are empty, so there is no method note to generalise from. Writing them would have
   meant inventing content rather than sanitising it. **Decide whether you want them written from
   scratch.**
2. **All case material.** No case library, per-case folder, source list, analysis, reflection,
   summary, diagram or knowledge graph was copied or read into the export.
3. **The course outline file.** Read once, by script, to build the blocklist. Nothing from it
   reached the export, and the workflow's dependence on it was removed.
4. **Per-case build prompts.** Thirteen existed; all were dropped because their descriptions carried
   case titles. Two cross-case prompts were dropped for the same reason.
5. **A specific machine's Graphviz workaround.** Removed with its absolute path. The transferable
   lesson about resolving output paths from a script's own location was kept.
6. **The knowledge-graph tool.** Referenced by URL only, marked optional, not vendored.
7. **Any collaboration or output folder from the private project**, including finished analyses and
   their evidence ledgers.

## Things I was unsure about

1. **Framework names and originators are present.** Names such as the five forces, the value chain,
   VRIO and the seven-element model appear throughout, along with a few originator surnames where
   they are part of the framework's common name. These are standard published vocabulary, not case
   material, and the kit cannot teach the methods without them. Flagging it because the line between
   "standard vocabulary" and "course material" is a judgment call and it is yours to confirm.
2. **The private project's own process vocabulary.** Terms such as "case identity anchor", "evidence
   ledger", "carry-forward" and "quality bar" survive in the workflow file. They describe the method
   rather than any case, but they are recognisably from the source project.
3. **The diagram layout table** in the workflow file lists framework-to-layout mappings. These are
   conventional and widely published, but the table as a set is the private project's compilation.
4. **Judgment about what counted as confidential.** 194 terms were enforced as hard blocks. A
   further 336 terms the automated sweep caught were classed as ordinary English or framework
   vocabulary and were not enforced, because enforcing them would have flagged legitimate method
   writing. The rule applied: a term stays enforced if it names an organisation, person, publisher,
   publication, course artefact, or case-bound particular. The full lists are in the private folder
   beside the export if you want to audit that call.
5. **No worked examples are included.** The brief allowed clearly labelled fictional ones. I wrote
   none, because a fictional example risks reading as a disguised real one. The skills rely on
   stated rules instead. **Tell me if you would rather have illustrative examples.**

## Leak scan result

Run over all 30 files in the export.

- 194 blocklist terms, case-insensitive with word boundaries: **0 hits**
- `Session <n>` references: **0**
- Case-ID shapes: **0**
- Local filesystem paths: **0**
- Email addresses: **0**
- URLs outside the two credited links: **0**
- Sensitive-keyword patterns: **0**
- Forbidden file types and directory names: **0**
- File paths referenced from a SKILL.md that do not exist: **0**

One hit was found and fixed on the first pass: `CHANGES.md` described what the scanner looks for and
matched its own description. The sentence was reworded and the whole scan re-run clean.

## Open decisions for you

1. **Licence.** No `LICENSE` file was created, as instructed. The content is original prose
   describing published frameworks. MIT or CC BY 4.0 would both fit; CC BY is the better match for
   prose. **Nothing ships until you choose.**
2. **Repository name.** The folder is `SMAIPlaybook-public-export`, which is an export name rather
   than a repository name. Something like `strategy-analysis-playbook` reads better publicly and
   carries no trace of the source project.
3. **Public or private.** Recommend pushing private first, reading the rendered files on the
   platform, and flipping to public only after that read. Rendered markdown surfaces things a
   scanner does not.
4. **The two missing skill groups.** Write them from scratch, or ship seven.
5. **Worked examples.** Add clearly labelled fictional ones, or keep the kit rule-only.
6. **Attribution.** Decide whether to credit yourself by name in the README. It currently says
   "the maintainer".

## Not done, by instruction

Nothing was pushed. No git repository was initialised, no remote added, no commit made. No network
call was made at any point in building this export.
