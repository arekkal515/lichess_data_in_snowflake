# Lichess Data in Snowflake
Git integration with Snowflake and lichess data

## Setup environment
Use commands from notebook

## Data Ingestion
Load extracted data through snowsql

```bash
USE DATABASE <name_of_database>;
USE SCHEMA <name_of_schema>;
PUT <absolute_path_of_file> <name_of_stage_in_Snowflake> AUTO_COMPRESS=TRUE;
```
