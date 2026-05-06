# Housing Price Prediction using FAIR Data Science Principles

This project implements a FAIR-compliant machine learning pipeline for housing price prediction using normalized relational databases, semantic metadata, and reproducible ML workflows.

The implementation follows FAIR principles:
- Findable
- Accessible
- Interoperable
- Reusable

---

# Project Objectives

The objectives of this project are:

- Build a normalized relational database for housing data
- Create SQL analytical views for ML processing
- Develop preprocessing, training, and evaluation pipelines
- Apply FAIR metadata standards
- Support semantic interoperability using RDF and ontology mappings
- Enable reproducible machine learning execution
- Provide containerized deployment support

---

# Repository Structure

```text
dast-2026-group13-housing-price-prediction/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── data/
│
├── docs/
│   ├── ontology-mapping/
│   ├── validation/
│   ├── data_provenance.md
│   ├── er-diagram.png
│   ├── experiment_tracking.md
│   ├── fair_assessment.md
│   ├── fair_workflow.md
│   ├── final_execution_report.md
│   ├── model-card.md
│   ├── model_versioning.md
│   ├── repository_packaging.md
│   ├── reproducibility.md
│   └── workflow_execution.md
│
├── metadata/
│   ├── rdf/
│   ├── dataset_metadata.md
│   ├── fair4ml.json
│   └── pipeline_metadata.json
│
├── notebooks/
│
├── outputs/
│   ├── figures/
│   ├── models/
│   ├── metrics.json
│   ├── model.pkl
│   ├── predictions.csv
│   └── training_log.txt
│
├── sql/
│   ├── schema.sql
│   └── views.sql
│
├── src/
│   ├── dbrepo/
│   ├── evaluation/
│   ├── preprocessing/
│   └── training/
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── README.md
├── codemeta.json
├── requirements.txt
└── ro-crate-metadata.json
```

---

# FAIR Metadata Components

The repository contains multiple FAIR metadata standards and semantic documentation files.

## Included FAIR Metadata

- RO-Crate metadata
- CodeMeta metadata
- FAIR4ML metadata
- RDF Turtle ontology mappings
- Data provenance documentation
- Workflow metadata
- Experiment tracking documentation
- Model versioning documentation
- FAIR assessment documentation

---

# Machine Learning Workflow

The machine learning workflow includes:

1. Data preprocessing
2. Feature engineering
3. Model training
4. Model evaluation
5. Prediction generation
6. Metadata documentation

---

# SQL Database Layer

The relational database implementation includes:

- normalized schema design
- analytical SQL views
- feature extraction support
- machine learning integration

Files:
- `sql/schema.sql`
- `sql/views.sql`

---

# Semantic Interoperability

The repository supports semantic interoperability using RDF and ontology mappings.

Included semantic resources:
- RDF Turtle ontology
- semantic unit mappings
- metadata mappings
- FAIR ontology references

---

# Reproducibility Support

The project supports reproducible research through:

- Docker containerization
- GitHub Actions CI workflow
- dependency management
- version-controlled metadata
- standardized documentation
- workflow execution tracking

---

# GitHub Actions CI

The repository includes a GitHub Actions workflow:

```text
.github/workflows/python-ci.yml
```

The workflow validates:
- Python setup
- dependency installation
- FAIR reproducibility configuration

---

# Docker Execution

## Build Docker Image

```bash
docker build -t housing-fair-ml .
```

## Run Docker Container

```bash
docker run housing-fair-ml
```

## Docker Compose

```bash
docker-compose up
```

---

# Local Installation

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Pipeline Execution

## Run Preprocessing

```bash
python src/preprocessing/preprocess.py
```

## Run Model Training

```bash
python src/training/train_model.py
```

## Run Evaluation

```bash
python src/evaluation/evaluate_model.py
```

---

# Documentation Files

| File | Purpose |
|---|---|
| `docs/fair_assessment.md` | FAIR compliance assessment |
| `docs/reproducibility.md` | Reproducibility strategy |
| `docs/model-card.md` | ML model documentation |
| `docs/data_provenance.md` | Dataset origin and lineage |
| `docs/experiment_tracking.md` | Experiment tracking process |
| `docs/model_versioning.md` | Model versioning strategy |
| `docs/fair_workflow.md` | FAIR ML workflow |
| `docs/workflow_execution.md` | Workflow execution steps |
| `docs/repository_packaging.md` | Repository packaging structure |
| `docs/final_execution_report.md` | Final execution validation report |

---

# Example Outputs

The project generates reproducible machine learning artifacts and evaluation outputs.

Generated outputs include:

- `outputs/metrics.json`
- `outputs/predictions.csv`
- `outputs/training_log.txt`
- `outputs/model.pkl`

These files demonstrate:
- model evaluation metrics
- prediction generation
- workflow logging
- trained model storage

---

# FAIR Principles Coverage

| FAIR Principle | Implementation |
|---|---|
| Findable | RO-Crate metadata, CodeMeta |
| Accessible | GitHub repository and documentation |
| Interoperable | RDF ontology mappings and semantic metadata |
| Reusable | Docker, CI workflows, reproducibility documentation |

---

# License

This project is released under the MIT License.

---

# Authors

FAIR Data Science Group 13  
TU Wien — DAST 2026
