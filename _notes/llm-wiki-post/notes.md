# Raakamuistiinpanot: LLM-wiki-postaus

Ohjeet ja muistilista: [notes_OHJEET.md](notes_OHJEET.md). Postauksen luonnos: [2026-11-10-llm-wiki-and-academic-review.md](2026-11-10-llm-wiki-and-academic-review.md). Tähän kirjataan uudet ajatukset, ja niistä siirretään luonnokseen.

Tähän tiedostoon on yhdistetty 2.11.2026 aiemmat erilliset tiedostot `llm-wiki-post-lessons.md` ja `kuinka_clauden_avulla_ohjeistaa_uutta_chattia.md` (ks. alla). `draft.md` ja `outline.md` poistettiin, koska luonnos korvaa ne. Kaikki löytyy git-historiasta.

## Linjaukset

- Kieli: englanti.
- Julkaisu vasta, kun paperi on Zenodossa, koska postaus linkittää siihen. Ensin blogi (kattavampi), sitten LinkedIn (lyhyt, ks. [linkedin_draft.md](linkedin_draft.md)).
- Kirjoitusyleisö: ensisijaisesti tutkijat, joille esitellään LLM-wikin käyttöä; myös data-ihmiset.
- Paperin sisällöstä (MEA) lyhyesti, pääosuus siitä, miten LLM-wiki-menetelmä rakennettiin, miten se toimii ja mitä opin.
- DISCLAIMER alkuun: vältetään AI sloppya, joten kävin itse läpi kaikki lähteet ja varsinkin väitteet.

## Kuvat

Kaikki kansiossa `_notes/pics/posts/`. Luonnoksessa pelkkinä linkkeinä, julkaisussa lisätään `!`.

| Kuva | Missä luonnoksessa | Parannusideoita |
|---|---|---|
| `llm-wiki_markmap_analysis.png` | The paper in brief | Näyttää vielä vanhan otsikon ("Charting the Field…"); ota uusi kuva. Teksti katkeaa oikealta; rajaa tai ota kuva leveämmästä ikkunasta. |
| `llm-wiki_graph_view_wiki_exclude_index.png` | The method | Obsidianin graafinäkymä, filtteri rajattu punaisella. Ehkä vähemmän päällekkäisiä nimiä. |
| `llm-wiki_loop_work.png` | The wiki structure pays off | Suomenkielinen agentin raportti; harkitse englanninkielistä tai lisää figcaptioniin "(in Finnish)". |
| `llm-wiki_loop_work2.png` | The wiki structure pays off | |
| `llm-wiki_human-in-the-loop-tarkeys.png` | Esimerkki C | Nimessä suomea; voi nimetä esim. `llm-wiki_human-in-the-loop.png`. |
| `llm-wiki_critical_assignment.png` | What else worked | Nimi "assignment" → "assessment"? |
| `llm-wiki_claude_memory.png` | What else worked | |
| (puuttuu) työnkulun kaavio | The method | `raw/` → ingest → `wiki/` → draft → `main.md`, lint takaisin wikiin; alla `AGENTS.md` ja skriptit. |
| (puuttuu) virheen leviämisen kaavio | How a wrong claim spreads | Sama kuva kelpaa LinkedIniin (ks. linkedin_draft.md). |
| (idea) ennen/jälkeen | The workflow in practice | Yksi kappale, jossa `[CITATION NEEDED]` korvautuu viitteellä; tai yksi paperi → wikisivu → viite main.md:ssä. |

## Ideoita (osa jo luonnoksessa)

- [critical_assignment](../pics/posts/llm-wiki_critical_assignment.png) hyvä lisä LLM-wikissä
- Hyvä ehdotus agentilta: "Kun haet PDF:t, ota Li 2025:stä myös supplementary-tiedosto. Supplementary Table 3 sisältää spike amplituden ja slopen lukuarvot."
- Human in the loop: AI:n tekemä paikkakorjaus voi jättää virkkeen ristiriitaiseksi, joten korjauksen jälkeen koko virke pitää lukea uudelleen: "*When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.*"

### Ideat MEA_review_llm_wiki/ToDo.md:n D-osiosta (2.11.2026)

- **Abbreviations helposti lopuksi**: kun wiki ja kaikki muu on kunnossa, skripti (`check_abbreviations.py`) tarkistaa, ettei mitään puutu, ja agentti ajaa sitä ja korjaa, kunnes valmista
- **Laajempi viesti kuin datalaatu**: "samalla ne korostavat entisestään laadukkaan dataperustan, hyvän datan hallinnan ja oikeiden arkkitehtuuripäätösten merkitystä." Mieti, saisiko mukaan muutakin kuin datalaadun (esim. arkkitehtuuri: raw/wiki/main-kerrokset, skeema AGENTS.md:ssä, tarkistusskriptit)
- **Yhteiskirjoittaminen ilman suuria IT-taitoja** (alkuun tai omaksi osiokseen). Ydinviesti: single source of truth on main.md versiohallinnassa, mutta kanssakirjoittajan ei tarvitse osata gitiä eikä edes markdownia
  - kolme tasoa kanssakirjoittajalle:
    1. kirjoittaa Wordilla (tai sähköpostiin): agentti ingestoi tekstin nimettyyn kappaleeseen tai osioon, näyttää muutokset diffinä ja päivittää samalla lokin, claims-rekisterin ja tarvittaessa viitteet; päävastuullinen hyväksyy
    2. editoi markdownia suoraan: riittää kun suostuu lukemaan ja kirjoittamaan tekstitiedostoja
    3. käyttää itse agenttia ja gitiä: agentti hoitaa branchit, commitit ja ristiriidat alkuasetusten jälkeen
  - miksi toimii: versiohallinta pitää jokaisen muutoksen ja sen tekijän näkyvissä, ja AGENTS.md:n säännöt (lähteet, viitteet, lokit, check.py) koskevat myös kanssakirjoittajan tekstiä, joten laatu ei riipu siitä, millä työkalulla teksti on kirjoitettu
  - rehellisesti rajoitteet: Word-tekstin muutosmerkinnät ja kommentit pitää tulkita; jos kaksi muokkaa samaa kappaletta, päätös jää ihmiselle; agentin ei pidä yhdistää tekstejä hiljaa vaan näyttää erot; Word-teksti pitää ingestoida nykyistä main.md:tä vasten, ei vanhaa versiota
  - HUOM: Word-ingestiä ei ole vielä kokeiltu tässä projektissa; esitä mahdollisuutena, ellei testata ennen julkaisua (esim. yksi kappale Wordilla → agentti ingestoi)
  - mahdollinen jatko: `ingest-coauthor`-tyyppinen ohje AGENTS.md:hen tai templaattiin (lähde-Word → osio → diff → hyväksyntä → loki)
- **Peruskuvaus järkevästä tavasta** (työnkulun vaiheet):
  - vibe-researching / palloittelu alkuun
    - raakaversio
    - lähteiden haku agenttinen + omat etsinnät (suositeltavaa)
  - kun karkea versio: "Catch mistakes sooner, not later & save time, hermoja and some money too!"
    - manuaalinen main luku → virheet korjataan, lisäykset kannattaa vasta seuraavassa iteraatiossa
    - claims-by-source läpikäynti alkupuolella, kun tarkastettavia on vasta vähän → helpompaa
  - lisäyksiä / täydennyksiä
    - uusia ideoita yms.
  - Grinding
    - lopullisen main.md:n läpikäynti
    - claims-päivitykset sen jälkeen
    - manuaalinen läpikäynti jokainen erikseen: DETAILS DO MATTER in Science
  - Highlights-lisäys
  - (mahdollinen lehden valinta; viittaukset, lähdeluettelo, kuvatekstit yms.)
  - Abbreviations-teko
  - ...
- **LinkedIn-postaus** (blogin jälkeen): viittaa repoon, Zenodoon ja blogiin. Hahmotelma: [linkedin_draft.md](linkedin_draft.md)

---

## Liite 1: opit (entinen llm-wiki-post-lessons.md)

Siirretty 31.10.2026 MEA_review_llm_wiki-repon ToDo.md:n osiosta 6 "Postaus aiheesta" sellaisenaan.

### 1) Datan laatu

Uusien lähteiden ja niistä tehtyjen päätösten tarkastaminen heti, ettei väärä informaatio leviä moneen paikkaan, "even though 'vibe-researching' is fun, going through sources as soon as possible infront pays in the end"

- kuinka tekisin uudelleen: datan eli lähteiden tarkasteleminen heti alussa paremmin, datalaatu kunniaan
- miten virheellinen tieto leviää tässä repossa (kolme lähtökohtaa):

```
Virhe A, lähteen väärinluku (esim. Ismaili, Matsuda, Hwang, Kabanov):
raw/lähde.pdf
  -> wiki/papers/lähde.md          (tiivistys liioittelee tai lukee väärin)
  -> wiki/<käsitesivu>.md          (esim. hipsc-cm-maturation.md, critical-assessment-maki-claims.md)
  -> wiki/index.md                 (yhden rivin tiivistelmä)
  -> main.md                       (useaan osioon: tekstiin, taulukkoon, kuvatekstiin)
  -> main.md Abstract/Conclusion   (yleistyy entisestään tiivistyksessä)
  -> docs/claims-by-source.md      (väitelista kopioi virheen main.md:stä)

Virhe B, tekoälyn oma täydennys ilman lähdettä (esim. "longitudinal" ensimmäisestä luonnoksesta, keksitty "Galli et al. 2024"):
AI-luonnos -> main.md -> docs/claims-by-source.md -> (wiki-sivujen "Relevance"-osiot)

Virhe C, paikkakorjaus (esim. Open pipelines -virke 27.10.):
korjaus yhteen kohtaan -> ristiriita saman virkkeen tai muiden kohtien kanssa
```

- mikä pysäyttää mitäkin: `check.py` pysäyttää rakennevirheet (puuttuvat viitteet, DOI-erot, rikkinäiset linkit), mutta ei sisältöä, joten A, B ja C menevät siitä läpi; claims-by-source ja lähteen lukeminen pysäyttävät A:n ja B:n, kun väite tarkistetaan lähdettä eikä wikisivua vasten; ihmisen kokonaisluenta pysäyttää C:n ja osioiden väliset ristiriidat
- opetus: mitä aikaisemmassa vaiheessa virhe syntyy, sitä useampaan paikkaan se kopioituu, joten tarkistus kannattaa tehdä jo ingestissä eikä vasta main.md:stä
- kattavampi lähdehaku useammalla eri tavalla, esim. toinen LLM kuten Gemini, oma googlettelu/Scholar ja lähteiden viitteiden ja viittausten oma tarkastelu
- esimerkki hakuväitteestä (30.10.): main.md väitti "targeted search of PubMed/MEDLINE, bioRxiv and Scopus (2 July 2026)", mutta haulle ei ollut kirjausta, ja se oli tekoälyn verkkohaku. Korvattiin dokumentoidulla haulla (docs/maturation-mea-search.md), joka löysi myös kaksi oleellista lähdettä (Li 2025, Lin 2023). Virhetyyppi B: uskottavalta kuulostava menetelmäkuvaus ilman tositetta
- esimerkkinä LLM-wikin riski: wikisivut sisälsivät lähteen vastaisia väitteitä (mm. Ismaili, Matsuda, Hwang, Kabanov), jotka löytyivät vasta lähdetekstin ja väitteiden rivi riviltä -vertailussa
- esimerkki human-in-the-loopin tärkeydestä (27.10.): Open pipelines -osion avausvirke oli ristiriitainen. Alku sanoi avoimien analyysiputkien ilmestyneen 2022 jälkeen, ja loppu kumosi sen ("open tools such as MultiElec and CardioMDA already existed before 2022"). Loppu oli lisätty 24.10. tarkistuksessa korjaukseksi, koska sekä Lee et al. (2024, Table 3) että Dunham et al. (2022, s. 2) toteavat, että avoimia työkaluja oli jo ennen, mutta alkua ei silloin muutettu vastaamaan sitä. Automaattiset tarkistukset eivät huomanneet ristiriitaa; löysin sen itse lukiessa. Lähteiden perusteella uutta 2022 jälkeen ei ole avoimuus vaan se, että uusia avoimia työkaluja on tehty uusille datatyypeille: CardioMEA HD-MEA-datalle (Lee) ja PhysioMEA sydänorganoideille (Weiser-Bitoun). Opetus: AI:n tekemä paikkakorjaus voi jättää virkkeen ristiriitaiseksi, joten korjauksen jälkeen koko virke pitää lukea uudelleen
  - > When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.

### 2) Lähteiden löytäminen

Good-old-googlettu ja lähteiden löytäminen ja niiden lähteiden sekä siihen viittaaminen lähteiden läpikäyminen

### 3) Skriptit yms. testit varmistamaan datalaatua

- Kuinka hyvin rakennettu wiki ja muut auttoivat joka kerta kun Claude teki jotain
  - Claude muisti päivittää pelkän main lisäksi myös login ja indeksit yms oleelliset
  - tulee aina kelpo Ehdotus commit-viestiksi: *reword the Declarations sentence about colleagues to name the CoEBoC collaboration* (koska haluan nämä aina varmistaa ilman automatisointia)

### 4) (mieti vielä onko tarpeen)

Hämmentävä suuri ero Claude code vs Gemini notebook

### Lisäykset 31.10. session pohjalta (Clauden ehdotuksia, eivät omia muistiinpanoja; käytä harkiten)

- **Päätösten "grillaus" ennen toimintaa.** Lähdevalinta 30.10. tehtiin käytännössä käsin grillaten: agentti ehdotti valintaa perusteluineen, tutkija iteroi ja päätti, vasta sitten dokumentoitiin (docs/maturation-mea-search.md). Tästä tehtiin repoon `/grill-paper`-skill (muokattu Matt Pocockin `grilling`-skillistä, MIT): kierroksittainen haastattelu, tosiasiat agentti hakee wikistä itse, päätökset jäävät tutkijalle. Mahdollinen opetus postaukseen: "otettu käyttöön myöhässä; alusta asti käytettynä moni korjauskierros olisi jäänyt pois".
- **Dokumentoitu haku tuotti uutta, ei vain vahvistusta.** Kun hakulausekkeet, osumamäärät ja viittausketjut kirjattiin, löytyi kaksi lähdettä (Li 2025, Lin 2023), jotka tarkensivat paperin aukkoväitettä, ja yksi kytkös (Scheurer 2025:n kypsyysluokat perustuvat Li 2025:een), jota aiempi verkkohaku ei tuonut esiin.
- **Julkaisupaikka:** Zenodo valittiin Preprints.orgin sijaan, koska paperia ei viedä lehteen; Europe PMC -näkyvyys ei harrasteprojektissa painanut seulonnan epävarmuutta (affiliaatio, AI-politiikka) enempää. Löydettävyys tulee postauksista ja reposta.

## Liite 2: alkuperäinen ohjeistuskehote uudelle chatille (entinen kuinka_clauden_avulla_ohjeistaa_uutta_chattia.md)

Luonnoksessa on tästä englanninkielinen, lyhennetty käännös. Tarkista käännös tätä vasten.

```text
Tehtävä: kirjallisuushaku yhteen aukkoon review-paperissani. Älä muokkaa main.md:tä etkä wikiä tässä vaiheessa; raportoi löydökset ensin.

Lue ensin:
- AGENTS.md (työtapa; erityisesti "Never invent citations" ja "Batch or undirected additions — verify before ingesting")
- main.md, osio "Maturation status as an unresolved confound for MEA-derived metrics" ja Conclusionin neljäs aukko ("hiPSC-CM maturation status lacks MEA-derived reference values")
- wiki/hipsc-cm-maturation.md
- wiki/papers/fetterman-2024-maturation.md, wiki/papers/clements-2025-aims-poster.md, wiki/papers/scheurer-2025-optical-ai.md, wiki/papers/guerrelli-2024-hipscm.md, wiki/papers/hayakawa-2014-motion-fp.md
- wiki/index.md (jo käsitellyt lähteet, ettei niitä ehdoteta uudelleen)
- docs/search-strategy.md

Kysymys: onko julkaistu (vertaisarvioitu tai preprint) työtä, joka ehdottaa tai validoi MEA:lla (extracellular field potential) mitattavia viitearvoja tai luokittelijaa hiPSC-kardiomyosyyttien kypsyysasteelle (esim. FPD, spike amplitude, upstroke/depolarisaation nopeus, conduction velocity, beat rate tai näiden yhdistelmä kypsyyden merkkinä)? Myös ennen 2022 julkaistut kelpaavat, jos ne vastaavat tähän; ne merkitään paperissa taustaksi (kuten Blinova 2018 ja Hayakawa 2014).

Hae ainakin PubMedista, Google Scholarista ja bioRxivista, ja seuraa löydettyjen papereiden viitteitä ja niihin viittaavia töitä. Hakusanoja: "hiPSC-CM maturation" + "multielectrode array" / "field potential" / "MEA", "maturity marker", "maturation index", "electrophysiological maturation" + "MEA", "conduction velocity maturation hiPSC-CM".

Raportoi jokaisesta ehdokkaasta: tekijät, vuosi, otsikko, lehti, DOI (vain jos varmistettu lähteestä; muuten merkitse "unverified"), mitä MEA-parametreja se kytkee kypsyyteen, onko se validoitu jotain vertailua vastaan (esim. patch clamp, geeniekspressio, aikuisen kudos), ja arvio: kattaako se aukon, osittain vai ei. Kirjaa myös hakulausekkeet, tietokannat ja päivämäärä, jotta main.md:n "targeted search" -virke voidaan perustaa todelliseen hakuun.

Älä lisää mitään raw/-kansioon. Lähetän PDF:t itse niistä, jotka päätän ingestoida.
```
