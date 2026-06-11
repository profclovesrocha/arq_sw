from flask import jsonify, request
from flask_login import login_required
from blueprints.ia import ia_bp
from services.ia_service import IAService

svc = IAService()

@ia_bp.route("/preview", methods=["POST"])
@login_required
def preview():
    dados = request.get_json() or {}
    historia, _ = svc.gerar_conteudo(dados)
    return jsonify({"historia": historia})
