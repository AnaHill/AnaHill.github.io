# Index information
<!-- Hi, I'm **A-J Mäki**—a curious mind with a passion for **data, sports, and lifelong learning**.  -->

<!-- 
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=200&duration=2000&pause=500&multiline=true&width=270&height=80&lines=%E2%80%A2+Data+Engineer+%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB;%E2%80%A2+Lifelong+Researcher+%F0%9F%91%A8%E2%80%8D%F0%9F%94%AC;%E2%80%A2+Data+Nerd+%F0%9F%A4%93)](https://git.io/typing-svg) 
-->

<!-- 🔍 *Additional references are available upon request.*   -->

<!-- - Student exchange, Hong Kong Polytechnic University, 2006-2007   -->

# some text currently not used in CV 
Besides data engineer tasks like developing and maintaining data pipelines and their monitoring systems, I have e.g. created a machine learning based recommendation system that was integrated to data pipelines for analysis and visualization purposes.

In smaller customer projects and inhouse trainings I have developed & deployed Azure resources by using Bicep and Azure Pipelines, build & used Snowflake & Crosser combination to ingest and analyze industrial data ( IIoT, Industrial IoT and OT-IT convergence), learnt data modeling techniques and especially Data Vault & ADE (Agile Data Engine), and built reports and analysis tools using Power BI.

Passionate data professional with a strong analytical background. Over two years, I have helped customers from different sectors (public domain and retail, energy, and mobile network industries) to build robust and scalable data solutions. 


## Solita inhouse trainings
- Data Academy: 5 weeks long training with SQL, Python & git, data modeling, Power BI, Data Vault & ADE (Agile Data Engine), Snowflake, 
- Data Architecht
- ADE
- Industrial Data Hothouse: a-month long inhouse training taught multiple data engineering and industrial skills, for example Python, Docker, IIoT (Industrial IoT) and OT-IT convergence.



# Publications

{% for pub in site.data.publications %}
  {% if pub.title contains "Barrier-free, open-top microfluidic chip for generating two distinct" %}
  - {%- for author in pub.authors -%}
      {% if author == pub.highlighted_author %}
        **{{ author }}**
      {% else %}
        {{ author }}
      {% endif %}{% if forloop.last == false %} and {% endif %}
    {%- endfor -%}.
    *"{{ pub.title }}"* {{ pub.journal }}, {{ pub.year }}.{% if pub.doi and pub.doi != "" %} [doi: {{ pub.doi }}](https://doi.org/{{ pub.doi }}){% endif %}
  {% endif %}
{% endfor %}


<!-- SELECTED PUBLICATIONS -->
Here, I list selected publications.
<details>
  <summary><strong>Show Selected Publications</strong></summary>  

> Yrjänäinen, Alma, Elina, Mesiä, Ella, Lampela, Joose, Kreutzer, Jorma, Vihinen, Kaisa, Tornberg, Hanna, Vuorenpää, Susanna, Miettinen, Pasi, Kallio, and **Antti-Juhana, Mäki**. "Barrier-free, open-top microfluidic chip for generating two distinct, interconnected 3D microvascular networks".Scientific Reports 14, no.1 (2024): 22916.

> 

</details>

<!-- Full Publication list -->
Here, you can see full publication list.
<details>
  <summary><strong>Show Full Publication List </strong></summary>   

> A. -J. Mäki, J. T. Koivumäki, J. Hyttinen and P. Kallio, "Simulation-Based Study of Control Strategies for Beating of Human Cardiomyocyte Cultures," in IEEE Transactions on Automation Science and Engineering, doi: 10.1109/TASE.2023.3309668.
>
> Yrjänäinen, Alma, Elina, Mesiä, Ella, Lampela, Joose, Kreutzer, Jorma, Vihinen, Kaisa, Tornberg, Hanna, Vuorenpää, Susanna, Miettinen, Pasi, Kallio, and **Antti-Juhana, Mäki**. "Barrier-free, open-top microfluidic chip for generating two distinct, interconnected 3D microvascular networks".Scientific Reports 14, no.1 (2024): 22916.
>
>Mykuliak, A, A, Yrjänäinen, AJ, Mäki, A, Gebraad, E, Lampela, M, Kääriäinen, TK, Pakarinen, P, Kallio, S, Miettinen, and H, Vuorenpää. "Vasculogenic potency of bone marrow-and adipose tissue-derived mesenchymal stem/stromal cells results in differing vascular network phenotypes in a microfluidic chip. Front Bioeng Biotechnol 10: 764237".Frontiers in Bioengineering and Biotechnology| www. frontiersin. org 10 (2022).
>
>Mäki, Antti-Juhana, and others. "Optically induced electric fields and their use in microfluidics and cell manipulation applications".Journal is required! (2010).

>Maki, Antti-Juhana, Pekka, Ronkanen, Quan, Zhou, and Pasi, Kallio. "Modeling continuous optoelectrowetting device." . In 2nd European Conference on Microfluidics (pp. $μ$FLU10–270).2010.
>
>Mäki, Antti-Juhana, Joose, Kreutzer, and Pasi, Kallio. "Modeling Drug Delivery in Gravity-Driven Microfluidic System." . In 12th International Conference on Nanochannels, Microchannels, and Minichannels (ICNMM2014), 2014, in press.2014.
>
>Mäki, Antti-Juhana, Samu, Hemmilä, Juha, Hirvonen, Nathaniel Narra, Girish, Joose, Kreutzer, Jari, Hyttinen, and Pasi, Kallio. "Modeling and Experimental Characterization of Pressure Drop in Gravity-Driven Microfluidic Systems".Journal of Fluids Engineering 137, no.2 (2015): 021105.
>
>Mäki, A-J, M, Peltokangas, J, Kreutzer, S, Auvinen, and P, Kallio. "Modeling carbon dioxide transport in PDMS-based microfluidic cell culture devices".Chemical Engineering Science 137 (2015): 515–524.
>
>Mäki, Antti-Juhana, Anton, Kontunen, Tomi, Ryynänen, Jarmo, Verho, Joose, Kreutzer, Jukka, Lekkala, and Pasi, Kallio. "Design and Simulation of a Thermal Flow Sensor for Gravity-Driven Microfluidic Applications".Journal is required! (2016).
>
>Mäki, Antti-Juhana, Tomi, Ryynänen, Jarmo, Verho, Joose, Kreutzer, Jukka, Lekkala, and Pasi J, Kallio. "Indirect temperature measurement and control method for cell culture devices".IEEE Transactions on Automation Science and Engineering 15, no.2 (2018): 420–429.
>
>Kreutzer, Joose, Laura, Ylä-Outinen, Antti-Juhana, Mäki, Mervi, Ristola, Susanna, Narkilahti, and Pasi, Kallio. "Cell culture chamber with gas supply for prolonged recording of human neuronal cells on microelectrode array".Journal of Neuroscience Methods 280 (2017): 27–35.
>
>Kreutzer, Joose, Marlitt, Viehrig, Antti-Juhana, Mäki, Pasi, Kallio, Rolle, Rahikainen, and Vesa, Hytönen. "Pneumatically actuated elastomeric device for simultaneous mechanobiological studies and live-cell fluorescent microscopy." . In 2017 International Conference on Manipulation, Automation and Robotics at Small Scales (MARSS) (pp. 1–5).2017.
>
>Skogberg, Anne, Antti-Juhana, Mäki, Marja, Mettänen, Panu, Lahtinen, and Pasi, Kallio. "Cellulose Nanofiber Alignment Using Evaporation-Induced Droplet-Casting, and Cell Alignment on Aligned Nanocellulose Surfaces".Biomacromolecules 18, no.12 (2017): 3936–3953.
>
>Mäki, Antti-Juhana, Jarmo, Verho, Joose, Kreutzer, Tomi, Ryynänen, Dhanesh, Rajan, Mari, Pekkanen-Mattila, Antti, Ahola, Jari, Hyttinen, Katriina, Aalto-Setälä, Jukka, Lekkala, and others. "A Portable Microscale Cell Culture System with Indirect Temperature Control".SLAS TECHNOLOGY: Translating Life Sciences Innovation 23, no.6 (2018): 566–579.
>
>Mäki, Antti-Juhana. "Modeling and Control of Microscale Cell Culture Environments." (2018).
>
>Rajan, Dhanesh Kattipparambil, Antti-Juhana, Mäki, Mari, Pekkanen-Mattila, Joose, Kreutzer, Tomi, Ryynänen, Hannu, Välimäki, Jarmo, Verho, Jussi T, Koivumäki, Heimo, Ihalainen, Katriina, Aalto-Setälä, and others. "Cardiomyocytes: Analysis of Temperature Response and Signal Propagation Between Dissociated Clusters Using Novel Video-Based Movement Analysis Software".IEEE Access 8 (2020): 109275–109288.
>
>Häkli, Martta, Joose, Kreutzer, Antti-Juhana, Mäki, Hannu, Välimäki, Henna, Lappi, Heini, Huhtala, Pasi, Kallio, Katriina, Aalto-Setälä, and Mari, Pekkanen-Mattila. "Human induced pluripotent stem cell-based platform for modeling cardiac ischemia".Scientific reports 11, no.1 (2021): 4153.
>
>Kreutzer, Joose, Marlitt, Viehrig, Rolle, Rahikainen, Antti, Mäki, Vesa P, Hytönen, and Pasi, Kallio. "Cell Stretching Device for Live-Cell Confocal Microscopy." . In Annual International Conference of the IEEE Engineering in Medicine and Biology Society.2016.
>
>Mäki, Antti, Dhanesh Kattipparambil, Rajan, Joose, Kreutzer, Anne, Skogberg, Mari, Pekkanen-Mattila, Jarmo Antero, Verho, Tomi, Ryynänen, Hannu, Välimäki, Antti, Ahola, Jari, Hyttinen, and others. "Platform for controlling cellular environment".Journal is required! (2018).
>
>Vilkko, Matti, J, Kaivosoja, Antti, Mäki, and Pasi, Kallio. "Compensation of detent torque in microstepping of linear permanent magnet stepping motors." . In 12th International Conference on New Actuators, Actuator 2010, Bremen, Germany, June 2010.2010.
>
>Mäki, Antti-Juhana, Joose, Kreutzer, and Pasi, Kallio. "Optimizing Elastomeric Mechanical Cell Stretching Device".Journal is required! (2018).
>
>Kreutzer, Joose, Disheet, Shah, Kaisa, Tornberg, Antti, Mäki, Mari, Pekkanen-Mattila, Katriina, Aalto-Setälä, and Pasi, Kallio. "Mini-incubator for prolonged hypoxia studies on MEA: Effect of hypoxia for IPSC-derived cardiomyocytes." . In MEA Meeting 2018| 11th International Meeting on Substrate Integrated Microelectrode Arrays.2018.
>
>Mäki, Antti, and Pasi, Kallio. "Modeling in vitro cell culture microenvironments." . In The Micronano System Workshop (MSW) (pp. 61).2018.
>
>Mäki, Antti-Juhana, Joose, Kreutzer, Xiaohui, Zhu, Jarmo, Verho, Tomi, Ryynänen, Yong, Yue, Jukka, Lekkala, and Pasi, Kallio. "Indirect Temperature Measurement in a Cell Culture Device".Journal is required! (Year is required!).
>
>Skogberg, Anne, Sanna, Siljander, Antti-Juhana, Mäki, Mari, Honkanen, Alexander, Efimov, Markus, Hannula, Panu, Lahtinen, Sampo, Tuukkanen, Tomas, Björkqvist, and Pasi, Kallio. "Self-assembled cellulose nanofiber–carbon nanotube nanocomposite films with anisotropic conductivity".Nanoscale 14, no.2 (2022): 448–463.
>
>Mykuliak, Anastasiia, Alma, Yrjänäinen, Antti-Juhana, Mäki, Arjen, Gebraad, Ella, Lampela, Minna, Kääriäinen, Toni-Karri, Pakarinen, Pasi, Kallio, Susanna, Miettinen, and Hanna, Vuorenpää. "Vasculogenic potency of bone marrow-and adipose tissue-derived mesenchymal stem/stromal cells results in differing vascular network phenotypes in a microfluidic chip".Frontiers in Bioengineering and Biotechnology 10 (2022): 764237.
>
>Gaballah, Mahmoud, Kirsi, Penttinen, Joose, Kreutzer, Antti-Juhana, Mäki, Pasi, Kallio, and Katriina, Aalto-Setälä. "Cardiac Ischemia On-a-Chip: Antiarrhythmic Effect of Levosimendan on Ischemic Human-Induced Pluripotent Stem Cell-Derived Cardiomyocytes".Cells 11, no.6 (2022): 1045.
>
>Peussa, Heidi, Joose, Kreutzer, Elina, Mäntylä, Antti-Juhana, Mäki, Soile, Nymark, Pasi, Kallio, and Teemu O, Ihalainen. "Pneumatic equiaxial compression device for mechanical manipulation of epithelial cell packing and physiology".PloS one 17, no.6 (2022): e0268570.
>
>Tornberg, Kaisa, Hannu, Välimäki, Silmu, Valaskivi, Antti-Juhana, Mäki, Matias, Jokinen, Joose, Kreutzer, and Pasi, Kallio. "Compartmentalized organ-on-a-chip structure for spatiotemporal control of oxygen microenvironments.".Biomedical Microdevices 24, no.4 (2022): 34–34.
>
>Häkli, Martta, Joose, Kreutzer, Antti-Juhana, Mäki, Hannu, Välimäki, Reeja Maria, Cherian, Pasi, Kallio, Katriina, Aalto-Setälä, and Mari, Pekkanen-Mattila. "Electrophysiological Changes of Human-Induced Pluripotent Stem Cell-Derived Cardiomyocytes during Acute Hypoxia and Reoxygenation".Stem cells international 2022, no.1 (2022): 9438281.
>
>Mykuliak, Anastasiia, Alma, Yrjänäinen, Antti-Juhana, Mäki, Arjen, Gebraad, Ella, Lampela, Minna, Kääriäinen, Toni-Karri, Pakarinen, Pasi, Kallio, Susanna, Miettinen, and Hanna, Vuorenpää. "Vasculogenic Potency of Bone Marrow-and Adipose Tissue-Derived Mesenchymal Stem/Stromal Cells".Organ Microenvironment in Vascular Formation, Homeostasis and Engineering 16648714 (2023).
>
>Mäki, Antti-Juhana, Jussi T, Koivumäki, Jari, Hyttinen, and Pasi, Kallio. "Simulation-Based Study of Control Strategies for Beating of Human Cardiomyocyte Cultures".IEEE Transactions on Automation Science and Engineering (2023).
>
>Mäki, Antti-Juhana. "Opinion: The correct way to analyze FP signals." (2023).
>
>Häkli, M, H, Välimäki, A, Mäki, J, Kreutzer, D, Rajan, Tomi, Ryynänen, P, Kallio, K, Aalto-Setälä, and M, Pekkanen-Mattila. "Modeling Cardiac Ischemia with Human Induced Pluripotent Stem Cell-Derived Cardiomyocytes." . In EUROOoCs conference of European Organ-on-Chip Society.2020.
>
>Salpavaara, T, A, Nummi, J, Verho, Tomi, Ryynänen, J, Väliaho, A, Mäki, J, Lekkala, and P, Kallio. "Understanding electrical signals in volume conductor on MEA." . In 12th International Conference on Microelectrode Arrays for Life Sciences.2022.
>
>Välimäki, H, A, Mäki, DK, Rajan, M, Pekkanen-Mattila, J, Kreutzer, Tomi, Ryynänen, J, Verho, K, Aalto-Setälä, and P, Kallio. "Combined electrophysiological and video-based motion analysis for human induced pluripotent stem cell-derived cardiomyocytes in hypoxia." . In EUROOoCs conference of European Organ-on-Chip Society.2021.
>
>Ryynänen, Tomi, A, Karttu, A, Mäki, L, Sukki, J, Väliaho, H, Välimäki, D, Rajan, J, Kreutzer, J, Lekkala, and P, Kallio. "Custom-designed 2D microelectrode array fabrication." . In EUROOoCs conference of European Organ-on-Chip Society.2019.
>

</details>

# TEST LIST PUBLICATIONS
## Selected Publications

{% for pub in site.data.publications limit:5 %}
  {% if pub.category == "selected_publication" %}
  - {% assign authors_list = pub.authors | split: ", " %}
    {% for author in authors_list %}
      {% if author == pub.highlighted_author %}
        **{{ author }}**
      {% else %}
        {{ author }}
      {% endif %}
      {%- if forloop.last == false -%}, {% endif %}
    {% endfor %}
    . *"{{ pub.title }}"* {{ pub.journal }}, {{ pub.year }}.
    {% if pub.doi and pub.doi != "" %} [DOI: {{ pub.doi }}](https://doi.org/{{ pub.doi }}) {% endif %}
    [Read more]({{ pub.link }})
  {% endif %}
{% endfor %}

---

## All Publications

{% for pub in site.data.publications limit:3 %}
- {% assign authors_list = pub.authors | split: ", " %}
  {% for author in authors_list %}
    {% if author == pub.highlighted_author %}
      **{{ author }}**
    {% else %}
      {{ author }}
    {% endif %}
    {%- if forloop.last == false -%}, {% endif %}
  {% endfor %}
  . *"{{ pub.title }}"* {{ pub.journal }}, {{ pub.year }}.
  {% if pub.doi and pub.doi != "" %} [DOI: {{ pub.doi }}](https://doi.org/{{ pub.doi }}) {% endif %}
  [Read more]({{ pub.link }})
{% endfor %}



<a href="{{ site.baseurl }}/" style="color:green">
  <strong><big>⬅ To My Main Page </big> </strong>
</a>