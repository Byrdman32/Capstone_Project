# backend/__init__.py
from flask import Flask
from flask_restx import Api
from backend.db import init_db_pool, close_db
from backend.namespaces import planets_ns, stars_ns, systems_ns
from backend.constants import *

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(DB_CONFIG)  # from constants or config.py

    # Set up database connection pooling
    init_db_pool(app)
    app.teardown_appcontext(close_db)

    # Set up RESTX API and Swagger
    api = Api(
        app,
        version='1.0',
        title='Exoplanets API',
        description='API for managing planets, stars, and stellar systems',
        doc='/swagger',  # Swagger UI will be available at /swagger
        prefix='/api',   # All endpoints will be prefixed with /api
        mask=None        # Hide "X-Fields" from Swagger UI
    )

    # Register namespaces
    api.add_namespace(planets_ns, path="/planets")
    api.add_namespace(stars_ns, path="/stars")
    api.add_namespace(systems_ns, path="/systems")

    return app