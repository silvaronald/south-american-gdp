CREATE DATABASE IF NOT EXISTS gdp_sa;
USE gdp_sa;

CREATE TABLE country (
    id VARCHAR(2) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    iso3_code VARCHAR(50) NOT NULL
);

CREATE TABLE gdp (
    country_id VARCHAR(2),
    year INT NOT NULL,
    value FLOAT,
    PRIMARY KEY (country_id, year),
    FOREIGN KEY (country_id) REFERENCES country(id)
)
