from flask import Blueprint
from .controller import Client
from app.config import BLUEPRINT_VERSION
from app.data.query import Query
from graphene import Schema


class ClientBluePrint:
    def __init__(self):
        blueprint = Blueprint('client', __name__, url_prefix=BLUEPRINT_VERSION)
        blueprint.add_url_rule('/client', methods=['POST'],
                               view_func=Client.as_view('client', schema=Schema(query=Query), graphiql=False))
        self.blueprint = blueprint
