---
layout: default
title: "Writing an academic review with an LLM wiki: what worked and what didn't"
date: 2026-11-10
categories: [llm]
tags: [LLM wiki, agent harness, academic writing, Claude Code, data quality]
---

{% include blog-meta.html %}

<!--
LUONNOS. Siirto julkaisuun: ks. notes_OHJEET.md.
- [ ] TODO = puuttuu sisältöä tai tarkistettava ennen julkaisua.
- [CLAUDE] = kohta perustuu Clauden ehdotuksiin (lessons-osio "Lisäykset 31.10."), ei omiin muistiinpanoihin. Tarkista tai poista.
- Kuvat ovat luonnosvaiheessa pelkkinä linkkeinä. Julkaisussa lisää jokaisen eteen ! (figcaption on jo valmiina).
-->

> 😎 Nerd your day! 🤓

**DISCLAIMER**: Be responsible and avoid AI slop. "*Vibe-researching*" is educational (and fun!🤓), but in science, **DETAILS**. **DO**. **MATTER**. A paper whose claims are 90% correct is not a good result. I have personally gone through every source and especially every claim in the paper, and I have done my best (with limited free time) to fix errors and inaccuracies.

In this post, I describe how I wrote a scientific review paper with an AI agent and an **LLM wiki**, and what I learned along the way. Spoiler: the biggest lesson was not about AI at all but about **data quality**. 🤓

- 📄 The paper: [Zenodo](TODO) <!-- - [ ] TODO: Zenodo DOI -->
- 💻 Everything behind it (sources, wiki, logs, scripts): [AnaHill/MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki)
- 🧰 Template to try it yourself: [llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template)

## Why an LLM wiki?

I wanted to write a narrative review on how the analysis of cardiomyocyte microelectrode array (MEA) recordings has developed since 2022. A literature review is mostly bookkeeping: which papers have I read, what exactly did each of them show, and which of my sentences are actually supported by a source. That bookkeeping is where I wanted help from my 🤖 friend, without handing over the thinking.

- [ ] TODO: 1–2 sentences on why an LLM wiki in particular, and not just chatting with an LLM or using a reference manager. Idea: a chat forgets, a reference manager does not know what the papers say; the wiki keeps both, as plain markdown under version control.

## The paper in brief

The paper is called *Four Methodological Gaps in Field Potential Analysis of hiPSC-Cardiomyocytes: A Narrative Review of Multielectrode Array Studies Since 2022*. It reviews field potential analysis methods for MEA recordings of human induced pluripotent stem cell-derived cardiomyocytes (hiPSC-CMs) since 2022, and in the studies examined it identifies four methodological gaps:

1. No validated field potential duration (FPD) rate correction for hiPSC-CMs was found.
2. Shared, validated criteria for classifying waveform morphology, and for choosing the fiducial definitions valid within each class, were not identified.
3. Dedicated validation of 2D-calibrated analysis frameworks was not found for either 3D tissues or spatially resolved recordings.
4. hiPSC-CM maturation status lacks MEA-derived reference values.

<!-- Otsikko ja aukot päivitetty 22.11. main.md:n mukaisiksi (Conclusion). Tarkista uudelleen, jos ne vielä muuttuvat. -->

The title went through several versions. The last change made it weaker on purpose: the earlier one claimed that the gaps *limit* comparability, which was the strongest statement in the paper while the text itself only calls it plausible.

I am honest about the limits in the paper itself, too: the selection of studies is not systematic (it was assembled with AI assistance and citation tracing), and the review was written by a single author without independent screening.

But enough about MEA, this post is about the method. 😊

## The method: three layers and four operations

The repository has three layers:

- `raw/`: the source PDFs. These never change. Well, not exactly true, as I might e.g. highlight some text in these files. 
- `wiki/`: pages maintained by the LLM: one summary page per paper, concept pages, a page for the gaps in the literature, plus `index.md`, `log.md` and `references.md`.
- `main.md`: the paper itself. This is the single source of truth.

On top of these, `AGENTS.md` tells the agent how to work (`CLAUDE.md` only points to it), `.claude/skills/` holds two skills that load only when I call them (`/grill-paper` and `/grinding`, more on both below), and `llm-wiki.md` explains the method. Next to them, `docs/` holds supporting material such as `claims-by-source.md` (every claim in the paper listed by its source) and the search documentation, and seven small scripts do the mechanical work: `check.py` (references, DOIs, links), `claim_quotes.py` (copies the current sentences of `main.md` under each claim), `check_abbreviations.py`, `render_pdf_pages.py` (PDF text and figures for the agent), `figures.py` and `export.py` (rendered figures and the build copy for the PDF), and `rotate_log.py` (keeps the log short enough to read).

I ask the agent to do four operations:

- **Ingest**: PDF → summary page, wiki updates and a reference entry.
- **Query**: a question → an answer from the wiki, with sources.
- **Draft**: write or rewrite a section of `main.md`.
- **Lint**: a health check: outdated claims, orphan pages, unsupported claims.

- [ ] TODO: workflow diagram: `raw/` → ingest → `wiki/` → draft → `main.md`, with lint going back to the wiki, and `AGENTS.md` + scripts underneath. (Same picture could be used for LinkedIn, see linkedin_draft.md.)

My tools were VS Code, [Obsidian](https://obsidian.md/) or [Foam](https://foambubble.github.io/foam/) for linking and the graph view, and Claude Code as the agent.

<!-- [CLAUDE 23.11.] Kuva vaihdettu samaksi kuin repon README:ssä; kopioitu pics/posts/-kansioon. -->

[Graph view of the wiki in Obsidian](../pics/posts/llm-wiki_graph_view_fpd-end-conventions.png "Graph view of the wiki")
<figcaption><em>The wiki in Obsidian's graph view: paper pages in blue, concept and method pages in orange, tags in green. Highlighted is the page that sets side by side how each source defines the end of the field potential duration, one of the four gaps of the paper. It holds no new evidence; it gathers what the paper pages record. A reference manager stores the sources; the wiki also stores how they relate.</em></figcaption>

## The harness: what surrounds the agent

"Agent harness" is a hot term right now, and for once the buzzword fits. A harness is everything around the model: the instructions it reads, the tools it can call, what it is allowed to touch, the checks that run after it acts, the procedures it loads on demand, what it remembers between sessions, how its output is evaluated, and the trace it leaves. Looking back, most of my work in this project was not prompting. It was building the harness, one piece at a time.

Without planning it that way, the result is close to what Anthropic's article [Building agents: when to fold subagents into your main agent loop](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop) recommends: one agent in one context window instead of an orchestrator handing work to specialist subagents, with "*one clear system prompt, 4-5 thin data tools, and firm output guardrails*".

What made the harness grow was not a design document but things going wrong:

| Part of the harness | In this repository | Added because… |
|---|---|---|
| Instructions | `AGENTS.md` (`CLAUDE.md` only points to it) | invented sources reached the draft (a "Galli et al. 2024" that does not exist, fabricated author lists), so "never invent citations" became an explicit rule |
| Tools | seven small scripts, e.g. `check.py`, `claim_quotes.py`, `render_pdf_pages.py` | references, links and DOIs drift silently; and only the figures of one study showed that its key analysis used rat cells, not human ones, which the text-based summary had obscured, so the agent now renders PDF pages and looks at the figures |
| Permissions | `.claude/settings.json`: no edits to my own `notes.md`, ask before any write to `raw/` | a rule in the prompt works as long as the agent remembers it; a rule in the settings works every time. A first, stricter version denied all writes to `raw/` and blocked legitimate file renames, so it became "ask" |
| Hooks | after every edit of `main.md`: abbreviation check, consistency check, and whether the claims checklist is still in step | a script that fails by producing nothing reads as done; now the agent sees the result at the moment of the edit |
| Skills | `/grinding` and `/grill-paper`, loaded only when called | checking one source claim by claim, and grilling a decision before acting, are long procedures that should not crowd every session |
| Memory | Claude's memory files | conventions such as the commit message style should not need repeating in every new session |
| Evaluation | `claims-by-source.md`: every claim listed under its source and ticked against the PDF; a separate register of my own inferences | the scripts check structure, not truth |
| Trace | `wiki/log.md` | every change and decision with its reason, which is also how I could write this table |

**Each part of the harness exists because something went wrong without it, and the log says what.** I have not measured whether the error rate fell as the harness grew, so I will not claim it. What I can show is the failure behind each part, and parts catching the next case. Two small examples from the last day: right after I added a citation to the paper, the hook reported that the claims checklist had no entry for it yet; and a new check for the register of my own inferences found, on its first run, three entries still quoting wordings that had since changed in the paper.

<!-- [CLAUDE 22.11.] -->
Silent failures were the recurring theme. My favourite: one invisible NUL byte, written into the log a month earlier, made `grep` treat the whole log as a binary file and return nothing at all. Nothing complained; searches just came back empty. A tool that fails by saying nothing looks exactly like a tool that found nothing.

The pattern I ended up with: **a rule in `AGENTS.md` and a mechanical check in a script, together.** A rule alone gets forgotten, and a script alone cannot judge what makes a good tag or link.

## The workflow in practice

Looking back, a sensible order of work would be this:

1. **Vibe-researching first.** Bounce ideas, get a rough first version, and search for sources both with the agent and by yourself (recommended!).
2. **Catch mistakes sooner, not later**, and save time, nerves and some money too! Once there is a rough version, read `main.md` yourself and fix the errors. Update (by yourself or by your agent) `wiki/` pages if needed. Save new additions for the next round. Go through `claims-by-source.md` early, when there are still only a few claims to check.
3. **Additions.** New ideas, new sources, new sections.
4. **Grinding.** Read the final `main.md` through, update the claims after it, and check every claim against its source one by one. DETAILS DO MATTER in science. The repo now has a `/grinding <source>` skill for this: the agent reads one source in full and reports a verdict per claim (holds, check, does not hold) with the sentence from `main.md`, the supporting passage and its page, and changes nothing until I ask. The ticking is still mine.
5. **Finishing touches.** Highlights, references, figure captions and abbreviations (and a possible choice of journal).

<!-- [CLAUDE 22.11.] -->
That is the order I would recommend. What actually happened, according to the log, was messier:

- **June–July:** a first draft, and cleaning up the invented references it contained. The first look at figures instead of extracted text caught two misreadings.
- **October:** the consistency script, the claims list and a first verification pass against the sources, which found unsupported statements on every one of the twelve wiki pages it checked. Then new sources and new sections.
- **November:** the harness grew (permissions, hooks, skills), every claim was checked source by source with `/grinding`, two external AI reviews were worked through, and the export was automated. November alone has more log entries than all the months before it.

In other words, I did steps 2 and 4 late and at full size. The `[CITATION NEEDED]` markers did their job, though: four were open at one point, and each was closed by finding and reading a real source or by deleting the sentence, never by letting the agent guess.

- [ ] TODO (optional): one concrete example: one paper, its summary page, and how it ends up as a citation in `main.md`.

### The wiki structure pays off every time

Every time the agent did something, the structure of the wiki helped. It remembered to update not only `main.md` but also the log, the index and the other related files. One change in the paper often touches several of them: the paragraph in `main.md`, the paper's wiki page, `claims-by-source.md` and the log. The agent made all of them in one go and reported what it changed. Then I reviewed the diff before committing.

[Agent's report after updating several files](../pics/posts/llm-wiki_loop_work.png "Agent's report")
<figcaption><em>The agent's report (in Finnish) after one change: main.md, the wiki page of the source and the claims list were all updated, and check.py gives 0 errors.</em></figcaption>

[Staged changes and the diff in VS Code](../pics/posts/llm-wiki_loop_work2.png "Staged changes in VS Code")
<figcaption><em>The same change in VS Code: four files staged, the diff of main.md, and the suggested commit message.</em></figcaption>

### Knowledge has to flow back from the paper to the wiki

Late in the project I noticed a gap in the method itself. The four operations move knowledge in one direction: ingest takes a source into the wiki, and draft takes the wiki into `main.md`. But writing the paper creates knowledge too. When `main.md` compares two sources in one sentence, gathers a theme into a section or finds a good word for a concept, none of that reached the wiki. A check found ten pairs of sources that the paper compared but whose wiki pages did not link to each other, three paper sections (open platforms, 3D models, machine learning) without a wiki page of their own, and 53 tags, 34 of them used only once. The graph view showed the result: a scatter of one-off tag nodes instead of themes.

The fix followed the rule-plus-check pattern above:

- **A rule:** the Draft operation in `AGENTS.md` got a "write back to the wiki" step. A connection made in `main.md` goes into the wiki too, as a link with a short reason ("T-wave peak versus APD90"), a recurring theme gets its own concept page, and a new tag enters a fixed vocabulary only if it fits at least three pages.
- **A check:** `check.py` now lists sources that `main.md` cites in one sentence but the wiki does not connect, and tags outside the vocabulary. Because the hook runs it after every edit of `main.md`, a missing connection shows up the moment it is written.

So creating knowledge or connections in `main.md` now forces the wiki to keep up, and the wiki stays a map of the paper rather than of the sources alone.

- [ ] TODO [CLAUDE 23.11.]: ota "after"-kuva samoilla ehdoilla kuin before-kuva (ohje: repon `docs/images/README.md`, "Before/after pair"), tallenna nimellä `llm-wiki_graph_view_after_tag_rework.png`, ja tarkista kuvatekstin tagiesimerkit uudesta kuvasta.

[Graph view before the tag rework](../pics/posts/llm-wiki_graph_view_wiki_exclude_index.png "Graph view before the tag rework")
<figcaption><em>Before: the wiki in Obsidian's graph view, with the tags as green nodes. Many of them were used once (<code>#brv</code>, <code>#video</code>, <code>#impedance</code>, <code>#chronic-assay</code>), a scatter of words rather than themes. The filter <code>path:wiki -index.md</code> leaves the index out, because otherwise everything links to it.</em></figcaption>

[Graph view after the tag rework](../pics/posts/llm-wiki_graph_view_after_tag_rework.png "Graph view after the tag rework")
<figcaption><em>After: the same view with the tags from a fixed vocabulary that follows the sections of the paper (<code>#fiducial-definition</code>, <code>#rate-correction</code>, <code>#maturation</code> …), paper pages in blue and concept pages in orange.</em></figcaption>

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

## Human in the loop, by design

The agent does the bookkeeping; the judgement stays with me. That split is built into the files rather than left to good intentions:

- **Every claim has a checkbox.** `claims-by-source.md` lists over 200 claims under more than 30 sources, each with the current sentence of `main.md` under it. I tick a claim only after reading the passage in the source, and a source gets a ✅ in its heading once all its claims are ticked. All of them are now ticked. <!-- luvut pyöristetty 22.11. (tarkat: 205 väitettä, 31 lähdettä, rekisterissä 39 kohtaa) -->
- **My own inferences are kept apart.** Whatever the paper says that is my inference rather than a source's finding goes into a separate register in the same file (nearly 40 items in the end), each with the sources it builds on and how far they support it, so it is visible which sentences rest on a source and which on me. Each item has a **Support** value from a fixed list (`sourced`, `thin`, `inference`, `opinion`, `none`, `inherited`), and a script warns about any other value, because two new values had once crept in without a definition.
- **The agent proposes, I decide.** When I asked it to shorten over-detailed passages, it listed candidates with a recommendation for each; I accepted most and rejected one. When I wanted to reinterpret another group's published figures (I suspected their signals were shown upside down), it laid out the arguments for and against and suggested keeping only a neutral sentence in the paper. I agreed, and the full reasoning went onto a separate wiki page.
- **Checking goes both ways.** I check the agent against the sources, and it checks me: looking up my own tool's GitHub repository showed that the paper had the wrong programming language and release year for it, and that the repository had no licence, which I then added.

This is also why the agent never commits: every change passes through my diff review.

<!-- [CLAUDE 22.11.] -->
But a diff review only works if the diff can be read. The claims list used to store a `main.md` line number after every quoted sentence, so adding one paragraph to the paper renumbered hundreds of lines. Over twelve commits, 91 % of the changed lines in that file were line numbers alone, and a real problem (a highlight still claiming something the text had withdrawn, see error D below) slipped through in exactly such a diff. The line numbers are gone from the file; the script prints them on demand. **Human in the loop needs a diff a human can actually read.**

## The main lesson: data quality

If I did this again, I would check the sources, and the decisions made from them, much more carefully right at the start. Even though vibe-researching is fun, going through the sources as early as possible pays off in the end. The reason is how errors spread in an LLM wiki.

### How a wrong claim spreads

I found four kinds of errors, and each one starts from a different place:

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

Error D, a summary outlives its claim:
a claim in the body is corrected -> the title, highlights and abstract still say the old thing
```

The lesson: **the earlier an error is born, the more places it is copied to.** So the check belongs in the ingest step, not at the end when reading `main.md`. Error D runs the other way: a correction travels down to the claims list but not up to the summaries, which restate the claim in their own words.

### What catches what

| Check | Catches | Misses |
|---|---|---|
| `check.py` | structural errors: missing references, DOI mismatches, broken links; connections made in `main.md` but missing from the wiki; tags outside the vocabulary | content, so A, B and C all pass |
| Hook after every edit of `main.md` | missing abbreviations and broken references, immediately rather than at the end | content |
| `claims-by-source.md` + reading the source | A and B, when the claim is checked against the source and not against the wiki page | C |
| `/grinding` (the agent reads the whole source) | A and B claim by claim, with page references, as a first pass | C, and anything the agent misreads itself |
| Register quote check (`claim_quotes.py`) | D, where the register quotes the summary's wording | D in a summary nobody quoted |
| A human reading the whole text | C, D and contradictions between sections | |

Scripts are still worth it for the boring parts. For example, abbreviations are easy to leave to the very end: once the text is otherwise ready, a script (`check_abbreviations.py`) lists what is missing, and the agent runs it and fixes the list until nothing is missing.

### Examples from this paper

**A: wiki pages contradicted their sources.** Several wiki pages (e.g. Ismaili, Matsuda, Hwang, Kabanov) contained claims that the source itself did not support. These were found only when I compared the source text and the claims line by line. This is the risk of an LLM wiki in a nutshell: the wiki looks tidy and confident, and the error is invisible until you go back to the PDF. In the first systematic pass, every one of the twelve wiki pages checked had at least one statement that went beyond its source. One page said a paper discussed MEA recordings, field potential duration and the Fridericia correction; the paper mentions none of them.

**B: an invented method sentence.** `main.md` claimed a "*targeted search of PubMed/MEDLINE, bioRxiv and Scopus (2 July 2026)*", but there was no record of such a search; it had been the AI's own web search. It sounded entirely plausible. I replaced it with a documented search (`docs/maturation-mea-search.md`, using the prompt shown above), which also found two relevant sources (Li 2025, Lin 2023). Other B-type errors: the word "longitudinal" in the very first draft, and an invented reference "Galli et al. 2024".

**C: a patch fix made a sentence contradict itself.** The opening sentence of the section on open analysis pipelines said that open pipelines had appeared after 2022, and the end of the same sentence said the opposite: "*open tools such as MultiElec and CardioMDA already existed before 2022*". The end had been added as a correction three days earlier, because both Lee et al. (2024, Table 3) and Dunham et al. (2022, p. 2) say that open tools existed before. The beginning was never changed to match. The automatic checks did not notice; I found it myself while reading. According to the sources, what is new after 2022 is not openness but new open tools for new types of data: CardioMEA for HD-MEA data (Lee) and PhysioMEA for cardiac organoids (Weiser-Bitoun).

[Heading and paragraph rewritten after the contradiction was found](../pics/posts/llm-wiki_human-in-the-loop.png "Human in the loop")
<figcaption><em>Human in the loop: the contradictory opening (red) and the rewritten heading and paragraph (green).</em></figcaption>

Since then the agent has this rule: "*When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.*"

<!-- [CLAUDE 22.11.] -->
**D: the title was the strongest claim in the paper.** After weeks of narrowing claims to what the sources support, the title still said that four gaps *limit* comparability, while the text only calls that plausible. A highlight had the same problem: the rate-correction section had just been reworded after an AI review, and the highlight above it still asserted what the section no longer claimed. No script saw either; both were found by reading. Now the register quotes the highlights, and a script reports a quoted wording that no longer occurs in the paper.

**What the claim-by-claim check changed.** The value of ticking 200 boxes is not the ticks but what did not survive them. A sentence saying that no study measured how much analysis methods affect results became the narrower and checkable "none applies two conventions to the same recordings". A tool described as built for 3D preparations turned out to rest on the word "organoid" alone; its source never calls the construct three-dimensional. And a sentence beginning "Two of them" did not survive counting.

## Finding sources: don't rely on one search

The agent's searches alone were not enough. Good old googling, Google Scholar, and going through the references of each source and the papers that cite it found things the agent did not. A second LLM (e.g. Gemini) is another way to widen the search.

<!-- [CLAUDE] seuraava kappale -->
A documented search also produced new findings, not just confirmation. Once the queries, hit counts and citation chains were recorded, the search found two sources (Li 2025, Lin 2023) that sharpened the paper's gap claim, and one connection (Scheurer 2025's maturity classes are based on Li 2025) that the earlier web search had not revealed.

<!-- [CLAUDE 22.11.] -->
**An absence claim is only as strong as the search behind it.** The paper's four gaps all say that something was *not found*. Only one of them has a documented database search behind it, so the other three are worded "in the studies examined", a limit of my sample rather than a claim about the field. The one with the search gets to say "A PubMed search found no …" in the highlights, and that line names the database because "a documented search" only asserts that documentation exists somewhere.

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

A review by another model family is useful because it is independent: re-checking with the same model easily repeats the same error. I ran two external reviews, one with ChatGPT and one with Google's NotebookLM (Gemini), each given only the paper and a short brief.

<!-- [CLAUDE 22.11.] -->
The brief mattered: it listed what the paper already admits about itself (non-systematic selection, single author, my own framework), so the reviewers did not spend their findings repeating the limitations section, and it required a DOI for any suggested source. Two lessons from working through the findings:

- **An abstract is not a source, and neither is an AI's reading of one.** A reviewer suggested two new papers. I read the one I could get in full: its abstract says the signals were "validated by calcium imaging", but the full text compares whole organoids, not electrode by electrode. The other paper stayed out, because I could read only its abstract.
- **When two reviews push the same way, watch for over-hedging.** Both said the gaps were overdrawn. Some fixes were right, but the gaps were already scoped to "the studies examined" in most places, and making them weaker than the evidence would have been an error too. I accepted some findings, declined others, and wrote down why for each.

And still, my own read-through comes last. Switching models does not replace it.

## What else worked

- **A critical assessment page.** A wiki page where the agent critically assesses claims, including my own earlier claims, was a good addition to the LLM wiki. It also gets corrected when the details are wrong, for example which figure in a source actually shows what.

  [Critical assessment page being corrected](../pics/posts/llm-wiki_critical_assessment.png "Critical assessment page")
  <figcaption><em>A correction on the critical assessment page: "Figs. 5–6" became "Fig. 5A–C; Fig. 6 is a simulation".</em></figcaption>

<!-- [CLAUDE 22.11.] -->
- **Reading the supplements, and recording the sources' own errors.** Supplementary files changed things more than once: in one paper, the ± values in the main text matched, for most groups, neither the standard deviation nor the standard error of the per-sample data in its supplement. The sources had their own slips too (a concentration given as 30 nM in one place and 100 nM in another, an error figure given three different ways). The wiki records these as found rather than smoothing them over, so a claim in the paper never quietly picks one of two conflicting values.
- **Useful suggestions from the agent.** For example: "*When you fetch the PDFs, also get the supplementary file for Li 2025. Supplementary Table 3 has the numeric values for spike amplitude and slope.*"
- **Memory between sessions, with a catch.** Claude's memory files kept things like commit message style and project conventions across chats. But a new chat loads only the index, `MEMORY.md`, one line per memory; the file behind a line is read only when the agent thinks it is relevant. My commit-style rule said "one line, no `Co-Authored-By`" in the file, while its index line said only "lowercase, present tense". Claude Code's own instructions, on the other hand, tell the agent to add a `Co-Authored-By` line to every commit. So in new chats the proposed message kept coming back with a body paragraph and the trailer, until I asked why. The fix was to put the rule into the index line itself. The lesson is the same as with `AGENTS.md`, one level down: **a memory works only if its one-line summary carries the rule, because the summary is all a new chat is sure to see.** And when a rule must hold every time, a memory is the wrong place for it.

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
- Put the hard rules into the tool settings from the start, not only into `AGENTS.md`.
- Let knowledge flow both ways from day one: whatever the paper connects, the wiki links too, with a fixed tag vocabulary.
- Write memory index lines so that the rule itself is in them, not just its topic.
- After rewording a claim, re-read the title, the highlights and the abstract. <!-- [CLAUDE 22.11.] -->
- Keep generated noise (such as line numbers) out of files that I review as diffs. <!-- [CLAUDE 22.11.] -->

## Practical tips

- Use Obsidian or Foam for linking and the graph view.
- Put the working rules in `AGENTS.md`, for example "never invent citations". Keep `CLAUDE.md` as a pointer to it, so other agents can use the same rules.
- Mark unsupported sentences with `[CITATION NEEDED]` instead of letting the agent guess a source.
- Keep a claims-by-source list and check it against the sources, not against the wiki.
- Use scripts like `check.py` for structural checks, but remember that they do not check content.
- Run a lint round (a health check of the wiki: contradictions, stale claims, orphan pages, unsupported claims in `main.md`) after every few ingests, findings only, and decide yourself what gets fixed. Lint checks the wiki against itself, not against the sources, so it does not replace reading the PDFs.
- Give each new chat one narrow task, the files to read first, and what it may not touch.
- Use a strong model for reading sources and wording claims, a lighter one for bookkeeping, and another model family for the final review.
- Put absolute rules into the tool settings, not only into the prompt: deny edits to the sources, and run the checks automatically with a hook.
- Pair each important rule with a script that checks it. The rule says what to do; the script notices when it was not done.
- When the paper connects sources, write the connection back to the wiki, so the graph shows the paper's themes and not one-off tags.
- Ask for findings first and fixes only after your go-ahead. The agent proposes, you decide.
- Word an absence claim to the size of the search behind it ("in the studies examined" unless you searched). <!-- [CLAUDE 22.11.] -->
- Look at the figures and read the supplements at ingest; text extraction misses what only a figure shows. <!-- [CLAUDE 22.11.] -->

## Where the paper is published

<!-- [CLAUDE] koko osio -->
I chose Zenodo instead of Preprints.org because the paper is not going to a journal. For a hobby project, Europe PMC visibility did not outweigh the uncertainty of the screening (affiliation, AI policy). Findability comes from posts like this one and from the repository.

## Finished or verified?

While I was finishing this, Google Research published [PaperOrchestra](https://github.com/google-research/paper-orchestra) ([arXiv 2604.05018](https://arxiv.org/abs/2604.05018)): five specialised agents (outline, literature review, section writing, refinement and plotting) turn an idea and an experimental log into a LaTeX manuscript, and find the literature themselves through Semantic Scholar. In side-by-side human evaluation it clearly beat other autonomous writers, especially on the literature review. My first reaction was "oh no, did this just make my setup obsolete?" 😅

I don't think so, because it optimises for something else. As far as the README and the abstract describe, there is no step where a human checks the claims against the sources, and the evaluation compares manuscripts with each other, not with the papers they cite. In a review, almost every sentence is a claim about someone else's work, and that is exactly where an agent goes wrong quietly. **Automated pipelines optimise for a finished manuscript; I wanted a verified one.** If authors use AI to write, the burden shifts to making the work checkable: every claim listed with its source, my own inferences kept apart, and the whole process in a public repository. The two could also work together: an automated first draft or wider literature search, then ingest, check and tick as usual.

## Summary

AI agents make writing faster, but at the same time they make a high-quality data foundation, good data management and the right architecture decisions even more important. In an LLM wiki, the sources are the data, the three layers and `AGENTS.md` are the architecture, and the scripts and the claims list are the data management. An error in the data does not stay in one place; it spreads. So check the sources early, and read everything yourself at the end. 🤓

And keep a human in the loop where it matters. The agent can do the bookkeeping, and it does it well, but choosing the sources, deciding what the paper claims and ticking each claim against its source stay with me.

📝 Happy (careful) writing! 😊

## Try it yourself

- Template for a personal wiki: [llm-wiki-template](https://github.com/AnaHill/llm-wiki-template)
- Template for researchers: [llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template)
- The paper repository: [MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki)
- The paper on Zenodo: TODO <!-- - [ ] TODO: Zenodo DOI -->

---
<a href="{{ site.baseurl }}/blog/" style="color:green;"><strong>⬅ To My Blog list</strong></a><br>
<a href="{{ site.baseurl }}/" style="color:green"><strong>⬅ To My Main Page</strong></a>
