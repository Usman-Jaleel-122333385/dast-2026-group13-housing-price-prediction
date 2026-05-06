# FAIR Workflow Documentation

## Overview

This document describes the FAIR-oriented workflow used in the housing price prediction project.

The workflow was designed to support reproducibility, interoperability, accessibility, and machine-readable metadata integration.

---

# Workflow Stages

## 1. Data Collection

The workflow begins with structured housing-related data acquisition.

Collected information includes:

- City information
- Country information
- Property characteristics
- Listing prices
- Property features

The collected data is normalized into relational database tables.

---

## 2. Data Storage

The dataset is stored using a normalized SQL schema consisting of:

- cities
- properties
- price_records
- property_features

Schema implementation:

```text
sql/schema.sql
```

---

## 3. Data Preprocessing

The preprocessing workflow performs:

- Missing-value handling
- Duplicate removal
- Feature preparation
- Data validation
- SQL analytical view generation

Implementation file:

```text
src/preprocessing/preprocess_data.py
```

---

## 4. Machine Learning Pipeline

The machine learning workflow includes:

- Feature selection
- Training/test split
- Linear Regression model training
- Model evaluation
- Performance reporting

Training script:

```text
src/training/train_model.py
```

Evaluation script:

```text
src/evaluation/evaluate_model.py
```

---

## 5. Metadata Integration

The project integrates multiple FAIR metadata standards:

| Metadata Standard | File |
|---|---|
| RO-Crate | ro-crate-metadata.json |
| CodeMeta | codemeta.json |
| FAIR4ML | metadata/fair4ml.json |
| RDF/Turtle Ontology | metadata/rdf/housing_ontology.ttl |

---

## 6. Semantic Interoperability

Semantic interoperability is supported using ontology mappings and RDF representations.

Ontologies used include:

- Schema.org
- GeoNames
- QUDT

Mapping files:

```text
docs/ontology-mapping/
```

---

## 7. Reproducibility Support

The workflow supports reproducibility through:

- Version-controlled code
- GitHub releases
- Structured project organization
- Requirements specification
- FAIR documentation
- Metadata versioning

---

## 8. FAIR Principles Alignment

| FAIR Principle | Implementation |
|---|---|
| Findable | GitHub releases and metadata |
| Accessible | Open repository structure |
| Interoperable | RDF and ontology mappings |
| Reusable | Documentation and licensing |

---

## Conclusion

This workflow demonstrates a complete FAIR-oriented machine learning and metadata integration pipeline for reproducible housing price prediction experiments.
