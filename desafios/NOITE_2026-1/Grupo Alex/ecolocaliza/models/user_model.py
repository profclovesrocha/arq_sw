from database import db  # <-- Alterado aqui também!

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @classmethod
    def verify_credentials(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user and user.password == password:
            return True
        return False

    @classmethod
    def register_user(cls, username, password):
        existing_user = cls.query.filter_by(username=username).first()
        if existing_user:
            return False
        
        new_user = cls(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return True