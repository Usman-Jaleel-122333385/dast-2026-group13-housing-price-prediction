# Housing Price Prediction FAIR Data Science Project

## Overview

This project implements a FAIR-compliant data science workflow for housing price prediction using SQL, Python, and machine learning techniques.

The repository includes:

- Normalized relational database schema
- SQL analytical views
- Machine learning preprocessing pipeline
- Model training and evaluation scripts
- FAIR metadata and semantic interoperability resources
- Reproducibility and validation documentation

---

# Repository Structure

```text
dast-2026-group13-housing-price-prediction/
│
├── data/
├── docs/
│   ├── ontology-mapping/
│   │   ├── semantic_mapping.md
│   │   └── unit_mapping.md
│   │
│   ├── validation/
│   │   └── data_validation.md
│   │
│   ├── er-diagram.png
│   ├── reproducibility.md
│   └── fair_assessment.md
│
├── metadata/
│   └── rdf/
│       └── housing_ontology.ttl
│
├── notebooks/
│   └── data_preprocessing.ipynb
│
├── outputs/
│
├── sql/
│   ├── schema.sql
│   └── views.sql
│
├── src/
│   ├── preprocessing/
│   │   └── preprocess_data.py
│   │
│   ├── training/
│   │   └── train_model.py
│   │
│   └── evaluation/
│       └── evaluate_model.py
│
├── requirements.txt
├── ro-crate-metadata.json
├── codemeta.json
├── LICENSE
└── README.md
```

---

# SQL Components

## Database Schema

Located in:

```text
sql/schema.sql
```

The schema contains normalized relational tables:

- cities
- properties
- price_records
- property_features

The design follows relational database normalization principles to reduce redundancy and improve data consistency.

---

## SQL Analytical Views

Located in:

```text
sql/views.sql
```

The analytical SQL views simplify data access for machine learning workflows and reporting.

Example analytical capabilities:

- Property feature aggregation
- Price analysis
- City-based comparisons
- ML-ready feature tables

---

# Documentation

## ER Diagram

Located in:

```text
docs/er-diagram.png
```

The ER diagram visualizes:

- Entity relationships
- Primary and foreign keys
- Database normalization structure

---

## Ontology Mapping Documentation

Located in:

```text
docs/ontology-mapping/
```

Files:

- semantic_mapping.md
- unit_mapping.md

These documents describe semantic interoperability and ontology alignment using standard vocabularies.

---

## Validation Documentation

Located in:

```text
docs/validation/data_validation.md
```

Contains:

- Dataset validation rules
- Missing value checks
- Constraint validation
- Data quality verification

---

## Reproducibility Documentation

Located in:

```text
docs/reproducibility.md
```

Contains:

- Environment setup instructions
- Dependency installation
- Pipeline execution workflow
- Reproducibility guidelines

---

## FAIR Assessment Documentation

Located in:

```text
docs/fair_assessment.md
```

Describes implementation of FAIR principles:

- Findable
- Accessible
- Interoperable
- Reusable

---

# Machine Learning Pipeline

## Data Preprocessing

Located in:

```text
src/preprocessing/preprocess_data.py
```

Responsibilities:

- Data cleaning
- Feature engineering
- Handling missing values
- Data transformation

---

## Model Training

Located in:

```text
src/training/train_model.py
```

Implements:

- Linear regression model training
- Dataset splitting
- Feature selection
- Model persistence

---

## Model Evaluation

Located in:

```text
src/evaluation/evaluate_model.py
```

Implements:

- RMSE calculation
- MAE calculation
- R² score evaluation
- Performance reporting

---

# Jupyter Notebook

Located in:

```text
notebooks/data_preprocessing.ipynb
```

Contains exploratory preprocessing workflow and experimental analysis.

---

# FAIR Metadata and Semantic Resources

## RO-Crate Metadata

Located in:

```text
ro-crate-metadata.json
```

Provides machine-readable research object metadata for FAIR compliance.

---

## CodeMeta Metadata

Located in:

```text
codemeta.json
```

Provides software metadata describing:

- Authors
- Programming languages
- Dependencies
- Repository information

---

## RDF/Turtle Semantic Representation

Located in:

```text
metadata/rdf/housing_ontology.ttl
```

Implements semantic interoperability using RDF/Turtle representation.

---

# Ontologies Used

The project uses the following ontologies:

- Schema.org
- QUDT Ontology
- GeoNames Ontology

These ontologies improve interoperability and metadata standardization.

---

# Python Requirements

Located in:

```text
requirements.txt
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# Technologies Used

## Database

- PostgreSQL
- SQL

## Programming

- Python

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## FAIR Technologies

- RO-Crate
- CodeMeta
- RDF/Turtle
- Schema.org
- QUDT
- GeoNames

## Documentation

- Markdown
- GitHub

---

# FAIR Principles Compliance

| FAIR Principle | Implementation |
|---|---|
| Findable | Metadata files and structured repository |
| Accessible | Public GitHub repository |
| Interoperable | RDF/Turtle and ontology mappings |
| Reusable | Documentation and reproducibility support |

---

# Versioning

GitHub Releases are used for milestone tracking:

- WP1 Initial Project Setup
- WP2 FAIR Database and ML Pipeline Setup

---

# License

This project is licensed under the MIT License.

See:

```text
LICENSE
```

for details.

---

# Contributors

- Usman Jaleel
- Wajahat Ali Raja
- Zohaib Sultan
- Hamza Rashid

---

# Author

Usman Jaleel  
FAIR Data Science Project  
Housing Price Prediction Workflow
