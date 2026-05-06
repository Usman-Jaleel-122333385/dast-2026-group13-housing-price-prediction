# Reproducibility Documentation

## Objective

This project follows reproducible machine learning and FAIR data science practices to ensure that all preprocessing, training, and evaluation steps can be repeated consistently.

---

## Repository Structure

The repository is organized into dedicated directories for:
- datasets
- preprocessing scripts
- training scripts
- evaluation scripts
- notebooks
- metadata
- SQL schema and views

---

## Reproducible Workflow

### Step 1 — Data Preprocessing

Run:

```bash
python src/preprocessing/preprocess_data.py
```

This script:
- removes duplicates
- removes missing values
- validates numeric columns
- exports processed datasets

---

### Step 2 — Model Training

Run:

```bash
python src/training/train_model.py
```

This script:
- loads processed datasets
- trains a linear regression model
- stores trained model artifacts

---

### Step 3 — Model Evaluation

Run:

```bash
python src/evaluation/evaluate_model.py
```

This script:
- loads trained models
- evaluates prediction quality
- reports evaluation metrics

---

## Software Dependencies

Dependencies are listed in:

```text
requirements.txt
```

---

## FAIR Reproducibility Support

The repository supports reproducibility through:
- version control using GitHub
- explicit preprocessing pipelines
- documented metadata
- semantic annotations
- structured SQL schemas
- reusable notebooks and scripts
