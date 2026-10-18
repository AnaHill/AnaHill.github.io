# Portfolio TODO

Kotisivun pienet avoimet tehtävät. Isompi uudistus on erikseen tiedostossa [site_redesign.md](site_redesign.md). Jos uudistus toteutetaan, alla olevat kuvat kannattaa tehdä sen yhteydessä eikä erikseen.

Päivitetty 18.10.2026.

## Avoimet

### index.md: profiilikuva

- [ ] Etusivun kuva `pics/ajm_profile.png` (`index.md`, rivi ~22) on staattinen kuva, ja siitä puuttuu **Fabric** (Data Engineer -haarassa: Azure, ETL, Python, Databricks, PostgreSQL, DataOps).
- Vaihtoehdot:
  - Piirrä uudelleen esim. Mermaidilla tai HTML/CSS:llä, jolloin sitä on helppo päivittää.
  - Tai ota taidot samasta datasta kuin work.md:n kuplakaavio (cv_generatorin `skills.chart`), jotta tiedot eivät ole kahdessa paikassa.

### academic.md: tutkimuksen kuplakuva

- [ ] `academic.md`, rivi ~91: `![research_summary](pics/bubble_expertise_academic.png "summary of my research")` on staattinen kuva.
- Idea: piirrä samalla tekniikalla kuin work.md:n Chart.js-kuplakaavio, ja jos academic.md siirretään cv_generatoriin, data `data/academic.yml`:iin.

### muita
- [ ] Vanha kuva `pics/ajm_de_bubble.png` on käyttämättä, sen voi poistaa.

## Tehty

- [x] **work.md:n osaamiskuva → Chart.js-kuplakaavio** (kolme kategoriaa: tech stack, konsultointitaidot, toissijainen tekniikka; kuplien koot ja sijainnit säädettävissä). Data on nyt cv_generatorin `data/cv.yml`:ssä (`skills.chart`), ja samaa dataa käyttää myös PDF-CV. 
