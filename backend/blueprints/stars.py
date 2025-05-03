from flask import Blueprint, jsonify, request
from backend.db import get_db  # Replace with your actual db access module

stars_bp = Blueprint('stars', __name__)

# GET /api/stars/ — Retrieve all stars
@stars_bp.route('/', methods=['GET'])
def get_stars():
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM stars;")
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

# GET /api/stars/<id> — Retrieve a specific star by ID
@stars_bp.route('/<id>', methods=['GET'])
def get_stars_by_id(id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM stars WHERE id = %s;", (id,))
        row = cur.fetchone()
        if row is None:
            return jsonify({"error": "Star not found"}), 404

        star = {
            "id": row[0],
            "name": row[1],
            "mass": row[2],
            "radius": row[3],
            "temperature": row[4],
        }
        return jsonify(star), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# GET /api/stars/<id>/planets — Retrieve all planets that orbit a given star
@stars_bp.route('/<id>/planets', methods=['GET'])
def get_planets_from_star_id(id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT p.id, p.name, p.radius, o.orbital_period
            FROM planets p
            JOIN planet_orbits o ON p.id = o.planet_id
            WHERE o.star_id = %s;
        """, (id,))
        rows = cur.fetchall()
        planets = [
            {
                "id": row[0],
                "name": row[1],
                "radius": row[2],
                "orbital_period": row[3],
            }
            for row in rows
        ]
        return jsonify(planets), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()