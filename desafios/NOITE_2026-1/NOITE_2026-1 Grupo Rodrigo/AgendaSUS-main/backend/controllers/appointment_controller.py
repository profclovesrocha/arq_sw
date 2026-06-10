from flask import jsonify, request, Blueprint
from models.appointment_model import do_appointment

appointment_bp = Blueprint('appointment', __name__)
def add_appointment():
    data = request.json

    try:
        do_appointment(data['patient_id'], data['free_schedule_id'])
        return jsonify({'Mensagem: ': 'Consulta agendada com sucesso.'}), 201
    except Exception as e:
        return jsonify({'Erro: ': str(e)}), 400
    
appointment_bp.add_url_rule('/add_appointment', view_func=add_appointment, methods=['POST'])