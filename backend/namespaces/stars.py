from flask import request
from flask_restx import Namespace, Resource, fields
from backend.db import get_db
from backend.models.shared_models import register_models
from backend.backend_modules.parser import valid_expression

# Define the REST namespace for stars
api = Namespace(
    'stars',
    description='Endpoints for stellar data, associated planetary systems, and advanced search capabilities.'
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
class StarList(Resource):
    @api.doc(
        params={
            'limit': 'Maximum number of planets to return (optional)',
            'offset': 'Number of planets to skip before starting to return results (optional)'
        }
    )
    @api.marshal_list_with(star_model, code=200, description='List of all stars', mask=None)
    @api.response(500, 'Internal Server Error')
    def get(self):
        """Retrieve all stars in the database."""
        conn = get_db()
        cur = conn.cursor()
        try:
            # Limit and offset are optional query parameters for pagination
            # They can be used to control the number of results returned and the starting point
            # For example: /stars?limit=10&offset=20
            limit = request.args.get('limit', default=None, type=int)
            offset = request.args.get('offset', default=0, type=int)

            query = "SELECT * FROM stars"
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
            return [dict(zip(columns, row)) for row in rows], 200
        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            cur.close()

@api.route('/<int:id>')
class StarByID(Resource):
    @api.marshal_with(star_model, code=200, description='Star found and returned', mask=None)
    @api.response(404, 'Star not found')
    @api.response(500, 'Internal Server Error')
    def get(self, id):
        """Retrieve a specific star by its ID."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM stars WHERE id = %s;", (id,))
            row = cur.fetchone()
            if not row:
                return {'error': 'Star not found'}, 404
            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row)), 200
        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            cur.close()

@api.route('/<int:id>/planets')
class StarPlanets(Resource):
    @api.marshal_list_with(planet_model, code=200, description='List of planets orbiting the star', mask=None)
    @api.response(500, 'Internal Server Error')
    def get(self, id):
        """Retrieve all planets that orbit the given star."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT p.*
                FROM planets p
                JOIN planet_orbits o ON p.id = o.planet_id
                WHERE o.star_id = %s;
            """, (id,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows], 200
        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            cur.close()

@api.route('/search')
class StarSearch(Resource):
    @api.doc(
        params={
            'limit': 'Maximum number of planets to return (optional)',
            'offset': 'Number of planets to skip before starting to return results (optional)'
        }
    )
    @api.expect(search_model)
    @api.marshal_list_with(star_model, code=200, description='Filtered list of stars returned', mask=None)
    @api.response(400, 'Invalid expression')
    @api.response(500, 'Internal Server Error')
    def post(self):
        """Search for stars using a validated SQL WHERE clause."""
        body = request.get_json()
        st = body.get('request_string', '')

        if not valid_expression(st):
            return {'error': 'Invalid expression'}, 400

        conn = get_db()
        cur = conn.cursor()
        try:
            # Limit and offset are optional query parameters for pagination
            # They can be used to control the number of results returned and the starting point
            # For example: /stars/search?limit=10&offset=20
            limit = request.args.get('limit', default=None, type=int)
            offset = request.args.get('offset', default=0, type=int)
            
            query = f"SELECT * FROM stars WHERE {st}"
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
            return [dict(zip(columns, row)) for row in rows], 200
        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            cur.close()

@api.route('/<int:id>/ai_description')
class StarAIDescription(Resource):
    @api.marshal_with(ai_response_model, code=200, description='AI-generated description returned', mask=None)
    @api.response(404, 'Star not found')
    @api.response(500, 'Internal Server Error')
    def get(self, id):
        """Generate a natural-language description of a star using AI."""
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM stars WHERE id = %s", (id,))
            row = cur.fetchone()
            if not row:
                return {'error': 'Star not found'}, 404
            columns = [desc[0] for desc in cur.description]
            star_data = dict(zip(columns, row))
        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            cur.close()

        try:
            description = generate_star_description(str(star_data))
            return {'description': description}, 200
        except Exception as e:
            return {'error': f"AI generation failed: {str(e)}"}, 500
