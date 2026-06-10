from flask import jsonify, Blueprint
from models.specialtie_model import get_all_specialties

specialtie_bp = Blueprint('specialtie', __name__)
def get_specialties_data():
    specialties = get_all_specialties()
    return jsonify(specialties)

specialtie_bp.add_url_rule('/specialties', view_func=get_specialties_data, methods=['GET'])