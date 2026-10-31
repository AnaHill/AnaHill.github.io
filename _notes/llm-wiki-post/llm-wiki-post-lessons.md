---
title: LLM-wiki-postauksen muistiinpanot (siirretty MEA_review_llm_wiki/ToDo.md:n osiosta 6, 31.10.2026)
---

# Postaus: AI-avusteinen katsausartikkeli LLM-wikillä

Lähde: MEA_review_llm_wiki-repon ToDo.md, osio 6 "Postaus aiheesta". Siirretty sellaisenaan, jotta muistiinpanot eivät katoa, kun ToDo.md poistetaan. Lopussa on tämän session lisäykset erikseen merkittyinä.

Julkaisut: LinkedIn (lyhyt) ja kotisivun blogi (kattavampi). Julkaistaan vasta, kun paperi on Zenodossa, koska postaus linkittää siihen.

- DISCLAIMER alkuun: Vältetään AI sloppya, joten kävin itse läpi kaikki lähteet ja varsinkin väitökset

## Tärkeimpiä kohtia

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

## Lisäykset 31.10. session pohjalta (Clauden ehdotuksia, eivät omia muistiinpanoja; käytä harkiten)

- **Päätösten "grillaus" ennen toimintaa.** Lähdevalinta 30.10. tehtiin käytännössä käsin grillaten: agentti ehdotti valintaa perusteluineen, tutkija iteroi ja päätti, vasta sitten dokumentoitiin (docs/maturation-mea-search.md). Tästä tehtiin repoon `/grill-paper`-skill (muokattu Matt Pocockin `grilling`-skillistä, MIT): kierroksittainen haastattelu, tosiasiat agentti hakee wikistä itse, päätökset jäävät tutkijalle. Mahdollinen opetus postaukseen: "otettu käyttöön myöhässä; alusta asti käytettynä moni korjauskierros olisi jäänyt pois".
- **Dokumentoitu haku tuotti uutta, ei vain vahvistusta.** Kun hakulausekkeet, osumamäärät ja viittausketjut kirjattiin, löytyi kaksi lähdettä (Li 2025, Lin 2023), jotka tarkensivat paperin aukkoväitettä, ja yksi kytkös (Scheurer 2025:n kypsyysluokat perustuvat Li 2025:een), jota aiempi verkkohaku ei tuonut esiin.
- **Julkaisupaikka:** Zenodo valittiin Preprints.orgin sijaan, koska paperia ei viedä lehteen; Europe PMC -näkyvyys ei harrasteprojektissa painanut seulonnan epävarmuutta (affiliaatio, AI-politiikka) enempää. Löydettävyys tulee postauksista ja reposta.
