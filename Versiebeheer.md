# Versiebeheer

## Versienamanagement

De versienummering van de validatiematrix maakt gebruik van [Semantic Versioning](https://semver.org/). In semantic versioning hebben release een MAJOR.MINOR.PATCH versienummer. Of iets een major of een minor change is worden de volgende regels gebruikt:

- Iedere wijziging van de validatiematrix waardoor documenten die eerder goedgekeurd werden maar nu niet meer valide zijn resulteren in een MAJOR wijziging. Dit betekent dat een toevoeging van een Blokkerende regel automatisch leidt tot een nieuwe MAJOR versie.
- Toevoegen, wijzigigen of verwijderen van een Waarschuwing is een Minor change.
- Het wijzigen of verwijderen van blokkerende regel  die niet resulteert in meer afgekeurde documenten is een MINOR change.
- Patches worden gebruikt voor het fixen van typefouten en andere wijzigingen die niet resulteren in een wijziging van wat er goed- en afgekeurd wordt.


## Wensen en Eisen List (WELT)
In de versiehistorie wordt met WELT-xx verwezen naar de Wensen en Eisen Lijst voor de TPOD-standaard. Deze lijst bevat meldingen en wijzigingsverzoeken die door gebruikers van de standaard zijn ingediend. De ingediende meldingen zijn te vinden via [https://www.geonovum.nl/geo-standaarden/omgevingswet/meldingen](https://www.geonovum.nl/geo-standaarden/omgevingswet/meldingen).


## Eedere versies van de validatiematrix 
De validatiematrix is eerder beschikbaar gesteld in de vorm van een spreadsheet.  De validatieregels in spreadsheet formaat zijn nog steeds beschikbaar en zijn te vinden via: [https://github.com/Geonovum/dso-validatiematrix/blob/main/Validatiematrix.xlsx](https://github.com/Geonovum/dso-validatiematrix/blob/main/Validatiematrix.xlsx). Deze spreadsheet bevat een aantal extra kolommen, deze zijn niet normatief. Uitleg van sommige extra kolommen in de spreadsheet:

| Kolom | Omschrijving |
|-------|--------------|
| geïmplementeerd |  Geeft aan of de validatie geïmplementeerd is in de keten. Omdat dit afhangt van de omgeving waarin gewerkt wordt is dit veld niet goed bij te houden.|
| meldingstekst | meldingstekst die getoond wordt als je niet aan de validatie voldoet |



## Wijzigingen in versie 1.5

| Validatieregel | Wijziging                  | 
|----------------|----------------------------|
| document       | Matrix omgezet van spreadsheet naar Respec          |
| OZON4006       | Regel toegevoegd n.a.v WELT-198 |
| OZON4007       | Regel toegevoegd n.a.v WELT-198 |
| OZON4008       | Regel toegevoegd n.a.v WELT-198 |
| OZON4009       | Regel toegevoegd n.a.v WELT-198 |
| OZON4010       | Regel toegevoegd n.a.v WELT-198 |