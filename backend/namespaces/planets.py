from flask import request
from flask_restx import Namespace, Resource, fields
from backend.db import get_db
from backend.models.shared_models import register_models
from backend.backend_modules.parser import valid_expression
from backend.backend_modules.ai import generate_planet_description

# Define the REST namespace for planets
api = Namespace(
    "planets",
    description="Endpoints for planetary data, advanced search capabilities, and AI-enhanced descriptions.",
)

# === Shared Models ===
models = register_models(api)
system_model = models["system_model"]
star_model = models["star_model"]
planet_model = models["planet_model"]
search_model = models["search_model"]
ai_response_model = models["ai_response_model"]


# === API Endpoints ===
@api.route("/")
class PlanetList(Resource):
    @api.marshal_list_with(
        planet_model, code=200, description="List of all planets", mask=None
    )
    @api.response(500, "Internal Server Error")
    def get(self):
        """Retrieve all planets in the database."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM planets;")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()


@api.route("/<int:id>")
class PlanetByID(Resource):
    @api.marshal_with(
        planet_model, code=200, description="Planet found and returned", mask=None
    )
    @api.response(404, "Planet not found")
    @api.response(500, "Internal Server Error")
    def get(self, id):
        """Retrieve a specific planet by its ID."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM planets WHERE id = %s;", (id,))
            row = cur.fetchone()
            if not row:
                api.abort(404, "Planet not found")
            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()


@api.route("/<int:id>/stars")
class PlanetStars(Resource):
    @api.marshal_list_with(
        star_model,
        code=200,
        description="List of starts orbiting the planet",
        mask=None,
    )
    @api.response(500, "Internal Server Error")
    def get(self, id):
        """Retrieve all stars that a planet orbits."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute(
                """
                SELECT s.*
                FROM stars s
                JOIN planet_orbits po ON po.star_id = s.id
                WHERE po.planet_id = %s;
            """,
                (id,),
            )
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()


@api.route("/search")
class PlanetSearch(Resource):
    @api.expect(search_model)
    @api.marshal_list_with(
        planet_model,
        code=200,
        description="Filtered list of planets returned",
        mask=None,
    )
    @api.response(400, "Invalid expression")
    @api.response(500, "Internal Server Error")
    def post(self):
        """Search for planets using a validated SQL WHERE clause."""
        body = request.get_json()
        st = body.get("request_string", "")

        if not valid_expression(st):
            api.abort(400, "Invalid expression")

        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT * FROM planets WHERE {st};")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()


@api.route("/<int:id>/ai_description")
class PlanetAIDescription(Resource):
    @api.marshal_with(
        ai_response_model,
        code=200,
        description="AI-generated description returned",
        mask=None,
    )
    @api.response(404, "Planet not found")
    @api.response(500, "Internal Server Error")
    def get(self, id):
        """Generate a natural-language description of a planet using AI."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM planets WHERE id = %s", (id,))
            row = cur.fetchone()
            if not row:
                api.abort(404, "Planet not found")
            columns = [desc[0] for desc in cur.description]
            planet_data = dict(zip(columns, row))
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()

        try:
            description = generate_planet_description(str(planet_data))
            return {"description": description}
        except Exception as e:
            api.abort(500, f"AI generation failed: {str(e)}")
