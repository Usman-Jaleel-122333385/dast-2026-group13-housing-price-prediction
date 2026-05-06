# Predicting Housing Prices Using Real Estate Data in European Cities

## Abstract
This project focuses on predicting housing prices using structured real estate data collected from European cities. The experiment follows FAIR data principles and includes metadata standards, semantic annotations, reproducible machine learning workflows, and open-science publication practices.

## Repository Structure

- `data/` — raw, processed, and external datasets
- `src/` — source code for preprocessing, training, evaluation, and DBRepo access
- `notebooks/` — Jupyter notebooks for experiment execution
- `outputs/` — generated figures, trained models, and predictions
- `docs/` — documentation, validation outputs, and ontology mapping notes
- `metadata/` — FAIR metadata files
- `sql/` — SQL schema and view definitions

## File Organisation

### Input datasets
`raw_<dataset-name>_<version>.csv`

### Processed datasets
`processed_<description>.csv`

### Scripts
`step##_task_description.py`

### Models
`model_<algorithm>_<date>.pkl`

### Figures
`fig_##_<description>.png`

### Configuration files
`config_<task>.yaml`

## Database Schema

The project database schema is implemented in Third Normal Form (3NF) and consists of the following tables:

- `cities`
- `properties`
- `price_records`
- `property_features`

The schema is defined in:

```text
sql/schema.sql
```

The entity-relationship diagram is available at:

```text
docs/er-diagram.png
```

## SQL Views

The project defines SQL views to provide query-ready data for analysis and machine learning.

### `ml_feature_table`
This view joins city, property, and price information into one feature table for the machine learning pipeline.

### `city_price_summary`
This view provides aggregated housing price information per city, including average listing price and number of properties.

### `large_properties`
This view filters properties larger than 100 square metres and can be used for analysis of larger housing units.

The SQL view definitions are stored in:

```text
sql/views.sql
```

## Contributors

- Usman Jaleel — 12333385
- Wajahat Ali Raja — 12333424
- Zohaib Sultan — 12319879
- Hamza Rashid — 12332272

## Licence

Software code in this repository is released under the MIT Licence.
