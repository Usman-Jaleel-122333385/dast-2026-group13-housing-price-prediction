# Repository Packaging Documentation

## Overview

This document describes the FAIR repository packaging strategy used in the Housing Price Prediction project. The repository is organized to support reproducibility, accessibility, interoperability, and reusability of machine learning workflows and metadata artifacts.

---

# Repository Structure

The repository is organized into modular directories for SQL schemas, preprocessing pipelines, training workflows, metadata management, and FAIR documentation.

```text
dast-2026-group13-housing-price-prediction/
│
├── docs/
│   ├── ontology-mapping/
│   ├── validation/
│   ├── data_provenance.md
│   ├── experiment_tracking.md
│   ├── fair_assessment.md
│   ├── fair_workflow.md
│   ├── model-card.md
│   ├── model_versioning.md
│   ├── reproducibility.md
│   ├── workflow_execution.md
│   └── repository_packaging.md
│
├── metadata/
│   ├── rdf/
│   ├── dataset_metadata.md
│   ├── fair4ml.json
│   └── pipeline_metadata.json
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
│   ├── evaluation/
│   │   └── evaluate_model.py
│   ├── preprocessing/
│   │   └── preprocess_data.py
│   └── training/
│       └── train_model.py
│
├── README.md
├── requirements.txt
├── codemeta.json
├── ro-crate-metadata.json
└── LICENSE
