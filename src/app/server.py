from http import HTTPStatus
from flask import Flask
from .log.logger import Logger
from .risk_controller.blueprint import RiskBluePrint
from app.config import PORT, DEBUG_MODE
from app.response.response import BaseResponse

logger = Logger(__name__).get_logger()


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.response_class = BaseResponse

    def start(self, host='0.0.0.0', port=PORT, debug=DEBUG_MODE):
        self._register_blueprints()
        self._errors_handler()
        self.app.run(host=host, port=port, debug=debug)

    def _register_blueprints(self):
        self.app.register_blueprint(RiskBluePrint().blueprint)

    def _errors_handler(self):
        app = self.app

        @app.errorhandler(HTTPStatus.BAD_REQUEST)
        def bad_request(error):
            logger.error(error)
            return {'errors': [{'message': error.description}]}, HTTPStatus.BAD_REQUEST

        @app.errorhandler(HTTPStatus.UNAUTHORIZED)
        def unauthorized(error):
            logger.error(error.description)
            return {'errors': [{'message': error.description}]}, HTTPStatus.UNAUTHORIZED

        @app.errorhandler(HTTPStatus.NOT_FOUND)
        def not_found(error):
            logger.error(error)
            return {'errors': [{'message': HTTPStatus.NOT_FOUND._name_}]}, HTTPStatus.NOT_FOUND

        @app.errorhandler(HTTPStatus.METHOD_NOT_ALLOWED)
        def method_not_allowed(error):
            logger.error(error)
            return {'errors': [{'message': error.description}]}, HTTPStatus.METHOD_NOT_ALLOWED

        @app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
        def internal_server_error(error):
            logger.error(error)
            return {'errors': [{'message': HTTPStatus.INTERNAL_SERVER_ERROR._name_}]}, HTTPStatus.INTERNAL_SERVER_ERROR

        @app.errorhandler(Exception)
        def internal_server_error_exception(error):
            logger.error(error)
            return {'errors': [{'message': HTTPStatus.INTERNAL_SERVER_ERROR._name_}]}, HTTPStatus.INTERNAL_SERVER_ERROR
