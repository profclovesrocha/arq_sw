from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt

# Decorator para verificar se o usuário é um professor
def professor_required(fn): 
    @wraps(fn)

    # Verifica o papel do usuário a partir dos claims do JWT
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        role = claims.get("role")

        if role != "professor":
            return jsonify({
                "error": "Acesso permitido apenas para professores"
            }), 403

        return fn(*args, **kwargs)

    return wrapper