import argparse
from flask_cors import CORS
from backend import create_app
from backend.constants import API_ADDRESS, API_PORT
from backend.backend_modules.exoplanets import fetch_and_generate_sql_file, refresh_database, nuke_database, build_database

app = create_app()
CORS(app)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--refreshdb', action='store_true', help='Nuke the database and refresh it with new data')
    parser.add_argument('--run', action='store_true', help='Generate SQL insert file')

    args = parser.parse_args()

    if args.refreshdb:
        nuke_database()
        build_database()
        fetch_and_generate_sql_file()
        refresh_database("api_results.sql")
    else:
        app.run(debug=True, host=API_ADDRESS, port=API_PORT)

