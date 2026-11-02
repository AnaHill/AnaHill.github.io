# Blogipostauksen luonnostelu: akateeminen paperi LLM-wiki-menetelmällä

kts `_notes\llm-wiki-post\notes_OHJEET.md` ohjeet, tähän vain ajatukset.
- Kieli: englanti
- Julkaisu vasta, kun paperi on valmis
- Kirjoitusyleisö ensisijaisesti tutkijat, joille esitellä LLM-wikin käyttöä; myös data-ihmiset voivat
- Paperin sisällöstä (MEA) lyhyesti, pääosuus miten tämä LLM-wiki menetelmä rakennettiin ja miten se toimii ja opetukset
- Samanlainen **DISCLAIMER** alkuun kuin postaukseen:* Vältetään AI sloppya*, joten kävin itse läpi kaikki lähteet ja varsinkin väitökset

**DISCLAIMER**: Be responsible. Avoid AI sloppy. Even though "*vibe-researching*" is educative (and fun!), I have done my best (with limited free time) to fix errors and epätarkkuudet. In science, DETAILS. DO. MATTER. It is not good result, if my claims are 90% correct. 

## Ajatuksia ja väitteitä 

- [critical_assignment](../pics/posts/llm-wiki_critical_assignment.png) hyvä lisä LLM-wikissä
- Graph view of wiki without index [graph view](../pics/posts/llm-wiki_graph_view_wiki_exclude_index.png)
- Markmap snapshot [llm-wiki markmap view](../pics/posts/llm-wiki_markmap_analysis.png)
- Clauden muistista [claudemuisti](../pics/posts/llm-wiki_claude_memory.png)
- kuinka päivittää useamman kohdan samalla kertaa [eka](../pics/posts/llm-wiki_loop_work.png) ja [toka](../pics/posts/llm-wiki_loop_work2.png)
- Human in the loop [human-in-the-loop-tarkeys](../pics/posts/llm-wiki_human-in-the-loop-tarkeys.png) " Opetus: AI:n tekemä paikkakorjaus voi jättää virkkeen ristiriitaiseksi, joten korjauksen jälkeen koko virke pitää lukea uudelleen: "*When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.*"

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
- **LinkedIn-postaus** (blogin jälkeen): viittaa repoon, Zenodoon ja blogiin
  - tagit: mitkä?
  - kuva mikä olisi hyvä? Vai animaatio?

## Mikä toimi
Hyviä ehdotuksia/ohjeita 
- > Kun haet PDF:t, ota Li 2025:stä myös supplementary-tiedosto. Supplementary Table 3 sisältää spike amplituden ja slopen lukuarvot.

## Mikä ei toiminut / yllätti

- ...

## Kuvat ja kaaviot (ideoita)

- Työnkulun kaavio: `raw/` → ingest → `wiki/` → draft → `main.md`, lint takaisin wikiin.
- Obsidianin tai Foamin graafinäkymä wikistä (kuvakaappaus).
- Esimerkki yhdestä paperiyhteenvedosta ja siitä, miten se päätyy viitteeksi `main.md`:ssä.
- Ennen/jälkeen: yksi kappale, jossa `[CITATION NEEDED]` korvautuu viitteellä.


---
<!-- #### Kun valmis, katso ohjeet -->
