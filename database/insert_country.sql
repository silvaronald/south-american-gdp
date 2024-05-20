INSERT INTO country (id, name, iso3_code)
VALUES (%s, %s, %s)
ON DUPLICATE KEY UPDATE id=id;