# Unit Mapping for Numeric Attributes

## Ontology Used

This project uses QUDT (Quantities, Units, Dimensions and Data Types) to provide semantic descriptions for units of measurement associated with numeric dataset attributes.

QUDT was selected because it is a well-established ontology for describing scientific quantities and units in interoperable machine-readable formats.

---

## Unit Mapping Table

| Numeric Attribute | Description | Unit | QUDT URI |
|---|---|---|---|
| property_size_m2 | Size of property | Square Metre | http://qudt.org/vocab/unit/M2 |
| listing_price_eur | Property listing price | Euro | http://qudt.org/vocab/currency/EUR |
| total_rooms | Number of rooms | Count | http://qudt.org/vocab/unit/NUM |
| construction_year | Construction year | Year | http://qudt.org/vocab/unit/YR |

---

## FAIR Interoperability Benefits

Semantic unit mappings improve interoperability and machine readability by linking numeric values to standardized unit definitions.

The use of QUDT allows external systems and metadata processing tools to correctly interpret quantitative information within the housing dataset.
