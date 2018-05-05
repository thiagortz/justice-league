from flask import request
from http import HTTPStatus


class Risk(object):
    def analysis(self, cpf):
        return {'CPF': cpf}
