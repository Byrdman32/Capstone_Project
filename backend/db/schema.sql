-- Filename: schema.sql

-- TODO
-- 1. Add a constraint to stars table to check for valid spectral types.
-- 2. Cleanup the comments and ensure they are consistent across all tables.




-- Creates the 'systems' table.
--
-- Fields:
-- id            : Auto-incrementing primary key for unique system identification
-- name          : Name or catalog designation of the system (required)
-- distance_ly   : Distance from Earth in light-years (required)
CREATE TABLE IF NOT EXISTS systems (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    system_name VARCHAR(255) NOT NULL,
    distance_ly float NOT NULL,

    -- TABLE CONSTRAINTS --
    CONSTRAINT system_name_unique UNIQUE (system_name)
);


-- Creates the 'stars' table to store information about stellar objects.
-- Each star MUST belong to a system, even if its the only object in the system.

-- Fields:
-- id               : Auto-incrementing primary key for unique star identification
-- name             : Name of the star (required)
-- mass             : Mass of the star (float, e.g., in solar masses)
-- radius           : Radius of the star (float, e.g., in solar radii)
-- apparent_magnitude : Brightness of the star as seen from Earth
-- spectral_type    : Classification like 'G2V' or 'M1'
-- age              : Estimated age of the star in years
-- system_id        : Foreign key referencing the star's planetary system (required)
-- On deletion of a system, all its associated stars are also deleted (CASCADE)

CREATE TABLE IF NOT EXISTS stars (
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    star_name varchar(64) NOT NULL,
    mass float,
    radius float,
    apparent_magnitude float,
    spectral_type varchar(16) ,
    age_years float,
    system_id int NOT NULL,
    FOREIGN KEY (system_id) REFERENCES systems(id) ON DELETE CASCADE,

    -- TABLE CONSTRAINTS --
    CONSTRAINT star_name_unique UNIQUE (star_name),
    CONSTRAINT expected_domain_check CHECK (
        mass > 0 AND radius > 0 AND apparent_magnitude > 0 AND age_years > 0
    )
    ----------- ADD CONSTRAINT TO CHECK THE SPECTRAL TYPE -------------
);


-- Creates the 'planets' table to store information about exoplanets.
-- Each planet MUST belong to a system, even if its the only object in the system (aka a rogue planet).

-- Fields:
-- id                : Auto-incrementing primary key for unique planet identification
-- planet_name       : Name or designation of the planet (required)
-- mass              : Mass of the planet (float in Earth masses)
-- radius            : Radius of the planet (float in Earth radii)
-- orbital_period    : Time it takes to complete one orbit around the host star (in days)
-- semi_major_axis   : Average distance from the star (in AU)
-- eccentricity      : Measure of how elliptical the orbit is (0 = circular, closer to 1 = very elliptical)
-- system_id         : Foreign key referencing the planetary system this planet belongs to (required)
-- On deletion of a system, all its associated planets are also deleted (CASCADE)

CREATE TABLE IF NOT EXISTS planets (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    planet_name VARCHAR(255) NOT NULL,
    mass FLOAT,
    radius FLOAT,
    orbital_period FLOAT,
    semi_major_axis FLOAT,
    eccentricity FLOAT,
    system_id INT NOT NULL,
    FOREIGN KEY (system_id) REFERENCES systems(id) ON DELETE CASCADE,

    -- TABLE CONSTRAINTS --
    CONSTRAINT planet_name_unique UNIQUE (planet_name),
    CONSTRAINT expected_domain_check CHECK (
        mass > 0 AND radius > 0 AND orbital_period > 0 AND semi_major_axis > 0 AND eccentricity >= 0 AND eccentricity < 1
    )
);

-- This table stores the mapping between planets and the stars they orbit.
-- While most planets orbit a single star, this schema allows for the possibility
-- of multiple parent stars, such as in binary or trinary star systems.

-- id: Surrogate primary key for each orbit entry
-- planet_id: References the planet involved in the orbiting relationship
-- star_id: References the star that the planet orbits
-- FOREIGN KEY (planet_id): Deletes the orbit entry if the planet is deleted
-- FOREIGN KEY (star_id): Deletes the orbit entry if the star is deleted
CREATE TABLE IF NOT EXISTS planet_orbits (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    planet_id INT NOT NULL,
    star_id INT NOT NULL,
    FOREIGN KEY (planet_id) REFERENCES planets(id) ON DELETE CASCADE,
    FOREIGN KEY (star_id) REFERENCES stars(id) ON DELETE CASCADE
);