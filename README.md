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
