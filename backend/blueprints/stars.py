from flask import Blueprint, jsonify, request
from backend.backend_modules.parser import valid_expression
from backend.db import get_db
import json

stars_bp = Blueprint('stars', __name__)

# GET /api/stars/ — Retrieve all stars
@stars_bp.route('/', methods=['GET'])
def get_stars():

    # Get a connection and cursor from the connection pool
    conn = get_db()
    cur = conn.cursor()
    try:
        # Select all stars from the database
        cur.execute("SELECT * FROM stars;")
        rows = cur.fetchall()

        # If no rows are returned, return an empty list
        if not rows:
            return jsonify([]), 200  # returning empty list is fine
        
        # Get the column names from the cursor description
        columns = [desc[0] for desc in cur.description]

        # Convert the rows to a list of dictionaries and return as JSON
        result = [dict(zip(columns, row)) for row in rows]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# GET /api/stars/<id> — Retrieve a specific star by ID
@stars_bp.route('/<id>', methods=['GET'])
def get_stars_by_id(id):

    # Get a connection and cursor from the connection pool
    conn = get_db()
    cur = conn.cursor()

    try:
        # Look up the planet by ID
        cur.execute("SELECT * FROM stars WHERE id = %s;", (id,))
        row = cur.fetchone()

        # Return 404 if the planet doesn't exist
        if not row:
            return jsonify({"error": "Planet not found"}), 404

        # Format the row as a dictionary
        columns = [desc[0] for desc in cur.description]

        # Convert the row to a dictionary and return as JSON
        result = dict(zip(columns, row))
        return jsonify(result)
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
            SELECT *
            FROM planets p
            JOIN planet_orbits o ON p.id = o.planet_id
            WHERE o.star_id = %s;
        """, (id,))

        # Fetch all rows from the executed query
        rows = cur.fetchall()

        # If no rows are returned, return a 404 error
        if not rows:
            return jsonify([]), 200  # returning empty list is fine

        # Get the column names from the cursor description
        columns = [desc[0] for desc in cur.description]

        # Convert the rows to a list of dictionaries and return as JSON
        result = [dict(zip(columns, row)) for row in rows]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()


@stars_bp.route('/search', methods=['POST'])
def search_stars():
    """
    POST /api/stars/search

    Searches for stars based on a query string.

    Query Parameters:
        - q: The search query string.

    Returns:
        200: JSON list of star objects matching the search query.
        400: {"error": "Invalid query"} if the query is invalid.
        500: {"error": "<error message>"} on failure.
    """

    st = request.json['request_string']

    conn = get_db()
    cur = conn.cursor()

    if not valid_expression(st):
        return jsonify({"error": "Invalid expression"}), 400

    try:
        # Execute the SQL query to get stars that orbit the given planet
        cur.execute(f"SELECT * FROM stars WHERE {st};")

        # Fetch all rows from the executed query
        rows = cur.fetchall()

        # If no rows are returned, return a 404 error
        if not rows:
            return jsonify([]), 200  # returning empty list is fine

        # Get the column names from the cursor description
        columns = [desc[0] for desc in cur.description]

        # Convert the rows to a list of dictionaries and return as JSON
        result = [dict(zip(columns, row)) for row in rows]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

@stars_bp.route('/<id>/ai_description', methods=['POST'])
def get_star_ai_description(id):
    return jsonify({"error": "Not implemented"}), 501