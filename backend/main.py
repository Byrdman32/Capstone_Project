
from backend import create_app
from flask_cors import CORS
from backend.constants import API_ADDRESS, API_PORT

app = create_app()
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host=API_ADDRESS, port=API_PORT)


