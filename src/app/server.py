from http import HTTPStatus
from flask import Flask
from .log.logger import Logger
from .client_controller.blueprint import ClientBluePrint
from app.config import PORT, DEBUG_MODE, SECRET_KEY, BLUEPRINT_VERSION
from app.response.response import BaseResponse
from datetime import timedelta
from flask_jwt import JWT
from app.model.user import User

logger = Logger(__name__).get_logger()


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.response_class = BaseResponse

    def start(self, host='0.0.0.0', port=PORT, debug=DEBUG_MODE):
        self.__register_blueprints()
        self.__errors_handler()
        self.__set_configs()
        self.__init_jwt()
        self.app.run(host=host, port=port, debug=debug)

    def __init_jwt(self):
        JWT(self.app, User.authenticate, User.identity)

    def __set_configs(self):
        self.app.config['SECRET_KEY'] = SECRET_KEY
        self.app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1)
        self.app.config['JWT_AUTH_URL_RULE'] = '{}/auth'.format(BLUEPRINT_VERSION)

    def __register_blueprints(self):
        self.app.register_blueprint(ClientBluePrint().blueprint)

    def __errors_handler(self):
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
