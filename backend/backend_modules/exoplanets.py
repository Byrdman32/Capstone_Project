# %%
# Imports
# Note - by including # %%'s, this can be run like a Jupyter notebook (interactive cell by cell) with Jupytext, or as a traditional Python script
from backend.constants import DB_CONFIG
import psycopg2 as pg
import requests as rq
import pandas as pd
import os

# %%
# Function definitions
directory_path = os.path.dirname(
    os.path.abspath(__file__)
)  # Avoids relative path issues when running alone or as a module
cached_api_results_path = f"{directory_path}/data/exoplanets.csv"
api_token_path = f"{directory_path}/tokens/api_token"


def refresh_exoplanet_data() -> None:
    url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=csv"
    with open(api_token_path, "r") as token_file:
        api_token = token_file.read().strip()

    response = rq.get(url, headers={"Authorization": f"Bearer {api_token}"})

    if response.status_code == 200:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(cached_api_results_path), exist_ok=True)

        with open(cached_api_results_path, "w") as file:
            file.write(response.text)
    else:
        print(f"Error: {response.status_code}")


def get_exoplanet_data(row_range: tuple = (0, 10)) -> pd.DataFrame:

    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    query = f"""
        SELECT
            pl_name,
            ROWNUM AS row_num,
        FROM ps 
        WHERE row_num <= {row_range[1]}
    """

    params = {
        "query": query,
        "format": "json",
    }

    response = rq.get(url, params=params)
    print(response.text)

def fetch_and_generate_sql_file(filename="api_results.sql", length=10) -> None:

    query = f"""
        SELECT pl_name, hostname, pl_bmasse, pl_rade, pl_orbper, pl_orbsmax, pl_orbeccen,
        sy_dist, sy_vmag, st_mass, st_rad, st_teff, st_spectype, st_age
        FROM pscomppars
        WHERE pl_name IS NOT NULL AND pl_bmasse IS NOT NULL AND pl_rade IS NOT NULL AND ROWNUM <= {length}
    """
    
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    params = {"query": query, "format": "json"}
    response = rq.get(url, params=params)

    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        print("Response:", response.text)
        return

    try:
        data = response.json()
    except Exception as e:
        print("Error parsing JSON:", e)
        print("Response content:", response.text)
        return

    systems, stars, planets, planet_orbits = {}, {}, [], []
    system_id_map, star_id_map = {}, {}
    system_counter = star_counter = planet_counter = 1

    for row in data:
        system_name = row['hostname']
        planet_name = row['pl_name']

        if not system_name or not planet_name:
            continue

        # Add system
        if system_name not in systems:
            distance = row.get('sy_dist')
            if distance is None:
                continue  # Required field
            systems[system_name] = {
                "id": system_counter,
                "name": system_name,
                "distance": distance
            }
            system_id_map[system_name] = system_counter
            system_counter += 1

        # Add star
        if system_name not in stars:
            star_mass = row.get('st_mass')
            star_radius = row.get('st_rad')
            star_age = row.get('st_age')
            if star_mass is not None and star_radius is not None and star_age is not None:
                if star_mass <= 0 or star_radius <= 0 or star_age <= 0:
                    continue  # Domain constraint
            stars[system_name] = {
                "id": star_counter,
                "star_name": system_name,
                "mass": star_mass,
                "radius": star_radius,
                "apparent_magnitude": row.get('sy_vmag'),
                "spectral_type": row.get('st_spectype'),
                "age_years": star_age * 1e9 if star_age else None,
                "system_id": system_id_map[system_name]
            }
            star_id_map[system_name] = star_counter
            star_counter += 1

        # Add planet
        planet_mass = row.get('pl_bmasse')
        planet_radius = row.get('pl_rade')
        orbital_period = row.get('pl_orbper')
        sma = row.get('pl_orbsmax')
        ecc = row.get('pl_orbeccen')

        if any(x is None for x in [planet_mass, planet_radius, orbital_period, sma, ecc]):
            continue
        if planet_mass <= 0 or planet_radius <= 0 or orbital_period <= 0 or sma <= 0:
            continue
        if ecc < 0 or ecc >= 1:
            continue

        planets.append({
            "id": planet_counter,
            "planet_name": planet_name,
            "mass": planet_mass,
            "radius": planet_radius,
            "orbital_period": orbital_period,
            "semi_major_axis": sma,
            "eccentricity": ecc,
            "system_id": system_id_map[system_name]
        })

        planet_orbits.append({
            "planet_id": planet_counter,
            "star_id": star_id_map[system_name]
        })

        planet_counter += 1

    def fmt(val):
        return 'NULL' if val is None else f"'{val}'" if isinstance(val, str) else str(val)

    systems_sql = "INSERT INTO systems (system_name, distance_ly)\nVALUES\n" + ",\n".join(
        f"('{s['name']}', {fmt(s['distance'])})" for s in systems.values()
    ) + ";\n\n"

    stars_sql = "INSERT INTO stars (star_name, mass, radius, apparent_magnitude, spectral_type, age_years, system_id)\nVALUES\n" + ",\n".join(
        f"('{s['star_name']}', {fmt(s['mass'])}, {fmt(s['radius'])}, {fmt(s['apparent_magnitude'])}, {fmt(s['spectral_type'])}, {fmt(s['age_years'])}, {s['system_id']})"
        for s in stars.values()
    ) + ";\n\n"

    planets_sql = "INSERT INTO planets (planet_name, mass, radius, orbital_period, semi_major_axis, eccentricity, system_id)\nVALUES\n" + ",\n".join(
        f"('{p['planet_name']}', {fmt(p['mass'])}, {fmt(p['radius'])}, {fmt(p['orbital_period'])}, {fmt(p['semi_major_axis'])}, {fmt(p['eccentricity'])}, {p['system_id']})"
        for p in planets
    ) + ";\n\n"

    orbits_sql = "INSERT INTO planet_orbits (planet_id, star_id)\nVALUES\n" + ",\n".join(
        f"({o['planet_id']}, {o['star_id']})" for o in planet_orbits
    ) + ";\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("-- Earth-unit exoplanet insert script matching schema\n\n")
        f.write(systems_sql)
        f.write(stars_sql)
        f.write(planets_sql)
        f.write(orbits_sql)

    print(f"✅ SQL insert file written to: {filename}")


def refresh_database(filename="api_results.sql"):

    conn = pg.connect(
        host=DB_CONFIG["DB_HOST"],
        port=DB_CONFIG["DB_PORT"],
        dbname=DB_CONFIG["DB_NAME"],
        user=DB_CONFIG["DB_USER"],
        password=DB_CONFIG["DB_PASSWORD"],
    )

    cur = conn.cursor()

    with open(filename, 'r', encoding='utf-8') as f:
        sql_script = f.read()
        cur.execute(sql_script)
    
    conn.commit()
    cur.close()
    conn.close()
    
def nuke_database(schema_file_path="backend/db/schema.sql"):
    conn = pg.connect(
        host=DB_CONFIG["DB_HOST"],
        port=DB_CONFIG["DB_PORT"],
        dbname=DB_CONFIG["DB_NAME"],
        user=DB_CONFIG["DB_USER"],
        password=DB_CONFIG["DB_PASSWORD"],
    )

    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS systems, stars, planets, planet_orbits;")
    conn.commit()

    with open(schema_file_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()
        cur.execute(sql_script)

    cur.close()
    conn.close()

def build_database(schema_file_path="backend/db/schema.sql"):
    conn = pg.connect(
        host=DB_CONFIG["DB_HOST"],
        port=DB_CONFIG["DB_PORT"],
        dbname=DB_CONFIG["DB_NAME"],
        user=DB_CONFIG["DB_USER"],
        password=DB_CONFIG["DB_PASSWORD"],
    )

    cur = conn.cursor()

    with open(schema_file_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()
        cur.execute(sql_script)

    conn.commit()
    cur.close()
    conn.close()
    
if __name__ == "__main__":

    fetch_and_generate_sql_file()
    refresh_database("api_results.sql")
