# data-visuals-names
#Polish version

Projekt wizualizacji danych udostępnionych przez polskie Ministerstwo Cyfryzacji na stronie:
https://dane.gov.pl/dataset/219,imiona-nadawane-dzieciom-w-polsce
Dane zawierają imiona nadane dzieciom urodzonym w 2019 roku z podziałem na województwa. 

Zwizualizowane zostały dwa pliki:
- Imiona żeńskie nadane dzieciom w Polsce w 2019 r. wg województw - imię pierwsze 
  (link: https://dane.gov.pl/dataset/219,imiona-nadawane-dzieciom-w-polsce/resource/21452/table?page=1&per_page=20&q=&sort=)
- Imiona męskie  nadane dzieciom w Polsce w 2019 r. wg województw - imię pierwsze
  (link: https://dane.gov.pl/dataset/219,imiona-nadawane-dzieciom-w-polsce/resource/21450/table?page=1&per_page=20&q=&sort=)

Wynikiem wizualizacji jest raport PDF z 4 figurami: 
- Rozkład słupkowy dla każdego wojewówdztwa z top 5 imionami
- Wykres kołowy z rozkładem procentowym dla całego kraju
- Chmura imion dla całego kraju
- Mapa województw z najczęściej występującym imieniem w danym województwie.

Wykorzystane biblioteki języka Python: 
- Pandas
- Geopandas
- Matplotlib
- Wordcloud
- Unidecode

Plik json zawierający kontury województw:
https://raw.githubusercontent.com/deldersveld/topojson/master/countries/poland/poland-provinces.json

#English version

Visualisation of open data published by polish Ministry of Digital Affairs on page:
https://dane.gov.pl/dataset/219,imiona-nadawane-dzieciom-w-polsce
Data files include names given for newborns in 2019 divided by polish provinces.

Files used in the visualisation:
- Imiona żeńskie nadane dzieciom w Polsce w 2019 r. wg województw - imię pierwsze 
  (link: https://dane.gov.pl/dataset/219,imiona-nadawane-dzieciom-w-polsce/resource/21452/table?page=1&per_page=20&q=&sort=)
- Imiona męskie  nadane dzieciom w Polsce w 2019 r. wg województw - imię pierwsze
  (link: https://dane.gov.pl/dataset/219,imiona-nadawane-dzieciom-w-polsce/resource/21450/table?page=1&per_page=20&q=&sort=)

The result of visualization is PDF file with 4 figures:
- Bar plots for each province with top 5 names
- Pie chart with percentage distribution
- Word cloud with names
- Polish provinces map with top 1 name

Python's libraries used in the project:
- Pandas
- Geopandas
- Matplotlib
- Wordcloud
- Unidecode

Json file with provinces boundaries:
https://raw.githubusercontent.com/deldersveld/topojson/master/countries/poland/poland-provinces.json
