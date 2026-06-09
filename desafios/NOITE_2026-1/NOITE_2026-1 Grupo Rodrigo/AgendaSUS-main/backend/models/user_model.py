from config import get_db_connection

def get_all_patients():
    db = get_db_connection()

    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM view_patients')
        return cursor.fetchall()

def get_patient_by_email(email):
    db = get_db_connection()

    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM view_patients WHERE email = %s', (email, ))
        return cursor.fetchone()
    
def create_patient(user_data, patient_data):
    db = get_db_connection()
    
    try:
        with db.cursor() as cursor:
            cursor.execute('INSERT INTO users (email, password, role) VALUES (%s, %s, %s)', (user_data['email'], user_data['password'], user_data['role'],))
            last_id = cursor.lastrowid
            cursor.execute('INSERT INTO patients (name, cpf, birth_date, phone_number, user_id) VALUES (%s, %s, %s, %s, %s)', (patient_data['name'], patient_data['cpf'], patient_data['birthdate'], patient_data['phoneNumber'], last_id))

            db.commit()
            return True
        
    except Exception as e:
        db.rollback()
        raise e