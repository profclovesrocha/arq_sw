from flask import jsonify,Blueprint
from models.clinic_model import get_all_clinics

clinic_bp = Blueprint('clinic', __name__)
def get_clinics_data():
    clinics = get_all_clinics()
    return jsonify(clinics)

clinic_bp.add_url_rule('/clinics', view_func=get_clinics_data, methods=['GET'])