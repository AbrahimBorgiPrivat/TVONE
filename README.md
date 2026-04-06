# TVONE

TVONE is a standalone extraction of the TV1 slice from `DATA PROJECTS`.

The repository contains the TV-specific resources, runtime definitions, ETL services, dbt project, semantic model, Tabular assets, and the shared Python code needed to run them without the old nested `tv1/` layout.

![TVONE overview](res/pbi/OVERVIEW-Page.png)

## What is included

- JSON source files for programs, seasons, episodes, and segmentation
- simulation code for users and streaming tracking
- ETL services for JSON load, SQL table/view creation, and simulations
- dbt models for staging and marts
- PBIP semantic model and Tabular Editor scripts

## Project structure

```text
TVONE/
|-- docs/
|-- res/
|   |-- json/
|   `-- pbi/
|-- src/
|   |-- code/
|   |   |-- libraries/
|   |   |-- runtime_definitions/
|   |   `-- service/
|   `-- workspace-serve/
`-- README.md
```

## Key paths

- `src/code/runtime_definitions/` holds runtime JSON files for each load step
- `src/code/service/etl/` contains the Dockerized ETL services
- `src/code/service/dbt/` contains the dbt project used for staging and marts
- `src/workspace-serve/SemanticModel/` contains the Power BI project and semantic model
- `src/workspace-serve/Tabular/` contains Tabular Editor scripts and DAX assets

## Typical flow

1. Load metadata JSON files into PostgreSQL via `service_json_to_client`
2. Create tables and supporting views via `service_create_table_views_from_sql`
3. Generate simulated users and tracking rows via `service_simulations`
4. Build staging and marts with dbt
5. Refresh the semantic model and Tabular assets

## Notes

- Paths have been flattened for the standalone repo, so references now point to local folders such as `res/json` and `src/code/runtime_definitions/...`
- Database and schema targets remain aligned with the original TV1 setup

## Documentation

- [Documentation overview](docs/README.md)
- [Tabular automation notes](src/workspace-serve/Tabular/README.md)
