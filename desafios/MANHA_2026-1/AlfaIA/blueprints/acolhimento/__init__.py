from flask import Blueprint
acolhimento_bp = Blueprint("acolhimento", __name__, url_prefix="/acolhimento")
from blueprints.acolhimento import routes  # noqa
