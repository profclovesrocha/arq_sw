from extensions import db, bcrypt, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(40),  unique=True, nullable=False)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role          = db.Column(db.String(30),  nullable=False, default="professor")
    ativo         = db.Column(db.Boolean, default=True)
    trilhas       = db.relationship("Trilha", backref="professor", lazy=True)
    ROLES         = ["professor", "extensionista", "coordenador", "admin"]

    def set_password(self, senha):
        self.password_hash = bcrypt.generate_password_hash(senha).decode("utf-8")

    def check_password(self, senha):
        return bcrypt.check_password_hash(self.password_hash, senha)

    def __repr__(self):
        return f"<User {self.username}>"


class Aluno(db.Model):
    __tablename__ = "alunos"
    id          = db.Column(db.Integer, primary_key=True)
    nome        = db.Column(db.String(80), nullable=False)
    idade       = db.Column(db.Integer, default=7)
    nivel_atual = db.Column(db.String(30), default="pre-silabico")
    ativo       = db.Column(db.Boolean, default=True)
    criado_em   = db.Column(db.DateTime, default=datetime.utcnow)
    trilhas     = db.relationship("Trilha", backref="aluno", lazy=True)
    NIVEIS      = ["pre-silabico", "silabico", "silabico-alfa", "alfabetico"]

    def __repr__(self):
        return f"<Aluno {self.nome}>"


class Trilha(db.Model):
    __tablename__ = "trilhas"
    id           = db.Column(db.Integer, primary_key=True)
    titulo       = db.Column(db.String(120), nullable=False)
    nivel        = db.Column(db.String(20), default="iniciante")
    status       = db.Column(db.String(20), default="ativa")
    criada_em    = db.Column(db.DateTime, default=datetime.utcnow)
    professor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    aluno_id     = db.Column(db.Integer, db.ForeignKey("alunos.id"), nullable=False)
    atividades   = db.relationship("Atividade", backref="trilha", lazy=True,
                                   cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Trilha {self.titulo}>"


class Atividade(db.Model):
    __tablename__ = "atividades"
    id        = db.Column(db.Integer, primary_key=True)
    titulo    = db.Column(db.String(100), nullable=False)
    tipo      = db.Column(db.String(30), default="exercicio")
    conteudo  = db.Column(db.Text)
    ordem     = db.Column(db.Integer, default=0)
    concluida = db.Column(db.Boolean, default=False)
    criada_em = db.Column(db.DateTime, default=datetime.utcnow)
    trilha_id = db.Column(db.Integer, db.ForeignKey("trilhas.id"), nullable=False)

    def __repr__(self):
        return f"<Atividade {self.titulo}>"
