from models import User
from extensions import db

class UserRepository:
    def buscar_por_email(self, email):
        return User.query.filter_by(email=email).first()
    def buscar_por_id(self, uid):
        return User.query.get(int(uid))
    def salvar(self, user):
        db.session.add(user)
        db.session.commit()
        return user
