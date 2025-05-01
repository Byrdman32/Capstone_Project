from flask import Blueprint, jsonify

planets_bp = Blueprint('planets', __name__)

@planets_bp.route('/', methods=['GET'])
def get_systems():
    return jsonify({"error": "Not implemented"}), 501

@planets_bp.route('/<id>', methods=['GET'])
def get_stars_by_id():
    return jsonify({"error": "Not implemented"}), 501

@planets_bp.route('/<id>/planets', methods=['GET'])
def get_planets_from_star_id():
    return jsonify({"error": "Not implemented"}), 501

@planets_bp.route('/search', methods=['GET'])
def get_stars_by_search():
    return jsonify({"error": "Not implemented"}), 501