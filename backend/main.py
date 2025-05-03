from flask_cors import CORS
from backend import create_app
from backend.constants import *

app = create_app()
CORS(app)

if __name__ == "__main__":
    app.run(host=API_ADDRESS, port=API_PORT, debug=True)
