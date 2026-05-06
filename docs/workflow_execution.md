# Workflow Execution Documentation

## Overview

This document explains how to execute the FAIR-compliant housing price prediction workflow.

The workflow includes:

1. Data preprocessing
2. Model training
3. Model evaluation
4. Metadata generation
5. FAIR documentation integration

---

# Environment Setup

Install project dependencies using:

```bash
pip install -r requirements.txt
```

---

# Workflow Steps

## Step 1 — Data Preprocessing

Run:

```bash
python src/preprocessing/preprocess_data.py
```

Purpose:

- clean raw housing data
- normalize features
- prepare ML-ready datasets

---

## Step 2 — Model Training

Run:

```bash
python src/training/train_model.py
```

Purpose:

- train Linear Regression model
- split training/testing datasets
- generate trained model artifacts

---

## Step 3 — Model Evaluation

Run:

```bash
python src/evaluation/evaluate_model.py
```

Purpose:

- compute MAE
- compute RMSE
- compute R² score

---

# Metadata Resources

The workflow integrates the following FAIR metadata resources:

| Resource | Description |
|---|---|
| ro-crate-metadata.json | RO-Crate metadata |
| codemeta.json | Software metadata |
| metadata/fair4ml.json | FAIR4ML metadata |
| metadata/pipeline_metadata.json | Pipeline configuration metadata |
| metadata/rdf/housing_ontology.ttl | RDF ontology representation |

---

# FAIR Documentation Resources

The workflow also references:

- FAIR assessment
- model card
- reproducibility documentation
- provenance tracking
- experiment tracking
- model versioning

---

# Reproducibility Support

The workflow ensures reproducibility through:

- version-controlled code
- fixed random seeds
- documented dependencies
- metadata integration
- semantic interoperability

---

# FAIR Compliance

The workflow supports FAIR principles by enabling:

- structured metadata
- reusable ML workflows
- semantic interoperability
- transparent experiment execution

---

# Conclusion

This workflow provides a reproducible and FAIR-compliant machine learning environment for housing price prediction experiments.
