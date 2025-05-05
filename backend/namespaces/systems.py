from flask import request
from flask_restx import Namespace, Resource, fields
from backend.db import get_db
from backend.models.shared_models import register_models
from backend.backend_modules.parser import valid_expression

# Define the REST namespace for systems
api = Namespace(
    'systems',
    description='Endpoints for planetary systems, including associated planets and stars.'
)

# === Shared Models ===
models = register_models(api)
system_model = models['system_model']
star_model = models['star_model']
planet_model = models['planet_model']
search_model = models['search_model']
ai_response_model = models['ai_response_model']

# === API Endpoints ===
@api.route('/')
class SystemList(Resource):
    @api.doc(
        params={
            'limit': 'Maximum number of planets to return (optional)',
            'offset': 'Number of planets to skip before starting to return results (optional)'
        }
    )
    @api.marshal_list_with(system_model, code=200, description='List of all systems', mask=None)
    @api.response(500, 'Internal Server Error')
    def get(self):
        """Retrieve all planetary systems in the database."""
        conn = get_db()
        cur = conn.cursor()
        try:
            # Limit and offset are optional query parameters for pagination
            # They can be used to control the number of results returned and the starting point
            # For example: /systems?limit=10&offset=20
            limit = request.args.get('limit', default=None, type=int)
            offset = request.args.get('offset', default=0, type=int)

            query = "SELECT * FROM systems"
            params = []

            if limit is not None:
                query += " LIMIT %s"
                params.append(limit)
            if offset > 0:
                query += " OFFSET %s"
                params.append(offset)
            query += ";"

            cur.execute(query, params if params else None)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()

@api.route('/<int:id>')
class SystemByID(Resource):
    @api.marshal_with(system_model, code=200, description='System found and returned', mask=None)
    @api.response(404, 'System not found')
    @api.response(500, 'Internal Server Error')
    def get(self, id):
        """Retrieve a specific system by ID."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM systems WHERE id = %s;", (id,))
            row = cur.fetchone()
            if not row:
                api.abort(404, "System not found")
            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()

@api.route('/<int:id>/planets')
class SystemPlanets(Resource):
    @api.marshal_list_with(planet_model, code=200, description='List of planets in the system', mask=None)
    @api.response(500, 'Internal Server Error')
    def get(self, id):
        """Retrieve all planets in a given system."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM planets WHERE system_id = %s;", (id,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()

@api.route('/<int:id>/stars')
class SystemStars(Resource):
    @api.marshal_list_with(star_model, code=200, description='List of stars in the system', mask=None)
    @api.response(500, 'Internal Server Error')
    def get(self, id):
        """Retrieve all stars in a given system."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM stars WHERE system_id = %s;", (id,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()

@api.route('/search')
class SystemSearch(Resource):
    @api.doc(
        params={
            'limit': 'Maximum number of planets to return (optional)',
            'offset': 'Number of planets to skip before starting to return results (optional)'
        }
    )
    @api.expect(search_model)
    @api.marshal_list_with(system_model, code=200, description='Filtered list of systems returned', mask=None)
    @api.response(400, 'Invalid expression')
    @api.response(500, 'Internal Server Error')
    def post(self):
        """Search for systems using a validated SQL WHERE clause."""
        body = request.get_json()
        st = body.get('request_string', '')

        if not valid_expression(st):
            api.abort(400, "Invalid expression")

        conn = get_db()
        cur = conn.cursor()
        try:
            # Limit and offset are optional query parameters for pagination
            # They can be used to control the number of results returned and the starting point
            # For example: /systems/search?limit=10&offset=20
            limit = request.args.get('limit', default=None, type=int)
            offset = request.args.get('offset', default=0, type=int)
            
            query = f"SELECT * FROM systems WHERE {st}"
            params = []

            if limit is not None:
                query += " LIMIT %s"
                params.append(limit)
            if offset > 0:
                query += " OFFSET %s"
                params.append(offset)
            query += ";"

            cur.execute(query, params if params else None)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()

@api.route('/<int:id>/ai_description')
class SystemAIDescription(Resource):
    @api.marshal_with(ai_response_model, code=200, description='AI-generated description returned', mask=None)
    @api.response(404, 'System not found')
    @api.response(500, 'Internal Server Error')
    def get(self, id):
        """Generate a natural-language description of a planetary system using AI."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM systems WHERE id = %s", (id,))
            row = cur.fetchone()
            if not row:
                api.abort(404, "System not found")
            columns = [desc[0] for desc in cur.description]
            system_data = dict(zip(columns, row))
        except Exception as e:
            api.abort(500, str(e))
        finally:
            cur.close()

        try:
            description = generate_system_description(str(system_data))
            return {'description': description}
        except Exception as e:
            api.abort(500, f"AI generation failed: {str(e)}")
