from flask import Blueprint
from .controller import Risk
from app.config import BLUEPRINT_VERSION
from app.data.score import QueryScore
from graphene import Schema


class RiskBluePrint:
    def __init__(self):
        blueprint = Blueprint('risk', __name__, url_prefix=BLUEPRINT_VERSION)
        blueprint.add_url_rule('/risk/analysis', methods=['POST'],
                               view_func=Risk.as_view('analysis', schema=Schema(query=QueryScore), graphiql=True))
        self.blueprint = blueprint
