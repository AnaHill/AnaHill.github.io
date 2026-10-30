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
- Clauden muistista [claudemuisti](../pics/posts/llm-wiki_claude_memory.png)
- kuinka päivittää useamman kohdan samalla kertaa [eka](../pics/posts/llm-wiki_loop_work.png) ja [toka](../pics/posts/llm-wiki_loop_work2.png)
- Human in the loop [human-in-the-loop-tarkeys](../pics/posts/llm-wiki_human-in-the-loop-tarkeys.png) " Opetus: AI:n tekemä paikkakorjaus voi jättää virkkeen ristiriitaiseksi, joten korjauksen jälkeen koko virke pitää lukea uudelleen: "*When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.*"

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
