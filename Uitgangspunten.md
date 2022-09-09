# Uitgangspunten

De volgende uitgangspunten gelden bij het samenstellen van de matrix:
  - De regels in dit document gaan over de keten ‘Van plan to publicatie’.
  - De regels in dit document zijn altijd herleidbaar tot (1) een standaard, (2) een koppelvlakafspraak of (3) en interne verwerkingsregel. Dit document is zelf dus geen bron van nieuwe regels.
  - Voor sommige validatieregels geldt dat ze wijzen op een fout in de interne consistentie van de keten (bijvoorbeeld als een id wel bekend is in de LVBB maar niet in OZON). Wanneer één van deze regel een foutmelding genereert is dat  niet te wijten aan een fout in het aangeleverde bestand maar op een keten probleem. Dit soort fouten wordt zoveel mogelijk afgevangen voordat ze bij de gebruiker terechtkomen.
  - Wijzigingen in dit document zijn altijd te herleiden tot de wijziging in de standaard, of het expliciet maken van een regel die al uit de standaard was af te leiden.
  - Dat een regel in dit document voorkomt betekent niet automatisch dat controle hierop in de keten is geïmplementeerd.
  - Welke regels zijn geïmplementeerd is te vinden in release notes van de keten.
  - Voor wijzigingsbeheer betekent dit dat de impact van dit document altijd klein is: de impact zit in het wijzigen van de standaard of in het feit dat de regel gaat worden afgedwongen.
  - Validatieregels worden zo nauwkeurig mogelijk gespecificeerd in natuurlijke taal, bijvoorbeeld door de richtlijnen van RuleSpeak toe te passen.
  - Een validatieregel heeft een eigenschap ernst met de waarde 'Blokkerend' of 'Waarschuwing'. Blokkerende validatieregels  leiden tot afkeuring van het document in de keten. Documenten met Waarschuwing resulteren alleen een melding op aan de indiener. Waarschuwing kunnen bijvoorbeeld worden gebruikt om te melden dat een bepaalde constructie in de huidige versie van de standaard nog wel is toegestaan, maar in de toekomst wellicht niet meer. 


  De validatiematrix heeft drie kolommen:

  | kolom        | omschrijving |
  |--------------|--------------|
  | id           | Unieke identificatie van de validatieregel die gebruikt kan worden in communicatie over de regel |
  | ernst        | 'Blokkerend' of 'Waarschuwing'. Blokkerende regels leiden tot afkeuring van het document in de keten. Een waarschuwing resulteert niet tot afkeuring van het document maar levert een melding bij de indiener van het document. |
  | omschrijving | Eenduidige omschrijving van de validatieregel. |


