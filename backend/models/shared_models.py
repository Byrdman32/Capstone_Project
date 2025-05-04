from flask_restx import fields

def register_models(api):
    system_model = api.model('System', {
        'id': fields.Integer(readOnly=True, description="Unique system ID (auto-generated)."),
        'system_name': fields.String(required=True, description="Name of the planetary system."),
        'distance_light_years': fields.Float(required=True, description="Distance from Earth in light years.")
    })

    star_model = api.model('Star', {
        'id': fields.Integer(readOnly=True, description="Unique star ID (auto-generated)."),
        'star_name': fields.String(required=True, description="Unique name of the star."),
        'mass': fields.Float(description="Mass of the star (must be > 0)."),
        'radius': fields.Float(description="Radius of the star (must be > 0)."),
        'apparent_magnitude': fields.Float(description="Apparent magnitude of the star."),
        'spectral_type': fields.String(description="Spectral classification (e.g. O, B, A, F, G, K, M)."),
        'age_years': fields.Float(description="Estimated age of the star in years (must be > 0)."),
        'system_id': fields.Integer(required=True, description="ID of the planetary system this star belongs to.")
    })

    planet_model = api.model('Planet', {
        'id': fields.Integer(readOnly=True, description="Unique planet ID (auto-generated)."),
        'planet_name': fields.String(required=True, description="Name of the planet."),
        'mass': fields.Float(description="Mass of the planet (in Earth masses)."),
        'radius': fields.Float(description="Radius of the planet (in Earth radii)."),
        'orbital_period': fields.Float(description="Orbital period in Earth days."),
        'semi_major_axis': fields.Float(description="Semi-major axis of the orbit (in AU)."),
        'eccentricity': fields.Float(description="Orbital eccentricity (0-1 range)."),
        'system_id': fields.Integer(required=True, description="ID of the planetary system this planet belongs to.")
    })

    search_model = api.model('SearchRequest', {
        'request_string': fields.String(required=True, description="SQL WHERE clause used to filter systems. This clause is validated before execution.")
    })

    ai_response_model = api.model('AIDescription', {
        'description': fields.String(description='AI-generated summary or contextual description of the system, star, or planet.'),
    })

    return {
        'system_model': system_model,
        'star_model': star_model,
        'planet_model': planet_model,
        'search_model': search_model,
        'ai_response_model': ai_response_model
    }
