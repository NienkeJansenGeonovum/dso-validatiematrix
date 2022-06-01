# De validatiematrix

| id | omschrijving|
|:---|:------------|
|BHKV1004|Voor een ontwerpbesluit MAG GEEN tijdstempel worden meegeleverd|
|BHKV1005|Een Besluit (tekst:BesluitCompact of tekst:BesluitKlassiek) MOET een identificatie hebben die aangeeft dat het een Besluit betreft (data:soortWork = /join/id/stop/work_003)|
|BHKV1006|Als de tekst van een besluit een initiële versie van een RegelingCompact/RegelingKlassiek/RegelingVrijetekst bevat; dan MOET de metadata van de regeling aangeven dat het een Regeling betreft (data:soortwork = /join/id/stop/work_019).|
|BHKV1009|De eId van een BeoogdeRegeling MOET voorkomen in het Besluit (bij BesluitCompact in het besluit-deel; dus NIET in de WijzigBijlage; bij BesluitKlassiek in RegelingKlassiek ) danwel in de Rectificatie(in BesluitMutatie)|
|BHKV1010|Elke eId van een Tijdstempel MOET genoemd worden in het Besluit (bij BesluitCompact in het besluit-deel; dus NIET in de WijzigBijlage; bij BesluitKlassiek in RegelingKlassiek ) danwel in de Rectificatie(in BesluitMutatie).|
|BHKV1011|Elke eId van een Intrekking van een Regeling MOET genoemd worden in het Besluit (bij BesluitCompact in het besluit-deel; dus NIET in de WijzigBijlage; bij BesluitKlassiek in RegelingKlassiek ) danwel in de Rectificatie(in BesluitMutatie).|
|BHKV1014|Het element data:heeftBestanden MOET in aan de LVBB aangeleverde (G)IOs naar precies één bestand verwijzen.|
|BHKV1015|heeftGeboorteregeling MOET aanwezig zijn INDIEN soortWork=/join/id/stop/work_010 èn formaatinformatieobject=/join/id/stop/informatieobject/gio_002|
|BHKV1016|De identificatie van een InformatieObject MOET als soort werk '/join/id/stop/work_010' zijn|
|BHKV1017|De officiele titel van een informatieobject MOET gelijk zijn aan het FRBRWork|
|BHKV1018|De collectie gebruikt in de AKN identifier van een informatieobject MOET overeenkomen met zijn data:publicatieinstructie|
|BHKV1028|Als de tekst van een besluit een initiële versie van een tijdelijk regelingdeel (tekst:RegelingTijdelijkdeel) bevat; dan MOET de metadata van de regeling aangeven dat het om een tijdelijk regelingdeel gaat (data:soortwork = /join/id/stop/work_021).|
|BHKV1030|INDIEN een GIO één of meer locatiegroepen bevat MOET voor de GIO symbolisatie worden aangeleverd met verbeeldingsinformatie voor elke locatiegroep in de GIO.|
|BHKV1031|INDIEN een GIO kwalitatieve normwaarden bevat MOET symbolisatie voor deze GIO worden aangeleverd met verbeeldingsinformatie voor elke kwalitatieve normwaarde in de GIO.|
|BHKV1032|INDIEN een GIO kwantitatieve normwaarden bevat MOET symbolisatie voor deze GIO worden aangeleverd zodat voor elke kwantitatieve normwaarde in de GIO verbeeldingsinformatie beschikbaar is.|
|BHKV1033|De inhoud van alle voorkomens van consolideerbare informatieobjecten in data:informatieobjectRef MOETEN ook voorkomen als data:BeoogdInformatieobject|
|BHKV1036|De eId en de Instrumentversie van elk BeoogdInformatieobject bij een besluit MOET d.m.v. een corresponderende ExtIORef (attributen eId en ref komen overeen) genoemd worden in de regeling(mutatie).|
|BHKV1044|Een @wordt-versie in een besluit MOET gelijk zijn aan precies één meegeleverde FRBRExpression-identificatie in de data:regelingversieinformatie.|
|BHKV1046|Procedurestap Publicatie MAG NIET aangeleverd worden.|
|BHKV1047|Bij een definitief besluit MOGEN ALLEEN de volgende procedurestappen voorkomen: VaststellingOndertekeningEinde BezwaartermijnEinde Beroepstermijn|
|BHKV1048|Een definitief besluit MOET de procedurestap Ondertekening hebben.|
|BHKV1049|Bij een ontwerpbesluit MOGEN ALLEEN de volgende procedurestappen voorkomen:VaststellingOndertekeningBegin InzagetermijnEinde Inzagetermijn|
|BHKV1057|Bij een kennisgeving MOGEN ALLEEN de volgende procedurestappen voorkomen:Einde BezwaartermijnEinde BeroepstermijnBegin InzagetermijnEinde Inzagetermijn|
|BHKV1058|De FRBRExpression-identificatie van lvbba:RegelingVersieInformatie MOET 1) bij een regelingmutatie voorkomen als @wordt in een tekst:RegelingMutatie; of 2) bij een initiele regeling als @wordt in het besluit (Bij BesluitCompact in tekst:RegelingCompact; tekst:RegelingTijdelijkdeel of tekst:RegelingVrijetekst en bij BesluitKlassiek in tekst:RegelingKlassiek).|
|BHKV1059|Bij een Besluit(of Rectificatie) behorende informatieobjecten MOETEN direct meegeleverd worden bij betreffend Besluit danwel Rectificatie.|
|BHKV1060|Met een Besluit of Rectificatie meegeleverd informatieobject MOET behoren bij betreffend Besluit danwel Rectificatie.|
|BHKV1063|De eId van een data:Intrekking van een informatieobject MOET verwijzen naar de plaats in de RegelingMutatie waar de tekst:ExtIORef wordt verwijderd. (Dat is de eId van de tekst:ExtIORef 1) binnen een wijzig- of verwijder-actie van een bovenliggend element; 2) binnen een tekst:verwijder; of 3) binnen een tekst:verwijderdeTekst.)|
|BHKV1064|De module se:FeatureTypeStyle MAG ALLEEN bij een Geo-Informatieobject(GIO) aangeleverd worden|
|BHKV1065|De module gio:JuridischeBorgingVan MAG ALLEEN bij een Geo-Informatieobject(GIO) aangeleverd worden|
|BHKV9999|Interne fout|
|GEOMETRY.03.1|geometrie is afwezig |
|GEOMETRY.03.2|geometrie is ongeldig (zie functionele documentatie op: https://aandeslagmetdeomgevingswet.nl/ontwikkelaarsportaal/api-register/api/geo-validatieservice/)|
|GEOMETRY.03.5|geometrie niet conform crs configuratie |
|GEOMETRY.03.6|geometrie niet conform gmlType configuratie |
|GEOMETRY.03.7|geometrie niet conform geostandaard configuratie |
|LVBB0002|Het locatie opdracht-zipbestand MOET bij een validatieVerzoek/publicatieVerzoek aanwezig zijn in het bericht.|
|LVBB0003|Het opdracht-zipbestand MOET bij een validatieGBVerzoek/publicatieGBVerzoek aanwezig zijn op de aangegeven locatie.|
|LVBB1001|Opdracht.zip MOET een geldige zip zijn.|
|LVBB1002|Bestand opdracht.xml MOET aanwezig zijn in het aangeleverde zip-bestand.|
|LVBB1003|Bestand manifest.xml MOET aanwezig zijn in het aangeleverde zip-bestand.|
|LVBB1004|De bestandsnaam MAG geen ongeldige karakters bevatten.|
|LVBB1006|Valideert opdracht.xml tegen schema?|
|LVBB1008|Valideert manifest.xml tegen schema?|
|LVBB1009|Zijn alle bestanden genoemd in manifest aanwezig in zip?|
|LVBB1010|Worden alle bestanden aanwezig in zip genoemd in manifest?|
|LVBB1012|Is de combinatie OIN id en leveringId uniek?|
|LVBB1013|Plaatjes mogen geen transparantie hebben|
|LVBB1015|Valideert manifest-ow.xml tegen schema?|
|LVBB1016|Zijn alle bestanden genoemd in manifest-ow aanwezig in zip?|
|LVBB1017|Is het bestandsformaat van de afbeelding een formaat dat ondersteund wordt?|
|LVBB1018|Komt het gespecificeerde contenttype van een afbeelding overeen met het werkelijke contenttype?|
|LVBB1019|Komt het gespecificeerde contenttype voor in de lijst met toegestane mimetypes?|
|LVBB1020|Is het aangeleverde contenttype ingevuld?|
|LVBB1021|Komt het gespecificeerde contenttype overeen met het werkelijke contenttype?|
|LVBB1024|Manifest-ow.xml mag 1 doel bevatten|
|LVBB1025|In het manifest-OW mag het objecttype Geometrie niet voorkomen.|
|LVBB1026|In het manifest-OW mag een bestandsnaam niet eindigen op '.gml'|
|LVBB1027|Bestand manifest-ow.xml MOET aanwezig zijn in het aangeleverde zip-bestand bij:- "validatieOpdracht" van een besluit;- "publicatieOpdracht" van een besluit;- "valideerRegelingVersie";- "registreerRegelingVersie";- "valideerDoorleverenRegelingVersie";- "doorleverenRegelingVersie"|
|LVBB1028|Bestand manifest-ow.xml MAG NIET aanwezig zijn in het aangeleverde zip-bestand bij:- "validatieOpdracht" van een kennisgeving;- "publicatieOpdracht" van een kennisgeving;- "breekPublicatieAfOpdracht";- "valideerGio";- "publiceerGio";- "valideerCio";- "publiceerCio"|
|LVBB1032|Valideert manifest-bhkv.xml tegen schema?|
|LVBB1033|Zijn alle bestanden genoemd in manifest-bhkv aanwezig in zip?|
|LVBB1034|manifest-bhkv.xml mag 1 doel bevatten|
|LVBB1035|In het manifest-bhkv mag alleen het objecttype Geometrie voorkomen.|
|LVBB1036|In het manifest-bhkv moet een bestandsnaam eindigen op '.gml'|
|LVBB1037|Bestand manifest-bhkv.xml MOET aanwezig zijn in het aangeleverde zip-bestand bij:- "valideerRegelingVersie";- "registreerRegelingVersie";- "valideerDoorleverenRegelingVersie";- "doorleverenRegelingVersie"|
|LVBB1038|Bestand manifest-bhkv.xml MAG NIET aanwezig zijn in het aangeleverde zip-bestand bij:- "validatieOpdracht" van een besluit;- "publicatieOpdracht" van een besluit;- "validatieOpdracht" van een kennisgeving;- "publicatieOpdracht" van een kennisgeving;- "validatieDirecteMutatieOpdracht"- "directeMutatieOpdracht"- "breekPublicatieAfOpdracht";- "valideerGio";- "publiceerGio";- "valideerCio";- "publiceerCio"|
|LVBB1039|Worden alle bestanden aanwezig in zip genoemd in manifest-bhkv?|
|LVBB1501|De  datumBekendmaking binnen de opdracht MOET een datum in juiste formaat (JJJJ-MM-DD) zijn en mag niet in het verleden liggen.|
|LVBB1502|De AKN in de opdracht (indien aanwezig) moet als derde veld 'bill' hebben|
|LVBB1505|De opdracht moet de datum bekendmaking bevatten|
|LVBB1506|Het publicatiebestand, waarvan de naam in de opdracht is vermeld, moet aanwezig zijn|
|LVBB1507|Alle bestanden voorkomend in het manifest moeten door de regisseur zijn klaargezet en omgekeerd|
|LVBB1509|Het opdracht bestand moet in de database aanwezig zijn met de afgeproken naam|
|LVBB1510|De opdracht MOET een id-bevoegd-gezag bevatten|
|LVBB1511|De opdracht MOET een id-aanleveraar bevatten|
|LVBB1512|Geen machtiging aanwezig voor aanleveraar namens bevoegd-gezag op aanleverdatum|
|LVBB1513|Bij aanlevering van een GIO zonder besluit MOET  het 4e veld van de AKN van de publicatie de waarde "officialGazette" bevatten|
|LVBB1515|De (soort) aanlevering MOET een besluit of kennisgeving zijn met een geldige schemaversie|
|LVBB1516|Naam van consolidatiebestand MOET gelijk zijn aan 'consolidaties.xml'|
|LVBB1517|Bij aanlevering van een GIO zonder besluit MOET  het 4e veld van de AKN-Id van de Regelingversie de waarde "act" bevatten|
|LVBB1518|Bij aanlevering van een GIO zonder besluit MOET  het 4e veld van de JOIN-Id van de GIO de waarde "regdata" bevatten|
|LVBB1550|Het opdracht bestand moet bij afbreken aanwezig zijn voor opgegeven oin en idlevering|
|LVBB1551|Bij Afbreken moet de opgegeven AKN bestaan|
|LVBB1553|Bij Afbreken moet de datum bekendmaking van het af te breken besluit in de toekomst liggen|
|LVBB1554|Publicatie dat afgebroken moet worden moet niet al in afwachting zijn om afgebroken te worden.|
|LVBB1555|Publicatie dat afgebroken moet worden mag niet gepubliceerd zijn|
|LVBB1556|Besluit dat afgebroken moet worden mag geen regelingversie bepalen die al gepubliceerd is|
|LVBB1557|Besluit dat afgebroken moet worden mag geen informatie-object hebben die al gepubliceerd is|
|LVBB1558|Besluit dat afgebroken moet worden mag geen regelingversie bepalen die gebruikt als was-versie voor een mutatie in een ander besluit|
|LVBB1559|Bestand met consolidatie-procedurestappen bij besluit wacht om afgebroken te worden|
|LVBB1560|Voor een af te breken besluit MAG NIET een kennisgeving naar dit besluit verwijzen|
|LVBB1561|Een besluit MAG NIET afgebroken worden, indiena) bij dit besluit minimaal 1 Informatie-Object wordt vastgesteld, dat een geo-id bevat; enb) dit besluit het enige besluit is, dat een Informatie-Object vaststelt, dat deze geo-id bevat; enc) vanuit een regelingversie, die vastgesteld is door een ander besluit, wordt verwezen naar deze geo-id.|
|LVBB1562|Voor een af te breken publicatie MOET er een besluit aanwezig zijn bij een regelingversie, tenzij de regelingversie via een consolidatie is aangeboden|
|LVBB1563|Indien ingevuld, MOET voor een af te breken besluit de 'datum juridisch-werkend-vanaf' van de regelingversie een datum in de toekomst zijn|
|LVBB1564|Indien ingevuld, MOET voor een af te breken besluit de 'datum juridisch-werkend-vanaf' van het InformatieObject een datum in de toekomst zijn|
|LVBB1571|Voor het verwerken van een aanlevering MOET de status van een opgestart proces (met gegeven status identifier) bekend zijn|
|LVBB1572|Voor het valideren van een aanlevering MOET een af te melden validatierapport bekend zijn|
|LVBB1573|Voor het valideren van een aanlevering MAG een eerder afgemeld validatierapport NIET opnieuw afgemeld worden|
|LVBB1600|Een Directe Mutatie op een Regelingversie MAG ALLEEN wanneer het Besluit, dat deze Regelingversie heeft vastgesteld, al gepubliceerd is|
|LVBB2002|Is er validatieplan aanwezig voor ConformProfiel|
|LVBB2003|Valideert het document tegen het imop schema?|
|LVBB2004|Is er een conformprofiel voor de regelingversie?|
|LVBB2008|Daar waar een AKN- of JOIN-identificatie wordt verwacht moet deze beginnen met akn of join|
|LVBB2009|Voor een AKN-identificatie (werk/expressie) moet het tweede deel een geldig land zijn (ln, aw, cw, sx)|
|LVBB2010|Voor een AKN-identificatie (werk/expressie) moet het derde deel een geldig type zijn (bill, act, doc, officialGazette)|
|LVBB2011|Voor een JOIN-identificatie (werk/expressie) moet het tweede deel geljk zijn aan 'id' of 'set'.|
|LVBB2012|Voor een JOIN-identificatie (werk/expressie) moet het derde deel een geldig type zijn (regdata, pubdata, infodata, proces, stop)|
|LVBB2013|Voor een AKN- of JOIN identificatie (werk/expressie) moet het vijfde deel een jaartal zijn of een geldige datum zijn|
|LVBB2015|Als voor een JOIN-identificatie (expressie) het eerste deel na de '@' een jaartal is dan moet dat gelijk zijn of groter dan het jaartal in het werk deel (vijfde deel)|
|LVBB2016|Voor een AKN- of JOIN-identificatie (expressie) moet deel voorafgaand aan de '@' een geldige taal zijn ('nld','eng','fry','pap','mul','und')|
|LVBB2017|Een AKN- of JOIN-identificatie mag geen punt bevatten|
|LVBB2019|Een AKN- of JOIN-identificatie MOET uit 7 delen bestaan tussen eerste '/' en '@'|
|LVBB2020|Het zevende deel van een AKN- of JOIN-identificatie MAG ALLEEN (hoofd)letters, cijfers en scheidingstekens (_ of -) ertussen bevatten|
|LVBB2021|Het zevende deel van een AKN- of JOIN-identificatie MAG NIET meer dan 128 tekens bevatten|
|LVBB2022|Het deel van de akn, dat volgt op 'officialGazette', MOET gelijk zijn aan de indicatie van een publicatie (stb, stcrt, trb, gmb, prb, bgr, wsb)|
|LVBB2501|Domeinmanifest bestaat niet|
|LVBB2502|Domeinmanifest moet doel hebben|
|LVBB2503|Doel in domeinmanifest moet bestaan|
|LVBB2504|De bestanden genoemd in het domeinmanifest moeten meegeleverd zijn|
|LVBB2505|Het doel moet gekoppeld zijn aan regelingversies, die horen bij de regeling die in het domeinmanifest staat|
|LVBB2511|Bestand 'manifest-bhkv.xml' MOET aanwezig zijn|
|LVBB2512|Bestand 'manifest-bhkv.xml' MOET doel hebben|
|LVBB2513|Doel in bestand 'manifest-bhkv.xml' MOET bestaan|
|LVBB2514|De bestanden genoemd in het bestand 'manifest-bhkv.xml' moeten meegeleverd zijn|
|LVBB2515|Het doel moet gekoppeld zijn aan regelingversies, die horen bij de regeling die in het bestand 'manifest-bhkv.xml' staat|
|LVBB2516|De bestanden genoemd in het bestand 'manifest-bhkv.xml' moeten meegeleverd zijn|
|LVBB3000|De GML van een afzonderlijke locatie (binnen de GIO) MAG NIET groter zijn dan xx MB|
|LVBB3002|Zijn de geometrieën toegestaan volgens STOP/TP: Simple Features Profile 2 (SF2) geometrieën exclusief cirkels en bogen|
|LVBB3003|Controleer of srsName (coördinatensysteem) is opgegeven voor de geometrieën. (dimension ook)|
|LVBB3004|Kan MarkLogic de gml opslaan?|
|LVBB3008|Klopt de meegeleverde hash met de zelf berekende hash voor informatie-objecten|
|LVBB3009|Valideert het gml document tegen het schema bij Geometrie?|
|LVBB3010|Valideert het gml document tegen het schema bij BasisGeometrie?|
|LVBB3011|Elk GML-element MOET complete coördinaten bevatten|
|LVBB3012|Elk GML-element MOET een ingevulde <gml:posList> bevatten|
|LVBB3020|Voor het verwerken van een aanlevering MOET de status van een opgestart proces (met gegeven status identifier) bekend zijn|
|LVBB3021|Voor het valideren van een aanlevering MOET een af te melden validatierapport bekend zijn|
|LVBB3022|Voor het valideren van een aanlevering MAG een eerder afgemeld validatierapport NIET opnieuw afgemeld worden|
|LVBB3501|Valideert het document tegen de versie-informatie bij het io schema?|
|LVBB3502|Het derde deel van de JOIN identificatie van een InformatieObject moet gelijk zijn aan pubdata|
|LVBB3504|Alle InformatieObjecten genoemd in de lijst met InformatieObjectRefs bij de BesluitMetadata MOETEN meegeleverd zijn|
|LVBB3506|GML bestand genoemd in IO is niet meegeleverd|
|LVBB3507|Het content-type van het meegeleverd bestand bij de IO is 'application/pdf' of 'application/gml+xml' |
|LVBB3508|De aangeleverde IO's mogen niet bestaan|
|LVBB3509|Elk aangeleverd InformatieObject MOET aanwezig zijn in de lijst met InformatieObjectRefs bij de BesluitMetadata.|
|LVBB3510|Geboorteregeling in een informatie-object moet voorkomen als regeling in het besluit|
|LVBB3511|Werk van join-id in informatie-object moet gelijk zijn aan die in bijbehorend GML-bestand|
|LVBB3512|Join-id in informatie-object moet gelijk zijn aan die in bijbehorend GML-bestand|
|LVBB3513|InformatieObjectMetadata MOET aanwezig zijn in het aangeleverde informatie-object, INDIEN een informatie-object betrekking heeft op een nieuw werk|
|LVBB3514|Alle InformatieObjecten, waaraan gerefereerd wordt in deze aanlevering, MOETEN meegeleverd zijn of in de LVBB-database (CDS) opgeslagen zijn voordat verdere verwerking kan plaatsvinden|
|LVBB3515|De informatieobjectversie (expressie-nivo), waarnaar de JOIN-identificatie in 'wasID' verwijst, MOET tot hetzelfde informatieobject (work-nivo) horen|
|LVBB3516|De informatieobjectversie (expressie-nivo), waarnaar de JOIN-identificatie in 'wasID' verwijst, MOET van hetzelfde informatieobject (work-nivo) de (enige) informatieobjectversie zijn, waarbij de einddatum (nog) onbekend is|
|LVBB3517|Ext-io-ref in besluit of consolidatie (m.b.t. JOIN-id) MAG GEEN voorloopspaties, naloopspaties of regelovergangen bevatten|
|LVBB3800|Het in te trekken Informatie-Object (op werk-nivo) MOET bestaan|
|LVBB3801|Het in te trekken Informatie-Object (op werk-nivo) MAG NIET al ingetrokken zijn|
|LVBB3802|Het in te trekken Informatie-Object (op werk-nivo) MOET minimaal 1 openstaande expressie bevatten|
|LVBB3900|Van alle aanleveringen MOET de Expressie-id van een Informatie Object uniek zijn|
|LVBB3901|Van alle aanleveringen MOET de Werk-id van een Informatie Object uniek zijn|
|LVBB4001|Is het AKN ID van het werk dat het BG aan Besluit heeft toegekend uniek?|
|LVBB4002|Elk WijzigArtikel of WijzigLid moet een verwijzing hebben naar een WijzigBijlage en omgekeerd|
|LVBB4005|De AKN door het bevoegd gezag aangeleverde regeling moet als derde veld 'act' hebben|
|LVBB4006|Er kan geen AMvB verwerkt worden omdat het daarvoor noodzakelijke gegeven met het staatsblad id niet in de aanlevering zit|
|LVBB4007|soortProcedure van de eerste RegelingMetadata in een besluit moet beginnen met '/join/id/stop/regelingtype_0' (zodat van daaruit later juiste waardes kunnen worden bepaald)|
|LVBB4014|Is wordt-versie nog niet aanwezig?|
|LVBB4015|Bestaat was-versie?|
|LVBB4017|Datum ondertekening moet aanwezig zijn in het besluit|
|LVBB4032|Elke AKN wordt-expressie in mutatie-element moet voorkomen als instrumentVersie in BeoogdeRegeling en omgekeerd (daarbij ook lettend op de IO die voor kunnen komen)|
|LVBB4033|Elke AKN wordt-expressie in mutatie-element moet voorkomen als FRBRExpression in ExpressionIdentificatie van RegelingVersieInformatie en omgekeerd|
|LVBB4034|Publicatie (besluit of kennisgeving) MOET een AKN identificatie bevatten voor het werk of de expressie|
|LVBB4036|De waardelijst behorend bij de schema-versie moet aanwezig zijn |
|LVBB4037|De waarde van tooi-identifiers in het besluit moet allemaal teruggevonden kunnen worden in de waardelijst|
|LVBB4038|Subitems genoemd in de publicatie moeten meegeleverd zijn en omgekeerd|
|LVBB4039|De mimetype van een subitem in het document moet gelijk zijn aan het aangeleverde mimetype|
|LVBB4040|RegelingMetadata MOET aanwezig zijn in het aangeleverde besluit, INDIEN een Regelingversie betrekking heeft op een nieuwe regeling|
|LVBB4041|JOIN-id van de GIO op werkniveau MOET een waarde bevatten tussen de 4e '/' en de 5e '/'|
|LVBB4042|De code van de eindverantwoordelijke MOET ingevuld zijn met een waarde uit de afgesproken (toegestane) waardelijst|
|LVBB4043|Regeling is opvolger van een intrekking, maar wordt niet ingetrokken volgens consolidatie-informatie |
|LVBB4044|soortWork van de Regeling MOET "/join/id/stop/work_021" zijn, indien het een RegelingTijdelijkDeel betreft; indien het geen RegelingTijdelijkDeel betreft MOET soortWork "/join/id/stop/work_019" zijn|
|LVBB4045|Een (unieke) RegelingVersieInformatie MAG alleen bij 1 element horen|
|LVBB4200|De 'datum JWV' van een wordt-versie MOET later zijn dan de 'datum JWV' van de was-versie|
|LVBB4201|Indien de was-versie een 'datum JWV'-einde heeft , dan MOET de 'datum JWV' van de wordt-versie eerder dan deze 'datum JWV'-einde zijn|
|LVBB4202|De 'datum JWV' van de wordt-versie moet gelijk zijn aan vandaag of een datum in de toekomst zijn|
|LVBB4204|Als de was-versie geen 'datum JWV' heeft dan moet de wordt-versie ook geen 'datum JWV' hebben.|
|LVBB4701|Het AKN ID van het werk dat het bevoegd gezag aan de Kennisgeving heeft toegekend moet uniek zijn|
|LVBB4702|Het besluit benoemd in de Kennisgeving in 'mededelingOver' moet reeds aanwezig zijn in de LVBB (in een eerdere aanlevering zijn aangeleverd).|
|LVBB4703|Datum begin inzagetermijn mag niet liggen voor datum bekendmaking kennisgeving[zoals benoemd in de opdracht.xml]|
|LVBB4704|Datum begin inzagetermijn mag niet liggen voor datum bekendmaking van gerelateerd besluit[zoals benoemd onder 'mededelingOver']|
|LVBB4705|Besluit met akn-id %1 horende bij deze kennisgeving heeft nog geen publicatie akn-identifier|
|LVBB4707|Derde veld waarde akn bij kennisgeving moet gelijk zijn aan 'doc'|
|LVBB4708|Derde veld waarde 'mededeling-over' in kennisgeving moet gelijk zijn aan 'bill'|
|LVBB4711|Kennisgeving MAG niet eerder gepubliceerd zijn|
|LVBB4712|Datum bekendmaking bij kennisgeving MAG niet in het verleden (= voor huidige dag) zijn|
|LVBB4713|Kennisgeving wacht om afgebroken te worden|
|LVBB4714|Besluit bij kennisgeving wacht om afgebroken te worden|
|LVBB4715|Kennisgeving MOET de laatste kennisgeving bij hetzelfde besluit zijn (om te kunnen afbreken)|
|LVBB4716|Bestand met consolidatie-procedurestappen behorend bij kennisgeving wacht om afgebroken te worden|
|LVBB4734|Een Kennisgeving MOET een AKN identificatie voor de het werk of voor de expressie bevatten|
|LVBB4737|De waarde van tooi-identifiers in de kennisgeving moet teruggevonden kunnen worden in de waardelijst|
|LVBB4750|In het resultaat van het procedureverloop van een (ontwerp)besluit en alle kennisgevingen over dit besluit mag elke code bij een procedurestap maximaal 1 keer voorkomen|
|LVBB4751|Het is niet mogelijk om een procedurestap te wijzigen of verwijderen die nog niet eerder is aangeleverd|
|LVBB4753|Het type procedureverloop MOET passen bij het type besluit waarvan het de procedure beschrijft.|
|LVBB4754|Soort stap MAG NIET aanwezig zijn in het besluit of de kennisgeving|
|LVBB4755|De procedurestappen MOGEN NIET dubbel voorkomen|
|LVBB4756|De datum bekend-op van de kennisgeving MOET liggen na de datum bekend-op van een eerdere consolidatie|
|LVBB4757|De datum ontvangen-op van de kennisgeving MOET liggen na de datum ontvangen-op van een eerdere consolidatie|
|LVBB4758|De datum einde inzagetermijn MOET later dan of gelijk zijn aan de datum begin inzagetermijn|
|LVBB4759|Datum bekendmaking kennisgeving %1 mag niet voor datum bekend op van het besluit %2 liggen |
|LVBB4760|Bij een kennisgeving ontwerp besluit MOGEN ALLEEN de volgende procedurestappen voorkomen:Begin inzagetermijnEinde inzagetermijn|
|LVBB4761|Bij een kennisgeving van een definitief besluit MOGEN ALLEEN de volgende procedurestappen voorkomen:Einde bezwaartermijnEinde beroepstermijn|
|LVBB4762|Bij een aanlevering van een kennisgeving MOET procedureverloopmutatie een waarde bevatten anders dan "vervangStappen" of "verwijderStappen"|
|LVBB5002|Indien een element verwijderd of vervangen moet worden, MOET dit element met aangegeven wId bestaan bij aangegeven regelingversieOF:Indien een element toegevoegd moet worden, MAG dit element met aangegeven wId NIET bestaan bij desbetreffend element in desbetreffende regelingversie, waaraan dit element moet worden toegevoegd|
|LVBB5005|De wordt-versie moet gevuld zijn|
|LVBB5006|De was-versie moet gevuld zijn bij niet-initiele mutaties|
|LVBB5007|De was-versie mag niet door een ontwerp besluit aangemaakt zijn|
|LVBB5008|De was-versie mag niet aangemaakt zijn door een besluit dat in afwachting is om afgebroken te worden|
|LVBB5009|De 'soort work' van de was-versie MOET gelijk zijn aan de 'soort work' van de wordt-versie|
|LVBB5010|VoegToe: bestaat het toe te voegen element nog niet|
|LVBB5011|Er mag maar een toelichting voorkomen bij toevoegen|
|LVBB5012|De regeling bij de was- en wordt-verie mag niet ingetrokken zijn|
|LVBB5013|Een in te trekken regeling MOET juridisch werkend zijn, d.w.z. een openstaande versie van dezelfde regeling hebben|
|LVBB5014|Een in te trekken regeling MOET (eerder) geregistreerd zijn|
|LVBB5015|De was-versie binnen de regeling MAG NIET eerder gebruikt zijn als versie-gebaseerd-op|
|LVBB5016|Het in te trekken Informatie-Object (op werk-nivo) MOET bestaan|
|LVBB5017|Het in te trekken Informatie-Object (op werk-nivo) MAG NIET al ingetrokken zijn|
|LVBB5018|Het in te trekken Informatie-Object (op werk-nivo) MOET minimaal 1 openstaande expressie bevatten|
|LVBB6000|Valideert de AfwijkVergunning tegen het imop <?> schema?|
|LVBB6001|Voor publicatie van de afwijkvergunning MAG de uri van elke nieuwe Doorlever-zip NIET bestaan|
|LVBB6002|Voor de afwijkvergunning MOET elk metadata-document, waarnaar vanuit de publicatie verwezen wordt, gevonden worden|
|LVBB6003|Voor de afwijkvergunning MOET elk GML-document, waarnaar vanuit de publicatie verwezen wordt, gevonden worden|
|LVBB7001|Lukt het expanderen van de toestand?|
|LVBB7003|Doel moet versies gekoppeld hebben op het moment dat er een datum inwerking wordt meegegeven|
|LVBB7004|Voor een regelingversie, aangeduid met een specifiek doel binnen een aangegeven regeling, MAG dit doel en bijbehorende datums maar 1 keer toegevoegd worden (en kan niet meer gewijzigd worden)|
|LVBB7005|Twee versies binnen dezelfde regeling moeten verschillende datums juridisch werkend vanaf hebben|
|LVBB7006|Versie gekoppeld aan doel bestaat niet|
|LVBB7007|Informatie-object gekoppeld aan doel bestaat niet|
|LVBB7008|Ingetrokken regeling gekoppeld aan doel bestaat niet|
|LVBB7009|Ingetrokken informatie-object (werk-nivo), dat gekoppeld is aan doel, MOET bestaan|
|LVBB7501|Valideert de RegelingVersie tegen het imop schema?|
|LVBB7502|Valideert de Consolidaties tegen het imop schema?|
|LVBB7503|Valideert de UitleveringProefversiebesluit tegen het imop schema?|
|LVBB7504|Valideert de WTI (WetTechnischeInformatie) tegen het imop <?> schema?|
|LVBB7701|Aantal Bekende Toestanden MOET 1 zijn|
|LVBB7702|Aantal Toestanden met samenloop MOET 0 zijn|
|LVBB7703|Aantal Doelen MOET 1 zijn|
|LVBB7704|Aantal Geldigheidsperiodes MOET 1 zijn|
|LVBB7705|Aantal RegelingVersies MOET 1 zijn|
|LVBB7706|Aantal Annotaties bij Toestand MOET 1 zijn|
|LVBB7707|Aantal RegelingMetadata MOET 1 zijn|
|LVBB7708|AKN aanvullend type MOET 'act' zijn|
|LVBB7709|AKN van de AnnotatieBijToestand moet een 5e veld hebben dat gelijk is aan "gemeente", "provincie", "waterschap" of  "ministerie"|
|LVBB7713|AKN van cvdr-werk-boven bij ConsolidatieIdentificatie MOET gelijk zijn aan AKN van cvdr-werk-onder bij AnnotatieBijToestand|
|LVBB7714|AKN van cvdr-expressie-boven bij ConsolidatieIdentificatie MOET gelijk zijn aan AKN van cvdr-expressie-onder bij AnnotatieBijToestand|
|LVBB7715|AKN van cvdr-werk-boven bij ConsolidatieIdentificatie MOET gelijk zijn aan AKN van cvdr-werk-onder bij RegelingVersie|
|LVBB7716|AKN van cvdr-expressie-boven bij Toestanden MOET gelijk zijn aan AKN van cvdr-expressie-onder bij RegelingVersie |
|LVBB7717|AKN van cvdr-werk-boven bij ConsolidatieIdentificatie MOET gelijk zijn aan werk van AKN van cvdr-expressie-boven bij ConsolidatieIdentificatie|
|LVBB7718|AKN van cvdr-werk-onder bij AnnotatieBijToestand MOET gelijk zijn aan werk van AKN van cvdr-expressie-onder bij AnnotatieBijToestand|
|LVBB7719|AKN van bevoegd gezag werk-boven bij ConsolidatieIdentificatie MOET gelijk zijn aan werk van AKN van bevoegd gezag expressie-boven bij Toestanden|
|LVBB7720|AKN van bevoegd gezag werk-onder bij RegelingVersie MOET gelijk zijn aan AKN van bevoegd gezag expressie-onder bij RegelingVersie|
|LVBB7721|soortWork regeling in ConsolidatieIdentificatie MOET gelijk zijn aan "/join/id/stop/work_006"|
|LVBB7722|soortWork geconsolideerde regeling in ConsolidatieIdentificatie MOET gelijk zijn aan "/join/id/stop/work_019"|
|LVBB7723|soortWork regeling in RegelingVersie MOET gelijk zijn aan "/join/id/stop/work_019"|
|LVBB7724|soortWork geconsolideerde regeling in AnnotatieBijToestand MOET gelijk zijn aan "/join/id/stop/work_006"|
|LVBB7725|'Datum bekend op' MOET voldoen aan het formaat JJJJ-MM-DD'|
|LVBB7726|'Datum bekend op' MOET een geldige datum bevatten|
|LVBB7728|Aantal Consolidaties MOET 1 zijn|
|LVBB7729|Aantal Toestanden MOET 1 zijn|
|LVBB7730|Soort werk InformatieObject in ConsolidatieIdentificatie MOET gelijk zijn aan "/join/id/stop/work_005"|
|LVBB7731|Soort werk geconsolideerde InformatieObject in ConsolidatieIdentificatie MOET gelijk zijn aan "/join/id/stop/work_010"|
|LVBB7732|Soort werk InformatieObject in InformatieObjectVersie MOET gelijk zijn aan "/join/id/stop/work_010"|
|LVBB7733|Soort werk geconsolideerde InformatieObject in AnnotatieBijToestand MOET gelijk zijn aan "/join/id/stop/work_005"|
|LVBB7734|Voor interne opdracht "valideerRegelingVersie", "registreerRegelingVersie", "valideerCIO" of "publiceerCIO" MOET voor een bij consolidatie meegeleverd informatieobject een schemaversie opgegeven zijn|
|LVBB7735|Voor interne opdracht "valideerRegelingVersie", "registreerRegelingVersie", "valideerCIO" of "publiceerCIO" MOET elk bij consolidatie in opdracht vermeld informatieobject meegeleverd zijn|
|LVBB8001|Valideert de OfficielePublicatie tegen het imop schema?|
|LVBB9400|Referentierapport OW MOET 1 doel en (bij dat doel) 1 wIdRegeling bevatten|
|LVBB9900|Niet (meer) ondersteunde versie van STOP/BHKV|
|OZON0010|Het objectType in het standbestand moet een Activiteit, Divisie, Gebiedsaanwijzing, Gebied, Gebiedengroep, Hoofdlijn, Punt, Puntengroep, Lijn, Lijnengroep, Regeltekst, RegelVoorIedereen, Instructieregel, Omgevingswaarderegel, Omgevingsnorm, Omgevingswaarde, Pons, Tekstdeel, Kaart, Kaartlaag, Ambtsgebied of Divisietekst zijn.|
|OZON0013|Het type van het owObject moet voorkomen in de lijst objectTypen in de inhoud.|
|OZON0017|Er moet een RegelVoorIedereen zijn die verwijst naar de Activiteit.|
|OZON0021| (TPOD1760) Een Gebiedsaanwijzing moet alleen verwijzen naar locaties van het type Gebied of Gebiedengroep|
|OZON0022|Er moet een RegelVoorIedereen, Instructieregel of Tekstdeel zijn die verwijst naar de Gebiedsaanwijzing|
|OZON0026|Er moet een RegelVoorIedereen of een Instructieregel zijn die verwijst naar de Omgevingsnorm.|
|OZON0030|Er moet een Omgevingswaarderegel zijn die verwijst naar de Omgevingswaarde.|
|OZON0033|Iedere RegelVoorIedereen verwijst naar een Regeltekst die bestaat.|
|OZON0035|Iedere Instructieregel verwijst naar een Regeltekst die bestaat.|
|OZON0037|Iedere Omgevingswaarderegel verwijst naar een Regeltekst die bestaat.|
|OZON0038|Als een RegelVoorIedereen verwijst naar een Activiteit, dan moet deze bestaan.|
|OZON0040|Als een RegelVoorIedereen verwijst naar een Gebiedsaanwijzing, dan moet deze bestaan.|
|OZON0041|Als een Instructieregel verwijst naar een Gebiedsaanwijzing, dan moet deze bestaan.|
|OZON0042|Als een RegelVoorIedereen verwijst naar een Omgevingsnorm, dan moet deze bestaan.|
|OZON0043|Als een Instructieregel verwijst naar een Omgevingsnorm, dan moet deze bestaan.|
|OZON0044|Als een Omgevingswaarderegel verwijst naar een Omgevingswaarde, dan moet deze bestaan.|
|OZON0045|Iedere RegelVoorIedereen moet verwijzen naar een of meerdere Locaties die bestaan.|
|OZON0046|Iedere InstructieRegel moet verwijzen naar een of meerdere Locaties die bestaan.|
|OZON0047|Iedere OmgevingswaardeRegel moet verwijzen naar een of meerdere Locaties die bestaan.|
|OZON0053|Iedere Gebiedengroep moet verwijzen naar Gebieden die bestaan.|
|OZON0059|Iedere Lijnengroep moet verwijzen naar Lijnen die bestaan.|
|OZON0065|Iedere Puntengroep moet verwijzen naar Punten die bestaan.|
|OZON0066|Voor ieder Gebied moet er een Geometrie aanwezig zijn in de levering.|
|OZON0067|Voor iedere Lijn moet er een Geometrie aanwezig zijn in de levering.|
|OZON0068|Voor ieder Punt moet er een Geometrie aanwezig zijn in de levering.|
|OZON0069|(TPOD940) Als een Locatie uit meer dan één geometrie bestaat, dan moeten de geometrieën volgens dezelfde coordinate reference system (crs) zijn opgebouwd.|
|OZON0070|Het veld RegelVoorIedereen.activiteitregelkwalificatie moet een waarde bevatten uit de waardelijst ActiviteitRegelkwalificatie.|
|OZON0071|Het veld Instructieregel.instructieregelTaakuitoefening moet een waarde bevatten uit de waardelijst Adressaat.|
|OZON0072|Het veld Instructieregel.instructieregelInstrument moet een waarde bevatten uit de waardelijst InstructieregelInstrument.|
|OZON0073|Het veld Activiteiten.groep moet een waarde bevatten uit de waardelijst Activiteitengroep.|
|OZON0074|Het veld Omgevingsnormgroep.groep moet een waarde bevatten uit de waardelijst Omgevingsnormgroep.|
|OZON0075|Het veld Omgevingswaarde.groep moet een waarde bevatten uit de waardelijst Omgevingswaardegroep.|
|OZON0076|Het veld Gebiedsaanwijzing.type moet een waarde bevatten uit de waardelijst TypeGebiedsaanwijzing.|
|OZON0077|Het veld RegelVoorIedereen.idealisatie moet een waarde bevatten uit de waardelijst Idealisatie.|
|OZON0078|Het veld Instructieregel.idealisatie moet een waarde bevatten uit de waardelijst Idealisatie.|
|OZON0079|Het veld Omgevingswaarderegel.idealisatie moet een waarde bevatten uit de waardelijst Idealisatie.|
|OZON0080|Het veld Gebiedsaanwijzing-groep moet een waarde bevatten uit de waardelijst Gebiedsaanwijzing-groep van het bijbehorende Gebiedsaanwijzing-Type. |
|OZON0082|(TPOD1730/TPOD1740) Iedere Activiteit moet verwijzen naar een bovenliggende activiteit die bestaat in de levering of in Ozon.|
|OZON0083|(TPOD1700/TPOD1710) Een Activiteit mag niet zichzelf als bovenliggende Activiteit hebben. Ook niet via andere bovenliggende activiteiten.|
|OZON0084|(TPOD1730/TPOD1740) Als een Activiteit gerelateerde Activiteiten heeft, dan moeten deze bestaan in de levering of in Ozon.|
|OZON0085|(TPOD1700/TPOD1710) Een Activiteit mag niet gerelateerd zijn aan zichzelf.|
|OZON0086|Naar iedere aangeleverde geometrie moet verwezen worden door een locatie|
|OZON0090|Iedere Divisie moet verwijzen naar een of meerdere Tekstdelen.|
|OZON0092|Ieder Tekstdeel verwijst naar een Divisie of Divisietekst die bestaat.|
|OZON0093|Als een Tekstdeel verwijst naar een Gebiedsaanwijzing, dan moet deze bestaan.|
|OZON0094|Als een Tekstdeel verwijst naar een Hoofdlijn, dan moet deze bestaan.|
|OZON0096|Iedere gebiedsaanwijzing moet verwijzen naar een of meerdere locaties die bestaan.|
|OZON0097|(TPOD1650) Iedere Normwaarde moet ofwel een kwalitatieve, ofwel een kwantitatieve waarde hebben.|
|OZON0098|(TPOD1850) Een Regeltekst die verwijst naar een RegelVoorIedereen, mag niet naar een Instructieregel of Omgevingswaarderegel verwijzen.|
|OZON0099|(TPOD1850)  Een Regeltekst die verwijst naar een RegelVoorIedereen, mag niet naar een Instructieregel of Omgevingswaarderegel verwijzen.|
|OZON0100|(TPOD1850) Een Regeltekst die verwijst naar een RegelVoorIedereen, mag niet naar een Instructieregel of Omgevingswaarderegel verwijzen.|
|OZON0101|Een Normwaarde moet verwijzen naar een locatie die bestaat.|
|OZON0102|Een Regeltekst moet verwijzen naar één of meer Juridische Regels.|
|OZON0103|(TPOD2180) Per Regeling moet er een Regelingsgebied zijn aangeleverd.|
|OZON0105|Het wijzigen van een OW-object mag alleen indien bij het doel het attribuut juridischWerkendVanaf aan de OP-kant dezelfde datum is of een recentere datum heeft dan juridischWerkendVanaf bij het vorige bekende doel van het OW-object.|
|OZON0106|Het wijzigen van een OW-object mag alleen indien bij het doel het attribuut geldigVanaf aan de OP-kant dezelfde datum is of een recentere datum heeft dan geldigVanaf bij het vorige bekende doel van het OW-object.|
|OZON0107|Het beëindigen van een OW-object mag alleen als de inhoud exact overeenkomt met de laatst aangeleverde OW-informatie.|
|OZON0108|Het aanleveren van een OW-object mag alleen indien de gegevens aangepast zijn t.o.v. de vorige versie van het OW-object.|
|OZON0109|OW-informatie waar naar verwezen wordt vanuit andere OW-informatie moet bestaan.|
|OZON0110|(geen wijzigingen met terugwerkende kracht) de datum geldigVanaf van de OW-informatie (met deze identificatie) mag niet voor datum inwerkingVanaf van deze zelfde OW-informatie (met deze identificatie) liggen. (tijdelijk)|
|OZON0111|Als een OW-object beëindigd is kan deze niet meer worden gewijzigd. (tijdelijk)|
|OZON0112|OW-objecten met een status anders dan 'B' worden niet verwerkt. (tijdelijk)|
|OZON0113|Het veld Omgevingsnorm.type moet een waarde bevatten uit de waardelijst TypeNorm.|
|OZON0114|Het veld Omgevingswaarde.type moet een waarde bevatten uit de waardelijst TypeNorm.|
|OZON0115|Het veld Omgevingsnorm.eenheid moet een waarde bevatten uit de waardelijst Eenheid.|
|OZON0116|Het veld Omgevingswaarde.eenheid moet een waarde bevatten uit de waardelijst Eenheid.|
|OZON0117|Het veld Instructieregel.thema moet een waarde bevatten uit de waardelijst Thema.|
|OZON0118|Het veld Omgevingswaarderegel.thema moet een waarde bevatten uit de waardelijst Thema.|
|OZON0119|Het veld RegelVoorIedereen.thema moet een waarde bevatten uit de waardelijst Thema.|
|OZON0120|Het veld Tekstdeel.thema moet een waarde bevatten uit de waardelijst Thema.|
|OZON0121|Iedere ActiviteitLocatieaanduiding moet verwijzen naar een of meerdere Locaties die bestaan.|
|OZON0122|Een ow-object mag alleen een status hebben met de waarde 'B' of geen status.|
|OZON0123|Het Ambtsgebied moet een geldige geldigOp-datum bevatten.|
|OZON0124|Een Regelingsgebied moet verwijzen naar een bestaande locatie|
|OZON0126|Een vastgesteld ow-object mag geen procedurestatus hebben.|
|OZON0127|Een ontwerp ow-object moet een procedurestatus met de waarde 'ontwerp' hebben.|
|OZON0128|Ontwerp symbolisatie-items worden nog niet ondersteund (tijdelijke validatie)|
|OZON0200|Elk type gebiedsaanwijzing in CIMOW is aanwezig in de waardelijst 'gebiedsaanwijzingstypen'|
|OZON0204|Als een Tekstdeel verwijst naar een locatie, dan moet deze bestaan.|
|OZON0205|Een activiteit moet altijd minstens één verwijzing naar een locatie hebben (conform RTRG0003). |
|OZON0210|Een levering mag niet de relatie tussen een regeltekst en het bijbehorende artikel of lid verbreken.|
|OZON0211|Een levering mag niet de relatie tussen een divisie/divisietekst en de bijbehorende (OP-)divisie/(OP-)divisietekst verbreken.|
|OZON0212|Bij een regeling met een gewijzigd workId moet een regelingsgebied meegeleverd zijn.|
|OZON0213|(RTRG0013) Als een activiteit van een gemeente verwijst naar een bovenliggende activiteit ook van een gemeente dan moet dit dezelfde gemeente zijn|
|OZON0214|(RTRG0014) Als een activiteit van een provincie verwijst naar een bovenliggende activiteit ook van een provincie dan moet dit dezelfde provincie zijn|
|OZON0215|(RTRG0015) Als een activiteit van een waterschap verwijst naar een bovenliggende activiteit ook van een waterschap dan moet dit hetzelfde waterschap zijn|
|OZON0216|Een Ambtsgebied moet verwijzen naar een geldig Bestuurlijk Gebied|
|OZON0217|Als een Pons verwijst naar een Locatie dan moet deze bestaan|
|OZON0218|Een Regeltekst mag niet voorkomen in een andere regeling (behalve bij intrekken vervangen; in de ingetrokken regeling|
|OZON0219|Een Divisie of Divisietekst mag niet voorkomen in een andere regeling (behalve bij intrekken vervangen; in de ingetrokken regeling).                         |
|OZON0220|Een vergunning moet een unieke gepubliceerdIn hebben|
|OZON0310|Identificaties van OW-objecten dienen globaal uniek te zijn.|
|OZON0320|Een regel voor iedereen mag niet twee keer verwijzen naar dezelfde locatie.|
|OZON0321|Een omgevingswaarderegel mag niet twee keer verwijzen naar dezelfde locatie.|
|OZON0322|Een instructieregel mag niet twee keer verwijzen naar dezelfde locatie.|
|OZON0324|Een regel voor iedereen mag niet twee keer verwijzen naar dezelfde omgevingsnorm.|
|OZON0325|Een regel voor iedereen mag niet twee keer verwijzen naar dezelfde omgevingswaarde.|
|OZON0326|Een regel voor iedereen mag niet twee keer verwijzen naar dezelfde gebiedsaanwijzing.|
|OZON0327|Een omgevingswaarderegel mag niet twee keer verwijzen naar dezelfde gebiedsaanwijzing.|
|OZON0328|Een instructieregel mag niet twee keer verwijzen naar dezelfde gebiedsaanwijzing.|
|OZON0329|Een instructieregel mag niet twee keer verwijzen naar dezelfde omgevingsnorm.|
|OZON0331|Een gebiedsaanwijzing mag niet twee keer verwijzen naar dezelfde locatie.|
|OZON0340|Een tekstdeel mag niet twee keer verwijzen naar dezelfde hoofdlijn.|
|OZON0341|Een tekstdeel mag niet twee keer verwijzen naar dezelfde locatie.|
|OZON0342|Een tekstdeel mag niet twee keer verwijzen naar dezelfde gebiedsaanwijzing.|
|OZON0343|Een regel voor iedereen mag niet twee keer verwijzen naar dezelfde kaart.|
|OZON0344|Een omgevingswaarderegel mag niet twee keer verwijzen naar dezelfde kaart.|
|OZON0345|Een instructieregel mag niet twee keer verwijzen naar dezelfde kaart.|
|OZON0346|Een tekstdeel mag niet twee keer verwijzen naar dezelfde kaart.|
|OZON0347|Een tekstdeel mag niet twee keer verwijzen naar dezelfde kaart.|
|OZON0348|Een regel voor iedereen mag niet twee keer verwijzen naar de zelfde activiteitlocatieaanduiding.|
|OZON0349|Als een kaartlaag verwijst naar een activiteitlocatieaanduiding, omgevingsnorm, omgevingswaarde of gebiedsaanwijzing, dan moet deze bestaan.|
|OZON0350|Wanneer een object wordt beëindigd, dan mag er geen ander object meer naar verwijzen.|
|OZON0351|Het beëindigen/wijzigen van een object mag niet leiden tot het verwezen van een ander object.|
|OZON0369|Een ActiviteitLocatieaanduiding mag niet twee keer verwijzen naar dezelfde Locatie.|
|OZON0370|Een Geometrie mag niet gebruikt worden in twee of meer OW-Locaties. (Mag altijd maar gebruikt worden in één OW-Locatie.)|
|OZON0371|Een activiteit mag niet twee keer verwijzen naar dezelfde gerelateerde activiteit|
|OZON0372|Een gebiedengroep mag niet twee keer verwijzen naar hetzelfde gebied|
|OZON0373|Een lijnengroep mag niet twee keer verwijzen naar dezelfde lijn.|
|OZON0374|Een puntengroep mag niet twee keer verwijzen naar dezelfde punt.   |
|OZON1019|Het bevoegd gezag moet het juiste format hebben: het moet eindigen met het type bevoegd gezag (ministerie, provincie, gemeente, waterschap), een /, en de organisatiecode, bijvoorbeeld ‘/gemeente/gm0037’. |
|OZON1020|Het soort regeling moet overeenkomen met de waardelijst soortregeling (uit OP-waardelijsten).|
|OZON1024|Een levering moet 1 of 2 toestanden bevatten.|
|OZON1025|Als een levering een regelingversie intrekt, dan moet deze bekend zijn bij Ozon.|
|OZON1026|Een initiele levering dient nog niet bekend te zijn bij Ozon.|
|OZON1027|Elke nieuwe regelingversie moet 1 doel hebben (tijdelijk).|
|OZON1028|De instrumentversie-identificatie van een nieuwe toestand moet overeenkomen met de FRBRExpression van de regelingversie.|
|OZON1029|Een nieuwe toestand moet aangeleverd worden met een regelingversie.|
|OZON1031|Als een RegelingVersie verwijst naar een afbeelding dan moet deze aanwezig zijn in de levering|
|OZON1032|Een Tijdelijk Deel moet verwijzen naar een bestaande RegelingVersie in de database|
|OZON1033|Intrekken/Vervangen van een RegelingVersie is niet toegestaan wanneer er een Tijdelijk Deel naar verwijst|
|OZON1034|Een ontwerp Ow-object mag niet bestaan in Ozon.|
|OZON1036|Een regeling die een tijdelijk deel is, mag zelf geen tijdelijk deel hebben.|
|OZON1038|Een ontwerpregeling kan niet geladen worden als er al een andere ontwerpregeling bestaat met hetzelfde expressionId of dezelfde ontwerpbesluitIdentificatie.|
|OZON1040|Een actualisatie van procedureverloop moet verwijzen naar een ontwerpregeling die bekend is in Ozon.|
|OZON1041|Een ontwerpregeling moet een regelingsgebied hebben of gekoppeld kunnen worden aan een vastgesteld document. |
|OZON2000|het wId van de Regeltekst in OW moet verwijzen naar een bestaande wId van een Artikel of Lid in OP|
|OZON2040|(TPOD2040) het id van Divisie of Divisietekst in OW moet verwijzen naar een bestaande id van een Divisie of Divisietekst in OP|
|OZON2060|(TPOD2060) Een OW-annotatie mag alleen worden toegevoegd op het niveau van een Artikel indien het Artikel geen leden heeft|
|OZON2140|(TPOD2140) Het WorkIDRegeling van het manifest-ow moet verwijzen naar een bestaande data:FRBRWork van een Regeling in OP|
|OZON2150|(TPOD2150) Het DoelID van het manifest-ow moet verwijzen naar een bestaand doel dat aanwezig is in de bijbehorende Regeling in OP|
|OZON2210|(TPOD2210) De combinatie van Doel en Regeling uit het manifest-OW moet ook als combinatie bestaan in OP|
|OZON3000|Er is onvoldoende informatie gevonden in de aanlevering om een object te kunnen vormen (volgens CIMOW). |
|OZON4000|Opeenvolgende versies van objecten moeten opeenvolgende tijdsparameters hebben.|
|OZON4001|Als een OwObject beeindigd wordt (status=B), moet deze bij Ozon bekend zijn.|
|OZON4002|Als een OwObject beeindigd wordt, moet de inhoud van dit object overeenkomen met wat bij Ozon bekend is.|
|OZON4003|Als een OwObject gewijzigd wordt, moet de inhoud van dit object veranderen ten opzichte van wat bij Ozon bekend is.|
|OZON4004|Als de Geometrie van een Locatie gewijzigd wordt, dan dient de Locatie opnieuw aangeboden te worden.|
|OZON4005|Als een OwObject gewijzigd wordt, moet het type van dit object hetzelfde zijn als dat van de vorige versie|
|OZON4006|Een levering mag niet meerdere regelingen bevatten met het zelfde regelingId en doel.                                     |
|OZON4007|Bij een levering met meerdere regelingen, mag ieder owBestand maar in één regeling gebruikt worden.                                                                                                          |
|OZON4008|Bij een levering met meerdere regelingen, mag ieder owObject maar in één regeling gebruikt worden.                                                |
|OZON4009|Bij een levering met meerdere regelingen, mag iedere geo maar in één regeling gebruikt worden.                  |
|OZON4010|Intrekken-vervangen (scenario 0) mag niet worden gebruikt in combinatie met meerdere regelingen.|
|RTRG0016|Als een activiteit van een gemeente verwijst naar een bovenliggende activiteit niet van een gemeente, dan moet deze verwijzen naar de activiteit: 'activiteit in omgevingsplan'|
|RTRG0017|Als een activiteit van een provincie verwijst naar een bovenliggende activiteit niet van een provincie, dan moet deze verwijzen naar de activiteit: 'activiteit in omgevingsverordening'|
|RTRG0018|Als een activiteit van een waterschap verwijst naar een bovenliggende activiteit niet van een waterschap, dan moet deze verwijzen naar de activiteit: 'activiteit in waterschapsverordening'|
|RTRG0019|Maximaal één activiteit van een gemeente mag verwijzen naar een bovenliggende activiteit niet van een gemeente|
|RTRG0020|Maximaal één activiteit van een provincie mag verwijzen naar een bovenliggende activiteit niet van een provincie|
|RTRG0021|Maximaal één activiteit van een waterschap mag verwijzen naar een bovenliggende activiteit niet van een waterschap|
|STOP0001|Een Lijst van het type 'ongemarkeerd' MAG GEEN lijst-items met nummering of symbolen hebben|
|STOP0002|Een Lijst van het type 'expliciet' MOET lijst-items hebben met nummering of symbolen|
|STOP0005|Een alinea MOET content bevatten|
|STOP0006|Een kop MOET content bevatten|
|STOP0007|Een referentie naar een noot MOET in de context van een tabel staan|
|STOP0008|Een referentie naar een noot MOET verwijzen naar een noot in dezelfde tabel|
|STOP0009|Een tabel MAG NIET in een lijst worden opgenomen|
|STOP0010|De waarde van IntRef/@ref MOET voorkomen als identifier (@eId) van een element binnen:OFWEL de tekst van dezelfde expression als de IntRef OFWEL binnen de tekst van hetzelfde component als de IntRef.|
|STOP0011|Een IntIoRef referentie MOET verwijzen naar @wId van ExtIoRef binnen hetzelfde bestand|
|STOP0012|De in de ExtIoRef weergegeven join-identifier MOET gelijk zijn aan de referentie|
|STOP0013|Een @eId MAG NIET eindigen met een punt '.'|
|STOP0014|Een @wId MAG NIET eindigen met een '.'|
|STOP0015|Een RegelingTijdelijkdeel MAG GEEN WijzigArtikel hebben|
|STOP0016|Een RegelingCompact MAG GEEN WijzigArtikel hebben|
|STOP0017|Een tekstuele mutatie ten behoeve van renvooi MAG NIET buiten een Regeling- of BesluitMutatie voorkomen|
|STOP0018|Een structuurwijziging ten behoeve van renvooi MAG NIET buiten een Regeling- of BesluitMutatie voorkomen|
|STOP0020|Een eId binnen een 'main' AKN-component MOET uniek zijn.|
|STOP0021|Een wId binnen een 'main' AKN-component MOET uniek zijn.|
|STOP0022|Een eId MOET voldoen aan de AKN-naamgevingsconventie|
|STOP0023|Een wId MOET voldoen aan de AKN-naamgevingsconventie|
|STOP0024|Een initiële regeling MOET een attribuut @componentnaam hebben met correcte naamgeving|
|STOP0025|Een initiële regeling MOET een attribuut @wordt hebben met de AKN-identificatie|
|STOP0026|Een componentnaam binnen een besluit MOET uniek zijn|
|STOP0027|Een eId binnen een AKN-component MOET uniek zijn|
|STOP0028|Een wId binnen een AKN-component MOET uniek zijn|
|STOP0029|Een tabel MOET ten minste twee kolommen hebben|
|STOP0032|Bij horizontale overspanning MOET de positie van @nameend groter zijn dan de positie van @namest|
|STOP0033|Bij horizontale overspanning MOET de @colname van eerste cel van de overspanning gelijk zijn aan de start (@namest) van de overspanning zijn.|
|STOP0036|De referentie van een cel MOET correct verwijzen naar een kolom|
|STOP0037|Het aantal colspec's MOET gelijk zijn aan het opgegeven aantal kolommen|
|STOP0038|Het totale aantal cellen MOET overeenkomen met het aantal mogelijke cellen|
|STOP0039|Een element WijzigInstructies MAG alleen voorkomen in een BesluitKlassiek|
|STOP0040|Een element RegelingMutatie binnen een WijzigArtikel mag alleen voorkomen in een BesluitKlassiek|
|STOP0043|Een onderdeel binnen een @eId MAG NIET eindigen met een punt '.'|
|STOP0044|Een onderdeel binnen een @wId MAG NIET eindigen met een '.'|
|STOP0045|Een (inline) Illustratie MAG GEEN attribuut @schaal hebben.|
|STOP0046|Een (inline) Illustratie MAG GEEN attribuut @kleur hebben.|
|STOP0047|Een element Wat MAG GEEN VerwijderdeTekst of NieuweTekst bevatten.|
|STOP0048|De wijzigacties nieuweContainer" en "verwijderContainer" MOGEN binnen een mutatieeenheid ALLEEN op de container Groep worden toegepast. Toepassing op andere containers (zoals Lijst; table of Citaat) kan potentieel leiden tot invalide XML of impliciet informatieverlies."|
|STOP0050|Een externe referentie MOET de juiste notatie gebruiken|
|STOP0051|Een element OpmerkingVersie MAG alleen in een BesluitKlassiek worden gebruikt|
|STOP0053|De scope van een interne verwijzing moet overeenkomen met de naam van het doelelement.|
|STOP0055|Het element Gereserveerd dat geen onderdeel is van een RegelingMutatie mag niet worden gevolgd door inhoud of structuur op hetzelfde niveau|
|STOP0058|Een structuur-element MOET altijd ten minste één element na de Kop bevatten|
|STOP0059|Een Artikel MOET altijd tenminste één element hebben na de Kop bevatten|
|STOP0060|Een Divisietekst MOET altijd één element anders dan een Kop bevatten|
|STOP0061|Een Kennisgeving MAG NIET onderverdeeld zijn in Divisies; maar mag alleen gestructureerd worden met DivisieTeksten|
|STOP0062|Indien een structuur-element vervallen is dan moeten ook alle onderliggende delen (structuur en tekst) vervallen zijn|
|STOP0063|tekst:Inhoud mag uitsluitend een @wijzigactie hebben gecombineerd met tekst:Vervallen; tekst:Gereserveerd of tekst:Lid.|
|STOP0064|Als het element Contact een attribuut @adres heeft; moet de inhoud van het attribuut een adres zijn dat is geformatteerd volgens de specificaties van de waarde van attribuut @soort.|
|STOP0065|Een wijzigactie voor Sluiting mag uitsluitend in een Vervang binnen BesluitMutatie worden gebruikt|
|STOP0066|Voor een mutatie MOET de waarde van de attributen @was en @wordt beginnen met dezelde akn identificatie van het work.|
|STOP0067|Een id voor een (voet-)noot binnen een AKN-component MOET uniek zijn|
|STOP0068|Een id voor een (voet-)noot MOET binnen een AKN-component uniek zijn.|
|STOP0070|Een Artikel MAG na een KOP slecht één ander type element (Vervallen; Gereserveerd; Inhoud of Lid) bevatten; combinaties zijn niet toegestaan.|
|STOP0073|Een WijzigArtikel in een BesluitCompact MAG GEEN Wijziglid bevatten|
|STOP0074|Het attribuut @wordt MOET uniek zijn binnen een besluit.|
|STOP0075|Het attribuut schemaversie op element tekst:Motivering MAG ALLEEN gebruikt worden in een uitwisselpakket.|
|STOP1000|Een AKN- of JOIN-identificatie mag geen punt bevatten.|
|STOP1001|Het deel vóór de taalcode/@" van de FRBRExpression moet gelijk aan zijn FRBRWork"|
|STOP1002|Voor een AKN-identificatie (werk/expressie) moet het tweede deel een landcode uit de lijst nl; aw; cw; sx zijn.|
|STOP1003|Voor een JOIN-identificatie (work) moet het tweede deel gelijk zijn aan 'id'|
|STOP1004|Voor een JOIN-identificatie moet het derde deel een geldig type zijn (regdata; pubdata; infodata)|
|STOP1006|Voor een AKN- of JOIN identificatie (werk/expressie) moet het vijfde deel een jaartal zijn of een geldige datum zijn|
|STOP1007|Voor een JOIN-identificatie (expressie) moet het eerste deel na de '@' een jaartal of een geldige datum zijn|
|STOP1008|JOIN-identificatie (expressie) MOET als eerste deel na de '@' een jaartal of een geldige datum hebben groter/gelijk aan jaartal in werk|
|STOP1009|Voor een AKN- of JOIN-identificatie (expressie) moet deel voorafgaand aan de '@' een geldige taal zijn ('nld';'eng';'fry';'pap';'mul';'und')|
|STOP1010|Vierde deel van de AKN / JOIN voor werken en expressies van een besluit; een regeling of een informatieobject moet gelijk zijn aan:een brp-code voor regeling; besluit of informatieobject;een code (bijvoorbeeld 'gemeente' of 'provincie') voor een geconsolideerde regeling of informatieobject.|
|STOP1011|De AKN van een officiele publicatie moet als derde veld 'officialGazette' hebben|
|STOP1012|De AKN van de door het bevoegd gezag aangeleverde regeling moet als derde veld 'act' hebben|
|STOP1013|De AKN van het door het bevoegd gezag aangeleverd besluit moet als derde veld 'bill' hebben|
|STOP1014|De AKN- of JOIN-identificatie MOET beginnen met /akn" of "/join""|
|STOP1015|De officieleTitel van InformatieObjectMetatada MOET starten met /join/id/|
|STOP1016|Versienummer van regeling moet voldoen aan de STOP-specificaties.|
|STOP1017|De AKN van een officiele publicatie moet als vierde veld een bladcode hebben|
|STOP1018|De waarde van data:informatieobjectRef MOET uniek zijn binnen één data:informatieobjectRefs|
|STOP1019|Binnen dezelfde container data:rechtsgebieden mag een unieke waarde maar één keer worden gebruikt.|
|STOP1020|Een alternatieve titel MAG niet gelijk zijn aan de citeertitel|
|STOP1021|Het patroon in data:uri moet overeenkomen met data:soortRefURL: correcte http(s)-referentieAKN: correcte AKNJCI: correcte JCI)|
|STOP1022|Een alternatieve titel MOET uniek zijn binnen alle alternatieve titels.|
|STOP1023|De opvolgingsrelatie data:opvolgerVan MOET uniek zijn binnen de container data:opvolging.|
|STOP1024|Een opvolgingsrelatie data:opvolgerVan MOET naar een work van een Regeling of een Informatieobject verwijzen|
|STOP1026|De instrumentversie van een BeoogdeRegeling moet een expressionID (/akn/nl/act) zijn|
|STOP1027|De instrumentversie van een BeoogdInformatieobject moet een /join/id/regdata zijn.|
|STOP1028|Het instrument binnen een Intrekking moet een akn- of join-identificatie hebben ('/akn/nl/act/[...]' of '/join/id/regdata/[...]').|
|STOP1029|Een doel kan maar één datum inwerkingtreding hebben|
|STOP1030|Binnen dezelfde container data:overheidsdomeinen mag een unieke waarde maar één keer worden gebruikt.|
|STOP1031|Binnen dezelfde container data:onderwerpen mag een unieke waarde maar één keer worden gebruikt.|
|STOP1032|Een officiële publicatie van een besluit MOET een datum ondertekening hebben.|
|STOP1033|Een officiële publicatie van een kennisgeving MAG GEEN datum ondertekening hebben.|
|STOP1034|Voor decentrale overheden (gemeente; provincie; waterschap) MOET soort bestuursorgaan" zijn ingevuld"|
|STOP1035|Het ingevulde soort bestuursorgaan" MOET passen bij de waarde in eindverantwoordelijke"|
|STOP1037|De AKN-identificatie van een kennisgeving moet als derde veld 'doc' hebben|
|STOP1038|Een doel identificatie moet zijn opgebouwd als /join/id/proces/[organisatie]/[datum of jaar]/[naam]"|
|STOP1044|De AKN-identificatie van een rectificatie MOET als derde deel doc hebben|
|STOP1058|Een GIO MOET bij aanlevering altijd precies één GML-bestand (*.gml)hebben.|
|STOP1059|Een consolideerbaar informatieobject (bijv. een GIO) MOET een geboorteregeling hebben.|
|STOP1060|Een verwijzing naar een geboorteregeling MOET naar een expression van een Regeling die begint met /akn/nl/act/... verwijzen.|
|STOP1071|Een componentverwijzing in akn of join moet beginnen met een '!'.|
|STOP1072|Het laatste deel van een akn of join voor een optionele componentverwijzing mag geen '!' bevatten.|
|STOP1073|Informatieobjecten van formaatInformatieobject /join/id/stop/informatieobject/gio_002 met het type alleen bekend te maken of informatief zijn NIET TOEGESTAAN zolang deze informatieobjecten niet expliciet benoemd zijn in een toepassingsprofiel(TPOD).|
|STOP1074|Informatieobjecten van formaatInformatieobject /join/id/stop/informatieobject/doc_001 (pdf) met het type informatief zijn NIET TOEGESTAAN zolang deze informatieobjecten niet expliciet benoemd zijn in een toepassingsprofiel(TPOD).|
|STOP1200|De IMOP-modules die binnen één Component zijn opgenomen MOETEN allen dezelfde IMOP-schemaversie gebruiken.|
|STOP1201|Elk in het uitwisselpakket opgenomen bestand MOET aangeroepen worden door de STOP-pakbon;een andersoortig manifest volgens een andere standaard of aangeroepen worden door een in het uitwisselpakket aanwezig bestand.Anders geformuleerd: er mogen geen ongebruikte" bestanden in het pakket opgenomen zijn."|
|STOP1202|Elk bestand dat middels de bestandsnaam aangeroepen wordt door één van onderstaande bestanden MOET aanwezig zijn in het uitwisselpakket. de STOP-pakboneen andersoortig manifest volgens een andere standaard ofeen ander bestand dat in het uitwisselpakket aanwezig isAnders geformuleerd: Elk aangeroepen bestand moet aanwezig zijn; een pakket moet compleet zijn.|
|STOP1203|Voor elk in het pakbon opgenomen XML-bestand MOET de combinatie van localName en namepace overeenkomen met het root-element van het aangewezen bestand. Een XML-bestand" is te herkennen aan mediatype="application/xml" of "application/xml+gml"."|
|STOP1204|Een IMOP-module met juridische regelteksten MOET samen een RegelingVersieMetadata-module binnen dezelfde component (instrument) worden uitgewisseld.|
|STOP1205|Een IMOP-informatieobject-module MOET samen een InformatieObjectVersieMetadata-module van dezelfde component (instrument) worden uitgewisseld.|
|STOP1206|Elk door een uitgewisselde IMOP-module aangeroepen bestand (zoals een bestand voor een illustratie of voor een informatieobject) MOET worden opgenomen in dezelfde Component binnen de pakbon van het uitwisselpakket.|
|STOP1207|Het mediatype zoals genoemd in de pakbon moet gelijk zijn aan het daadwerkelijke media-type (oftewel MIME type") van het bestand."|
|STOP1208|Een Component in een pakbon MOET een Module van type ExpressionIdentificatie of ConsolidatieIdentificatie bevatten TENZIJ het een versieinformatie Component is.|
|STOP1209|De Work-identificatie van de Component in een pakbon MOET gelijk zijn aan de Work-identificatie in de ExpressionIdentificatie- of ConsolidatieIdentificatie-module.|
|STOP1210|De Expression-identificatie van de Component in een pakbon MOET gelijk zijn aan de FRBRExpression in de ExpressionIdentificatie- of ConsolidatieIdentificatie-module.|
|STOP1211|De soort Work van de Component in een pakbon MOET gelijk zijn aan de soort Work in de ExpressionIdentificatie- of ConsolidatieIdentificatie-module.|
|STOP1212|De IMOP-schemaversie van een IMOP-module in de pakbon MOET overeenkomen met de IMOP-schemaversie in het XML bestand zelf.|
|STOP1213|Bij gebruik van het uitwisselpakket voor het uitwisselen van een (nieuwe) versie van een of meer regelingen MOET het uitwisselpakket één versie van een (set van samenhangende) regeling(en) met één versie van de bijbehorende informatieobjecten bevatten. De versie van de regelingen/informatieobjecten mogen alleen over meerdere uitwisselpakketten verdeeld worden als die via een (download)service in samenhang verkregen kunnen worden.|
|STOP1214|Bij gebruik van het uitwisselpakket voor het uitwisselen van een (nieuwe) versie van een of meer regelingen MOETEN gewijzigde regeling- en informatieobjectversies (Componenten) in het uitwisselpakket met één besluit tegelijk in werking (kunnen) treden (m.a.w. gewijzigde componenten hangen samen met één en hetzelfde doel).|
|STOP1215|Bij gebruik van het uitwisselpakket voor het uitwisselen van een (nieuwe) versie van een of meer regelingen MOET het uitwisselpakket van elke component altijd alle modules bevatten (m.a.w. 'compleet' zijn). Optionele modules moeten aanwezig zijn als ze voor betreffend component bestaan.|
|STOP1216|Bij gebruik van het uitwisselpakket voor het uitwisselen van een (nieuwe) versie van een of meer regelingen MOET de pakbon in het uitwisselpakket een component Versieinformatie bevatten.|
|STOP1217|Component Versieinformatie in de pakbon van een uitwisselpakket MOET de module Momentopname bevatten.|
|STOP1218|Een IMOP-module die voor een component vermeld is in de pakbon MOET volgens de vermelde versie van IMOP daadwerkelijk een module van de component zijn.|
|STOP1300|Het procedureverloop MOET alleen stappen bevatten die bij één type procedureverloop horen.Het procedureverloop kan bijvoorbeeld geen stappen bevatten die specifiek zijn voor een procedure rond een ontwerpbesluit; en tevens stappen specifiek voor een (definitief) besluit.|
|STOP1301|Het type procedureverloop MOET passen bij het type besluit waarvan het de procedure beschrijft.|
|STOP1302|Bepaalde stappen in het procedureverloop MOGEN hooguit één keer voorkomen.Sommige stappen worden maar één keer gezet in een procedure en kennen dus ook maar één datum waarop ze voltooid zijn. Als blijkt dat de datum niet correct is; kan die via een mutatie van het procedureverloop aangepast worden. De uniciteit van deze stappen is belangrijk omdat de datum ervan nodig is om de relevantie te bepalen van besluiten en/of kennisgevingen erover.|
|STOP1303|De stappen die door (de organisatie van) het bevoegd gezag gedaan worden MOETEN in het procedureverloop opgenomen zijn in de volgorde waarin de besluitvormingsprocedure verloopt.Besluit volgordeVaststellingOndertekeningPublicatie|
|STOP1304|De stappen die relevant zijn voor de reactie van belanghebbenden op het besluit MOETEN in het procedureverloop opgenomen zijn in de juiste volgorde.Welke stappen dat zijn hangt af van het type besluit. Zie de beschrijving voor de juiste volgorde.|
|STOP1305|De stappen gerelateerd aan de instelling en behandeling van een beroep tegen het besluit MOETEN in het procedureverloop opgenomen zijn in de volgorde waarin de besluitvormingsprocedure verloopt.Beroep volgordeVaststellingOndertekeningBeroep(en) ingesteldEinde Beroepstermijn|
|STOP1310|Een stap die het begin van een beroepsperiode aangeeft MOET ofwel als eerste voorkomen; ofwel nadat een eerdere beroepsperiode is afgesloten.BeroepsperiodeStart: Beroep(en) ingesteldEind: Beroep(en) definitief afgedaan|
|STOP1311|Stappen die samenhangen met de schorsing van een besluit door een rechter MOETEN in het procedureverloop tussen de start en het einde van de beroepsperiode opgenomen zijn.|
|STOP1312|Een stap die het einde van een beroepsperiode aangeeft MOET volgen op een stap die het begin van de beroepsperiode aangeeft.|
|STOP1313|Een stap die het begin van een schorsingsperiode aangeeft MOET ofwel als eerste voorkomen; ofwel nadat een eerdere schorsingsperiode is afgesloten.SchorsingsperiodeStart: SchorsingEind: Schorsing opgeheven|
|STOP1315|Een stap die het einde van een schorsingsperiode aangeeft MOET volgen op een stap die het begin van de schorsingsperiode aangeeft.|
|STOP1319|Sommige stappen MOETEN in het procedureverloop vermeld worden omdat de informatie anders niet compleet is:Stap 'Einde inzagetermijn' MOET vermeld worden als 'Begin inzagetermijn' is opgenomen.Stap 'Einde beroepstermijn' MOET vermeld worden als 'Beroep(en) ingesteld' is opgenomen.Stap 'Ondertekening' MOET vermeld worden als 'Beroep(en) ingesteld' is opgenomenStap 'Ondertekening' MOET vermeld worden als 'Einde beroepstermijn' is opgenomenStap 'Ondertekening' MOET vermeld worden als 'Publicatie' is opgenomenStap 'Ondertekening' MOET vermeld worden als 'Einde bezwaar' is opgenomenAls deze stappen niet vermeld zijn is het niet mogelijk afgeleide informatie te bepalen op manieren die in de standaard beschreven staan; zoals de relevantie van het besluit en/of gerelateerde kennisgevingen op een moment in de tijd; of de status van een besluit.|
|STOP1320|Bij een kennisgeving van een definitief besluit MOGEN ALLEEN de volgende procedurestappen voorkomen:Einde bezwaartermijnEinde beroepstermijn|
|STOP1321|Bij een kennisgeving ontwerp besluit MOGEN ALLEEN de volgende procedurestappen voorkomen:Begin inzagetermijnEinde inzagetermijn|
|STOP1400|Een procedureverloopmutatie MAG NIET leiden tot een ongeldig procedureverloop (Het resulterende procedureverloop moet voldoen aan de beschrijving en dus aan de procedureverloop-bedrijfsregels).|
|STOP2001|Een ontwerpbesluit treedt niet in werking en kent geen geldigheid.|
|STOP2002|Als FRBRWork begint met '/akn/nl/bill/' dan moet het soortwork '/join/id/stop/work_003' (generiek besluit) zijn.|
|STOP2003|Als FRBRWork begint met '/akn/nl/act/' dan moet het soortwork een van de volgende zijn:'/join/id/stop/work_019' (regeling)'/join/id/stop/work_006' (geconsolideerde regeling)'/join/id/stop/work_021' (tijdelijk regelingdeel)'/join/id/stop/work_019' (consolidatie van tijdelijk regelingdeel)|
|STOP2004|De identificatie van een tijdelijk regelingdeel (data:ExpressionIdentificatie bevat data:isTijdelijkDeelVan) MOET als soortWork '/join/id/stop/work_021' (tijdelijk regelingdeel) hebben.|
|STOP2006|Elke data:wId (tekst) of JOIN-id (informatieobject) waar in een tekst:ArtikelgewijzeToelichting toelichting op wordt gegeven én die wordt genoemd in de data:Toelichtingsrelatie MOET voorkomen in de juridische tekst van de regeling of het besluit; of moet als IO bij het besluit horen (dus voorkomen in de BesluitMetadata; ook na een rectificatie).|
|STOP2009|De data:wId waar een data:Toelichtingsrelatie naar verwijst; MOET voorkomen in de tekst:ArtikelgewijzeToelichting bij de regeling of het besluit.|
|STOP2011|De ConsolidatieInformatie van een Informatieobject verwijst naar de plaats in de regelingtekst waar die versie; juridisch gezien; ontstaat (tekst:ExtIORef).|
|STOP2019|De ConsolidatieInformatie van een BeoogdeRegeling MOET verwijzen naar waar in de juridische tekst staat dat deze nieuwe versie; juridisch gezien; ontstaat. In het klassieke model is dit binnen tekst:RegelingKlassiek; maar niet binnen tekst:wijzigArtikel of tekst:RegelingKlassiek zelf. In het compacte model is dit binnen tekst:Artikel van tekst:Lichaam van tekst:BesluitCompact(Besluit) of tekst:BesluitMutatie(Rectificatie).|
|STOP2020|Een Tijdstempel in de Consolidatieinformatie MOET verwijzen naar waar in de juridische tekst de tijdstempel; juridische gezien; ontstaat. In het klassieke model is dit binnen een tekst:Artikel. In het compacte model is dit binnen een tekst:Artikel van tekst:Lichaam van tekst:BesluitCompact (Besluit) of tekst:BesluitMutatie(Rectificatie).|
|STOP2021|Een Intrekking van een Regeling in de Consolidatieinformatie MOET verwijzen naar waar in de juridische tekst de Regeling; juridisch gezien; wordt ingetrokken. In het klassieke model is dit binnen een tekst:Artikel In het compacte model is dit binnen een tekst:Artikel van tekst:Lichaam van tekst:BesluitCompact(besluit) of tekst:BesluitMutatie(rectificatie).|
|STOP2022|De ConsolidatieInformatie van een ingetrokken Informatieobject verwijst naar de plaats in de regelingtekst waar die versie; juridisch gezien; ophoudt te bestaan (wijzigen of verwijderen van tekst:ExtIORef).|
|STOP2023|Elk consolideerbaar informatieobject MOET een geboorteregeling hebben.|
|STOP2024|Als FRBRWork begint met '/join/id/' dan moet het soortwork een van de volgende zijn: '/join/id/stop/work_010' (informatieobject)'/join/id/stop/work_005' (geconsolideerd informatieobject)|
|STOP2025|data:officieleTitel van een informatieobject MOET gelijk zijn aan het data:FRBRWork|
|STOP2026|De collectie(regdata; pubdata of infodata) gebruikt in de JOIN identifier van een informatieobject MOET overeenkomen met zijn data:publicatieinstructie|
|STOP2030|Een met een besluit of rectificatie meegeleverde consolideerbare informatieobject-versie MOET als inhoud van tekst:ExtIoRef genoemd worden in de Regeling of Regelingmutatie.|
|STOP2031|Externe verwijzingen (imop-tekst:ExtRef en imop-tekst:ExtIORef) in een ontwerpbesluit mogen alleen verwijzen naar met het ontwerpbesluit meegeleverde informatieobjecten; ofnaar eerder bekend gemaakte ontwerp- of definitieve besluiten en bijbehorende informatieobjecten.|
|STOP2032|Externe verwijzingen (imop-tekst:ExtRef en imop-tekst:ExtIORef) in een definitief besluit mogen alleen verwijzen naar met het besluit meegeleverde informatieobjecten; ofnaar eerder bekend gemaakte definitieve besluiten en bijbehorende informatieobjecten.|
|STOP2033|Een met een besluit of rectificatie meegeleverd  alleen bekend te maken informatieobject MAG ALLEEN als inhoud van tekst:ExtRef genoemd worden in het besluitdeel van een Besluit/Rectificatie (dus niet in de Regeling of een Regelingmutatie).|
|STOP2034|Een met een besluit of rectificatie meegeleverd Informatief informatieobject MAG NIET voorkomen in de tekst van het besluit.|
|STOP2039|Een rectificatie MOET verwijzen naar een reeds gepubliceerde besluitversie.|
|STOP2042|Wijzigen van informatieobjecten bij een besluit is alleen toegestaan via een juridisch instrument (zoals rectificatie).|
|STOP2050|De tekstmodule bij een data:ExpressionIdentificatie met data:soortWork '/join/id/stop/work_003' MOET een root-element tekst:BesluitCompact of tekst:BesluitKlassiek hebben.|
|STOP2051|De tekstmodule bij een data:ExpressionIdentificatie met data:soortWork '/join/id/stop/work_019' MOET een root-element tekst:RegelingCompact; tekst:RegelingKlassiek of tekst:RegelingVrijetekst hebben.|
|STOP2052|Als FRBRWork begint met '/akn/nl/doc/' dan moet het soortwork een van de volgende zijn:'/join/id/stop/work_018' (rectificatie)'/join/id/stop/work_023' (kennisgeving)|
|STOP2053|De tekstmodule van een data:ExpressionIdentificatie met data:soortWork '/join/id/stop/work_021' MOET root-element tekst:RegelingTijdelijkdeel hebben.|
|STOP2055|Elke Terugtrekking(-Regeling; -Tijdstempel; -Intrekking) MOET genoemd worden in BesluitMutatie; bijv. bij een Rectificatie.|
|STOP2056|Elke TerugtrekkingInformatieobject MOET genoemd worden in de RegelingMutatie; bijv. bij een Rectificatie.|
|STOP2057|De identificatie van een tijdelijk regelingdeel (data:soortWork = '/join/id/stop/work_021') MOET tijdelijk deel zijn van een regeling met soortWork '/join/id/stop/work_019' (regeling).|
|STOP2058|De identificatie van een tijdelijk regelingdeel (data:soortWork = '/join/id/stop/work_021') MOET aangeven waarvan het een tijdelijk deel is (heeft data:isTijdelijkDeelVan).|
|STOP2060|STOP elementen van het type *:dtWaardeRef moeten waarden uit de correcte waardelijst gebruiken.|
|STOP2061|De data:ExpressionIdentificatie van een tekstmodule met root-element tekst:RegelingTijdelijkdeel MOET data:soortWork '/join/id/stop/work_021' hebben.|
|STOP2063|ALS het soortwork van het Work waar een tijdelijk regelingdeel toe behoort '/join/id/stop/work_019' (regeling) is; DAN MOET het derde deel van het FRBRWork '/act/' zijn.|
|STOP2064|Elke Terugtrekking(-Regeling; -Informatieobject; -Tijdstempel; of -Intrekking) MOET voorkomen in de ConsolidatieInformatie van het originele Besluit; bijv. bij een Rectificatie.|
|STOP3000|Als er 1 locatie is in een GIO waar een waarde groepID is ingevuld MOET de groepID bij alle locaties zijn ingevuld.|
|STOP3001|Als een locatie een groepID heeft; dan MOET deze voorkomen in het lijstje groepen.|
|STOP3002|Als GroepID voorkomt mag het niet leeg zijn.|
|STOP3003|Twee groepIDs in het lijstje groepen mogen niet dezelfde waarde hebben.|
|STOP3004|Twee labels in het lijstje groepen mogen niet dezelfde waarde hebben.|
|STOP3005|Als een groepID voorkomt in het lijstje groepen dan MOET er minstens 1 locatie zijn met dat groepID.|
|STOP3006|Als er één locatie is in een GIO waar kwantitatieveNormwaarde is ingevuld MOETEN alle locaties een kwantitatieveNormWaarde hebben.|
|STOP3007|Als er één locatie is in een GIO waar kwalitatieveNormwaarde is ingevuld MOETEN alle locaties een kwalitatieveNormwaarde hebben.|
|STOP3008|Van de elementen kwalitatieveNormwaarde en kwantitatieveNormwaarde in een Locatie mag er slechts één ingevuld zijn.|
|STOP3009|Als de locaties van de GIO kwantitatieve normwaarden hebben; moet de eenheid(eenheidlabel en eenheidID) aanwezig zijn in de GIO.|
|STOP3010|Een kwalitatieveNormwaarde mag geen lege string (“”) zijn.|
|STOP3011|Als de locaties van de GIO kwantitatieve òf kwalitatieve normwaarden hebben; dan moet de norm (normlabel en normID) aanwezig zijn.|
|STOP3012|Een Locatie binnen een GIO mag niet zowel een groepID (GIO-deel) als een (kwalitatieve of kwantitatieve) Normwaarde bevatten.|
|STOP3013|Binnen 1 GIO mag elke basisgeo:id (GUID) van de geometrische data van een locatie maar één keer voorkomen.|
|STOP3015|Als de locaties van de GIO kwalitatieve normwaarden hebben; MOGEN eenheidlabel en eenheidID NIET voorkomen.|
|STOP3016|In een GIO waar locaties geen kwalitatieve of kwantitatieve normwaarde hebben; MOGEN eenheidID; eenheidlabel; normID en normlabel NIET voorkomen.|
|STOP3018|ALS een geometrisch object (basisgeo:geometrie) wordt opgenomen in meerdere GIO's en/of GIO-versies met dezelfde identificatie basisgeo:id(GUID) dan MOET de geometrische data in alle GIO's hetzelfde zijn.|
|STOP3019|Locaties in een GIO MOETEN een geometrische data hebben (basisgeo:geometrie in basisgeo:Geometrie MAG NIET onbreken of leeg zijn).|
|STOP3020|Coördinaten van een geometrisch object in een GIO MOETEN gebruikmaken van één van de twee ruimtelijke referentiesystemen:RD: srsName='urn:ogc:def:crs:EPSG::28992' ofETRS89: srsName='urn:ogc:def:crs:EPSG::4258'.|
|STOP3021|De geometrische coördinaten van alle locaties in een GIO MOETEN gebaseerd zijn op hetzelfde ruimtelijke referentiesysteem.|
|STOP3022|Normwaarden of geometrische begrenzingen MOGEN NIET zowel in een GIO als in de tekst van de regeling staan.|
|STOP3023|Locatiegroepen in een GIO MOETEN door symbolisatie duidelijk te onderscheiden zijn als het volledige GIO met de bijbehorende symbolisatie wordt getoond.|
|STOP3024|Een GIO kan maximaal één locatiegroep-indeling hebben.|
|STOP3025|Locatiegroepen MOGEN elkaar NIET overlappen.|
|STOP3026|Een locatie kan slechts deel uitmaken van één locatiegroep.|
|STOP3027|Van een versie van een te consolideren GIO die onderdeel is van een besluit; MOET de Expression (JOIN ID) worden genoemd in òf de regelingtekst(mutatie) van het besluit; òf de besluittekst (bijvoorbeeld indien het GIO gebruikt wordt als Pons).|
|STOP3028|Alle Expressies van een GIO Work MOETEN betrekking hebben op dezelfde norm. (De eenheid kan wijzigen en ook de norm-ID en norm-label kunnen wijzigen; maar de GIO moet betrekking houden op dezelfde norm)|
|STOP3029|Als een GIO normwaarden bevat dan MOETEN deze normwaarden door symbolisatie duidelijk te onderscheiden zijn als het volledige GIO met de bijbehorende symbolisatie wordt getoond.|
|STOP3070|Een vastgestelde GIO heeft een vaststellingscontext (achtergrondkaart); waarvan de versie is aangegeven.|
|STOP3071|Elke GIO-versie heeft een eigen vaststellingscontext. Deze hoeft niet gelijk te zijn aan de vaststellingscontext van andere GIO-versies van hetzelfde Work.|
|STOP3072|ALS de nauwkeurigheid van het GIO en/of de vaststellingscontext leidt tot verplicht gebruik van de Basisregistratie Grootschalige Topografie (BGT); dan MOET als geografische context de BGT worden gebruikt.|
|STOP3073|De juridische nauwkeurigheid van de geometrische data in een GIO komt overeen met die van de geografische context (kaart) die voor de vaststelling is gebruikt.|
|STOP3074|Zijn er bij de vaststelling van een GIO ook context-GIO’s getoond; dan MOETEN deze GIO’s ook als context-GIO's opgenomen worden in het GIO.|
|STOP3075|Een berekende GIO bevat een nauwkeurigheidsgraad die is aangegeven in decimeters.|
|STOP3076|Een gedeeltelijk gewijzigde GIO heeft een was-ID met de Expression ID van het GIO zodat de wijzigingen van het GIO kunnen worden bepaald.|
|STOP3077|In een GIO zonder was-ID wordt elk onderdeel van de GIO als gewijzigd beschouwd.|
|STOP3078|ALS een GIO een wasID heeft; dan MOET de wasID een voorgaande expressie zijn van hetzelfde work.|
|STOP3079|Of een GIO opnieuw(zonder was-ID) of gewijzigd (met was-ID) wordt vastgesteld; kan gevolgen hebben voor de mogelijkheid om beroep of bezwaar aan te tekenen tegen de vaststelling van de GIO.|
|STOP3100|De FeatureTypeStyle MAG GEEN se:Name bevatten.|
|STOP3101|De FeatureTypeStyle MAG GEEN se:Description bevatten.|
|STOP3102|De waarde voor FeatureTypeName moet de waarde Locatie (met eventueel de correcte namespace-prefix) hebben.|
|STOP3103|FeatureTypeStyle:SemanticTypeIdentifier MOET zijn geo:geometrie; geo:groepID; geo:kwalitatieveNormwaarde of geo:kwantitatieveNormwaarde (evt. met een andere namespace prefix voor https://standaarden.overheid.nl/stop/imop/geo/).|
|STOP3114|Als Rule een Filter bevat dan MOET de SemanticTypeIdentifier zijn geo:groepID;geo:kwalitatieveNormwaarde of geo:kwantitatieveNormwaarde(evt. met een andere namespace prefix voor https://standaarden.overheid.nl/stop/imop/geo/).|
|STOP3115|PropertyName MOET overeenkomen met de SemanticTypeIdentifier (zonder namepace prefix).|
|STOP3118|Als Rule:Filter:PropertyIsBetween; PropertyIsNotEqualTo; PropertyIsLessThan; PropertyIsGreaterThan; PropertyIsLessThanOrEqualTo of PropertyIsGreaterThanOrEqualTo is; dan MOET de SemanticTypeIdentifier gelijk zijn aan geo:kwantitatieveNormwaarde (evt. met een andere namespace prefix voor https://standaarden.overheid.nl/stop/imop/geo/).|
|STOP3120|Als Rule:Filter:And is; dan MOETEN de operanden PropertyIsLessThan en PropertyIsGreaterThanOrEqualTo bevatten.|
|STOP3126|De Description:Title MAG NIET leeg zijn (dit is de legenda-regel).|
|STOP3135|De PointSymbolizer:Graphic:Mark:Fill MAG GEEN se:GraphicFill bevatten|
|STOP3138|De PointSymbolizer MOET een van de vormen hebben: se:Graphicse:Markse:Fillse:GraphicFillse:SvgParameter|
|STOP3139|Het name" attribute van de Stroke:SvgParameter MOET zijn stroke; stroke-width; stroke-dasharray; stroke-linecap; stroke-opacity; of stroke-linejoin."|
|STOP3140|SvgParameter met name" attribute "stroke" MOET aan de reguliere expressie ^#[0-9a-f]{6}$ voldoen. (string van 7 karakters; met als eerste karakters een # en de volgende zes karakters een hexadecimale waarde.)"|
|STOP3141|SvgParameter met name" attribute "stroke-width" MOET aan de reguliere expressie ^[0-9]+(.[0-9])?[0-9]?$ voldoen. (positief getal met 0; 1 of 2 decimalen)"|
|STOP3142|SvgParameter met name" attribute "stroke-width" MOET aan de reguliere expressie ^([0-9]+ ?)*$ voldoen. (string met één of meer positief gehele getal gescheiden door een spatie)"|
|STOP3143|SvgParameter met name" attribute "stroke-linecap" MOET "butt" bevatten."|
|STOP3144|SvgParameter met met name attribute stroke-opacity" MOET aan de reguliere expressie  ^0((.[0-9])?[0-9]?)|1((.0)?0?)$ voldoen. (string met een positief decimaal getal tussen 0.0 en 1.0 (beide inclusief) met 0;1 of 2 decimalen)"|
|STOP3145|SvgParameter met name" attribute "stroke-linejoin" MOET "round" bevatten."|
|STOP3146|Het name" attribute van de Fill:SvgParameter MOET fill of fill-opacity zijn."|
|STOP3147|SvgParameter met name" attribute "fill" MOET aan de reguliere expressie ^#[0-9a-f]{6}$ voldoen. (string van 7 karakters; met als eerste karakters een # en de volgende zes karakters een hexadecimale waarde.)"|
|STOP3148|SvgParameter met met name attribute fill-opacity" MOET aan de reguliere expressie ^0((.[0-9])?[0-9]?)|1((.0)?0?)$ voldoen. (string met een positief decimaal getal tussen 0 en 1 (beide inclusief) met 0;1 of 2 decimalen)"|
|STOP3157|De PointSymbolizer:Graphic:Mark:WellKnownName MOET zijn:cross (of cross_fill); square; circle; star of triangle|
|STOP3163|De Graphic:Size MOET aan de reguliere expressie ^[0-9]+$ voldoen. (een positief geheel getal)|
|STOP3170|Als de PolygonSymbolizer:Fill een GraphicFill:Graphic bevat; DAN MOET deze alleen se:ExternalGraphic bevatten.|
|STOP3173|Een PolygonSymbolizer:Fill:GraphicFill:Graphic:ExternalGraphic:InlineContent met attribute encoding=base64" MOET aan de reguliere expressie ^[A-Z0-9a-z/+ =]*$ voldoen. (hoofd- en kleine letters; cijfers; plus-teken; /-teken)"|
|STOP3174|ExternalGraphic:Format MOET de waarde image/png hebben.|
|TPOD0410|Een Hoofdstuk moet worden geduid met de label Hoofdstuk.|
|TPOD0420|Hoofdstukken moeten oplopend worden genummerd in Arabische cijfers, indien nodig gevolgd door een letter.|
|TPOD0460|Een Titel moet worden geduid met de label Titel.|
|TPOD0470|De nummering van Titels moet beginnen met het nummer (en evt. letter) van het Hoofdstuk waarin de Titel voorkomt.|
|TPOD0480|Titels moeten oplopend worden genummerd in Arabische cijfers, indien nodig gevolgd door een letter|
|TPOD0490|Achter het laatste cijfer van een titelnummer mag geen punt worden opgenomen.|
|TPOD0510|Een Afdeling moet worden geduid met de label Afdeling.|
|TPOD0520|Als tussen Hoofdstuk en Afdeling Titel voorkomt dan moet de nummering van Afdelingen beginnen met het samengestelde nummer van de Titel (en evt. letter) waarin de Afdeling voorkomt, gevolgd door een punt.|
|TPOD0530|Afdelingen moeten oplopend worden genummerd in Arabische cijfers, indien nodig gevolgd door een letter.|
|TPOD0540|Achter het laatste cijfer van een Afdelingnummer mag geen punt worden opgenomen.|
|TPOD0560|Als tussen Hoofdstuk en Afdeling geen Titel voorkomt dan moet de nummering van Afdelingen beginnen met het nummer van het Hoofdstuk (en evt. letter) waarin de Afdeling voorkomt, gevolgd door een punt.|
|TPOD0570|Een Paragraaf moet worden geduid met de label Paragraaf of het paragraaf-teken.|
|TPOD0580|De nummering van Paragrafen begint met het samengestelde nummer (en evt. letter) van de Afdeling waarin de Paragraaf voorkomt, gevolgd door een punt.|
|TPOD0590|Paragrafen moeten oplopend worden genummerd in Arabische cijfers, indien nodig gevolgd door een letter.|
|TPOD0600|Achter het cijfer van een Paragraafnummer mag geen punt worden opgenomen.|
|TPOD0620|Een Subparagraaf moet worden geduid met de label Subparagraaf.|
|TPOD0630|De nummering van Subparagrafen begint met het samengestelde nummer (en evt. letter) van de Paragraaf waarin de Subparagraaf voorkomt, gevolgd door een punt.|
|TPOD0640|Subparagrafen moeten oplopend worden genummerd in Arabische cijfers, indien nodig gevolgd door een letter|
|TPOD0650|Achter het laatste cijfer van een Subparagraafnummer mag geen punt worden opgenomen.|
|TPOD0670|Een Subsubparagraaf moet worden geduid met de label Subsubparagraaf.|
|TPOD0680|De nummering van Subsubparagrafen begint met het samengestelde nummer (en evt. letter) van de Subparagraaf waarin de Subsubparagraaf voorkomt, gevolgd door een punt.|
|TPOD0690|Subsubparagrafen moeten oplopend worden genummerd in Arabische cijfers, indien nodig gevolgd door een letter|
|TPOD0700|Achter het laatste cijfer van een Subsubparagraafnummer mag geen punt worden opgenomen.|
|TPOD0741|De nummering van Artikelen begint met het nummer van het Hoofdstuk (en evt. letter) waarin het Artikel voorkomt, gevolgd door een punt, daarna oplopende nummering van de Artikelen in Arabische cijfers inclusief indien nodig een letter.|
|TPOD0750|Achter het cijfer van een Artikelnummer mag geen punt worden opgenomen.|
|TPOD0781|Leden worden per artikel oplopend genummerd in Arabische cijfers en indien nodig een letter.|
|TPOD0790|Het eerste lid van ieder artikel krijgt het nummer 1.|
|TPOD0800|Het cijfer van een Lid moet worden opgevolgd door een punt.|
|TPOD0811|Het is verboden om gebruik te maken van het Lijstaanhef-element.|
|TPOD0830|De onderdelen van de Lijst op het eerste niveau moeten worden aangegeven met letters.|
|TPOD0831|Het teken voor een Lijstitem mag zelf bepaald worden door het bevoegd gezag, ook als een lijst binnen een lid wordt gebruikt.|
|TPOD0840|De onderdelen van de Lijst op het tweede niveau moeten worden aangegeven met Arabische cijfers.|
|TPOD0841|Het teken voor een Lijstitem mag zelf bepaald worden door het bevoegd gezag, ook als een lijst binnen een lid wordt gebruikt.|
|TPOD0850|De onderdelen van de Lijst op het derde niveau moeten worden aangegeven met Romeinse cijfers.|
|TPOD0851|Het teken voor een Lijstitem mag zelf bepaald worden door het bevoegd gezag, ook als een lijst binnen een lid wordt gebruikt.|
|TPOD0880|Hoofdstuk 1 heeft het Opschrift Algemene bepalingen|
|TPOD0980|Hoofdstuk 1 moet een artikel 'begripsbepalingen' bevatten.|
|TPOD1000|Een Begrip moet bestaan uit één term en één definitie.|
|TPOD1010|Begrippen moeten in alfabetische volgorde worden gesorteerd.|
|TPOD1020|Begrippen mogen niet worden genummerd. (Het LiNummer mag niet gebruikt worden binnen een Begrippenlijst.)|
|TPOD1070|Meet- en rekenbepalingen mogen niet worden genummerd. (Het LiNummer mag niet gebruikt worden binnen een Begrippenlijst.)|
|TPOD1110|IMOW-objecttypen kunnen alleen worden toegepast op het Lichaam van een Regeling, niet op Bijlagen of Toelichtingen.|
|TPOD1310|Locatie heeft het attribuut hoogte, indien het attribuut hoogte gevuld wordt dient hier een waarde uit de waardelijst eenheid gekozen te worden.|
|TPOD1650|Het attribuut 'normwaarde' moet bestaan uit één van de drie mogelijke attributen; 'kwalitatieveWaarde' óf 'kwantitatieveWaarde' of 'waardeInRegeltekst'|
|TPOD1730|Gerelateerde activiteiten moeten bestaan indien er naar verwezen wordt.|
|TPOD1740|Bovenliggende activiteiten moeten bestaan indien er naar verwezen wordt.|
|TPOD1830|Binnen het object ‘Gebiedsaanwijzing’ is de waarde ‘functie’ van attribuut ‘type’ (datatype TypeGebiedsaanwijzing) niet toegestaan. (voor AMvB/MR)|
|TPOD1840|Binnen het object ‘Gebiedsaanwijzing’ is de waarde ‘beperkingengebied’ van attribuut ‘type’ (datatype TypeGebiedsaanwijzing) niet toegestaan. (voor AMvB/MR) |
|TPOD1890|De identificatie van het OwObject moet de naam van het OwObject zelf bevatten.|
|TPOD1960|Iedere verwijzing naar een gmlObject vanuit een Lijn moet een lijn-geometrie zijn.|
|TPOD1970|Iedere verwijzing naar een gmlObject vanuit een Punt moet een punt-geometrie zijn.|
|TPOD1980|Iedere verwijzing naar een gmlObject vanuit een Gebied moet een gebied-geometrie zijn.|
|TPOD1990|Ieder OwObject, behalve Activiteit heeft minstens een OwObject dat ernaar verwijst.|
|TPOD2000|het wId van de Regeltekst in OW moet verwijzen naar een bestaande wId van een Artikel of Lid in OP|
|TPOD2040|Het wId van de Divisie of Divisietekst in OW moet verwijzen naar een bestaande wId van een Divisie in OP|
|TPOD2060|Indien het Artikel is onderverdeeld in Leden, dan dient er geannoteerd te worden op het Lid (en mag er niet geannoteerd worden op het Artikel).|
|TPOD2080|Binnen een instructieregel dient er gekozen te worden tussen InstructieregelInstrument of InstructieregelTaakuitoefening (één van de twee moet voorkomen, niet meer, niet minder).|
|TPOD2090|Alle normwaarden van een norm moeten hetzelfde type zijn (kwalitatief, kwantitatief, of waardeInRegeltekst).|
|TPOD2100|Eenheid mag alleen voorkomen bij een Norm met de normwaarden van het type kwantitatief.|
|TPOD2110|Idealisatie (bij Tekstdeel) is verplicht als Tekstdeel een locatie heeft.|
|TPOD2140|Het WorkIDRegeling van het manifest-ow moet verwijzen naar een bestaande data:FRBRWork van een Regeling in OP|
|TPOD2150|Het DoelID van het manifest-ow moet verwijzen naar een bestaand doel dat aanwezig is in de bijbehorende Regeling in OP.|
|TPOD2190|In het manifest-OW mag het objecttype Geometrie niet voorkomen.|
|TPOD2200|In het manifest-OW mag een bestandsnaam niet eindigen op '.gml'|
|TPOD2210|De combinatie van Doel en Regeling uit het manifest-OW moet ook als combinatie bestaan in OP|
|TPOD2220|De door Ozon (met het Referentierapport) aangegeven geometrie(ën) MOET(EN) in de LVBB (eerder) aangeleverd en geregistreerd zijn|
|TPOD2230|De aangeleverde geometrie(ën) MOET(EN) aanwezig zijn als OW-Locatie|
|TPOD2400|Het OW-object: Regeltekst mag niet voorkomen bij Regelingen met een Vrijetekststructuur(Regelingen met een Vrijetekststructuur zijn: Omgevingsvisie, Projectbesluit, Programma, Instructie)|
|TPOD2401|Het OW-object: RegelVoorIedereen mag niet voorkomen bij Regelingen met een Vrijetekststructuur(Regelingen met een Vrijetekststructuur zijn: Omgevingsvisie, Projectbesluit, Programma, Instructie)|
|TPOD2402|Het OW-object: Instructieregel mag alleen voorkomen bij Regelingen van het type: AMvB, MR, Omgevingsverordening, en Voorbeschermingsregels op de Omgevingsverordening|
|TPOD2403|Het OW-object: Omgevingswaarderegel mag alleen voorkomen bij Regelingen van het type: AMvB, MR, Omgevingsplan en Voorbeschermingsregels|
|TPOD2404|Het OW-object: Divisie mag niet voorkomen bij Regelingen met een Artikelstructuur(Regelingen met een Artikelstructuur zijn: AMvB/ MR, Omgevingsverordening, Waterschapsverordening, Omgevingsplan, Voorbeschermingsregels, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2405|Het OW-object: Divisietekst mag niet voorkomen bij Regelingen met een Artikelstructuur(Regelingen met een Artikelstructuur zijn: AMvB/ MR, Omgevingsverordening, Waterschapsverordening, Omgevingsplan, Voorbeschermingsregels, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2406|Het OW-object: Tekstdeel mag niet voorkomen bij Regelingen met een Artikelstructuur(Regelingen met een Artikelstructuur zijn: AMvB/ MR, Omgevingsverordening, Waterschapsverordening, Omgevingsplan, Voorbeschermingsregels, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2407|Het OW-object: Hoofdlijn mag niet voorkomen bij Regelingen met een Artikelstructuur(Regelingen met een Artikelstructuur zijn: AMvB/ MR, Omgevingsverordening, Waterschapsverordening, Omgevingsplan, Voorbeschermingsregels, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2408|De OW-objecten: Activiteit en ActiviteitLocatieaanduiding mag alleen voorkomen bij Regelingen van het type: AMvB, MR, Waterschapsverordening, Omgevingsplan, Voorbeschermingsregels, en Toegangsbeperkingsbesluit|
|TPOD2409|Het OW-object: Omgevingswaarde mag alleen voorkomen bij Regelingen van het type: AMvB, MR, Omgevingsplan en Voorbeschermingsregels|
|TPOD2410|Het OW-object: Omgevingsnorm mag niet voorkomen bij Regelingen met een Vrijetekststructuur(Regelingen met een Vrijetekststructuur zijn: Omgevingsvisie, Projectbesluit, Programma, Instructie)|
|TPOD2411|Het OW-object: Gebiedsaanwijzing van het type: Beperkingengebied mag alleen voorkomen bij Regelingen van het type: Omgevingsverordening, Waterschapsverordening, Omgevingsplan en Voorbeschermingsregels|
|TPOD2412|Het OW-object: Gebiedsaanwijzing van het type: Bodem mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie, N2000 Aanwijzingsbesluit, Toegangsbeperkingsbesluit|
|TPOD2413|Het OW-object: Gebiedsaanwijzing van het type: Bouw mag alleen voorkomen bij Regelingen van het type: Omgevingsplan|
|TPOD2414|Het OW-object: Gebiedsaanwijzing van het type: Defensie mag niet voorkomen bij Regelingen van het type: Waterschapsverordening, Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2415|Het OW-object: Gebiedsaanwijzing van het type: Energievoorziening mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2416|Het OW-object: Gebiedsaanwijzing van het type: Erfgoed mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2417|Het OW-object: Gebiedsaanwijzing van het type: Externe veiligheid mag niet voorkomen bij Regelingen van het type: Waterschapsverordening, Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2418|Het OW-object: Gebiedsaanwijzing van het type: Functie mag alleen voorkomen bij Regelingen van het type: Omgevingsverordening, Omgevingsplan, Voorbeschermingsregels|
|TPOD2419|Het OW-object: Gebiedsaanwijzing van het type: Geluid mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2420|Het OW-object: Gebiedsaanwijzing van het type: Geur mag niet voorkomen bij Regelingen van het type: Waterschapsverordening, Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2421|Het OW-object: Gebiedsaanwijzing van het type: Landschap mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2422|Het OW-object: Gebiedsaanwijzing van het type: Leiding mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2423|Het OW-object: Gebiedsaanwijzing van het type: Lucht mag niet voorkomen bij Regelingen van het type: Waterschapsverordening, Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2424|Het OW-object: Gebiedsaanwijzing van het type: Mijnbouw mag niet voorkomen bij Regelingen van het type: Waterschapsverordening, Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2425|Het OW-object: Gebiedsaanwijzing van het type: Natuur mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie|
|TPOD2426|Het OW-object: Gebiedsaanwijzing van het type: Recreatie mag niet voorkomen bij Regelingen van het type: Waterschapsverordening, Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2427|Het OW-object: Gebiedsaanwijzing van het type: Ruimtelijk gebruik mag niet voorkomen bij Regelingen van het type: Waterschapsverordening, Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2428|Het OW-object: Gebiedsaanwijzing van het type: Verkeer mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2429|Het OW-object: Gebiedsaanwijzing van het type: Water en watersysteem mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie, Aanwijzingsbesluit N2000, Toegangsbeperkingsbesluit|
|TPOD2430|Het OW-object: Kaart mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie|
|TPOD2431|Het OW-object: Kaartlaag mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie|
|TPOD2432|Het OW-object: SymbolisatieItem mag niet voorkomen bij Regelingen van het type: Instructie, Reactieve interventie|
|TPOD2433|Het OW-object: Pons mag alleen voorkomen bij Regelingen van het type: Omgevingsplan|
