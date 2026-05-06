# Housing Price Prediction using FAIR Data Science Principles

This project implements a FAIR-compliant machine learning pipeline for housing price prediction using normalized relational databases, semantic metadata, and reproducible ML workflows.

---

# Project Objectives

The main objectives of this project are:

- Build a housing price prediction pipeline
- Apply FAIR Data Science principles
- Normalize housing datasets into SQL schemas
- Create reproducible ML workflows
- Implement semantic metadata standards
- Support interoperability and reproducibility
- Provide machine-readable FAIR metadata

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
│   ├── experiment_tracking.md
│   ├── fair_assessment.md
│   ├── fair_workflow.md
│   ├── model-card.md
│   ├── model_versioning.md
│   ├── repository_packaging.md
│   ├── reproducibility.md
│   └── workflow_execution.md
│
├── metadata/
│   ├── rdf/
│   │   └── housing_ontology.ttl
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
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── LICENSE
├── codemeta.json
├── requirements.txt
└── ro-crate-metadata.json
```

---

# FAIR Metadata Implementation

This repository includes multiple FAIR metadata standards:

| Metadata File | Description |
|---|---|
| ro-crate-metadata.json | RO-Crate research object metadata |
| codemeta.json | Software metadata specification |
| metadata/fair4ml.json | FAIR4ML metadata for ML workflows |
| metadata/pipeline_metadata.json | Pipeline metadata configuration |
| metadata/rdf/housing_ontology.ttl | RDF Turtle semantic ontology |

---

# FAIR Documentation

The repository includes detailed FAIR documentation:

| Documentation File | Purpose |
|---|---|
| docs/fair_assessment.md | FAIR compliance assessment |
| docs/reproducibility.md | Reproducibility strategy |
| docs/model-card.md | Model transparency documentation |
| docs/data_provenance.md | Dataset provenance tracking |
| docs/experiment_tracking.md | Experiment logging procedures |
| docs/model_versioning.md | Model version management |
| docs/fair_workflow.md | FAIR workflow lifecycle |
| docs/workflow_execution.md | Workflow execution documentation |
| docs/repository_packaging.md | Repository packaging structure |

---

# Machine Learning Pipeline

The project pipeline consists of:

1. Data preprocessing
2. SQL normalization
3. Feature engineering
4. Model training
5. Model evaluation
6. Metadata generation
7. FAIR documentation

---

# SQL Database Design

The housing dataset is normalized into relational schemas using SQL.

Files:

- `sql/schema.sql`
- `sql/views.sql`

The SQL implementation supports:

- normalized data storage
- analytical queries
- machine learning feature extraction
- reproducible data workflows

---

# Semantic Ontology Mapping

Semantic interoperability is implemented using RDF Turtle ontology mappings.

Location:

```text
metadata/rdf/housing_ontology.ttl
```

Ontology mappings improve:

- interoperability
- semantic discoverability
- metadata reuse
- linked data compatibility

---

# FAIR Reproducibility Features

This repository supports reproducible machine learning through:

- Git versioning
- GitHub Releases
- Docker containers
- Docker Compose
- GitHub Actions CI/CD
- metadata standards
- workflow documentation
- environment configuration

---

# GitHub Actions Workflow

Continuous Integration workflow:

```text
.github/workflows/python-ci.yml
```

The workflow automatically validates:

- Python syntax
- metadata availability
- documentation completeness
- SQL resources
- FAIR repository structure

---

# Containerization Support

## Docker

Docker support is included through:

```text
Dockerfile
```

## Docker Compose

Container orchestration support:

```text
docker-compose.yml
```

## Environment Configuration

Example environment variables:

```text
.env.example
```

---

# FAIR Principles Compliance

| FAIR Principle | Implementation |
|---|---|
| Findable | Metadata standards and GitHub releases |
| Accessible | Public repository and documentation |
| Interoperable | RDF, RO-Crate, FAIR4ML metadata |
| Reusable | Reproducible workflows and containers |

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Data Preprocessing

```bash
python src/preprocessing/preprocess_data.py
```

## Train the Model

```bash
python src/training/train_model.py
```

## Evaluate the Model

```bash
python src/evaluation/evaluate_model.py
```

## Run with Docker

### Build Docker Image

```bash
docker build -t housing-price-prediction .
```

### Run Docker Container

```bash
docker run housing-price-prediction
```

## Run with Docker Compose

```bash
docker-compose up
```

---

# Releases

The repository uses semantic versioning and GitHub Releases.

Example releases:

| Version | Description |
|---|---|
| v0.1.0-wp1 | Initial repository setup |
| v0.2.0-wp2 | FAIR database and ML pipeline setup |
| v0.3.0-t3 | FAIR metadata and documentation completion |

---

# License

This project is distributed under the MIT License.

See:

```text
LICENSE
```

---

# Authors

FAIR Data Science Project  
Housing Price Prediction using FAIR ML Principles

---

# Conclusion

This repository demonstrates a complete FAIR-compliant machine learning workflow for housing price prediction using reproducible pipelines, semantic metadata, interoperable standards, and reproducible deployment environments.
