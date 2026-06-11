from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token


# Blueprint da rota
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# REGISTRO
@auth_bp.route("/register", methods=["POST"])
def register():
    # recebe JSON
    data = request.get_json()

    # campos obrigatórios
    required_fields = ["name", "email", "password", "role"]

    # loop para verificar se todos os campos obrigatórios estão presentes
    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Campo '{field}' é obrigatório"
            }), 400

     # cargos 
    allowed_roles = ["aluno", "professor"]
    # verifica se o cargo é válido

    if data["role"] not in allowed_roles:
        return jsonify({
            "error": f"Campo 'role' deve ser 'aluno' ou 'professor'"
        }), 400

    # Verifica se email já existe
    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({
            "error": "Email já registrado"
        }), 400

    # Criptografa senha
    hashed_password = generate_password_hash( data["password"])

    # Cria usuário
    user = User(
        name=data["name"],
        email=data["email"],
        password=hashed_password,
        role=data["role"]
    )

    # Salva no banco
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Usuário criado com sucesso"
    }), 201


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    # recebe JSON
    data = request.get_json()

    # Busca usuário
    user = User.query.filter_by(
        email=data["email"]
    ).first()

    # Verifica se email existe
    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({
            "error": "Email já registrado"
        }), 400

    # Verifica senha
    if not user or not check_password_hash(
        user.password,
        data["password"]
    ):

        return jsonify({
            "error": "Credenciais inválidas"
        }), 401

    # Cria token JWT
    token = create_access_token(
        identity=str(user.id)
    , additional_claims={"role": user.role}
    )

    return jsonify({
        "token": token,
        "role": user.role
    })