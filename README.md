# Housing Price Prediction using FAIR Data Science Principles

This project implements a FAIR-compliant machine learning pipeline for housing price prediction using normalized relational databases, semantic metadata, and reproducible ML workflows.

---

# Project Objectives

- Build a normalized relational database schema for housing datasets
- Create SQL analytical views for machine learning
- Implement preprocessing, training, and evaluation pipelines
- Apply FAIR Data Science principles
- Provide semantic metadata and ontology mappings
- Ensure reproducibility and interoperability

---

# Repository Structure

```text
dast-2026-group13-housing-price-prediction/
│
├── docs/
│   ├── ontology-mapping/
│   │   ├── semantic_mapping.md
│   │   └── unit_mapping.md
│   │
│   ├── validation/
│   │   └── data_validation.md
│   │
│   ├── er-diagram.png
│   ├── fair_assessment.md
│   ├── model-card.md
│   ├── data_provenance.md
│   ├── fair_workflow.md
│   └── reproducibility.md
│
├── metadata/
│   ├── rdf/
│   │   └── housing_ontology.ttl
│   │
│   ├── dataset_metadata.md
│   └── fair4ml.json
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
│   ├── dbrepo/
│   ├── preprocessing/
│   │   └── preprocess_data.py
│   │
│   ├── training/
│   │   └── train_model.py
│   │
│   └── evaluation/
│       └── evaluate_model.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── codemeta.json
└── ro-crate-metadata.json
```

---

# Database Design

The project uses a normalized relational schema containing:

- cities
- properties
- property_features
- price_records

The schema supports:

- historical housing price tracking
- feature engineering
- machine learning analytics
- semantic interoperability

---

# ER Diagram

The relational schema ER diagram is provided in:

```text
docs/er-diagram.png
```

---

# SQL Components

## schema.sql

Contains:

- normalized relational schema
- primary keys
- foreign keys
- constraints

## views.sql

Contains analytical SQL views for:

- ML feature extraction
- property aggregation
- price analysis
- semantic integration

---

# Machine Learning Pipeline

## Preprocessing

File:

```text
src/preprocessing/preprocess_data.py
```

Tasks:

- data cleaning
- missing value handling
- feature engineering
- normalization

---

## Training

File:

```text
src/training/train_model.py
```

Implements:

- Linear Regression training
- train/test split
- model serialization

---

## Evaluation

File:

```text
src/evaluation/evaluate_model.py
```

Computes:

- MAE
- RMSE
- R² Score

---

# FAIR Metadata and Semantic Resources

## RO-Crate Metadata

File:

```text
ro-crate-metadata.json
```

Provides machine-readable metadata for:

- datasets
- software
- workflows
- authorship

---

## CodeMeta Metadata

File:

```text
codemeta.json
```

Provides software-level metadata using the CodeMeta standard.

---

## FAIR4ML Metadata

File:

```text
metadata/fair4ml.json
```

Describes FAIR metadata for machine learning workflows and models.

---

# Semantic Ontology Mapping

Directory:

```text
docs/ontology-mapping/
```

Contains:

- semantic_mapping.md
- unit_mapping.md

Mapped ontologies include:

- Schema.org
- GeoNames
- QUDT

---

# RDF/Turtle Representation

File:

```text
metadata/rdf/housing_ontology.ttl
```

Provides semantic RDF/Turtle ontology representation of the housing dataset.

---

# FAIR Documentation

## FAIR Assessment

File:

```text
docs/fair_assessment.md
```

Documents FAIR compliance analysis.

---

## Model Card

File:

```text
docs/model-card.md
```

Describes:

- model purpose
- limitations
- intended use
- ethical considerations

---

## Data Provenance

File:

```text
docs/data_provenance.md
```

Tracks:

- dataset origin
- preprocessing history
- transformation lineage

---

## FAIR Workflow

File:

```text
docs/fair_workflow.md
```

Documents:

- FAIR ML lifecycle
- metadata integration
- reproducibility workflow

---

## Reproducibility

File:

```text
docs/reproducibility.md
```

Contains reproducibility instructions for:

- environment setup
- dependency installation
- workflow execution

---

# Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 — Preprocessing

```bash
python src/preprocessing/preprocess_data.py
```

## Step 2 — Training

```bash
python src/training/train_model.py
```

## Step 3 — Evaluation

```bash
python src/evaluation/evaluate_model.py
```

---

# FAIR Compliance Summary

This repository implements several FAIR principles:

| FAIR Principle | Implementation |
|---|---|
| Findable | RO-Crate + CodeMeta metadata |
| Accessible | Structured repository and documentation |
| Interoperable | RDF/Turtle ontology and semantic mappings |
| Reusable | Reproducible ML workflows and metadata |

---

# Authors

Group 13 — DAST 2026

Project: Housing Price Prediction using FAIR Data Science Principles

---

# License

This project is licensed under the MIT License.
