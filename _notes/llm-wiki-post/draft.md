# Writing an academic review with an LLM wiki: what worked and what didn't

<!-- Luonnos koostettu tiedostoista notes.md, notes_OHJEET.md, outline.md ja kuinka_clauden_avulla_ohjeistaa_uutta_chattia.md. TODO-kohdat = puuttuu sisältöä tai tarkistettava. Kuvat ovat luonnosvaiheessa tarkoituksella pelkkinä linkkeinä (ei !). -->

**DISCLAIMER**: Be responsible and avoid AI slop. "*Vibe-researching*" is educational (and fun!), but in science, **DETAILS**. **DO**. **MATTER**. A paper whose claims are 90% correct is not a good result. I have personally gone through every source and especially every claim in the paper, and I have done my best (with limited free time) to fix errors and inaccuracies.

## Why

I wanted to write a narrative review on how the analysis of cardiomyocyte microelectrode array (MEA) recordings has developed since 2022. A literature review is mostly bookkeeping: which papers have I read, what exactly did each of them show, and which of my sentences are actually supported by a source. That bookkeeping is where I wanted help from an LLM, without handing over the thinking.

TODO: a couple of sentences on why the LLM wiki approach in particular (vs. just chatting with an LLM or a reference manager).

The paper and everything behind it is public: [AnaHill/MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki).

## The paper in one paragraph

TODO: short summary of the paper's content (MEA, hiPSC-CMs, main themes, the gaps found). Keep this brief; the post is about the method.

## The method in brief

The repository has three layers:

- `raw/`: the source PDFs. These never change.
- `wiki/`: pages maintained by the LLM: one summary page per paper, concept pages, a page for the gaps in the literature, plus `index.md`, `log.md` and `references.md`.
- `main.md`: the paper draft itself.

On top of these there is a schema file, `AGENTS.md`, that tells the agent how to work (`CLAUDE.md` only points to it), a `skills/` folder, and `llm-wiki.md`, which explains the method.

I ask the agent to do four operations:

- **Ingest**: PDF → summary page, wiki updates and a reference entry.
- **Query**: a question → an answer from the wiki, with sources.
- **Draft**: write or rewrite a section of `main.md`.
- **Lint**: a health check: outdated claims, orphan pages, unsupported claims.

TODO: workflow diagram: `raw/` → ingest → `wiki/` → draft → `main.md`, with lint going back to the wiki.

Tools: VS Code with [Foam](https://foambubble.github.io/foam/) for linking and the graph view, and an LLM agent (Claude).

[Graph view of the wiki, index excluded](../pics/posts/llm-wiki_graph_view_wiki_exclude_index.png)

## The workflow in practice

TODO: what a typical working session looked like. Go through `wiki/log.md` in the paper repo; it is a ready-made timeline of what was done.

TODO: example of one paper: its summary page and how it ends up as a citation in `main.md`.

TODO: before/after: one paragraph where `[CITATION NEEDED]` is replaced by a real citation.

### Giving a new chat a well-scoped task

A lot of the work happened in fresh chats, each with one narrow task. The prompt matters more than I expected. Here is an example of a literature search for one gap in the review (translated from Finnish and shortened, TODO: check the translation):

> Task: literature search for one gap in my review paper. Do not edit main.md or the wiki at this stage; report findings first.
>
> Read first: AGENTS.md (especially "Never invent citations" and "Batch or undirected additions — verify before ingesting"), the relevant section of main.md, the related wiki pages, wiki/index.md (sources already processed, so they are not suggested again) and docs/search-strategy.md.
>
> Question: is there published work that proposes or validates MEA-derived reference values or a classifier for hiPSC-cardiomyocyte maturation? (...)
>
> For each candidate, report: authors, year, title, journal, DOI (only if verified from the source; otherwise mark "unverified"), which MEA parameters it links to maturation, whether it is validated against something, and whether it covers the gap fully, partially or not at all. Also record the search queries, databases and date, so the "targeted search" sentence in main.md can be based on an actual search.
>
> Do not add anything to raw/. I will add the PDFs myself for those I decide to ingest.

What makes this work:

- **Report first, edit later.** The agent cannot change the paper or the wiki before I have seen the results.
- **No invented references.** A DOI is reported only if it was verified from the source.
- **The search itself is documented**, so the method sentence in the paper describes a search that actually happened.
- **I decide what gets ingested.** The agent never adds sources to `raw/` on its own.

### Updating several places at once

One change in the paper often touches several files: the paragraph in `main.md`, the paper's wiki page, a claims-by-source list and the log. I asked the agent to make all of them in one go and to report what it changed, including a suggested commit message. Then I reviewed the diff before committing.

[Agent's report after updating several files](../pics/posts/llm-wiki_loop_work.png)

[The resulting staged changes and diff in VS Code](../pics/posts/llm-wiki_loop_work2.png)

TODO: mention `check.py` (what it checks).

## What worked

- **A critical assessment page.** A wiki page where the agent critically assesses claims, including my own earlier claims, was a good addition to the LLM wiki. It also gets corrected when the details are wrong (for example, which figure in a source actually shows what).

  [Critical assessment page being corrected](../pics/posts/llm-wiki_critical_assignment.png)

- **Useful suggestions from the agent.** For example: "*When you fetch the PDFs, also get the supplementary file for Li 2025. Supplementary Table 3 has the numeric values for spike amplitude and slope.*"
- **Memory between sessions.** Claude's memory files kept things like commit message style and project conventions across chats.

  [Claude's memory files](../pics/posts/llm-wiki_claude_memory.png)

- TODO: more.

## What didn't work / lessons learned

- **Patch fixes can leave a sentence contradictory.** When the AI corrects one claim, the rest of the sentence may no longer fit. After a correction, re-read the whole sentence. I added this rule for the agent: "*When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.*"

  [Human in the loop: a heading and paragraph rewritten after a correction](../pics/posts/llm-wiki_human-in-the-loop-tarkeys.png)

- TODO: limits, mistakes, where human judgement was needed. `[CITATION NEEDED]` markers in the paper repo show where support was missing.

## Practical tips

- Use Foam (or Obsidian) for linking and the graph view.
- Put the working rules in the schema file (`AGENTS.md`), for example "never invent citations". Keep `CLAUDE.md` as a pointer to it, so other agents can use the same rules.
- Mark unsupported sentences with `[CITATION NEEDED]` instead of letting the agent guess a source.
- Run lint rounds regularly.
- TODO: more.

## Try it yourself

- Template for a personal wiki: [llm-wiki-template](https://github.com/AnaHill/llm-wiki-template)
- Template for researchers: [llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template)
- The paper repository: [MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki)
