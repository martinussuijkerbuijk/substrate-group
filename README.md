# Substrate Collective — Knowledge Base

Investigating AI through Ecology | Capital | Code

---

## What this repo is

A living research knowledge base for the Substrate Collective agent team. It is maintained by Claude Code; humans read and research, Claude keeps the wiki coherent.

Three tiers:
- **`raw/`** — full-text source materials (books, papers as markdown). Do not edit. Search via QMD `substrate-raw` collection.
- **`wiki/`** — synthesized, navigable knowledge. Max one page per file. Start here. Search via QMD `substrate-wiki` collection.
- **`dossiers/`** — active investigation outputs. Search via QMD `substrate-dossiers` collection.

Team structure and roles: `.substrate/TEAM.md`  
Claude maintenance rules: `CLAUDE.md`

---

## Status

### Done

- [x] **Wiki folder structure** — `concepts/`, `methods/`, `sources/`, `entities/`, `patterns/`
- [x] **Source synthesis notes** — all 14 books and 1 paper in `raw/` have a one-page wiki note in `wiki/sources/`
- [x] **Core concept entries** — 8 concepts extracted from team files and sources: `boundary-objects`, `threshold-of-detectability`, `situated-knowledge`, `infrastructure-invisibility`, `rentier-capitalism`, `opacity-architecture`, `lawscape`, `technics-as-unthought`
- [x] **Method entries** — 3 core team methods documented: `four-layer-evidence-analysis`, `counter-forensics`, `gap-as-finding`
- [x] **Evidence pattern entries** — 2 recurring patterns: `opacity-by-design`, `regulatory-capture-through-complexity`
- [x] **Dossier template** — full scaffold at `dossiers/_template/` covering all 4 evidence layers + synthesis (convergence map, divergence log, shape of the gap)
- [x] **QMD collections configured** — `substrate-wiki`, `substrate-raw`, `substrate-dossiers` added to `~/.config/qmd/index.yml`, separated from Climate-Code-Capital collections by prefix
- [x] **`CLAUDE.md`** — project-level instructions for Claude Code on wiki maintenance

---

## To do

### Immediate
- [ ] **Fill quote placeholders** — source notes marked `[find in raw/...]` need actual quotes pulled. Ask Claude to find a specific quote, or add them as you read.
- [ ] **Add `concepts/epistemic-justice.md`** — referenced in Fanon note and Community Liaison role but not yet written
- [ ] **Add `concepts/counter-forensics.md`** — currently lives in `methods/` but also needs a concept entry linking back
- [ ] **Populate `wiki/entities/`** — no entity files yet. Start as soon as the first investigation identifies recurring actors (companies, agencies, infrastructure nodes)

### When you start an investigation
- [ ] Copy `dossiers/_template/` to `dossiers/[investigation-name]/`
- [ ] Fill in `DOSSIER.md` — object of investigation, research questions, institutional position
- [ ] Assign each evidence layer to its lead agent

### As the knowledge base grows
- [ ] **Add new concept entries** as they emerge from investigations — Claude will do this automatically when a concept appears in 3+ sources
- [ ] **Add `wiki/patterns/` entries** as recurring evidence patterns are identified across dossiers
- [ ] **Add new source notes** to `wiki/sources/` whenever a new file is added to `raw/` — Claude will do this when asked or when a new session opens and sees new raw files
- [ ] **Update entity files** after each investigation synthesis phase

### Longer term
- [ ] Consider a `wiki/investigations/` index once multiple dossiers are running — a one-page overview of all active and completed investigations
- [ ] Consider adding `developments/` or `drafts/` folders (mirroring Climate-Code-Capital structure) for working documents that are not yet dossier-quality

---

## Quick reference

| I want to... | Go to |
|---|---|
| Understand a theoretical concept | `wiki/concepts/` |
| Know why a book matters before reading it | `wiki/sources/books/` |
| Plan an investigation step | `wiki/methods/` |
| Check if a pattern has been seen before | `wiki/patterns/` |
| Track an actor across investigations | `wiki/entities/` |
| Start a new investigation | Copy `dossiers/_template/` |
| Read a full source text | `raw/books/` or `raw/papers/` |
| Search across everything | QMD `substrate-wiki` collection |
