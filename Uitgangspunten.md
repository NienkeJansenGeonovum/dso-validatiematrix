# Uitgangspunten

De volgende uitgangspunten gelden bij het samenstellen van de matrix:
  - De regels in dit document gaan over documenten die worden aangeboden in de
    ‘Van plan to publicatie’ keten.  Vereisten aan deze document die nodig zijn
    voor correcte verwerking zijn hier wel in meegenomen.
  - De regels in dit document zijn altijd herleidbaar tot (1) een standaard, (2) een koppelvlakafspraak of (3) en interne verwerkingsregel. Dit document is zelf dus geen bron van nieuwe regels.
  - Als gevolg hiervan is de Validatiematrix dus ook geen standaard, maar een werkafspraak.
  - Voor sommige validatieregels geldt dat ze wijzen op een fout in de interne consistentie van de keten (bijvoorbeeld als een id wel bekend is in de LVBB maar niet in OZON). Wanneer één van deze regel een foutmelding genereert is dat  niet te wijten aan een fout in het aangeleverde bestand maar op een keten probleem. Dit soort fouten wordt zoveel mogelijk afgevangen voordat ze bij de gebruiker terechtkomen.
  - Wijzigingen in dit document zijn altijd te herleiden tot de wijziging in de standaard, of het expliciet maken van een regel die al in de standaard stond.
  - Dat een regel in dit document voorkomt betekent niet automatisch dat controle hierop in de keten is geïmplementeerd.
  - Welke regels zijn geïmplementeerd is te vinden in release notes van het betreffende ketenonderdeel.
  - Voor wijzigingsbeheer betekent dit dat de impact van dit document altijd klein is: de impact zit in het wijzigen van de standaard of in het feit dat de regel gaat worden afgedwongen.
  - Validatieregels worden zo nauwkeurig mogelijk gespecificeerd in natuurlijke taal, bijvoorbeeld door de richtlijnen van [RuleSpeak](https://www.rulespeak.com/nl/) toe te passen.
  - Een validatieregel heeft een eigenschap ernst met de waarde 'Blokkerend' of 'Waarschuwing'. Blokkerende validatieregels  leiden tot afkeuring van het document in de keten. Documenten met Waarschuwing resulteren in een melding aan de indiener. Waarschuwing kunnen bijvoorbeeld worden gebruikt om te melden dat een bepaalde constructie in de huidige versie van de standaard nog wel is toegestaan, maar in de toekomst niet meer.
  - Eigenaarschap van regels: voor het regelen van verantwoordelijkheden binnen de validatiematrix is het wenselijk om per regel een eigenaar aan te wijzen. Een begin hiervan is te vinden in de identificatie van de regels waar de letters aan het begin een indicatie zijn van de eigenaar. Dit wordt verder uitgewerkt in volgende versies van dit document.