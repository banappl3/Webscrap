# Data on Automobile by Yongguang Lin


### 🗂️ Download our complete automobile dataset : [CSV](https://...de) | [DB](https://..db) | [JSON](https://..json)

Unser vollständiger Automible-Datensatz ist eine Sammlung der Fahrzeug-Daten, die von [_mobile.de_](https://www.mobile.de/) und [_AutoScount24_](https://www.autoscout24.de/) zur Verfügung gestellt werden. Wir werden ihn regelmäßig aktualisieren (weitere Informationen zu unserem Aktualisierungsprozess und Zeitplan [hier](https://..de)). Er enthält die folgenden Daten:

| Metrics                     | Quellen                                                    | Updated | Länder |
|-----------------------------|-----------------------------------------------------------|---------|-----------|
| Gebrauchswagen                | mobile.de      | jährlich   | 1, DE   |
| Neuwagen          | mobile.de     | jährlich  | 1, DE       |
| Gebrauchswagen                | autoscout24.de      | jährlich   | 1, DE   |
| Neuwagen          | autoscout24.de     | jährlich  | 1, DE       |

Unser vollständiger Fahrzeug-Datensatz ist in den Formaten CSV, DB und JSON verfügbar und enthält alle unsere historischen Daten der letzten 10 Jahren bis zum Datum der Veröffentlichung.

Die CSV-Dateien verwendet den Seperator ";" und die UTF-8-Kodierung. Die DB-Dateien werden mit dem Python-Package sqlite3 geladen. Die JSON-Version ist nach dem Postleitzahl des Bundeslandes aufgeteilt.


### Tabellenbeschreibung

| Variable                         | Description                                                                                                                                                                                            |
|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `marke`                    | Der Autohersteller z.B. Audi, BMW oder Mercedes-Benz|
| `modell`                    | Das Automodell des Herstellers z.B. A3 der Marke Audi|
| `variante`                    | Die Variante des Automodells |
| `preis`                    | Der veröffentlichte Preiswert des Autos |
| `ort`                    | Der Verkaufsort |
| `plz`                    | Die Postleitzahl |
| `straße`                    | Die Straße |
| `bundesland`                    | Das Bundesland, in dem das Fahrzeug sich befindet |
| `land`                    | Nur in Deutschland verkaufte Fahrzeuge |
| `kilometerstand`                    | Der gefahrene Kilometerstand |
| `leistung`                    | Die Fahrzeugleistung in kW |
| `baujahr`                    | Das Baujahr des Fahrzeugs |
| `hubraum`                    | Der Hubraum des Fahrzeugs |
| `karosserieform`                    | Die Karosserieform z.B. Kombi |
| `fahrzeughalter`                    | Die Anzahl des  Fahrzeughalters|
| `ausstattung`                    | Die Ausstattungen des Fahrzeugs z.B. Sommer- und/oder Winterreifen|
| `getriebe`                    | Das Fahrzeuggetriebe: Schaltgetrieb oder Automatik |
| `verkaeufer`                    | Verkauf durch Haendler oder privater Verkauf |
| `scheckheftgepflegt`                    | Pflege des Scheckhefts |
| `schadstoffklasse`                    | Die Schadstoffklasse |
| `umweltplakette`                    | Umweltplakette z.B. Euro 6 |
| `kraftstoffverbrauch`                    | Der Kraftstoffverbrauch , innerorts - außerorts - kombiniert|
| `...`                    |  |

	


