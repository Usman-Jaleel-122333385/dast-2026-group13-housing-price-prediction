CREATE VIEW ml_feature_table AS
SELECT
    p.property_id,
    c.city_name,
    c.country_name,
    p.property_type,
    p.construction_year,
    p.total_rooms,
    p.property_size_m2,
    pr.listing_price_eur
FROM properties p
JOIN cities c ON p.city_id = c.city_id
JOIN price_records pr ON p.property_id = pr.property_id;

CREATE VIEW city_price_summary AS
SELECT
    c.city_name,
    AVG(pr.listing_price_eur) AS average_price,
    COUNT(p.property_id) AS total_properties
FROM cities c
JOIN properties p ON c.city_id = p.city_id
JOIN price_records pr ON p.property_id = pr.property_id
GROUP BY c.city_name;

CREATE VIEW large_properties AS
SELECT
    p.property_id,
    p.property_type,
    p.property_size_m2,
    pr.listing_price_eur
FROM properties p
JOIN price_records pr ON p.property_id = pr.property_id
WHERE p.property_size_m2 > 100;
