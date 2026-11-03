---
layout: default
title: "Writing an academic review with an LLM wiki: what worked and what didn't"
date: 2026-11-10
categories: [llm]
tags: [LLM wiki, academic writing, Claude Code, data quality]
---

{% include blog-meta.html %}

<!--
LUONNOS. Siirto julkaisuun: ks. notes_OHJEET.md.
- [ ] TODO = puuttuu sisältöä tai tarkistettava ennen julkaisua.
- [CLAUDE] = kohta perustuu Clauden ehdotuksiin (lessons-osio "Lisäykset 31.10."), ei omiin muistiinpanoihin. Tarkista tai poista.
- Kuvat ovat luonnosvaiheessa pelkkinä linkkeinä. Julkaisussa lisää jokaisen eteen ! (figcaption on jo valmiina).
-->

> 😎 Nerd your day! 🤓

**DISCLAIMER**: Be responsible and avoid AI slop. "*Vibe-researching*" is educational (and fun!), but in science, **DETAILS**. **DO**. **MATTER**. A paper whose claims are 90% correct is not a good result. I have personally gone through every source and especially every claim in the paper, and I have done my best (with limited free time) to fix errors and inaccuracies.

In this post, I describe how I wrote a scientific review paper with an AI agent and an **LLM wiki**, and what I learned along the way. Spoiler: the biggest lesson was not about AI at all but about **data quality**. 🤓

- 📄 The paper: [Zenodo](TODO) <!-- - [ ] TODO: Zenodo DOI -->
- 💻 Everything behind it (sources, wiki, logs, scripts): [AnaHill/MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki)
- 🧰 Template to try it yourself: [llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template)

## Why an LLM wiki?

I wanted to write a narrative review on how the analysis of cardiomyocyte microelectrode array (MEA) recordings has developed since 2022. A literature review is mostly bookkeeping: which papers have I read, what exactly did each of them show, and which of my sentences are actually supported by a source. That bookkeeping is where I wanted help from our 🤖 friend, without handing over the thinking.

- [ ] TODO: 1–2 sentences on why an LLM wiki in particular, and not just chatting with an LLM or using a reference manager. Idea: a chat forgets, a reference manager does not know what the papers say; the wiki keeps both, as plain markdown under version control.

## The paper in brief

The paper is called *Four Gaps Limiting Comparability in MEA Analysis of hiPSC-Cardiomyocytes*. It is a narrative review of field potential analysis methods for MEA recordings of human induced pluripotent stem cell-derived cardiomyocytes (hiPSC-CMs) since 2022, and it identifies four gaps that limit comparability between studies:

1. No validated field potential duration (FPD) rate correction for hiPSC-CMs was found.
2. Shared, validated waveform morphology classification criteria were not identified.
3. The transfer of 2D-calibrated analysis frameworks to 3D models and ultra-high-density platforms proceeds empirically.
4. hiPSC-CM maturation status lacks MEA-derived reference values.

- [ ] TODO: update the Markmap screenshot; the current one still shows the old title ("Charting the Field…").

[Markmap view of the paper structure](../pics/posts/llm-wiki_markmap_analysis.png "Markmap view of the paper")
<figcaption><em>The structure of the paper (main.md) as a Markmap mind map.</em></figcaption>

I am honest about the limits in the paper itself, too: the selection of studies is not systematic (it was assembled with AI assistance and citation tracing), and the review was written by a single author without independent screening.

But enough about MEA, this post is about the method. 😊

## The method: three layers and four operations

The repository has three layers:

- `raw/`: the source PDFs. These never change. Well, not exactly true, as I might e.g. highlight some text in these files. 
- `wiki/`: pages maintained by the LLM: one summary page per paper, concept pages, a page for the gaps in the literature, plus `index.md`, `log.md` and `references.md`.
- `main.md`: the paper itself. This is the single source of truth.

On top of these, `AGENTS.md` tells the agent how to work (`CLAUDE.md` only points to it), `skills/` holds reusable instructions, and `llm-wiki.md` explains the method. Next to them, `docs/` holds supporting material such as `claims-by-source.md` (every claim in the paper listed by its source) and the search documentation, and `check.py` runs structural checks.

I ask the agent to do four operations:

- **Ingest**: PDF → summary page, wiki updates and a reference entry.
- **Query**: a question → an answer from the wiki, with sources.
- **Draft**: write or rewrite a section of `main.md`.
- **Lint**: a health check: outdated claims, orphan pages, unsupported claims.

- [ ] TODO: workflow diagram: `raw/` → ingest → `wiki/` → draft → `main.md`, with lint going back to the wiki, and `AGENTS.md` + scripts underneath. (Same picture could be used for LinkedIn, see linkedin_draft.md.)

My tools were VS Code, [Obsidian](https://obsidian.md/) or [Foam](https://foambubble.github.io/foam/) for linking and the graph view, and Claude Code as the agent.

[Graph view of the wiki in Obsidian](../pics/posts/llm-wiki_graph_view_wiki_exclude_index.png "Graph view of the wiki")
<figcaption><em>Graph view of the wiki in Obsidian. Red nodes are wiki pages (papers and concepts), green ones are tags. The filter <code>path:wiki -index.md</code> leaves the index out, because otherwise everything links to it.</em></figcaption>

## The workflow in practice

Looking back, a sensible order of work would be this:

1. **Vibe-researching first.** Bounce ideas, get a rough first version, and search for sources both with the agent and by yourself (recommended!).
2. **Catch mistakes sooner, not later**, and save time, nerves and some money too! Once there is a rough version, read `main.md` yourself and fix the errors. Update (by yourself or by your agent) `wiki/` pages if needed. Save new additions for the next round. Go through `claims-by-source.md` early, when there are still only a few claims to check. Rem
3. **Additions.** New ideas, new sources, new sections.
4. **Grinding.** Read the final `main.md` through, update the claims after it, and check every claim against its source one by one. DETAILS DO MATTER in science.
5. **Finishing touches.** Highlights, references, figure captions and abbreviations (and a possible choice of journal).

- [ ] TODO: check the order against `wiki/log.md` in the paper repo, which is a ready-made timeline of what was actually done. Maybe add one concrete example: one paper, its summary page, and how it ends up as a citation in `main.md` (or a paragraph where `[CITATION NEEDED]` is replaced by a real citation).

### The wiki structure pays off every time

Every time the agent did something, the structure of the wiki helped. It remembered to update not only `main.md` but also the log, the index and the other related files. One change in the paper often touches several of them: the paragraph in `main.md`, the paper's wiki page, `claims-by-source.md` and the log. The agent made all of them in one go and reported what it changed. Then I reviewed the diff before committing.

[Agent's report after updating several files](../pics/posts/llm-wiki_loop_work.png "Agent's report")
<figcaption><em>The agent's report after one change: main.md, the wiki page of the source and the claims list were all updated, and check.py gives 0 errors.</em></figcaption>

[Staged changes and the diff in VS Code](../pics/posts/llm-wiki_loop_work2.png "Staged changes in VS Code")
<figcaption><em>The same change in VS Code: four files staged, the diff of main.md, and the suggested commit message.</em></figcaption>

Every report also ended with a decent commit message suggestion, for example "*reword the Declarations sentence about colleagues to name the CoEBoC collaboration*". I did not automate committing, because I want to check every change myself.

### Giving a new chat a well-scoped task

A lot of the work happened in fresh chats, each with one narrow task. The prompt matters more than I expected. Here is the prompt for a literature search on one gap in the review (translated from Finnish and shortened):

- [ ] TODO: check the translation.

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

Scripts are still worth it for the boring parts. For example, abbreviations are easy to leave to the very end: once the text is otherwise ready, a script (`check_abbreviations.py`) lists what is missing, and the agent runs it and fixes the list until nothing is missing.

### Examples from this paper

**A: wiki pages contradicted their sources.** Several wiki pages (e.g. Ismaili, Matsuda, Hwang, Kabanov) contained claims that the source itself did not support. These were found only when I compared the source text and the claims line by line. This is the risk of an LLM wiki in a nutshell: the wiki looks tidy and confident, and the error is invisible until you go back to the PDF.

**B: an invented method sentence.** `main.md` claimed a "*targeted search of PubMed/MEDLINE, bioRxiv and Scopus (2 July 2026)*", but there was no record of such a search; it had been the AI's own web search. It sounded entirely plausible. I replaced it with a documented search (`docs/maturation-mea-search.md`, using the prompt shown above), which also found two relevant sources (Li 2025, Lin 2023). Other B-type errors: the word "longitudinal" in the very first draft, and an invented reference "Galli et al. 2024".

**C: a patch fix made a sentence contradict itself.** The opening sentence of the section on open analysis pipelines said that open pipelines had appeared after 2022, and the end of the same sentence said the opposite: "*open tools such as MultiElec and CardioMDA already existed before 2022*". The end had been added as a correction three days earlier, because both Lee et al. (2024, Table 3) and Dunham et al. (2022, p. 2) say that open tools existed before. The beginning was never changed to match. The automatic checks did not notice; I found it myself while reading. According to the sources, what is new after 2022 is not openness but new open tools for new types of data: CardioMEA for HD-MEA data (Lee) and PhysioMEA for cardiac organoids (Weiser-Bitoun).

[Heading and paragraph rewritten after the contradiction was found](../pics/posts/llm-wiki_human-in-the-loop-tarkeys.png "Human in the loop")
<figcaption><em>Human in the loop: the contradictory opening (red) and the rewritten heading and paragraph (green).</em></figcaption>

Since then the agent has this rule: "*When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.*"

## Finding sources: don't rely on one search

The agent's searches alone were not enough. Good old googling, Google Scholar, and going through the references of each source and the papers that cite it found things the agent did not. A second LLM (e.g. Gemini) is another way to widen the search.

<!-- [CLAUDE] seuraava kappale -->
A documented search also produced new findings, not just confirmation. Once the queries, hit counts and citation chains were recorded, the search found two sources (Li 2025, Lin 2023) that sharpened the paper's gap claim, and one connection (Scheurer 2025's maturity classes are based on Li 2025) that the earlier web search had not revealed.

- [ ] TODO (optional): the confusingly large difference between Claude Code and Gemini notebook. Decide whether it is worth a paragraph.

## Which model for which step?

<!-- Pohjana Clauden ehdotus 3.11. Mallinimet vanhenevat nopeasti; tarkista ne julkaisuhetkellä. -->

Not every step needs the strongest (and most expensive) model, but not everything should run on a lighter one either. My rule of thumb: **use a strong model where an error would go unnoticed**, that is, reading the sources and wording the claims, and a lighter model for the bookkeeping. This is my own judgment; I have not measured the models for this work.

| Step | Model |
|---|---|
| Ingest: reading PDFs (text, figures, tables) into summary pages | Strong model. This is where an error starts spreading to the whole wiki. |
| Bookkeeping: index, log, references, `check.py` | A lighter model is enough, e.g. Sonnet 5.5 with medium effort. |
| Drafting and writing `main.md` | Strong model. Whether a claim is correct often depends on how strongly it is worded and how it is hedged. |
| Checking claims against the sources | Strong model, and a human (me) last. |
| Decisions and `/grill-paper` | Strong model. It has to look up the facts from the wiki and the sources itself, while I make the decisions. |
| Final review | A different model family. |

Checking the claims is a good example of how the choice depends on who does what:

- **I read the sources, the agent fixes.** The agent edits the marked spots in `main.md`, the claims list and the log, and runs the scripts. This is routine work, and Sonnet with medium effort handles it.
- **The agent reads the PDFs and compares them with the claims.** Here the errors are subtle: a number, a hedge ("rarely", "may") or the wrong figure. So I would use Opus 5.5 or Fable 5.1, or Sonnet with a higher effort level. The repo has had invented references, so this is where paying for quality pays off.

A review by another model family is useful because it is independent: re-checking with the same model easily repeats the same error. I ran the final review with Gemini; a third check with an OpenAI model would be an optional extra.

And still, my own read-through comes last. Switching models does not replace it.

## What else worked

- **A critical assessment page.** A wiki page where the agent critically assesses claims, including my own earlier claims, was a good addition to the LLM wiki. It also gets corrected when the details are wrong, for example which figure in a source actually shows what.

  [Critical assessment page being corrected](../pics/posts/llm-wiki_critical_assignment.png "Critical assessment page")
  <figcaption><em>A correction on the critical assessment page: "Figs. 5–6" became "Fig. 5A–C; Fig. 6 is a simulation".</em></figcaption>

- **Useful suggestions from the agent.** For example: "*When you fetch the PDFs, also get the supplementary file for Li 2025. Supplementary Table 3 has the numeric values for spike amplitude and slope.*"
- **Memory between sessions.** Claude's memory files kept things like commit message style and project conventions across chats.

  [Claude's memory files](../pics/posts/llm-wiki_claude_memory.png "Claude's memory files")
  <figcaption><em>Claude Code's memory folder for the project: one file per remembered fact, and MEMORY.md as the index.</em></figcaption>

<!-- [CLAUDE] seuraava kohta -->
- **"Grilling" decisions before acting.** Choosing which sources to include was in practice done by grilling: the agent proposed a choice with its reasoning, I iterated and decided, and only then was it documented. This became a `/grill-paper` skill in the repo (adapted from Matt Pocock's `grilling` skill, MIT): a round-by-round interview where the agent looks up the facts from the wiki itself and the decisions stay with the researcher. I took it into use late; used from the start, it would have saved many correction rounds.

## Co-writing without git skills

<!-- HUOM: Word-ingestiä ei ole vielä kokeiltu tässä projektissa. Kirjoitettu mahdollisuutena. Jos ehdit testata (esim. yksi kappale Wordilla → agentti ingestoi), muuta kokemukseksi. -->

The single source of truth is `main.md` under version control, but a co-author does not need to know git, or even markdown. I see three levels:

1. **Write in Word (or in an email).** The agent ingests the text into a named paragraph or section, shows the changes as a diff, and updates the log, the claims list and the references when needed. The main author approves.
2. **Edit the markdown directly.** It is enough to be willing to read and write text files.
3. **Use the agent and git yourself.** After the initial setup, the agent handles branches, commits and conflicts.

Why this works: version control keeps every change and its author visible, and the rules in `AGENTS.md` (sources, references, logs, `check.py`) apply to the co-author's text too. So the quality does not depend on the tool the text was written with.

To be honest about the limits: tracked changes and comments in Word have to be interpreted. If two people edit the same paragraph, the decision stays with a human. The agent should not merge texts silently but show the differences. And the Word text has to be ingested against the current `main.md`, not an old version.

I have not tried the Word route in this project yet, so take this as a possibility, not a report. 😉

## What I would do differently

- Check the sources right at the start, at ingest, before anything is built on them.
- Go through `claims-by-source.md` early, while it is still short.
- Search for sources in several ways from the beginning, not only through the agent.
- Use grilling for decisions from day one. <!-- [CLAUDE] -->

## Practical tips

- Use Obsidian or Foam for linking and the graph view.
- Put the working rules in `AGENTS.md`, for example "never invent citations". Keep `CLAUDE.md` as a pointer to it, so other agents can use the same rules.
- Mark unsupported sentences with `[CITATION NEEDED]` instead of letting the agent guess a source.
- Keep a claims-by-source list and check it against the sources, not against the wiki.
- Use scripts like `check.py` for structural checks, but remember that they do not check content.
- Run a lint round (a health check of the wiki: contradictions, stale claims, orphan pages, unsupported claims in `main.md`) after every few ingests, findings only, and decide yourself what gets fixed. Lint checks the wiki against itself, not against the sources, so it does not replace reading the PDFs.
- Give each new chat one narrow task, the files to read first, and what it may not touch.
- Use a strong model for reading sources and wording claims, a lighter one for bookkeeping, and another model family for the final review.

## Where the paper is published

<!-- [CLAUDE] koko osio -->
I chose Zenodo instead of Preprints.org because the paper is not going to a journal. For a hobby project, Europe PMC visibility did not outweigh the uncertainty of the screening (affiliation, AI policy). Findability comes from posts like this one and from the repository.

## Summary

AI agents make writing faster, but at the same time they make a high-quality data foundation, good data management and the right architecture decisions even more important. In an LLM wiki, the sources are the data, the three layers and `AGENTS.md` are the architecture, and the scripts and the claims list are the data management. An error in the data does not stay in one place; it spreads. So check the sources early, and read everything yourself at the end. 🤓

📝 Happy (careful) writing! 😊

## Try it yourself

- Template for a personal wiki: [llm-wiki-template](https://github.com/AnaHill/llm-wiki-template)
- Template for researchers: [llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template)
- The paper repository: [MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki)
- The paper on Zenodo: TODO <!-- - [ ] TODO: Zenodo DOI -->

---
<a href="{{ site.baseurl }}/blog/" style="color:green;"><strong>⬅ To My Blog list</strong></a><br>
<a href="{{ site.baseurl }}/" style="color:green"><strong>⬅ To My Main Page</strong></a>
