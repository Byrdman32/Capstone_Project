from flask import Flask, send_from_directory, jsonify
from backend_modules import exoplanets
from blueprints.systems import systems_bp
from constants import *
import os

parent_directory_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
app = Flask(
    __name__, static_folder=f"{parent_directory_path}/frontend/build"
)  # Serve static files from frontend/build

exoplanet_df = exoplanets.get_exoplanet_data()

app.register_blueprint(systems_bp, url_prefix="/api/systems")
app.register_blueprint(planets_bp, url_prefix="/api/planets")
app.register_blueprint(stars_bp, url_prefix="/api/stars")

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


@app.route("/api/message")
def get_message():
    print("/api/message invoked")
    return jsonify(message=f"First exoplanet: {str(exoplanet_df.iloc[0].to_dict())}")


if __name__ == "__main__":
    app.run(host=API_ADDRESS, port=API_PORT, debug=True)
