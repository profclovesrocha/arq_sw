from config import get_db_connection

def do_appointment(patient_id, free_schedule_id):
    db = get_db_connection()

    try:
        with db.cursor() as cursor:
            cursor.execute('INSERT INTO appointments (status, patient_id, free_schedule_id) VALUES ("SCHEDULED", %s, %s)', (patient_id, free_schedule_id))

            db.commit()
            return True
        
    except Exception as e:
        db.rollback()
        raise e