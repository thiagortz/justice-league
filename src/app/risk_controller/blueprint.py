from flask import Blueprint
from .controller import Risk
from app.config import BLUEPRINT_VERSION


class RiskBluePrint:
    def __init__(self):
        blueprint = Blueprint('risk', __name__, url_prefix=BLUEPRINT_VERSION)
        blueprint.add_url_rule('/risk/analysis/<cpf>', methods=['GET'], view_func=Risk().analysis)
        self.blueprint = blueprint