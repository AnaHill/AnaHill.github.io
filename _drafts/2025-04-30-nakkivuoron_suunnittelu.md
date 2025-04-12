---
layout: default
title: "Kuinka suunnitella nakkivuorot (talkoolista) tekoälyn avulla"
date: 2025-04-30 
# last_modified_at: 2025-03-14
categories: [suomeksi]
tags: [AI, schedule designer]
---

{% include blog-meta.html %}

> 😎 Nerd your day! 🤓  
This post is in Finnish, sorry (if there is even any reader whom this matters)!

Tässä kerron tehtävästäni, minkä sain toimiessani joukkueenjohtajana jälkikasvun harrastuksessa, ja kuinka valjastin tekoälyn siinä auttamaan.

**tl;dr**: tekoälyn avulla tulkitaan vanhempien menot ja yhdistetään talkoovuorotarpeisiin. Näistä sitten koitetaan suunnitella mahdollisimman tasapuolinen vuorolista tietyillä reunaehdoilla.

## Tehtävä / tavoite: vuorolistasuunnittelu! (ilman aikaisempaa kokemusta)
- 45 tuntia talkoovuoroja viikonlopun aikana
- tarvitaan vaihtelevasti 2-4 henkilöä kerralla
- kymmenkunta perhettä joille nämä vuorot pitäisi kohtuullisen tasapuolisesti jakaa
- ...tietyillä reunaehdoilla

# Oma lähestymistapa: Valjasta tekoäly kaveriksi vuorosuunnitteluun!
Tässä projektissa, vaikka datamäärät hyvin pieniä olivatkin, huomasi kyllä konkreettisesti sen vanhan totuuden kuinka paljon aikaa saa kulumaan etukäteisvalmisteluun, kuten datan keruuseen, koontiin ja siivoamiseen, ennen kuin oikeasti pääsee itse kiinnostavaan työvuorosuositteluun. Se nyrkkisääntö 80% piti varmaan aika hyvin kutinsa tässä tapauksessa.

## Alkuvalmistelut
Aluksi määrittellään talkoovuorotarpeet
1. hae useammasta eri lähteestä talkoovuorojen aikataulut
2. etsi niistä mihin kaikkiin vuoroihin joukkueesi on laitettu
3. koosta niistä karkea aikataulutarve; esimerksi nyt oli aina kaksi henkilöä pelijärkkäreiksi ja kaksi myyntihommiin

Vaiheet 1-2 tehtiin täysin käsin, koska en halunnut jakaa monen muun ryhmän kanssa jaettuja vuorolistoja tekoälylle; olisi toki ollut mahdollista että se olisi löytänyt ja osannut tulkita 



Vanhempien toiveet/pääsyt
1. pyydä vanhempien lähettää nämä whatsapilla (vaikutti olevan lopulta helpoin tapa)
2. kerää tiedot yhteen
3. anonymisoi henkilötiedot (vaikkei tässä nyt ollut kuin etunimi yleensä niin olen tarkka etten niitäkään eteenpäin luovuta)
   

pyydä GenAI:ta analysoimaan toiveet
1. 


Muutama esimerkki vanhemmilta ykköskohtaan
> - voisin päästä lauantaina klo 13-15 ja henkilöX su aamusta
> - mulle ei sovi kuin sunnuntai
> - mä voin olla joko la aamusta tai sitten su iltapäivällä
> - voin olla pitkän päivän joko la tai su


Tätä lukiessa joku voisi miettiä, **miksen vain jakanut jotain taulukkoa mihin vanhemmat saisivat itse laittaa vuoronsa** "_nopeat syövät hitaat periaatteella_"? Arvaapa, teinkö näin aikaisempana vuotena? :D
Ohjeistin jokaisen merkkaamaan noin 5 tuntia taulukkoon jonka linkin jaoin; silloin tapahtui
- netissä olevan taulukon täyttämisessä oli yllättäviä vaikeuksia; osa pääsyoikeuksiin liittyen, osa käyttäjien taitoihin, jouduin kyllä silloin melkoisesti neuvomaan ja täyttelemään toisten puolesta
- kun sitten vuorot saatiin suunnilleen täytettyä, niin arvaapa
  - oliko siellä aukkoja, esim yksittäisiä tunteja, jotka kumminkin on täytettävä
  - tuliko kaikenlaisia perumisia yms ja jäikö sinne lopulta tuplavuoro minun hoidettavakseni

...edellisen vuoden kokomuksella ajattelin siis, että tämä tämän vuotinen lähestymistapa on 
- minulle helpompi & kiinnostavampi kun pääsin samalla tutustumaan GenAI:n ja Agentteihinkin minua hyödyttävän tehtävän tiimoilta
- lopulta vanhemmille parempi, koska suuria mussutuksia ei tullut edes ekasta vedosta

## Itse työvuorolistan suunnittelu ja toteutus
- .csv
- 
<!-- 
1) how to linking to your reference section [list](#ref)

2) how to include pic
![manual_h1_title](/pics/posts/manual_h1_title_outcome.png "how manually written h1 text is shown currently") 
or 
<figure style="text-align: center;">
  <img src="pics/ajm_profile.png" alt="my profile">
  <figcaption><em>"This is me." </em></figcaption>
</figure>


2) how to link to some file in the repo with absolut path
[View the Python script on GitHub](https://github.com/AnaHill/AnaHill.github.io/blob/main/_data/convert_bib_to_yaml.py "convert bib file to yaml")

-->



📝 Mukavaa vuorosuunnittelua! 😊


## <span id="ref"> Lisätietoja </span>
- reference1

--- 
<a href="{{ site.baseurl }}/blog/" style="color:green;"><strong>⬅ To My Blog list</strong></a><br>
<a href="{{ site.baseurl }}/" style="color:green"><strong>⬅ To My Main Page</strong></a>

