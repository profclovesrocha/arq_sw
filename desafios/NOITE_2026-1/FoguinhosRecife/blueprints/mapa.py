from flask import Blueprint, jsonify

mapa_bp = Blueprint('mapa', __name__)

@mapa_bp.route("/api/locais", methods=["GET"])
def obter_locais():
    # No futuro, isso buscaria as coordenadas reais do banco de dados
    return jsonify({
        "msg": "Módulo de Mapa operante.",
        "pontos_calor": [
            {"lat": -8.0631, "lng": -34.8711, "intensidade": "alta"},
            {"lat": -8.0090, "lng": -34.8550, "intensidade": "media"}
        ]
    })