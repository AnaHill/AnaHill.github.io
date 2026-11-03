# LinkedIn-postaus: hahmotelma (2.11.2026)

Kieli: englanti (sama kuin blogissa). Julkaistaan blogin jälkeen, kun Zenodo-DOI on olemassa. Pituus: noin 150–250 sanaa, koska LinkedIn näyttää ennen "see more" -katkoa vain 2–3 ensimmäistä riviä.

---

## Versio A: oppi edellä

Can an AI agent help write a scientific review without producing AI slop?

I tried. The result is a narrative review on how cardiomyocyte MEA analysis has evolved since 2022, written with an "LLM wiki": the agent summarises every source into a wiki, keeps the reference list and logs in sync, and drafts text. I select the sources, make the decisions and check every claim.

What I learned:
🔹 Check sources at ingest, not at the end. One misread summary spread to five places before I caught it.
🔹 Scripts catch structure (missing references, broken links), and the agent's health checks of the wiki catch contradictions and stale claims. Neither catches a misread source. Only reading the source does that.
🔹 A plausible-sounding sentence can still be wrong. "A targeted search of PubMed…" had no record behind it, so I redid the search properly, and it found two relevant papers.
🔹 Use the strongest model where an error would go unnoticed (reading sources, wording claims), a lighter one for bookkeeping, and another model family for the final check. No model replaces my own read-through.
🔹 Everything is plain markdown under version control: transparent, reproducible, and easy to co-write.

In science, details do matter. A paper that is 90 % correct is not good enough.

📝 Blog post, the whole story: <BLOG-LINKKI>
📄 The paper (Zenodo, open access): <ZENODO-DOI>
💻 Everything behind it, including sources, wiki and logs: https://github.com/AnaHill/MEA_review_llm_wiki
🧰 Template to try it yourself: https://github.com/AnaHill/llm-wiki-academic-template

#AIinResearch #LLM #OpenScience #ScientificWriting #Cardiology #StemCells #ResearchIntegrity

---

## Versio B: lyhyempi, kysymys edellä

What does it take to write a scientific review with an AI agent and still stand behind every sentence?

I wrote a review on cardiomyocyte MEA analysis using an LLM-maintained wiki. The agent did the bookkeeping. I did the thinking, and I checked every claim against its source.

The biggest lesson: AI makes errors cheap to create and expensive to find. Catch them at the source, early.

📝 Blog: <BLOG-LINKKI>
📄 Paper: <ZENODO-DOI>
💻 Repo: https://github.com/AnaHill/MEA_review_llm_wiki

#AIinResearch #OpenScience #LLM #ResearchIntegrity

---

## Muistiinpanot postaukseen

- **Linkkien sijainti:** LinkedIn rajoittaa ulkoisten linkkien näkyvyyttä. Vaihtoehto on laittaa linkit ensimmäiseen kommenttiin ja tekstiin "links in the first comment 👇". Päätä itse. Linkit tekstissä ovat suoraviivaisempi ratkaisu, ja ne kertovat avoimuudesta.
- **Avaus on tärkein:** ensimmäinen rivi näkyy ennen katkoa. Kysymys ("Can an AI agent…") tai provokaatio ("90 % correct is not good enough") toimii.
- **Tarkistettavat väitteet ennen julkaisua:**
  - "I check every claim" pitää paikkansa vasta, kun ToDo:n A3-lähdetarkistus on tehty.
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

Vaihtoehdot paremmuusjärjestyksessä:

1. **Virheen leviämisen kaavio (oma kuva, suositus).** Kuvassa näkyy, kuinka yksi lähteen väärinluku leviää: raw PDF → wiki-sivu → käsitesivu → index → main.md → abstrakti. Vieressä on, mikä pysäyttää minkäkin: check.py, claims-rekisteri tai ihmisen luenta. Tämä on postauksen ydinviesti visuaalisena, ja se erottuu geneerisistä AI-kuvista. Muoto: neliö (1080×1080) tai pysty (1080×1350), iso fontti, koska kuvaa katsotaan puhelimella.
2. **Kolmen kerroksen arkkitehtuuri:** `raw/` → `wiki/` → `main.md` ja niiden alla AGENTS.md ja skriptit. Selkeä mutta tavallisempi.
3. **Wikin graafinäkymä** (Obsidian tai Foam, jo kuvattu: llm-wiki_graph_view_wiki_exclude_index.png). Näyttävä, mutta kertoo vähän ilman selitystä. Sopii parhaiten karuselliin muiden kuvien rinnalle.
4. **Karuselli (PDF-dokumenttipostaus), 4–6 sivua:** kansi (kysymys) → menetelmä → virheen leviäminen → mikä pysäyttää mitäkin → opit → linkit. LinkedInissä karusellit saavat usein hyvin näkyvyyttä, mutta ne ovat isompi työ.
5. **Lyhyt video tai GIF (15–30 s):** näyttötallenne, jossa agentti ingestoi PDF:n ja wiki-sivu, index, references ja loki päivittyvät. Tämän jälkeen check.py ajetaan ja näyttää "0 errors". Vakuuttava "näin se toimii" -todiste, mutta vaatii editointia. Lisää tekstitys, koska videot katsotaan usein ilman ääntä.

Ehdotus: kuva 1 yksittäispostaukseen. Jos jaksat enemmän, karuselli 4, jonka yksi sivu on kuva 1.

Vältä:
- tekoälyllä generoitua kuvituskuvaa (ristiriidassa "no AI slop" -viestin kanssa)
- kuvakaappausta pelkästä tekstistä ilman korostuksia