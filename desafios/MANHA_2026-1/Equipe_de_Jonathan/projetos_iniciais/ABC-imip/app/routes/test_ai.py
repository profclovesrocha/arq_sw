from flask import Blueprint, jsonify

test_ai_bp = Blueprint("test_ai", __name__, url_prefix="/test")

@test_ai_bp.route("/ai", methods=["GET"])
def test_ai():
    return jsonify({
        "message": "rota funcionando"
    })