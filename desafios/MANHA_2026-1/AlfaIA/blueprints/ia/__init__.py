from flask import Blueprint
ia_bp = Blueprint("ia", __name__, url_prefix="/ia")
from blueprints.ia import routes  # noqa
