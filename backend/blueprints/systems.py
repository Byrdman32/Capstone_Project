from flask import Blueprint, jsonify
from backend.db import get_db  # Replace with actual DB accessor

systems_bp = Blueprint('systems', __name__)

# GET /api/systems/ — Retrieve all systems
@systems_bp.route('/', methods=['GET'])
def get_systems():
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, distance_ly FROM systems;")
        rows = cur.fetchall()
        systems = [
            {
                "id": row[0],
                "name": row[1],
                "distance_ly": row[2],
            }
            for row in rows
        ]
        return jsonify(systems), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# GET /api/systems/<id> — Retrieve a specific system by ID
@systems_bp.route('/<id>', methods=['GET'])
def get_system_by_id(id):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, distance_ly FROM systems WHERE id = %s;", (id,))
        row = cur.fetchone()
        if row is None:
            return jsonify({"error": "System not found"}), 404

        system = {
            "id": row[0],
            "name": row[1],
            "distance_ly": row[2],
        }
        return jsonify(system), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# GET /api/systems/<id>/planets — Retrieve all planets in a given system
@systems_bp.route('/<id>/planets', methods=['GET'])
def get_planets_from_system_by_id(id):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, radius FROM planets WHERE system_id = %s;", (id,))
        rows = cur.fetchall()
        planets = [
            {
                "id": row[0],
                "name": row[1],
                "radius": row[2],
            }
            for row in rows
        ]
        return jsonify(planets), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# GET /api/systems/<id>/stars — Retrieve all stars in a given system
@systems_bp.route('/<id>/stars', methods=['GET'])
def get_stars_from_system_by_id(id):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, mass, radius, temperature FROM stars WHERE system_id = %s;", (id,))
        rows = cur.fetchall()
        stars = [
            {
                "id": row[0],
                "name": row[1],
                "mass": row[2],
                "radius": row[3],
                "temperature": row[4],
            }
            for row in rows
        ]
        return jsonify(stars), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

@systems_bp.route('/search', methods=['GET'])
def get_systems_by_search(id):
    return jsonify({"error": "Not implemented"}, {"okay": id}), 501