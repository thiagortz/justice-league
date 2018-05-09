from flask_graphql import GraphQLView
from flask_jwt import jwt_required


class Client(GraphQLView):

    @jwt_required()
    def get_middleware(self, request):
        return self.middleware
