from flask import Blueprint, jsonify

catalogo_bp = Blueprint('catalogo', __name__)

@catalogo_bp.route("/api/eventos", methods=["GET"])
def listar_catalogo():
    # No futuro, integraria com APIs externas e filtros de recomendação
    return jsonify({
        "msg": "Catálogo integrado com sucesso.",
        "eventos_recomendados": [
            {"nome": "Festival Emergentes", "categoria": "Rock"},
            {"nome": "Feira Gastronômica", "categoria": "Gastronomia"}
        ]
    })