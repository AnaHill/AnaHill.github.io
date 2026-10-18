# Kotisivun uudistus: ideat ja vaihtoehdot

Muistiinpano 18.10.2026. Ei vielä toteutettu mitään. Tähän voi palata, kun uudistus on ajankohtainen.

## Lähtötilanne

- Jekyll + GitHub Pages, teemana `pages-themes/merlot@v0.2.0` (`_config.yml`).
- Sisältö on pitkinä sivuina: `work.md` (~300 riviä), `academic.md` (~500 riviä), `projects.md`, `index.md`, blogi.
- Ilmeessä on vanhentuneita elementtejä: shields.io-badget yhteystiedoille, typing-SVG etusivulla, runsaasti emojeita otsikoissa ja tekstissä.
- `work.md` ja `resume_ajm.pdf` generoidaan yksityisessä `cv_generator`-repossa, ja `projects.md` on tulossa samaan putkeen (`docs/tasks/projects_page.md`).

## Inspiraatio

[abdessamad-amtoug.netlify.app](https://abdessamad-amtoug.netlify.app/):

- Yläpalkin navigaatio (Home, Projects, Skills, About, Contact).
- Aloitusosio: nimi, titteli, lyhyt esittely, kuva ja "Download CV" -painike. Ensimmäinen näkymä kertoo olennaisen.
- Projektit kortteina: kuva, otsikko, lyhyt kuvaus ja linkkipainikkeet.
- Kokemus ja koulutus aikajanana, taidot ryhmiteltyinä lohkoina.
- Hillitty visuaalinen kieli.

Ero omaan sivuun syntyy pääasiassa **rakenteesta**, ei tekniikasta.

## Ehdotettu sivurakenne

Rakenne ei riipu tekniikasta, joten päätä se ensin.

| Sivu | Sisältö |
|---|---|
| **Home** | Aloitusosio, nykyinen rooli, avainteknologiat tageina, 3 nostettua projektia, 3 uusinta blogikirjoitusta |
| **Experience** | Aikajana, jossa jokainen rooli on avattava kortti. Työprojektit linkittyvät oman roolinsa alle |
| **Projects** | Korttiruudukko suodattimilla (Data & AI, Apps, Research tools), työprojektit erikseen |
| **Research** | Julkaisut (`_data/publications.bib` on jo olemassa), tutkimusprojektit, väitöskirja |
| **Blog** | Nykyiset kirjoitukset |

Yhteystiedot ja CV-linkki tulevat yläpalkkiin ja alatunnisteeseen, eivät jokaiselle sivulle erikseen.

## Toteutusvaihtoehdot

### 1. Uusi Jekyll-teema (pienin muutos)

Liquid, nykyiset sivut ja cv_generatorin tuottamat md-tiedostot toimivat lähes sellaisenaan.

- [al-folio](https://github.com/alshedivat/al-folio): tehty tutkija-ammattilaisille, lukee julkaisut suoraan BibTeX-tiedostosta. Tyylikäs, mutta melko akateeminen ilme. Käyttää GitHub Actions -buildia lisäosien takia.
- [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes): joustava yleisteema, jossa on navigaatio, tekijän sivupalkki ja korttiasettelu.
- [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy): moderni, mutta blogipainotteinen.

### 2. Astro (modernein, sopii cv_generatoriin parhaiten)

- Esimerkkisivun kaltainen ilme: kortit, aikajana, tumma tila. Valmiita portfoliopohjia [Astron teemagalleriassa](https://astro.build/themes/).
- Julkaisu GitHub Pagesiin GitHub Actionsilla.
- cv_generator voisi tuottaa md-tiedostojen sijaan **JSON-dataa**, josta sivusto rakentaa kortit ja aikajanan. Ulkoasu ja sisältö olisivat aidosti erillään, ja sama data syöttäisi sekä sivuston että PDF:t.
- Vaatii eniten alkutyötä: Liquid-osat ja sivut kirjoitetaan uudelleen komponenteiksi. Blogikirjoitukset siirtyvät markdownina lähes sellaisenaan.

### 3. Hugo + Hugo Blox (ent. Wowchemy)

Tutkijoiden suosima ja monipuolinen, mutta raskas ja monimutkainen konfiguroida. **Ei suositella.**

## Suositus

1. **Päätä sivurakenne ensin** (yllä oleva taulukko tai oma muunnelma). Se ratkaisee ilmeestä eniten.
2. **Valitse tekniikka:**
   - Vähällä työllä selvästi parempi ilme → al-folio tai Minimal Mistakes.
   - Esimerkkisivun tyylinen moderni ilme ja yhtenäinen data cv_generatorin kanssa → Astro. Enemmän alkutyötä, mutta johdonmukaisempi pitkällä aikavälillä.

## Säilytettävä siirrossa

- Blogikirjoitusten osoitteet: `permalink: /blog/:title.html`.
- CV-PDF:n osoite `https://anahill.github.io/resume_ajm.pdf`, koska sitä on jaettu muualle (esim. LinkedIn).
- Sivujen osoitteet `work.html`, `projects.html` ja `academic.html`, tai uudelleenohjaukset uusiin osoitteisiin.
- Kotisivun Chart.js-kuplakaavio (`skills.chart` cv.yml:ssä), jos se halutaan pitää.

## Liittyvät avoimet TODOt

`portfolio_todo.md`:ssä on kuvien uudistusideoita (profiilikuva ja akateeminen kuplakuva esim. Mermaidilla). Ne kannattaa ratkaista uudistuksen yhteydessä eikä erikseen.

## Mahdolliset seuraavat askeleet

- Kahden teeman rinnakkaisvertailu omalla sisällöllä (esim. al-folio vs. Astro-pohja).
- Home-sivun luonnos omaan haaraansa ennen lopullista päätöstä.
- Jos valinta on Astro: cv_generatoriin JSON-ulostulo (`build.py json`) sivuston dataa varten.
