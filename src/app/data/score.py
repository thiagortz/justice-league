from graphene import ObjectType, Field, String
import json
from app.model.score import Score
from app.service.client import Client  as ClientService
from app.service.business_delegate import ServiceDelegate
from app.service.business_service import SMan
from app.helper.json import json2obj
from flask import abort
from http import HTTPStatus


class QueryScore(ObjectType):
    score = Field(Score, CPF=String(required=True))

    def resolve_score(self, args, CPF):
        service = ServiceDelegate(SMan(CPF=CPF))
        client = ClientService(service).to_call()

        if not client.ok:
            abort(HTTPStatus.NOT_FOUND, 'score not found for client {}'.format(CPF))

        return json2obj(json.dumps(client.json()['score']))
