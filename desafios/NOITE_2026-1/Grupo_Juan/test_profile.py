from app import app, db, seed

with app.app_context():
    db.drop_all()
    seed()
    client = app.test_client()
    response = client.post('/login', data={'email': 'ana@ravix.com', 'password': '123456'}, follow_redirects=True)
    print('Login status code:', response.status_code)
    print('Dashboard text found:', 'Dashboard' in response.get_data(as_text=True))
    profile = client.get('/profile')
    print('/profile status code:', profile.status_code)
    text = profile.get_data(as_text=True)
    print('Profile page loaded:', 'Meu Perfil' in text)
    print('Turma name found:', 'Matemática 9º Ano' in text)
