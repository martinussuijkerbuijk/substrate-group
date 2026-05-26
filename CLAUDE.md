# Substrate Collective — Claude Code Instructions

## Role

You maintain this knowledge base. The human team focuses on research; you keep the wiki coherent, synthesized, and navigable.

## Wiki maintenance rules

**When a new file appears in `raw/`:**
- Create a synthesis note in `wiki/sources/books/` or `wiki/sources/papers/` using `wiki/sources/_template.md`
- Max one page. Argument, why it matters to us, key concepts, relevant agents, key quotes, link to raw
- If the source introduces a concept that doesn't have a `wiki/concepts/` entry yet, create one

**When a concept appears in 3+ sources:**
- Create or update `wiki/concepts/[slug].md`
- Link back from each source note using `[[slug]]` notation

**When starting an investigation:**
- Copy `dossiers/_template/` to `dossiers/[investigation-name]/`
- Populate `DOSSIER.md` with the object of investigation and research questions

**What NOT to do:**
- Do not write long summaries of sources — synthesize (argument + why it matters to us)
- Do not resolve divergences in the divergence log — document them
- Do not treat a gap as a failure — tag it and move on
- Do not add content to `raw/` — that folder is source material only

## QMD collections for this project

- `substrate-raw` — search for quotes and full-text verification across books and papers
- `substrate-dossiers` — search across active investigation findings

The wiki is navigated by folder structure, not QMD — it is small and structured enough not to need search.

The `research`, `books`, `drafts`, `developments`, `inspiration`, `concepts` collections belong to the Climate-Code-Capital project — do not mix them.

## Team

See `.substrate/TEAM.md` for agent roles, evidence layers, confidence levels, and synthesis rhythm. That file is authoritative.
