from flask import Blueprint, jsonify

systems_bp = Blueprint('systems', __name__)

@systems_bp.route('/', methods=['GET'])
def get_systems():
    return jsonify({"error": "Not implemented"}), 501

@systems_bp.route('/<id>', methods=['GET'])
def get_system_by_id(id):
    return jsonify({"error": "Not implemented"}, {"okay": id}), 501

@systems_bp.route('/<id>/planets', methods=['GET'])
def get_planets_from_system_by_id(id):
    return jsonify({"error": "Not implemented"}, {"okay": id}), 501

@systems_bp.route('/<id>/stars', methods=['GET'])
def get_stars_from_system_by_id(id):
    return jsonify({"error": "Not implemented"}, {"okay": id}), 501

@systems_bp.route('/search', methods=['GET'])
def get_systems_by_search(id):
    return jsonify({"error": "Not implemented"}, {"okay": id}), 501