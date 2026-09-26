# Schema: how this wiki works

Pattern source: Andrej Karpathy's `llm-wiki.md` gist
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The idea is that an assistant
incrementally builds and maintains a persistent, structured, cross-referenced wiki instead of
re-deriving the same knowledge from raw sources every time it runs. This directory is that pattern
applied to strategy analysis, so that a run on the tenth case starts from more accumulated judgment
than a run on the first.

## The three layers

1. **Raw sources** (immutable). The material for each case you analyse. The wiki process only ever
   reads from these; it never edits them.
2. **The wiki** (this directory, assistant-maintained). Structured, interlinked markdown that
   compiles what has been learned, so later runs build on synthesis rather than re-reading.
3. **The schema** (this file, plus the fuller workflow in `rules/project-rules.md`). Conventions
   governing how the three operations below behave. The rules file is authoritative; this file is a
   short pointer for anyone opening the wiki cold.

## Layout

- `index.md`: entry point. Links every framework page and every judgment file. Read it first.
- `frameworks/<slug>.md`: one page per framework ever applied. Each page compounds across every
  case that framework has touched. It does **not** hold the definition of the framework (that
  belongs with the per-case concept note); it holds what has been learned about applying the
  framework well.
- `capability-log.md`: one entry per run, recording which analytical skill was genuinely sharpened.
- `reusable-heuristics.md`: judgment rules earned from real analysis.
- `open-threads.md`: contradictions and unresolved tensions between runs, resolved in place when
  closed.
- `validated-conclusions.md`: one row per run, authoritative only once a human has confirmed it.

## The three operations

- **Query**, before a run starts. Read `index.md`, then the four judgment files, then only the
  framework pages relevant to this run's scope. Do not read the whole wiki indiscriminately.
- **Ingest**, after a run's analysis is done. Update every framework page actually used, plus the
  judgment files, plus `index.md` if anything new was created. Append; never overwrite a prior
  entry.
- **Lint**, immediately after Ingest. A short audit for contradictions, staleness, orphaned pages
  and gaps. Report findings; fix only broken index links directly, and log anything else for a
  human rather than silently changing a judgment file.

## Writing rules for framework pages

Keep each page transferable. Record the rule, not the case that taught it. A page entry should
still make sense to someone who has never seen the material it came from, and should not name the
organisation, people, dates or conclusions of any particular case. If a lesson cannot be stated
without naming its source material, it is a case finding rather than a method rule, and it belongs
in that case's own write-up.
