from flask import Blueprint, jsonify, request
from backend.backend_modules.parser import valid_expression
from backend.db import get_db
import json

planets_bp = Blueprint('planets', __name__)

# Route 1: GET /api/planets/
@planets_bp.route('/', methods=['GET'])
def get_all_planets():
    """
    GET /api/planets/

    Retrieves all planets in the database.

    Returns:
        200: JSON list of planet objects.
        500: {"error": "<error message>"} on failure.
    """

    # Get a connection and cursor from the connection pool
    conn = get_db()
    cur = conn.cursor()
    try:
        # Select all planets from the database
        cur.execute("SELECT * FROM planets;")
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


# Route 2: GET /api/planets/<id>
@planets_bp.route('/<int:id>', methods=['GET'])
def get_planet_by_id(id):
    """
    GET /api/planets/<id>

    Retrieves a single planet by its ID.

    Returns:
        200: JSON object for the planet.
        404: {"error": "Planet not found"} if no match.
        500: {"error": "<error message>"} on failure.
    """
    
    # Get a connection and cursor from the connection pool
    conn = get_db()
    cur = conn.cursor()

    try:
        # Look up the planet by ID
        cur.execute("SELECT * FROM planets WHERE id = %s;", (id,))
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

# Route 3: GET /api/planets/<id>/stars
@planets_bp.route('/<int:id>/stars', methods=['GET'])
def get_stars_from_planet_id(id):
    """
    GET /api/planets/<id>/stars

    Retrieves all stars that the given planet (by ID) orbits.

    Returns:
        200: JSON list of star objects.
        404: If the planet exists but orbits no stars or does not exist.
        500: {"error": "<error message>"} on failure.
    """
    # Get a connection and cursor from the connection pool
    conn = get_db()
    cur = conn.cursor()

    try:
        # Execute the SQL query to get stars that orbit the given planet
        cur.execute("""
            SELECT s.*
            FROM stars s
            JOIN planet_orbits po ON po.star_id = s.id
            WHERE po.planet_id = %s;
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


@planets_bp.route('/search', methods=['POST'])
def get_planets_by_search():

    st = request.json['request_string']

    conn = get_db()
    cur = conn.cursor()

    if not valid_expression(st):
        return jsonify({"error": "Invalid expression"}), 400

    try:
        # Execute the SQL query to get stars that orbit the given planet
        cur.execute(f"SELECT * FROM planets WHERE {st};")

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