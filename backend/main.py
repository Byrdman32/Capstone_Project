from flask import Flask, jsonify
from flask_cors import CORS
from backend_modules import exoplanets
from constants import *

app = Flask(__name__)
CORS(app)

exoplanet_df = exoplanets.get_exoplanet_data()

@app.route("/api/message")
def get_message():
    print("/api/message invoked")
    return jsonify(message=f"First exoplanet: {str(exoplanet_df.iloc[0].to_dict())}")


if __name__ == "__main__":
    app.run(host=API_ADDRESS, port=API_PORT, debug=True)
