from flask import Blueprint
relatorios_bp = Blueprint("relatorios", __name__, url_prefix="/relatorios")
from blueprints.relatorios import routes  # noqa
