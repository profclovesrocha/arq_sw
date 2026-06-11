from flask import Blueprint
pedagogico_bp = Blueprint("pedagogico", __name__, url_prefix="/pedagogico")
from blueprints.pedagogico import routes  # noqa
