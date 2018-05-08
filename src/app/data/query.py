from graphene import ObjectType, Field, String
import json
from app.model import score, client, event
from app.service.client import Client  as ClientService
from app.service.business_delegate import ServiceDelegate
from app.service.business_service import SuperMan, SolomonGrundy, TheFlash
from app.helper.json import json2obj
from flask import abort
from http import HTTPStatus


class Query(ObjectType):
    score = Field(score.Score, CPF=String(required=True))
    client = Field(client.Client, CPF=String(required=True))
    event = Field(event.Event, CPF=String(required=True))

    def resolve_score(self, args, CPF):
        client_service = ClientService(ServiceDelegate(SuperMan(CPF=CPF)))
        score = client_service.to_call()

        if not score.ok:
            abort(HTTPStatus.NOT_FOUND, 'unable to get requested score')

        return json2obj(score.text)

    def resolve_client(self, agrs, CPF):

        service_solomon = SolomonGrundy(CPF=CPF)
        service_sman = SuperMan(CPF=CPF)
        service_the_flash = TheFlash(CPF=CPF)

        service_delegate = ServiceDelegate(service_solomon)
        client_service = ClientService(service_delegate)

        client = client_service.to_call()
        service_delegate.set_business_service(service_sman)
        score = client_service.to_call()
        service_delegate.set_business_service(service_the_flash)
        event = client_service.to_call()

        if not client.ok or not score.ok or not event.ok:
            abort(HTTPStatus.NOT_FOUND, 'unable to get requested client {}'.format(CPF))

        client_j = json.loads(client.text)
        client_j['score'] = json.loads(score.text)
        client_j['events'] = [json.loads(event.text)]

        return json2obj(json.dumps(client_j))

    def resolve_event(self, args, CPF):
        service = ServiceDelegate(TheFlash(CPF=CPF))
        event = ClientService(service).to_call()

        if not event.ok:
            abort(HTTPStatus.NOT_FOUND, 'unable to get requested event')

        return json2obj(event.text)
