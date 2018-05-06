from flask import request
from http import HTTPStatus
from app.service.client import Client
from app.service.business_delegate import ServiceDelegate
from app.service.business_service import SMan, TFlash, SolomonG


class Risk(object):
    def analysis(self, cpf):
        service = ServiceDelegate(SMan(cpf=cpf))
        return Client(service).to_call()
