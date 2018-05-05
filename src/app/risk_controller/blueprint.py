from flask import Blueprint
from .controller import Risk


class RiskBluePrint:
    def __init__(self):
        blueprint = Blueprint('risk', __name__, url_prefix='/v1')
        blueprint.add_url_rule('/risk/analysis/<cpf>', methods=['GET'], view_func=Risk().analysis)
        self.blueprint = blueprint