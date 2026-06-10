from flask import jsonify, request, Blueprint
from models.schedule_model import get_all_schedules, get_schedule_by_specialtie_and_date, get_schedule_by_patient

schedule_bp = Blueprint('schedule', __name__)
def get_schedules_data():
    schedules = get_all_schedules()
    return jsonify(schedules)

def get_filtered_schedules():
    print("--> ENTOU NO CONTROLLER GET_FILTERED_SCHEDULES!", flush=True)
    specialtie = request.args.get('specialtie', '').strip()
    start_time = request.args.get('start_time', '').strip()
    
    filter = {
        'specialtie': specialtie,
        'start_time': start_time,
    }

    clinic_arg = request.args.get('clinic')
    if clinic_arg and clinic_arg not in ['undefined', 'null', '']:
        filter['clinic'] = clinic_arg.strip()

    schedules = get_schedule_by_specialtie_and_date(filter)
    print("Resultado no Python:", schedules, flush=True)
    return jsonify(schedules)

def get_patient_schedules():
    patient_id = request.args.get('patient')
    
    schedules = get_schedule_by_patient(patient_id)
    return jsonify(schedules)

schedule_bp.add_url_rule('/free_schedules', view_func=get_schedules_data, methods=['GET'])
schedule_bp.add_url_rule('/filtered_schedules/search', view_func=get_filtered_schedules, methods=['GET'])
schedule_bp.add_url_rule('/schedule_by_patient/search', view_func=get_patient_schedules, methods=['GET'])