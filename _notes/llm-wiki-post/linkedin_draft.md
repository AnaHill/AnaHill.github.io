# LinkedIn-postaus: hahmotelma (2.11.2026)

Kieli: englanti (sama kuin blogissa). Julkaistaan blogin jälkeen. Zenodo-DOI on olemassa (paperi julkaistu 23.11.2026). Pituus: noin 150–250 sanaa, koska LinkedIn näyttää ennen "see more" -katkoa vain 2–3 ensimmäistä riviä.

---
<!-- [CLAUDE 23.11.] "four gaps that limit comparability" → "four methodological gaps" kaikissa versioissa: paperin otsikko heikennettiin tarkoituksella ("limit" oli vahvempi kuin teksti, joka sanoo sen vain uskottavaksi), ja blogi kertoo tämän. -->
<!-- älä poista tätä, sisältää mahdollisia emojia: 👨‍🔬Passionate Hobby Scientist hello! 💡 👨🏼‍🎓 
-->

## Versio A: oppi edellä

Can an AI agent help write a scientific review without producing AI slop?

I tried, applying my day job in data & AI to my old postdoc topic as a hobby scientist. 👨‍🔬 The result is a narrative review of four methodological gaps in MEA analysis of hiPSC-derived cardiomyocytes. I wrote it with an "LLM wiki": the agent summarises every source into a wiki, keeps the reference list and logs in sync, and drafts text. I select the sources, make the decisions and check the claims.

What I learned:
🔹 Check sources at ingest, not at the end. One misread summary spread to five places before I caught it.
🔹 Scripts catch structure (missing references, broken links), and the agent's health checks of the wiki catch contradictions and stale claims. Neither catches a misread source. Only reading the source does that.
🔹 A plausible-sounding sentence can still be wrong. "A targeted search of PubMed…" had no record behind it, so I redid the search properly, and it found two relevant papers.
🔹 Use the strongest model where an error would go unnoticed (reading sources, wording claims), a lighter one for bookkeeping, and another model family for the final check. No model replaces my own read-through.
🔹 Everything is plain markdown under version control: transparent, reproducible, and easy to co-write.

In science, details do matter. A paper that is 90 % correct is not good enough.

📝 Blog post, the whole story: https://anahill.github.io/blog/llm-wiki-and-academic-review.html
📄 The paper (Zenodo, open access): https://doi.org/10.5281/zenodo.24459573
💻 Everything behind it, including sources, wiki and logs: https://github.com/AnaHill/MEA_review_llm_wiki
🧰 Template to try it yourself: https://github.com/AnaHill/llm-wiki-academic-template

#AIinResearch #LLM #OpenScience #ScientificWriting #Cardiology #StemCells #ResearchIntegrity

---

## Versio B: lyhyempi, kysymys edellä

What does it take to write a scientific review with an AI agent and still stand behind every sentence?

I wrote a review on cardiomyocyte MEA analysis using an LLM-maintained wiki. The agent did the bookkeeping. I did the thinking, and I checked every claim against its source.

The biggest lesson: AI makes errors cheap to create and expensive to find. Catch them at the source, early.

📝 Blog: https://anahill.github.io/blog/llm-wiki-and-academic-review.html
📄 Paper: https://doi.org/10.5281/zenodo.24459573
💻 Repo: https://github.com/AnaHill/MEA_review_llm_wiki

#AIinResearch #OpenScience #LLM #ResearchIntegrity

---

## Versio C: konkreettinen tapaus edellä (3.11., noin 170 sanaa)

Erot versioon A: avaus on konkreettinen tapaus eikä kysymys; harrastajatutkijan rooli on toisessa kappaleessa eikä vie ensimmäistä riviä; kerrotaan suoraan, että virhe korjattiin ennen julkaisua; kolme oppia viiden sijaan; tarkistamattomat väitteet ("five places", "easy to co-write") pois; kolme linkkiä ja neljä hashtagia. Templaattilinkki ei ole omana rivinään, joten varmista, että templaatti löytyy repon README:stä.

My AI agent wrote a perfectly plausible methods sentence about a literature search that never happened.

I'm a passionate hobby scientist 👨‍🔬, and I wrote a narrative review on MEA analysis of hiPSC-derived cardiomyocytes with an AI agent and an "LLM wiki": the agent summarises every source into linked notes and keeps references and logs in sync. I choose the sources, make the decisions and check the claims against the original papers.

I caught that sentence before publication, redid the search properly and documented it. The new search found two relevant papers that the first one had missed.

What I learned:
🔹 Check each source when it comes in. One misread summary is copied into the wiki, the draft and finally the abstract.
🔹 Scripts check structure, not truth. Only the source does that.
🔹 Use a strong model where errors hide, and read everything yourself at the end.

In science, details do matter. 90 % correct is not good enough.

📝 Blog, the whole story: https://anahill.github.io/blog/llm-wiki-and-academic-review.html
📄 Paper (Zenodo): https://doi.org/10.5281/zenodo.24459573
💻 Sources, wiki, logs and a template to try it: https://github.com/AnaHill/MEA_review_llm_wiki

#AIinResearch #OpenScience #ResearchIntegrity #ScientificWriting

---

## Versio D (C:n runko, A:n esittely ja B:n ydinlause, 3.11., noin 190 sanaa)

My AI agent wrote a perfectly plausible methods sentence about a literature search that never happened.

I applied my day job in data & AI to my old postdoc topic as a hobby scientist 👨‍🔬 and wrote a narrative review of four methodological gaps in MEA analysis of hiPSC-derived cardiomyocytes. I used an AI agent and an "LLM wiki": the agent summarises every source into linked notes and keeps references and logs in sync. I choose the sources, make the decisions and check every claim against the original papers.

I caught that sentence before publication, redid the search properly and documented it. The new search found two relevant papers that the first one had missed.

The biggest lesson: AI makes errors cheap to create and expensive to find.
🔹 Check each source when it comes in. One misread summary is copied into the wiki, the draft and finally the abstract.
🔹 Scripts check structure, not truth. Only the source does that.
🔹 Use a strong model where errors hide, and read everything yourself at the end.

In science, details do matter. 90 % correct is not good enough.

📝 Blog, the whole story: https://anahill.github.io/blog/llm-wiki-and-academic-review.html
📄 Paper (Zenodo): https://doi.org/10.5281/zenodo.24459573
💻 Sources, wiki, logs and the text: https://github.com/AnaHill/MEA_review_llm_wiki
💻 a template to try it yourself: 
https://github.com/AnaHill/llm-wiki-academic-template

#AIinResearch #OpenScience #ResearchIntegrity #ScientificWriting

---

## Versio E: suositus (D:n runko + human in the loop, 11.11., noin 230 sanaa)

Erot versioon D: toinen kappale sanoo suoraan, mitä agentti tekee ja mitä ihminen; oppilista on otsikoitu human-in-the-loopin kautta ja siinä on väitelista ja asetuksiin kirjatut kovat rajat; ydinlause "AI makes errors cheap to create…" on siirretty loppuun. Väitteiden määrä pyöristetty 22.11. muotoon "200+" (tarkka 205, kaikki rastitettu), jotta se ei vanhene pienistä muutoksista. 22.11.: "Hard rules live in the tooling" -kohta korvattu harness-bulletilla (blogin osio "The harness: what surrounds the agent"), ja hashtag #AIAgents lisätty. Jos teksti on liian pitkä, harness-bulletin voi lyhentää muotoon "Most of the work was building the harness around the agent, not prompting." Lisätty 14.11.: "Knowledge flows both ways" -kohta (wikin paluusuunta main.md:stä, ks. blogin osio "Knowledge has to flow back from the paper to the wiki"); teksti on nyt noin 250 sanaa, joten jos pituus on ongelma, valitse joko tämä tai "Hard rules" -kohta. Lisätty 15.11.: PaperOrchestra-rivi (ks. blogin osio "Finished or verified?"); nyt noin 265 sanaa. Rivi on helppo pudottaa, mutta se antaa postaukselle ajankohtaisen vertailukohdan. Jos julkaisu viivästyy kuukausia, sana "new" kannattaa poistaa.

My AI agent wrote a perfectly plausible methods sentence about a literature search that never happened.

I applied my day job in data & AI to my old postdoc topic as a hobby scientist 👨‍🔬 and wrote a narrative review of four methodological gaps in MEA analysis of hiPSC-derived cardiomyocytes, with an AI agent and an "LLM wiki". The agent does the bookkeeping: it summarises every source into linked notes and keeps references, logs and checks in sync. I stay in the loop wherever judgement is needed: I choose the sources, make the decisions and check every claim against the original paper.

I caught that sentence before publication, redid the search properly and documented it. The new search found two relevant papers that the first one had missed.

What made human-in-the-loop work in practice:
🔹 Every claim in the paper (200+) is listed under its source, and I ticked each one off against the PDF.
🔹 Check each source when it comes in. One misread summary is copied into the wiki, the draft and finally the abstract.
🔹 Most of the work was not prompting but building the harness around the agent: rules, checks that run after every edit, hard permission limits. Each part exists because something went wrong without it.
🔹 Knowledge flows both ways: when the paper connects two sources, the wiki has to learn it too, and a script flags it when it doesn't.
🔹 Scripts check structure, not truth. Only the source, read by a human, does that.

Fully automated pipelines, such as Google's new PaperOrchestra, optimise for a finished manuscript. I wanted a verified one.

AI makes errors cheap to create and expensive to find. In science, details do matter. 90 % correct is not good enough.

📝 Blog, the whole story: https://anahill.github.io/blog/llm-wiki-and-academic-review.html
📄 Paper (Zenodo): https://doi.org/10.5281/zenodo.24459573
💻 Sources, wiki, logs and the text: https://github.com/AnaHill/MEA_review_llm_wiki
🧰 A template to try it yourself: https://github.com/AnaHill/llm-wiki-academic-template

#AIinResearch #AIAgents #HumanInTheLoop #OpenScience #ResearchIntegrity #ScientificWriting

### Vaihtoehtoja versioon E (22.11.)

**Avaus A (nykyinen):** "My AI agent wrote a perfectly plausible methods sentence about a literature search that never happened."

**Avaus B:** "The strongest claim in my paper was its title." Jatko esimerkiksi: "After weeks of checking every claim against its source, the title still promised more than the text could support. No script caught it; reading did." Tämä sopii, jos haluat painottaa tarkistamista enemmän kuin AI:n virhettä. Huom: B:n kanssa toinen kappale ("I caught that sentence…") pitää muotoilla uudelleen tai poistaa, koska se viittaa avauksen A lauseeseen.

**Bulletti, jos haluat vaihtaa jonkin nykyisistä:** "🔹 Summaries drift: after fixing a claim in the text, re-read the title, highlights and abstract. They keep saying the old thing." Ehdokas korvattavaksi: "Check each source when it comes in", joka on blogissa laajemmin.

**Bulletti pääviestistä (23.11.), vaihtoehto jollekin nykyisistä:** "🔹 The LLM wiki pattern says the human curates sources and thinks about what it all means, and the LLM does everything else. "Everything else" was cheap. Checking it was not." Sama ajatus on blogissa osiona "The part that is easy to skip".

## Muistiinpanot postaukseen

- **Linkkien sijainti:** LinkedIn rajoittaa ulkoisten linkkien näkyvyyttä. Vaihtoehto on laittaa linkit ensimmäiseen kommenttiin ja tekstiin "links in the first comment 👇". Päätä itse. Linkit tekstissä ovat suoraviivaisempi ratkaisu, ja ne kertovat avoimuudesta.
- **Avaus on tärkein:** ensimmäinen rivi näkyy ennen katkoa. Kysymys ("Can an AI agent…") tai provokaatio ("90 % correct is not good enough") toimii.
- **Oletus:** kaikki väitteet tarkistetaan lähteitä vasten ennen julkaisua, joten postauksessa voi sanoa "check every claim".
- **Tarkistettavat väitteet ennen julkaisua:**
  - "spread to five places" on tyyppiesimerkki virhetyypistä A. Tarkista, löytyykö oikea luku, tai muotoile yleisemmin ("spread to several places").
  - "Easy to co-write" on toistaiseksi idea, koska Word-ingestiä ei ole kokeiltu. Muotoile "designed for co-writing" tai jätä pois.
  - Lint on kirjoitettu muotoon "health checks of the wiki", koska sana "lint" on LinkedIn-yleisölle jargonia. Blogi selittää sen tarkemmin.
  - Mallivalinta-kohta on harkintaa, ei mittaus (blogissa sanotaan tämä suoraan). Jos versio A on liian pitkä, tämä kohta on helpoin pudottaa, koska blogi kertoo sen tarkemmin.
- **Mainitse yhteistyö?** Jos CoEBoC-kollegat tai muut haluavat näkyä, mainitse heidät postauksessa (@-maininnat vasta luvan kanssa).
- **Lopetus:** kutsu kokeilemaan templaattia tai kysymys yleisölle ("How do you check AI-assisted text in your work?") lisää kommentteja.

---

## Hashtagit ja avainsanat

LinkedIn suosittelee noin 3–5 hashtagia. Valitse yksi kustakin ryhmästä:

| Ryhmä | Vaihtoehdot |
|---|---|
| AI ja menetelmä | #AIinResearch #LLM #GenerativeAI #AIAgents #ClaudeCode |
| Tiede ja avoimuus | #OpenScience #ResearchIntegrity #ScientificWriting #Reproducibility #Preprint |
| Aihe | #Cardiology #StemCells #iPSC #Electrophysiology #CardiacSafety #DrugDiscovery |
| Data ja työkalut | #DataQuality #Markdown #VersionControl #Git |

Avainsanat tekstiin (LinkedIn-haku osuu myös tekstiin): AI-assisted writing, narrative review, LLM wiki, hiPSC-derived cardiomyocytes, multielectrode array (MEA), open science, human in the loop, source verification.

---

## Kuva tai video

<!-- [CLAUDE 27.11.] Valittu kuva lisätty; alla oleva vaihtoehtolista jää taustaksi. -->
**Valittu (27.11.): työnkulun kaavio, LinkedIn-versio** `_notes/pics/posts/llm-wiki_workflow_linkedin.png` (1243×1137, noin 1,1:1; valmis 27.11.). <!-- [CLAUDE 27.11.] mitat päivitetty valmiin kuvan mukaan --> Sama kaavio kuin blogin The method -osiossa (`llm-wiki_workflow.png`), mutta export alaspäin, jotta kuva on lähes neliö ja näkyy syötteessä isompana. Kuva ladataan LinkedIniin käsin: sitä ei siirretä kansioon `pics/posts/`, koska blogi ei käytä sitä.

Alt-teksti LinkedIniin (lisää kuvan latauksen yhteydessä, "Alt text"):

> Workflow diagram. On the left, the human: choose the sources, review the wiki, write and review the paper, and check each claim against the source. On the right, the harness (AGENTS.md, scripts, hooks, skills, log), where the agent ingests the source files into a wiki, drafts the paper (main.md), writes connections back to the wiki and lists 200+ claims by source. The paper is then exported with export.py into the publication (PDF, Zenodo). Headline: Not just 'vibe-researching'! Stop AI slop, use your brain. You check the facts.

Kuva tukee version E bulletteja "Every claim … I ticked each one off against the PDF" ja "Most of the work was … building the harness", joten tekstiin ei tarvitse lisätä kuvan selitystä.

Alkuperäiset vaihtoehdot paremmuusjärjestyksessä (ennen 23.11. päätöstä):

1. **Virheen leviämisen kaavio (oma kuva, suositus).** Kuvassa näkyy, kuinka yksi lähteen väärinluku leviää: raw PDF → wiki-sivu → käsitesivu → index → main.md → abstrakti. Vieressä on, mikä pysäyttää minkäkin: check.py, claims-rekisteri tai ihmisen luenta. Tämä on postauksen ydinviesti visuaalisena, ja se erottuu geneerisistä AI-kuvista. Muoto: neliö (1080×1080) tai pysty (1080×1350), iso fontti, koska kuvaa katsotaan puhelimella.
2. **Kolmen kerroksen arkkitehtuuri:** `raw/` → `wiki/` → `main.md` ja niiden alla AGENTS.md ja skriptit. Selkeä mutta tavallisempi.
3. **Wikin graafinäkymä, yksi sivu korostettuna** (`llm-wiki_graph_view_fpd-end-conventions.png`, sama kuin repon README:ssä ja blogissa, 23.11.). Keskellä menetelmäsivu, joka vertaa, miten lähteet määrittelevät FPD:n lopun, ja sen linkit 14 paperisivulle. Kertoo enemmän kuin vanha korostamaton graafi (`llm-wiki_graph_view_wiki_exclude_index.png`), mutta tarvitsee silti yhden rivin selitystä, esim. "One wiki page that sets side by side how the sources define the same measurement, and the pages it connects. A reference manager stores the sources; the wiki also stores how they relate." (Älä sano "14 sources define": kaikki 14 linkitettyä sivua eivät ole FPD-taulukossa.) Puhelimella solmujen nimet jäävät pieniksi, joten rajaa tiukemmin keskisolmun ympärille. Sopii myös karuselliin.
4. **Karuselli (PDF-dokumenttipostaus), 4–6 sivua:** kansi (kysymys) → menetelmä → virheen leviäminen → mikä pysäyttää mitäkin → opit → linkit. LinkedInissä karusellit saavat usein hyvin näkyvyyttä, mutta ne ovat isompi työ.
5. **Lyhyt video tai GIF (15–30 s):** näyttötallenne, jossa agentti ingestoi PDF:n ja wiki-sivu, index, references ja loki päivittyvät. Tämän jälkeen check.py ajetaan ja näyttää "0 errors". Vakuuttava "näin se toimii" -todiste, mutta vaatii editointia. Lisää tekstitys, koska videot katsotaan usein ilman ääntä.

Ehdotus: kuva 1 yksittäispostaukseen. Jos jaksat enemmän, karuselli 4, jonka yksi sivu on kuva 1.

Vältä:
- tekoälyllä generoitua kuvituskuvaa (ristiriidassa "no AI slop" -viestin kanssa)
- kuvakaappausta pelkästä tekstistä ilman korostuksia