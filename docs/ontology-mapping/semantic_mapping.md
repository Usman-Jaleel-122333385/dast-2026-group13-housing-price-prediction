# Semantic Mapping of Housing Dataset Attributes

## Ontologies Used

This project uses semantic mappings to improve the Findability and Interoperability aspects of FAIR principles.

The following ontologies were selected:

- Schema.org
- GeoNames Ontology
- QUDT (Quantities, Units, Dimensions and Data Types)

These ontologies were selected because they are widely used, well-documented, and appropriate for describing real-estate and geographical data.

---

## Attribute Mapping Table

| Dataset Attribute | Semantic Meaning | Ontology | Concept URI |
|---|---|---|---|
| city_name | Name of city | Schema.org | https://schema.org/City |
| country_name | Country location | Schema.org | https://schema.org/Country |
| property_type | Type of property | Schema.org | https://schema.org/Residence |
| construction_year | Year building constructed | Schema.org | https://schema.org/Date |
| total_rooms | Number of rooms | Schema.org | https://schema.org/numberOfRooms |
| property_size_m2 | Property area size | QUDT | http://qudt.org/schema/qudt/Quantity |
| listing_price_eur | Listing price in Euro | QUDT | http://qudt.org/schema/qudt/MonetaryUnit |
| listing_date | Property listing date | Schema.org | https://schema.org/Date |

---

## FAIR Interoperability Justification

The selected ontologies provide semantic interoperability by linking dataset attributes to standardized concepts that are machine-readable and internationally recognized. This improves metadata consistency and supports data reuse across systems and platforms.

Schema.org was selected because it is widely adopted for describing structured web and real-estate information. Geo-related concepts support geographical interpretation of the dataset, while QUDT enables semantic description of quantitative measurements and monetary values.
