-- Filename: schema.sql

-- Creates the 'systems' table.
--
-- Fields:
-- id            : Auto-incrementing primary key for unique system identification
-- name          : Name or catalog designation of the system (required)
-- distance_ly   : Distance from Earth in light-years (required)
CREATE TABLE IF NOT EXISTS systems (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    float distance_ly NOT NULL
);


-- Creates the 'stars' table to store information about stellar objects.
-- Each star MUST belong to a system, even if its the only object in the system.

-- Fields:
-- id               : Auto-incrementing primary key for unique star identification
-- name             : Name of the star (required)
-- mass             : Mass of the star (double precision, e.g., in solar masses)
-- radius           : Radius of the star (double precision, e.g., in solar radii)
-- apparent_magnitude : Brightness of the star as seen from Earth
-- spectral_type    : Classification like 'G2V' or 'M1'
-- age              : Estimated age of the star in billions of years
-- system_id        : Foreign key referencing the star's planetary system (required)
-- On deletion of a system, all its associated stars are also deleted (CASCADE)

CREATE TABLE IF NOT EXISTS stars (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    string name NOT NULL,
    double mass,
    double radius,
    double apparent_magnitude,
    double spectral_type,
    float age,
    system_id INT  NOT NULL,
    FOREIGN KEY (system_id) REFERENCES systems(id) ON DELETE CASCADE
);


-- Creates the 'planets' table to store information about exoplanets.
-- Each planet MUST belong to a system, even if its the only object in the system (aka a rogue planet).

-- Fields:
-- id                : Auto-incrementing primary key for unique planet identification
-- name              : Name or designation of the planet (required)
-- mass              : Mass of the planet (double precision, likely in Earth or Jupiter masses)
-- radius            : Radius of the planet (double precision, often in Earth or Jupiter radii)
-- orbital_period    : Time it takes to complete one orbit around the host star (in days)
-- semi_major_axis   : Average distance from the star (in AU or other units, depending on dataset)
-- eccentricity      : Measure of how elliptical the orbit is (0 = circular, closer to 1 = very elliptical)
-- system_id         : Foreign key referencing the planetary system this planet belongs to (required)
-- On deletion of a system, all its associated planets are also deleted (CASCADE)
CREATE TABLE IF NOT EXISTS planets (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    string name NOT NULL,
    double mass,
    double radius,
    double orbital_period,
    double semi_major_axis,
    double eccentricity,
    system_id INT  NOT NULL,
    FOREIGN KEY (system_id) REFERENCES systems(id) ON DELETE CASCADE
);

-- This table is used to store a list of parent stars
-- that a planet orbits. In general this will only be one star,
-- but in some cases, such as binary stars, it can be more than one.
--
---- The table is used to store the relationship between planets and stars.
CREATE TABLE IF NOT EXISTS planet_orbits (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
);