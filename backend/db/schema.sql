-- WIP --

CREATE TABLE IF NOT EXISTS systems (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS stars (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS planets (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
);

-- This table is used to store a list of parent stars
-- that a planet orbits. In general this will only be one star,
-- but in some cases, such as binary stars, it can be more than one.
--
---- The table is used to store the relationship between planets and stars.
CREATE TABLE IF NOT EXISTS planet_orbits (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
);