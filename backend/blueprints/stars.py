from flask import Blueprint, jsonify

stars_bp = Blueprint('stars', __name__)

@stars_bp.route('/', methods=['GET'])
def get_stars():
    return jsonify({"error": "Not implemented"}), 501

@stars_bp.route('/<id>', methods=['GET'])
def get_stars_by_id():
    return jsonify({"error": "Not implemented"}), 501

@stars_bp.route('/<id>/planets', methods=['GET'])
def get_planets_from_star_id():
    return jsonify({"error": "Not implemented"}), 501

@stars_bp.route('/search', methods=['GET'])
def get_stars_by_search():
    return jsonify({"error": "Not implemented"}), 501