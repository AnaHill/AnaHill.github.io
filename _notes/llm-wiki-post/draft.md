# Writing an academic review with an LLM wiki: what worked and what didn't

<!--
Luonnos koostettu tiedostoista: llm-wiki-post-lessons.md (pääsisältö: opit), notes.md, notes_OHJEET.md, outline.md ja kuinka_clauden_avulla_ohjeistaa_uutta_chattia.md.
- TODO-kohdat = puuttuu sisältöä tai tarkistettava.
- [CLAUDE] = kohta perustuu lessons-tiedoston osioon "Lisäykset 31.10. session pohjalta (Clauden ehdotuksia, eivät omia muistiinpanoja)". Tarkista tai poista.
- Kuvat ovat luonnosvaiheessa tarkoituksella pelkkinä linkkeinä (ei !).
- Julkaisu: tämä on kattavampi blogiversio. LinkedIniin erikseen lyhyt versio. Molemmat julkaistaan vasta, kun paperi on Zenodossa, koska postaus linkittää siihen.
-->

**DISCLAIMER**: Be responsible and avoid AI slop. "*Vibe-researching*" is educational (and fun!), but in science, **DETAILS**. **DO**. **MATTER**. A paper whose claims are 90% correct is not a good result. I have personally gone through every source and especially every claim in the paper, and I have done my best (with limited free time) to fix errors and inaccuracies.

## Why

I wanted to write a narrative review on how the analysis of cardiomyocyte microelectrode array (MEA) recordings has developed since 2022. A literature review is mostly bookkeeping: which papers have I read, what exactly did each of them show, and which of my sentences are actually supported by a source. That bookkeeping is where I wanted help from an LLM, without handing over the thinking.

 - [ ] TODO: a couple of sentences on why the LLM wiki approach in particular (vs. just chatting with an LLM or a reference manager).

The paper and everything behind it is public: [AnaHill/MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki). 
- [ ] TODO: Zenodo link to the paper.

## The paper in one paragraph

- [ ] TODO: short summary of the paper's content (MEA, hiPSC-CMs, main themes, the gaps found). 

Keep this brief; the post is about the method.

## The method in brief

The repository has three layers:

- `raw/`: the source PDFs. These never change.
- `wiki/`: pages maintained by the LLM: one summary page per paper, concept pages, a page for the gaps in the literature, plus `index.md`, `log.md` and `references.md`.
- `main.md`: the paper draft itself.

On top of these there is a schema file, `AGENTS.md`, that tells the agent how to work (`CLAUDE.md` only points to it), a `skills/` folder, and `llm-wiki.md`, which explains the method. Next to them, `docs/` holds supporting material such as `claims-by-source.md` (every claim in the paper listed by its source) and the search documentation, and `check.py` runs structural checks.

I ask the agent to do four operations:

- **Ingest**: PDF → summary page, wiki updates and a reference entry.
- **Query**: a question → an answer from the wiki, with sources.
- **Draft**: write or rewrite a section of `main.md`.
- **Lint**: a health check: outdated claims, orphan pages, unsupported claims.

- [ ] TODO: workflow diagram: `raw/` → ingest → `wiki/` → draft → `main.md`, with lint going back to the wiki.

Tools: VS Code with [Foam](https://foambubble.github.io/foam/) or [Obsidian](https://obsidian.md/) for linking and the graph view, and an LLM agent (Claude Code).

[Graph view of the wiki, index excluded](../pics/posts/llm-wiki_graph_view_wiki_exclude_index.png)

## The workflow in practice

TODO: what a typical working session looked like. Go through `wiki/log.md` in the paper repo; it is a ready-made timeline of what was done.

TODO: example of one paper: its summary page and how it ends up as a citation in `main.md`.

TODO: before/after: one paragraph where `[CITATION NEEDED]` is replaced by a real citation.

### The wiki structure pays off every time

Every time the agent did something, the structure of the wiki helped. It remembered to update not only `main.md` but also the log, the index and the other related files. One change in the paper often touches several of them: the paragraph in `main.md`, the paper's wiki page, `claims-by-source.md` and the log. The agent made all of them in one go and reported what it changed. Then I reviewed the diff before committing.

[Agent's report after updating several files](../pics/posts/llm-wiki_loop_work.png)

[The resulting staged changes and diff in VS Code](../pics/posts/llm-wiki_loop_work2.png)

Every report also ended with a decent commit message suggestion, for example "*reword the Declarations sentence about colleagues to name the CoEBoC collaboration*". I did not automate committing, because I want to check every change myself.

### Giving a new chat a well-scoped task

A lot of the work happened in fresh chats, each with one narrow task. The prompt matters more than I expected. Here is the prompt for a literature search on one gap in the review (translated from Finnish and shortened, TODO: check the translation):

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
- **The search itself is documented**, so the method sentence in the paper describes a search that actually happened. Why this mattered is explained below.
- **I decide what gets ingested.** The agent never adds sources to `raw/` on its own.

## The main lesson: data quality

If I did this again, I would check the sources, and the decisions made from them, much more carefully right at the start. Even though vibe-researching is fun, going through the sources as early as possible pays off in the end. The reason is how errors spread in an LLM wiki.

### How a wrong claim spreads

I found three kinds of errors, and each one starts from a different place:

```
Error A, a source is misread:
raw/source.pdf
  -> wiki/papers/source.md        (the summary exaggerates or misreads)
  -> wiki/<concept page>.md       (e.g. hipsc-cm-maturation.md, critical-assessment-maki-claims.md)
  -> wiki/index.md                (one-line summary)
  -> main.md                      (several sections: text, tables, figure captions)
  -> main.md Abstract/Conclusion  (generalised even further when summarised)
  -> docs/claims-by-source.md     (the claim list copies the error from main.md)

Error B, the AI fills a gap without a source:
AI draft -> main.md -> docs/claims-by-source.md -> ("Relevance" sections of wiki pages)

Error C, a patch fix:
a fix in one place -> contradiction with the rest of the sentence or with other sections
```

The lesson: **the earlier an error is born, the more places it is copied to.** So the check belongs in the ingest step, not at the end when reading `main.md`.

### What catches what

| Check | Catches | Misses |
|---|---|---|
| `check.py` | structural errors: missing references, DOI mismatches, broken links | content, so A, B and C all pass |
| `claims-by-source.md` + reading the source | A and B, when the claim is checked against the source and not against the wiki page | C |
| A human reading the whole text | C and contradictions between sections | |

### Examples from this paper

**A: wiki pages contradicted their sources.** Several wiki pages (e.g. Ismaili, Matsuda, Hwang, Kabanov) contained claims that the source itself did not support. These were found only when I compared the source text and the claims line by line. This is the risk of an LLM wiki in a nutshell: the wiki looks tidy and confident, and the error is invisible until you go back to the PDF.

**B: an invented method sentence.** `main.md` claimed a "*targeted search of PubMed/MEDLINE, bioRxiv and Scopus (2 July 2026)*", but there was no record of such a search; it had been the AI's own web search. It sounded entirely plausible. I replaced it with a documented search (`docs/maturation-mea-search.md`, using the prompt shown above), which also found two relevant sources (Li 2025, Lin 2023). Other B-type errors: the word "longitudinal" in the very first draft, and an invented reference "Galli et al. 2024".

**C: a patch fix made a sentence contradict itself.** The opening sentence of the section on open analysis pipelines said that open pipelines had appeared after 2022, and the end of the same sentence said the opposite: "*open tools such as MultiElec and CardioMDA already existed before 2022*". The end had been added as a correction three days earlier, because both Lee et al. (2024, Table 3) and Dunham et al. (2022, p. 2) say that open tools existed before. The beginning was never changed to match. The automatic checks did not notice; I found it myself while reading. According to the sources, what is new after 2022 is not openness but new open tools for new types of data: CardioMEA for HD-MEA data (Lee) and PhysioMEA for cardiac organoids (Weiser-Bitoun).

[Human in the loop: heading and paragraph rewritten after the contradiction was found](../pics/posts/llm-wiki_human-in-the-loop-tarkeys.png)

Since then the agent has this rule: "*When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.*"

## Finding sources: don't rely on one search

The agent's searches alone were not enough. Good old googling, Google Scholar, and going through the references of each source and the papers that cite it found things the agent did not. A second LLM (e.g. Gemini) is another way to widen the search.

[CLAUDE] A documented search produced new findings, not just confirmation. Once the queries, hit counts and citation chains were recorded, the search found two sources (Li 2025, Lin 2023) that sharpened the paper's gap claim, and one connection (Scheurer 2025's maturity classes are based on Li 2025) that the earlier web search had not revealed.

TODO: ehkä oma osio: hämmentävän suuri ero Claude Coden ja Gemini notebookin välillä. Mieti vielä, onko tarpeen.

## What else worked

- **A critical assessment page.** A wiki page where the agent critically assesses claims, including my own earlier claims, was a good addition to the LLM wiki. It also gets corrected when the details are wrong (for example, which figure in a source actually shows what).

  [Critical assessment page being corrected](../pics/posts/llm-wiki_critical_assignment.png)

- **Useful suggestions from the agent.** For example: "*When you fetch the PDFs, also get the supplementary file for Li 2025. Supplementary Table 3 has the numeric values for spike amplitude and slope.*"
- **Memory between sessions.** Claude's memory files kept things like commit message style and project conventions across chats.

  [Claude's memory files](../pics/posts/llm-wiki_claude_memory.png)

- [CLAUDE] **"Grilling" decisions before acting.** Choosing which sources to include was in practice done by grilling: the agent proposed a choice with its reasoning, I iterated and decided, and only then was it documented. This became a `/grill-paper` skill in the repo (adapted from Matt Pocock's `grilling` skill, MIT): a round-by-round interview where the agent looks up the facts from the wiki itself and the decisions stay with the researcher. I took it into use late; used from the start, it would have saved many correction rounds.

## What I would do differently

- Check the sources right at the start, at ingest, before anything is built on them.
- Search for sources in several ways from the beginning, not only through the agent.
- Use grilling for decisions from day one. [CLAUDE]
- TODO: more.

## Practical tips

- Use Foam (or Obsidian) for linking and the graph view.
- Put the working rules in the schema file (`AGENTS.md`), for example "never invent citations". Keep `CLAUDE.md` as a pointer to it, so other agents can use the same rules.
- Mark unsupported sentences with `[CITATION NEEDED]` instead of letting the agent guess a source.
- Keep a claims-by-source list and check it against the sources, not against the wiki.
- Use scripts like `check.py` for structural checks, but remember that they do not check content.
- Run lint rounds regularly.
- Give each new chat one narrow task, the files to read first, and what it may not touch.
- TODO: more.

## Where the paper is published

[CLAUDE] I chose Zenodo instead of Preprints.org because the paper is not going to a journal. For a hobby project, Europe PMC visibility did not outweigh the uncertainty of the screening (affiliation, AI policy). Findability comes from posts like this one and from the repository.

## Try it yourself

- Template for a personal wiki: [llm-wiki-template](https://github.com/AnaHill/llm-wiki-template)
- Template for researchers: [llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template)
- The paper repository: [MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki)
- TODO: the paper on Zenodo
