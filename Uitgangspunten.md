# Uitgangspunten

De volgende uitgangspunten gelden bij het samenstellen van de matrix:
  - De regels in dit document gaan over omgevingsdocumenten die worden aangeboden in de
    ‘Van plan to publicatie’ keten.  Vereisten aan deze documenten die nodig zijn
    voor correcte verwerking zijn hier wel in meegenomen. NJ: ik begrijp niet wat je met die laatste zin bedoelt. Het woord wel lijkt te suggereren dat er ook regels niet zijn meegenomen, maar dat staat er niet....
  - De regels in dit document zijn altijd herleidbaar tot (1) een standaard, (2) een koppelvlakafspraak of (3) een interne verwerkingsregel. Dit document is zelf dus geen bron van nieuwe regels.
  - Als gevolg hiervan is de Validatiematrix dus ook geen standaard, maar een werkafspraak. NJ: ik vind de term werkafspraak heel vreemd. Die gebruiken we voor heel iets anders. Ik zou , maar een werkafspraak weglaten
  - Voor sommige validatieregels geldt dat ze wijzen op een fout in de interne consistentie van de keten (bijvoorbeeld als een id wel bekend is in de LVBB maar niet in OZON). Wanneer één van deze regels een foutmelding genereert is dat  niet te wijten aan een fout in het aangeleverde bestand maar aan een ketenprobleem. Dit soort fouten wordt zoveel mogelijk afgevangen voordat ze bij de gebruiker terechtkomen.
  - Wijzigingen in dit document zijn altijd te herleiden tot wijzigingen in de standaard, of het expliciet maken van een regel die al in de standaard stond.
  - Opname van een regel in dit document betekent niet automatisch dat de regel in de keten wordt afgedwongen. Dit is te vinden in release notes van het betreffende ketenonderdeel.
  - Voor wijzigingsbeheer betekent dit dat de impact van dit document altijd klein is: de impact zit in het wijzigen van de standaard of in het feit dat de regel gaat worden afgedwongen.
  - Validatieregels worden zo nauwkeurig mogelijk gespecificeerd in natuurlijke taal, bijvoorbeeld door de richtlijnen van [RuleSpeak](https://www.rulespeak.com/nl/) toe te passen.
  - Een validatieregel heeft een eigenschap ernst met de waarde 'Blokkerend' of 'Waarschuwing'. Blokkerende validatieregels leiden tot afkeuring van het omgevingsdocument in de keten. Omgevingsdocumenten met Waarschuwing worden wel toegelaten in de keten maar resulteren in een melding aan de indiener. Waarschuwing kunnen bijvoorbeeld worden gebruikt om te melden dat een bepaalde constructie in de huidige versie van de standaard nog wel is toegestaan, maar in de toekomst niet meer.
  - Eigenaarschap van regels: voor het regelen van verantwoordelijkheden binnen de validatiematrix is het wenselijk om per regel een eigenaar aan te wijzen. Een begin hiervan is te vinden in de identificatie van de regels waar de letters aan het begin een indicatie zijn van de eigenaar. Dit wordt verder uitgewerkt in volgende versies van dit document.
