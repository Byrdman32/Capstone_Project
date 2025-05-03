
from backend import create_app
from backend.constants import API_ADDRESS, API_PORT

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host=API_ADDRESS, port=API_PORT)

from flask import Flask, jsonify
from flask_cors import CORS
from backend_modules import exoplanets
from blueprints.systems import systems_bp
from constants import *

app = Flask(__name__)
CORS(app)

exoplanet_df = exoplanets.get_exoplanet_data()

app.register_blueprint(systems_bp, url_prefix="/api/systems")
app.register_blueprint(planets_bp, url_prefix="/api/planets")
app.register_blueprint(stars_bp, url_prefix="/api/stars")

@app.route("/api/message")
def get_message():
    print("/api/message invoked")
    return jsonify(message=f"First exoplanet: {str(exoplanet_df.iloc[0].to_dict())}")


if __name__ == "__main__":
    app.run(host=API_ADDRESS, port=API_PORT, debug=True)

