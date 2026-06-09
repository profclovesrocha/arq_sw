from config import get_db_connection

def get_all_schedules():
    db = get_db_connection()

    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM view_free_schedules')
        return cursor.fetchall()
    
def get_schedule_by_specialtie_and_date(filter):
    db = get_db_connection()

    with db.cursor() as cursor:
        if filter.get('clinic'):
            cursor.execute('SELECT * FROM view_free_schedules WHERE specialtie = %s AND start_time >= %s AND clinic = %s', (filter['specialtie'], filter['start_time'], filter['clinic']), )
            return cursor.fetchall()

        cursor.execute('SELECT * FROM view_free_schedules WHERE specialtie = %s AND start_time >= %s', (filter['specialtie'], filter['start_time']))
        return cursor.fetchall()
    
def get_schedule_by_patient(patient_id):
    db = get_db_connection()

    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM view_appointments WHERE patient_id = %s', (patient_id, ))
        return cursor.fetchall()