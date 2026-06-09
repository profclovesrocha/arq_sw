<<<<<<< HEAD:desafios/NOITE_2026-1/FoguinhosRecife/models/models.py
from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    local = db.Column(db.String(200))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
=======
from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    # Define o papel no sistema: 'professor' ou 'extensionista'
    tipo = db.Column(db.String(20), nullable=False)

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    local = db.Column(db.String(200))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
>>>>>>> 1b23910f8fbdb558822ef0643423323080a8cd90:desafios/NOITE_2026-1/Grupo Giovanna/models.py
