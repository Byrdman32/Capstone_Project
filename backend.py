from flask import Flask, send_from_directory, jsonify
import time
import os

app = Flask(
    __name__, static_folder="build"
)  # Only difference from React is the folder we look for the static files in
# Only very minimal back-end changes are required to replace the front-end


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
    timestamp = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    return jsonify(message=f"Hello World from the Python backend at {timestamp}")


if __name__ == "__main__":
    app.run(port=9000)
