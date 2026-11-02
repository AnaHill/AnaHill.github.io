# Blogipostauksen luonnostelu: akateeminen paperi LLM-wiki-menetelmällä

Ohjeet ja muistilista. Tämä kansio ei julkaista sivustolle, mutta se näkyy julkisessa repossa, ja se on tarkoituksella sallittu, koska paperin repo [MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki) on jo julkinen.

## Tiedostot

- [2026-11-10-llm-wiki-and-academic-review.md](2026-11-10-llm-wiki-and-academic-review.md): **blogipostauksen luonnos** (englanti), jossa front matter ja include ovat jo valmiina. Avoimet kohdat on merkitty `- [ ] TODO` ja Clauden ehdotukset `[CLAUDE]`.
- [linkedin_draft.md](linkedin_draft.md): LinkedIn-postauksen hahmotelma (julkaistaan blogin jälkeen).
- [notes.md](notes.md): raakamuistiinpanot, ideat, kuvien lista ja alkuperäinen ohjeistuskehote. Uudet ajatukset kirjataan tänne, ja niistä siirretään luonnokseen.
- Kuvat: `_notes/pics/posts/llm-wiki_*.png` (lista ja parannusideat tiedostossa notes.md).

## Lähteet ja aineisto

- Paperin repo: [AnaHill/MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki) (narratiivinen katsaus, kardiomyosyyttien MEA-analyysin kehitys vuodesta 2022). Rakenne: `raw/` (lähde-PDF:t, muuttumattomat), `wiki/` (LLM:n ylläpitämät sivut: paperiyhteenvedot, käsitteet, aukot, `index.md`, `log.md`, `references.md`), `main.md` (paperiluonnos), `skills/`, `AGENTS.md` (skeema ja ohjeet LLM:lle; `CLAUDE.md` vain viittaa siihen), `llm-wiki.md` (menetelmän selitys).
- Neljä operaatiota, joita agentilta pyydetään: **Ingest** (PDF → yhteenvetosivu + wiki-päivitys + viite), **Query** (kysymys → vastaus wikistä lähdeviitteineen), **Draft** (kirjoita tai kirjoita uudelleen osio), **Lint** (terveystarkastus: vanhentuneet väitteet, orvot sivut, tukemattomat väitteet).
- Työkalut: VS Code, [Obsidian](https://obsidian.md/) tai [Foam](https://foambubble.github.io/foam/) (graafinäkymä, linkitys), Claude Code.
- Pohjat, jotka olen tehnyt: [llm-wiki-template](https://github.com/AnaHill/llm-wiki-template) (henkilökohtainen wiki) ja [llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template) (tutkijoille).
- **Wikin `wiki/log.md` on valmis aikajana siitä, mitä prosessissa on tehty.** Käy se läpi, kun alan kirjoittaa "miten tämä eteni" -osiota. Samoin `[CITATION NEEDED]`-merkinnät kertovat, missä tuki puuttui.

---
<!-- #### Kun valmis ##################### -->
## Muistilista: miten luonnos muuttuu postaukseksi

Tämä osio poistetaan, kun postaus on julkaistu.

### Työn aikana

- Kirjoita postausta suoraan luonnostiedostoon `2026-11-10-llm-wiki-and-academic-review.md` ja raakoja ajatuksia tiedostoon `notes.md`.
- **Kuvat ovat kansiossa `_notes/pics/posts/`, joka peilaa kansiota `pics/posts/`.** Tämä tiedosto on tasolla `_notes/llm-wiki-post/`, joten kuviin viitataan muodossa `![kuvaus](../pics/posts/<nimi>.png)`. Sama viittaus toimii sellaisenaan julkaisun jälkeen: `_posts/<postaus>.md` viittaa tiedostopuussa kansioon `pics/posts/`, ja sivun osoitteesta `/blog/<otsikko>.html` katsottuna `../` osuu sivuston juureen eli osoitteeseen `/pics/posts/<nimi>.png`.
- **Älä muuta tämän tiedoston kansiotasoa** (`_notes/<kansio>/<tiedosto>.md`), koska `../`-viittaukset perustuvat siihen.
- Kuvan liittäminen leikepöydältä: asetus `markdown.copyFiles.destination` on `.vscode/settings.json`:ssa, ja se kopioi liitetyt kuvat kansioon `_notes/pics/posts/` ja kirjoittaa linkin automaattisesti. **Tiedosto on gitignoressa**, joten se on vain tällä koneella. Uudessa kloonissa asetus pitää luoda uudestaan (kopioi se tästä): `"markdown.copyFiles.destination": {"/_notes/**/*": "${documentWorkspaceFolder}/_notes/pics/posts/${fileName}"}`.
- Jos linkistä puuttuu `!`, se renderöityy linkkinä eikä kuvana. Korjaa käsin muotoon `![kuvaus](../pics/posts/<nimi>.png)`.
- Käytä kuvien nimissä yhteistä alkua (esim. `llm-wiki_…`), jotta nimet eivät törmää kansion `pics/posts/` nykyisiin kuviin siirrossa.

### Siirto julkaisuun

1. Tarkista, että kaikki `- [ ] TODO`- ja `[CLAUDE]`-kohdat on käsitelty, ja poista luonnoksen alun HTML-kommentti.
2. Lisää kuvalinkkeihin `!`, eli `[kuvaus](../pics/posts/…)` → `![kuvaus](../pics/posts/…)`. Figcaptionit ovat jo valmiina.
3. Päivitä front matterin `date` ja tiedostonimen päivämäärä julkaisupäiväksi, jos se ei ole 2026-11-10. Front matter ja include ovat jo luonnoksessa (malli: `_posts/2025-03-23-my-struggle-to-make-post-work-properly.md`).
4. Siirrä kuvat kansiosta `_notes/pics/posts/` kansioon `pics/posts/`. Siirrä vain ne, joita postaus käyttää, ja tarkista, ettei samannimistä kuvaa ole jo olemassa. Linkkejä ei tarvitse muuttaa.
5. Siirrä luonnos: `git mv _notes/llm-wiki-post/2026-11-10-llm-wiki-and-academic-review.md _posts/`.
6. Aja Jekyll paikallisesti tai tarkista GitHub Pagesin build push:n jälkeen. Tarkista erityisesti, että kuvat näkyvät postauksen sivulla (`../pics/posts/…` ratkeaa osoitteessa `/blog/<otsikko>.html` kansioon `/pics/posts/`). Jos ei, vaihda polut muotoon `/pics/posts/…`, kuten aiemmissa postauksissa.
7. Poista `_notes/llm-wiki-post/` tai merkitse se valmiiksi, kun postaus on julkaistu.

### Älä tee

- Älä laita keskeneräistä tekstiä `_posts/`-kansioon: ensimmäinen push julkaisee sen.
- Älä jätä luonnostiedostoa juureen: juuren `.md`-tiedostot julkaistaan sivustolle.
- Älä liitä luonnoskuvia suoraan kansioon `pics/posts/`: ne julkaistaan sivustolle heti pushin jälkeen ja löytyvät osoitteesta `https://anahill.github.io/pics/posts/<nimi>.png`, vaikka postaus ei olisi julkaistu. Kansion `_notes/pics/posts/` kuvia Jekyll ei julkaise (alaviivalla alkavat kansiot jäävät pois), mutta ne näkyvät GitHubissa.
