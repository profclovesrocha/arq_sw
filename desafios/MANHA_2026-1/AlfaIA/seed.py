from app import create_app
from extensions import db
from models import User, Aluno

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    prof = User(username="prof_ana", email="professor@imip.br", role="professor")
    prof.set_password("123456")
    admin = User(username="admin", email="admin@imip.br", role="admin")
    admin.set_password("admin123")
    db.session.add_all([prof, admin])

    alunos = [
        Aluno(nome="Joao Pedro",  idade=7,  nivel_atual="pre-silabico"),
        Aluno(nome="Maria Clara", idade=8,  nivel_atual="silabico"),
        Aluno(nome="Lucas Souza", idade=9,  nivel_atual="silabico-alfa"),
        Aluno(nome="Ana Beatriz", idade=10, nivel_atual="alfabetico"),
    ]
    db.session.add_all(alunos)
    db.session.commit()
    print("Banco populado com sucesso!")
    print("   Login: professor@imip.br / 123456")
    print("   Admin: admin@imip.br / admin123")
