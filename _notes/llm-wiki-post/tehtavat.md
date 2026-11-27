# Avoimet tehtävät: postaukset

Paperi on julkaistu: https://doi.org/10.5281/zenodo.24459573

## Postaukset (kotisivun blogi kattava ensin, LinkedIn lyhyt sen jälkeen)
Sisältö ja ideat `docs\private\llm-wiki-post`. Luonnostelu rinnakkain, blogipostaus julkaistaan ensin koska LinkedIn teskti tarvitsee linkin. Luvut pyöristetään ("yli 200 väitettä", "yli 30 lähdettä", "lähes 40 omaa päätelmää"), kun tarkka arvo ei ole oleellinen.
- [x] Blogipostaus ensin `2026-11-27-llm-wiki-and-academic-review.md`: katso kohdat kuntoon [blogi-tehtävälistaus](#julkaisu-kotisivulle)

- [ ] Kun blogi on julkaistu:
  - [ ] lisää sen linkki MEA_review_llm_wiki-repon README:hen (templaatin linkki on jo siellä)
  - [ ] tarkista blogin osoite MEA_review_llm_wiki-repon `docs/private/mainosviestit.md`:ssä, täytä LinkedIn-viestien `<name>`/`<nimi>` ja lähetä viestit (Slack, WhatsApp, LinkedIn)
  - [ ] poista `_notes/llm-wiki-post/` tai merkitse valmiiksi ("Siirto julkaisuun", askel 7)

- [ ] LinkedIn-postaus blogin jälkeen `linkedin_draft.md`: viittaa repoon, Zenodoon ja blogiin
  - [ ] valitse versio (suositus E) ja avaus A tai B; B:n kanssa toinen kappale kirjoitetaan uudelleen (vaihtoehdot `linkedin_draft.md`:ssä, "Vaihtoehtoja versioon E")
  - [ ] mahdolliset bulletinvaihdot: "Summaries drift" ja/tai pääviestin bulletti
  - [ ] PaperOrchestra-rivi: pidä vai pudota; jos julkaisu viivästyy, poista sana "new"
  - [ ] tarkista, että `/grinding` skills mainittu, ja karsi hashtagit
  - [x] korvaa `<BLOG-LINKKI>` (5 kohtaa): https://anahill.github.io/blog/llm-wiki-and-academic-review.html
  - [ ] liitä kuvat ja niiden alt-tekstit (`linkedin_draft.md`): ensin `llm-wiki_workflow_linkedin.png` ("Kuva tai video"), sitten `llm-wiki_highlights_linkedin.png` ("Academic Highlights")

## Julkaisu kotisivulle
- [x] luonnos ja sen 9 kuvaa siirretty `git mv`:llä (27.11.): `_posts/2026-11-27-llm-wiki-and-academic-review.md` ja `pics/posts/llm-wiki_*.png` ("Siirto julkaisuun", askeleet 1–5)
- [x] commit ja push: julkaistu 27.11., https://anahill.github.io/blog/llm-wiki-and-academic-review.html
- [ ] tarkista julkaistu sivu ("Siirto julkaisuun", askel 6): kuvat näkyvät, ja kuvatekstin jälkeen on väli ennen seuraavaa kappaletta (GitHubin esikatselussa väliä ei ole)

### Työn aikana

- Kirjoita postausta suoraan luonnostiedostoon `2026-11-27-llm-wiki-and-academic-review.md`.
- **Kuvat ovat kansiossa `_notes/pics/posts/`, joka peilaa kansiota `pics/posts/`.** Tämä tiedosto on tasolla `_notes/llm-wiki-post/`, joten kuviin viitataan muodossa `![kuvaus](../pics/posts/<nimi>.png)`. Sama viittaus toimii sellaisenaan julkaisun jälkeen: `_posts/<postaus>.md` viittaa tiedostopuussa kansioon `pics/posts/`, ja sivun osoitteesta `/blog/<otsikko>.html` katsottuna `../` osuu sivuston juureen eli osoitteeseen `/pics/posts/<nimi>.png`.
- **Älä muuta tämän tiedoston kansiotasoa** (`_notes/<kansio>/<tiedosto>.md`), koska `../`-viittaukset perustuvat siihen.
- Kuvan liittäminen leikepöydältä: asetus `markdown.copyFiles.destination` on `.vscode/settings.json`:ssa, ja se kopioi liitetyt kuvat kansioon `_notes/pics/posts/` ja kirjoittaa linkin automaattisesti. **Tiedosto on gitignoressa**, joten se on vain tällä koneella. Uudessa kloonissa asetus pitää luoda uudestaan (kopioi se tästä): `"markdown.copyFiles.destination": {"/_notes/**/*": "${documentWorkspaceFolder}/_notes/pics/posts/${fileName}"}`.
- Liittäminen voi pudottaa kuvapolun keskelle tekstiä (27.11. kymmenessä kohdassa, kahdessa polku korvasi tekstiä). Tarkista liittämisen jälkeen: `grep -n "pics/posts" <luonnos>` ja katso, että jokainen osuma on kuvalinkissä.
- Käytä kuvien nimissä yhteistä alkua (esim. `llm-wiki_…`), jotta nimet eivät törmää kansion `pics/posts/` nykyisiin kuviin siirrossa.
- `_notes/pics/posts/llm-wiki-explained.md` on Excalidraw-kuvan varmuuskopio, ei osa postausta: älä siirrä sitä julkaisuun.

### Siirto julkaisuun

1. Tarkista, että kaikki `- [ ] TODO`- ja `[CLAUDE]`-kohdat on käsitelty.
2. Tarkista, että jokaisessa kuvalinkissä on `!` (27.11. kaikissa on).
3. Päivitä front matterin `date` ja tiedostonimen päivämäärä julkaisupäiväksi, jos se ei ole 2026-11-27 (molemmat ovat nyt 2026-11-27). Front matter ja include ovat jo luonnoksessa (malli: `_posts/2025-03-23-my-struggle-to-make-post-work-properly.md`).
4. Siirrä kuvat kansiosta `_notes/pics/posts/` kansioon `pics/posts/`. Siirrä vain ne, joita postaus käyttää (ei `llm-wiki_workflow_linkedin.png`:ää eikä `llm-wiki-explained.md`:tä), ja tarkista, ettei samannimistä kuvaa ole jo olemassa. Linkkejä ei tarvitse muuttaa.
5. Siirrä luonnos: `git mv _notes/llm-wiki-post/2026-11-27-llm-wiki-and-academic-review.md _posts/`.
6. Aja Jekyll paikallisesti tai tarkista GitHub Pagesin build push:n jälkeen. Tarkista erityisesti, että kuvat näkyvät postauksen sivulla (`../pics/posts/…` ratkeaa osoitteessa `/blog/<otsikko>.html` kansioon `/pics/posts/`). Jos ei, vaihda polut muotoon `/pics/posts/…`, kuten aiemmissa postauksissa.
7. Poista `_notes/llm-wiki-post/` tai merkitse se valmiiksi, kun postaus on julkaistu.

### Älä tee

- Älä laita keskeneräistä tekstiä `_posts/`-kansioon: ensimmäinen push julkaisee sen.
- Älä jätä luonnostiedostoa juureen: juuren `.md`-tiedostot julkaistaan sivustolle.
- Älä liitä luonnoskuvia suoraan kansioon `pics/posts/`: ne julkaistaan sivustolle heti pushin jälkeen ja löytyvät osoitteesta `https://anahill.github.io/pics/posts/<nimi>.png`, vaikka postaus ei olisi julkaistu. Kansion `_notes/pics/posts/` kuvia Jekyll ei julkaise (alaviivalla alkavat kansiot jäävät pois), mutta ne näkyvät GitHubissa.

## Kuvat

Kaikki kansiossa `../pics/posts/` eli `_notes/pics/posts/`. Kotisivu on ainoa paikka: paperin repon `docs/private/`-kopiot poistettiin 23.11.2026.

| Kuva | Missä luonnoksessa | Huomiot |
|---|---|---|
| `llm-wiki_workflow.png` | The method | Valmis 27.11. LinkedIn-versio `llm-wiki_workflow_linkedin.png` ladataan LinkedIniin käsin, ei siirretä `pics/posts/`-kansioon. |
| `llm-wiki_graph_view_fpd-end-conventions.png` | The method | Sama kuin MEA_review_llm_wiki-repon README:ssä (`docs/images/fpd-end-conventions-graph-view.png`, 23.11.), kopioitu tänne. Asetukset: repon `docs/images/README.md`. |
| `llm-wiki_graph_view_wiki_exclude_index.png` | Knowledge has to flow back (before) | Ennen tagiremonttia: kertakäyttötagit (`#brv`, `#video`, `#impedance` …) näkyvät. Filtteripaneeli saa jäädä, se selittää indexin puuttumisen. |
| `llm-wiki_graph_view_after_tag_rework.png` | Knowledge has to flow back (after) | Otettu 27.11. Korostettuna `#rate-correction` (13 sivua). Ryhmävärit ja "Existing files only" eroavat before-kuvasta, siksi kuvatekstissä "a similar view". |
| `llm-wiki_loop_work.png` | The wiki structure pays off | Suomenkielinen agentin raportti; figcaptionissa "(in Finnish)". |
| `llm-wiki_loop_work2.png` | The wiki structure pays off | |
| `llm-wiki_human-in-the-loop.png` | Esimerkki C | |
| `llm-wiki_critical_assessment.png` | What else worked | |
| `llm-wiki_claude_memory.png` | What else worked | Heikko: näyttää vain lokakuun tiedostolistan, kun teksti puhuu `MEMORY.md`:n indeksirivistä. Parempi kuva olisi esim. `MEMORY.md`:n sisältö, jossa commit-sääntö on indeksirivillä. |
