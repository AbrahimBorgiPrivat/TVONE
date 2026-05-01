# TVONE

[GitHub Pages](https://abrahimborgiprivat.github.io/TVONE/html/index.html)

TVONE er et komplet streaming analytics-projekt med fokus på metadata, simuleret brugeradfærd, ETL, datamodellering og Power BI-rapportering.

Projektet samler hele flowet fra kildedata til rapport i ét repo:

- JSON-baserede metadata for programmer, sæsoner, episoder og segmentering
- Python-services til data load, SQL-oprettelse og simulationer
- PostgreSQL som datalager
- dbt til staging- og marts-modeller
- semantisk model og Power BI-rapportering
- dokumentation, billeder og GitHub Pages-site

![TVONE overview](res/rapport/img/OVERVIEW-Page.png)

## Formål

TVONE er bygget som en case, der viser hvordan et streamingdomæne kan modelleres og rapporteres uden adgang til produktionsdata. Løsningen kombinerer indholdsmetadata med simulerede brugere og streaminghændelser, så rapporten kan analysere aktivitet, platformsmønstre og programperformance.

## Hvad projektet indeholder

- `res/json/`
  rå metadatafiler for programmer, sæsoner, episoder og segmentering
- `src/code/runtime_definitions/`
  runtime-filer til load, SQL-jobs og simulationer
- `src/code/service/etl/`
  ETL-services til JSON-load, oprettelse af tabeller/views og simulationer
- `src/code/service/dbt/`
  dbt-projekt med staging- og marts-lag
- `src/workspace-serve/SemanticModel/`
  semantisk model og rapportgrundlag
- `site/`
  statisk GitHub Pages-site for præsentation af casen
- `docs/`
  dokumentation og Word/PDF-præsentation

## Projektstruktur

```text
TVONE/
|-- .github/
|-- docs/
|-- res/
|   |-- json/
|   `-- rapport/
|       `-- img/
|-- site/
|   |-- assets/
|   |-- css/
|   `-- html/
|-- src/
|   |-- code/
|   |   |-- libraries/
|   |   |-- runtime_definitions/
|   |   `-- service/
|   |       |-- dbt/
|   |       `-- etl/
|   `-- workspace-serve/
`-- README.md
```

## Centrale stier

- `src/code/runtime_definitions/json_to_client/`
  runtime-filer til indlæsning af JSON-metadata
- `src/code/runtime_definitions/create_table_and_views/`
  runtime-filer og SQL til schema, tabeller og views
- `src/code/runtime_definitions/simulations/`
  runtime-filer til generering af brugere og tracking
- `src/code/service/etl/`
  de kørbare ETL-services
- `src/code/service/dbt/models/`
  staging-, marts- og view-modeller til rapportlaget
- `src/workspace-serve/SemanticModel/`
  semantisk model med tabeller, relationer og measures

## Overordnet flow

1. Metadata for programmer, sæsoner, episoder og segmentering indlæses i PostgreSQL.
2. SQL-services opretter schema, tabeller og understøttende views.
3. Python-simulationer genererer brugere og streaminghændelser.
4. dbt bygger staging- og marts-lag oven på de indlæste data.
5. Den semantiske model og Power BI-rapporten læser de transformerede tabeller.

## Rapportering

Rapportdelen er i denne case bygget som én samlet overview-side. Den viser blandt andet:

- stream-minutter, sessioner og aktive brugere
- fordeling på platforme som TV, Mobile og Tablet
- udvikling over tid
- mest sete programmer
- filtrering på målinger, kategori, program og periode

## Dokumentation

- [Dokumentationsoversigt](docs/README.md)
- [Word-præsentation](docs/Abrahim_Borgi_TVONE_Simulation_Project.docx)
- [GitHub Pages-site](site/html/index.html)
