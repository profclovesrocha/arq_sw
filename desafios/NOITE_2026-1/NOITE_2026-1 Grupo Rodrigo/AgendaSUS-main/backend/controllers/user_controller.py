from flask import jsonify, request,Blueprint
from models.user_model import get_all_patients, get_patient_by_email, create_patient

user_bp = Blueprint('user',__name__)

@user_bp.route('/users', methods=['GET'])
def get_patients_data():
    patients = get_all_patients()
    return jsonify(patients)

@user_bp.route('/users/search', methods=['GET'])
def get_patient():
    email = request.args.get('email')
    patient = get_patient_by_email(email)

    if not patient:
        return jsonify({'Erro: ': f'E-mail {email} não encontrado.'}), 404
    
    return jsonify(patient)

@user_bp.route('/addUser', methods=['POST'])
def add_patient():
    data = request.json

    try:
        create_patient(data.get('users'), data.get('patient'))
        return jsonify({'Mensagem: ': 'Usuário criado com sucesso.'}), 201
    except Exception as e:
        return jsonify({'Erro: ': str(e)}), 400
    
user_bp.add_url_rule('/users', view_func=get_patients_data, methods=['GET'])
user_bp.add_url_rule('/users/search', view_func=get_patient, methods=['GET'])
user_bp.add_url_rule('/addUser', view_func=add_patient, methods=['POST'])