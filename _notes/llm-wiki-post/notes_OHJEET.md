# Blogipostauksen luonnostelu: akateeminen paperi LLM-wiki-menetelmällä

Hajanainen työtiedosto. Kirjoita tähän vapaasti, rakenne tulee myöhemmin (ks. [outline.md](outline.md)). Tämä kansio ei julkaista sivustolle, mutta se näkyy julkisessa repossa, ja se on tarkoituksella sallittu, koska paperin repo [MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki) on jo julkinen.

## Lähteet ja aineisto

- Paperin repo: [AnaHill/MEA_review_llm_wiki](https://github.com/AnaHill/MEA_review_llm_wiki) (narratiivinen katsaus, kardiomyosyyttien MEA-analyysin kehitys vuodesta 2022). Rakenne: `raw/` (lähde-PDF:t, muuttumattomat), `wiki/` (LLM:n ylläpitämät sivut: paperiyhteenvedot, käsitteet, aukot, `index.md`, `log.md`, `references.md`), `main.md` (paperiluonnos), `skills/`, `CLAUDE.md` (skeema ja ohjeet LLM:lle), `llm-wiki.md` (menetelmän selitys).
- Neljä operaatiota, joita agentilta pyydetään: **Ingest** (PDF → yhteenvetosivu + wiki-päivitys + viite), **Query** (kysymys → vastaus wikistä lähdeviitteineen), **Draft** (kirjoita tai kirjoita uudelleen osio), **Lint** (terveystarkastus: vanhentuneet väitteet, orvot sivut, tukemattomat väitteet).
- Työkalut: VS Code + [Foam](https://foambubble.github.io/foam/) (graafinäkymä, linkitys), LLM-agentti.
- Pohjat, jotka olen tehnyt: [llm-wiki-template](https://github.com/AnaHill/llm-wiki-template) (henkilökohtainen wiki) ja [llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template) (tutkijoille).
- **Wikin `wiki/log.md` on valmis aikajana siitä, mitä prosessissa on tehty.** Käy se läpi, kun alan kirjoittaa "miten tämä eteni" -osiota. Samoin `[CITATION NEEDED]`-merkinnät kertovat, missä tuki puuttui.

## Ajatuksia ja väitteitä (raakana)

- ...


## Mikä toimi

- ...

## Mikä ei toiminut / yllätti

- ...

## Kuvat ja kaaviot (ideoita)

- Työnkulun kaavio: `raw/` → ingest → `wiki/` → draft → `main.md`, lint takaisin wikiin.
- Foamin graafinäkymä wikistä (kuvakaappaus).
- Esimerkki yhdestä paperiyhteenvedosta ja siitä, miten se päätyy viitteeksi `main.md`:ssä.
- Ennen/jälkeen: yksi kappale, jossa `[CITATION NEEDED]` korvautuu viitteellä.

## Avoimet kysymykset

- Kieli: englanti (kuten aiemmat postaukset) vai suomi?
- Kenelle kirjoitan: tutkijat, jotka harkitsevat LLM:n käyttöä, vai data-ihmiset yleensä?
- Kuinka paljon kerron paperin sisällöstä (MEA) ja kuinka paljon pelkästä menetelmästä?
- Julkaisen vasta, kun paperi on valmis, vai kirjoitan ensin "tähänastiset opit"?

---
<!-- #### Kun valmis ##################### -->
## Muistilista: miten luonnos muuttuu postaukseksi

Tämä osio poistetaan, kun postaus on julkaistu.

### Työn aikana

- Luonnostele tähän tiedostoon.
- **Kuvat ovat kansiossa `_notes/pics/posts/`, joka peilaa kansiota `pics/posts/`.** Tämä tiedosto on tasolla `_notes/llm-wiki-post/`, joten kuviin viitataan muodossa `![kuvaus](../pics/posts/<nimi>.png)`. Sama viittaus toimii sellaisenaan julkaisun jälkeen: `_posts/<postaus>.md` viittaa tiedostopuussa kansioon `pics/posts/`, ja sivun osoitteesta `/blog/<otsikko>.html` katsottuna `../` osuu sivuston juureen eli osoitteeseen `/pics/posts/<nimi>.png`.
- **Älä muuta tämän tiedoston kansiotasoa** (`_notes/<kansio>/notes.md`), koska `../`-viittaukset perustuvat siihen.
- Kuvan liittäminen leikepöydältä: asetus `markdown.copyFiles.destination` on `.vscode/settings.json`:ssa, ja se kopioi liitetyt kuvat kansioon `_notes/pics/posts/` ja kirjoittaa linkin automaattisesti. **Tiedosto on gitignoressa**, joten se on vain tällä koneella. Uudessa kloonissa asetus pitää luoda uudestaan (kopioi se tästä): `"markdown.copyFiles.destination": {"/_notes/**/*": "${documentWorkspaceFolder}/_notes/pics/posts/${fileName}"}`.
- Jos linkistä puuttuu `!`, se renderöityy linkkinä eikä kuvana. Korjaa käsin muotoon `![kuvaus](../pics/posts/<nimi>.png)`.
- Käytä kuvien nimissä yhteistä alkua (esim. `llm-wiki_…`), jotta nimet eivät törmää kansion `pics/posts/` nykyisiin kuviin siirrossa.

### Siirto julkaisuun

1. Luo tiedosto `_posts/YYYY-MM-DD-otsikko.md` (päivämäärä on julkaisupäivä, otsikko englanniksi viivoilla, jos postaus on englanniksi).
2. Kopioi **front matter ja include vasta nyt** esimerkiksi aiemmasta postauksesta `_posts/2025-03-23-my-struggle-to-make-post-work-properly.md`:

   ```yaml
   ---
   layout: default
   title: "Otsikko tähän"
   date: YYYY-MM-DD
   categories: [llm]
   tags: [LLM wiki, academic writing, Foam]
   ---

   {% include blog-meta.html %}
   ```

3. Siirrä kuvat kansiosta `_notes/pics/posts/` kansioon `pics/posts/`. Siirrä vain ne, joita postaus käyttää, ja tarkista, ettei samannimistä kuvaa ole jo olemassa. Linkkejä ei tarvitse muuttaa.
4. Siirrä teksti `_notes/llm-wiki-post/notes.md` → `_posts/YYYY-MM-DD-otsikko.md` ja lisää alkuun front matter ja include (kohta 2).
5. Aja Jekyll paikallisesti tai tarkista GitHub Pagesin build push:n jälkeen. Tarkista erityisesti, että kuvat näkyvät postauksen sivulla (`../pics/posts/…` ratkeaa osoitteessa `/blog/<otsikko>.html` kansioon `/pics/posts/`). Jos ei, vaihda polut muotoon `/pics/posts/…`, kuten aiemmissa postauksissa.
6. Poista `_notes/llm-wiki-post/` tai merkitse se valmiiksi, kun postaus on julkaistu.

### Älä tee

- Älä laita keskeneräistä tekstiä `_posts/`-kansioon: ensimmäinen push julkaisee sen.
- Älä jätä luonnostiedostoa juureen: juuren `.md`-tiedostot julkaistaan sivustolle.
- Älä liitä luonnoskuvia suoraan kansioon `pics/posts/`: ne julkaistaan sivustolle heti pushin jälkeen ja löytyvät osoitteesta `https://anahill.github.io/pics/posts/<nimi>.png`, vaikka postaus ei olisi julkaistu. Kansion `_notes/pics/posts/` kuvia Jekyll ei julkaise (alaviivalla alkavat kansiot jäävät pois), mutta ne näkyvät GitHubissa.
