from flask import Blueprint, request, jsonify
from models import db, bcrypt
from models.models import User, Post

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "Usuário já existe"}), 400

    # Aplicação do Hashing Bcrypt com decode para string literal
    senha_criptografada = bcrypt.generate_password_hash(data["senha"]).decode('utf-8')
    
    novo_user = User(
        email=data["email"],
        senha=senha_criptografada,
        tipo=data.get("tipo", "extensionista") # Captura o papel enviado pelo front
    )

    db.session.add(novo_user)
    db.session.commit()
    return jsonify({"msg": "Usuário criado com sucesso!"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    # Verificação segura comparando o texto puro com o hash criptográfico
    if user and bcrypt.check_password_hash(user.senha, data["senha"]):
        return jsonify({"status": "ok", "user_id": user.id, "tipo": user.tipo})

    return jsonify({"status": "erro", "msg": "E-mail ou senha incorretos"}), 401
