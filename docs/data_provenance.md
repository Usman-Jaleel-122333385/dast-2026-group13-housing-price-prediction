# Data Provenance Documentation

## Overview

This document describes the provenance and lifecycle of the housing price prediction dataset used in this FAIR Data Science project.

The purpose of provenance tracking is to improve transparency, reproducibility, and trustworthiness of the data processing workflow.

---

## Dataset Origin

The dataset consists of structured housing-related information used for educational machine learning experiments.

The dataset contains:

- Property information
- Construction year
- Property size
- Number of rooms
- City and country information
- Housing listing prices

The dataset was prepared specifically for FAIR and reproducible data science experimentation.

---

## Data Collection Process

The dataset was collected from publicly available structured housing-related records and manually organized into normalized relational tables.

The data collection workflow included:

1. Data acquisition
2. Schema normalization
3. Data cleaning
4. Missing-value handling
5. Validation and consistency checking

---

## Data Transformation Pipeline

The preprocessing workflow includes:

- Duplicate removal
- Missing value handling
- Numerical feature selection
- Feature scaling preparation
- SQL analytical view generation
- Export preparation for machine learning tasks

The preprocessing implementation is located in:

```text
src/preprocessing/preprocess_data.py
