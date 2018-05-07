import requests
from app.config import SMAN
from app.log.logger import Logger

logger = Logger(__name__).get_logger()


class BusinessServiceABS(object):
    def __init__(self):
        pass

    def to_call(self):
        pass


class SMan(BusinessServiceABS):
    def __init__(self, **kwargs):
        self._url_api = SMAN['url_api']
        self._params = kwargs
        pass

    def to_call(self):
        return self._request_get(resource='5aefb4bc2f00004a00739bf6', params=self._params)

    def _request_get(self, resource, params):
        resp = requests.get('{}/{}'.format(self._url_api, resource), params=self._params)
        logger.info('##* SMAN: {}'.format(resp.json()))
        return resp


class TFlash(BusinessServiceABS):
    def __init__(self, **kwargs):
        self.params = kwargs

    def to_call(self):
        return {"The Flash": 'Ok'}


class SolomonG(BusinessServiceABS):
    def __init__(self, **kwargs):
        self.params = kwargs

    def to_call(self):
        return {"Solomon Grundy": 'Ok'}
