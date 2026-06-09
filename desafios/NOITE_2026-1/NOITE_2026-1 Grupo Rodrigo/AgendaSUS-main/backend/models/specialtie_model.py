from config import get_db_connection

def get_all_specialties():
    db = get_db_connection()

    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM specialties')
        return cursor.fetchall()