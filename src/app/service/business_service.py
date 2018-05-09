import requests
from app.config import SUPER_MAN, THE_FLASH, SOLOMON_GRUNDY
from app.log.logger import Logger

logger = Logger(__name__).get_logger()


class BusinessServiceABS(object):
    def __init__(self):
        pass

    def to_call(self):
        pass

    def _request_get(self, resource, params):
        pass


class SuperMan(BusinessServiceABS):
    def __init__(self, **kwargs):
        self._url_api = SUPER_MAN['url_api']
        self._params = kwargs

    def to_call(self):
        return self._request_get(resource='5af099f2310000610096c6ee', params=self._params)

    def _request_get(self, resource, params):
        resp = requests.get('{}/{}'.format(self._url_api, resource), params=self._params)
        logger.info('#### SuperMan: {}'.format(resp.json()))
        return resp


class TheFlash(BusinessServiceABS):
    def __init__(self, **kwargs):
        self._url_api = THE_FLASH['url_api']
        self._params = kwargs

    def to_call(self):
        return self._request_get(resource='5af0bb973100004a0096c74d', params=self._params)

    def _request_get(self, resource, params):
        resp = requests.get('{}/{}'.format(self._url_api, resource), params=self._params)
        logger.info('#### TheFlash: {}'.format(resp.json()))
        return resp


class SolomonGrundy(BusinessServiceABS):
    def __init__(self, **kwargs):
        self._url_api = SOLOMON_GRUNDY['url_api']
        self._params = kwargs

    def to_call(self):
        return self._request_get(resource='5af076bc3100004d0096c66b', params=self._params)

    def _request_get(self, resource, params):
        resp = requests.get('{}/{}'.format(self._url_api, resource), params=self._params)
        logger.info('####  SolomonGrundy: {}'.format(resp.json()))
        return resp
