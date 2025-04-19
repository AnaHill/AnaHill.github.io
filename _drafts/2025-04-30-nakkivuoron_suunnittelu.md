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
This post is in Finnish, sorry (not sure though, is there even any reader whom this would matter...)!

Tässä kerron tehtävästäni, minkä sain toimiessani joukkueenjohtajana jälkikasvun harrastuksessa, ja kuinka valjastin tekoälyn siinä auttamaan.

**tl;dr**: tekoälyn avulla tulkitaan perheiden pääsemiset&toiveet, jotka sitten yhdistetään joukkueen talkoovuorotarpeisiin ja näiden  perusteella suunnitellaan mahdollisimman reilu vuorolista.

# Tehtävä: Vuorolistasuunnittelu 
- yhteensä 45 tuntia talkoovuoroja viikonlopun aikana
- tarvitaan vaihtelevasti 2-4 henkilöä kerralla eri tehtäviin
- kymmenkunta perhettä joille nämä vuorot pitäisi kohtuullisen tasapuolisesti jakaa
- ...tietyillä reunaehdoilla

Tätä lukiessa joku voisi miettiä, **miksen vain jakanut jotain taulukkoa mihin vanhemmat saisivat itse laittaa vuoronsa** "_nopeat syövät hitaat periaatteella_" vuorolistasuunnittelun sijaan? Arvaapa, teinkö näin aikaisempana vuotena? :D
Silloin ohjeistin jokaisen merkitsemään viitisen tuntia netissä jakamaani  taulukkoon; silloin tapahtui
- täyttämisessä oli yllättäviä vaikeuksia; osa pääsyoikeuksiin liittyen, osa käyttäjien taitoihin; jouduin lopulta melkoisesti neuvomaan ja täyttelemään toisten puolesta sitä taulukkoa
- kun sitten vuorot saatiin suunnilleen täytettyä, niin arvaapa
  - oliko siellä aukkoja, esimerkiksi yksittäisiä tunteja, jotka kumminkin on täytettävä
  - tuliko kaikenlaisia perumisia yms ja jäikö sinne lopulta tuplavuoro minun hoidettavakseni

...edellisen vuoden kokomuksella ajattelin siis, että tämä tämän vuotinen lähestymistapa on 
- minulle helpompi & kiinnostavampi kun pääsin samalla tutustumaan GenAI:n ja Agentteihinkin minua hyödyttävän tehtävän tiimoilta
- lopulta vanhemmillekin parempi; perustuen siihen koska suuria mussutuksia tai muutoksia ei tullut edes ekasta vuorolistaehdotuksestani, mistä olin kyllä positiivisen yllättynyt!

# Tavoitteeni: Tekoäly kaveriksi vuorosuunnitteluun!
**Alustuksena**: Tässä projektissa, vaikka datamäärät hyvin pieniä olivatkin, huomasi kyllä konkreettisesti sen vanhan totuuden kuinka paljon aikaa saa kulumaan etukäteisvalmisteluun, kuten datan keruuseen, koontiin ja siivoamiseen (sekä uusien asioiden oppimiseen), ennen kuin oikeasti pääsee tekemään sitä kiinnostavaa työvuorosuosittelua. Se nyrkkisääntö 80% piti varmaan aika hyvin kutinsa tässä tapauksessa.

Ideaalitapauksessa lopullinen ratkaisuni olisi skaalautuva; tässä tapauksessa se toimisi myös muiden talkoovuoroja tekevien joukkueiden, joita kymmenkunta (ja osa huomattavasti isompia sisältäen parikymmentä perhettä), tarpeisiin tulevina vuosina.

# Alkuvalmistelut
## Joukkueen talkoovuorotarpeiden määritys
Ensiksi, etsin kaikki joukkueeni talkoovuorotarpeet useammasta eri Excel-taulukosta, missä oli myös kaikkien muiden joukkueiden aikataulut. Sen jälkeen koostin niistä karkean aikataulutarpeen; tällä kertaa meillä oli nyt oli aina kaksi henkilöä pelijärkkäreinä ja kaksi myyntihommissa

Nämä vaiheet tein täysin käsin, koska en halunnut jakaa monen muun joukkueen kanssa jaettuja vuorolistoja tekoälylle; olisi toki ollut mahdollista että se olisi löytänyt ja osannut tulkita useamman erimuotoisen Excel-taulukon ja etsiä niistä omaa joukkuettani koskevat, mutta väittäisin ettei se ihan helppoa olisi ollut tässä tapauksessa kun lähdetaulut eivät olleet mitenkään formaalissa muodossa.

## Vanhempien toiveet ja pääsemiset
Pyysin ensiksi vanhempien lähettää toiveet/pääsemiset/esteet minulle whatsapilla, koska se vaikutti olevan lopulta helpoin tapa. Keräsin nämä sitten yhteen ja anonymisoin henkilötiedot (vaikkei tässä nyt ollut kuin etunimi yleensä niin olen tarkka etten niitäkään eteenpäin luovuta); käytännössä nimet muuttuivat geneerisiin muotoihin _Person1_, _Person2_,... ja perhekokonaisuudet _Family1_, _Family2_ ja niin edelleen.

Tässä vaiheessa kyselin jo tekoälyltä, mikä olisi järkevä tapa antaa nämä toiveet jatkovaiheita varten. Lopulta päädyimme `availability_raw_data.csv` tyyliseen ratkaisuun.

## JATKA: Analysoi toiveet GenAI:ta apuna käyttäen 
pyydä GenAI:ta analysoimaan toiveet
1. 

Muutama esimerkki vanhemmilta ykköskohtaan
> - voisin päästä lauantaina klo 13-15 ja henkilöX su aamusta
> - mulle ei sovi kuin sunnuntai
> - mä voin olla joko la aamusta tai sitten su iltapäivällä
> - voin olla pitkän päivän joko la tai su



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

