# backend/__init__.py
from flask import Flask
from backend.db import init_db_pool, close_db
from backend.namespaces import planets_bp, stars_bp, systems_bp
from backend.constants import *

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(DB_CONFIG)  # from constants or config.py

    init_db_pool(app)
    app.teardown_appcontext(close_db)

    app.register_blueprint(planets_bp, url_prefix='/api/planets')
    app.register_blueprint(stars_bp, url_prefix='/api/stars')
    app.register_blueprint(systems_bp, url_prefix='/api/systems')

    return app