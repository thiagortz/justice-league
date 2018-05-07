from flask import Response, jsonify


class BaseResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(BaseResponse, cls).force_type(rv, environ)
