INSERT INTO systems (system_name, distance_ly)
VALUES 
('Vega', 25.05),
('Sirius', 8.611),
('Alpha_Centauri', 4.367);


INSERT INTO stars (star_name, mass, radius, apparent_magnitude, spectral_type, age_years, system_id)
VALUES 
('Vega', 2.1, 2.3, 0.03, 'A0V', 455000000, 1),
('Sirius_A', 2.0, 1.7, -1.46, 'A1V', 200000000, 2),
('Sirius_B', 1.0, 0.9, 8.44, 'DA2', 120000000, 2),
('Alpha_Centauri_A', 1.1, 1.2, 0.01, 'G2V', 5000000000, 3),
('Alpha_Centauri_B', 0.9, 0.8, 0.2, 'K1V', 5000000000, 3),
('Proxima_Centauri', 0.12, 0.14, 15.5, 'M5.5Ve', 5000000000, 3);


INSERT INTO planets (planet_name, mass, radius, orbital_period, semi_major_axis, eccentricity, system_id)
VALUES 
('Vega_b', 0.5, 1.2, 0.5, 0.1, 0, 1),
('Sirius_A_b', 0.8, 1.5, 1.0, 0.2, 0, 2),
('Proxima_Centauri_b', 0.3, 1.1, 0.2, 0.05, 0, 3),
('Proxima_Centauri_c', 0.4, 1.3, 0.3, 0.07, 0, 3),
('Proxima_Centauri_d', 0.2, 1.0, 0.4, 0.08, 0, 3);


INSERT INTO planet_orbits (planet_id, star_id)
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 3),
(5, 3);