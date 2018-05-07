from flask_graphql import GraphQLView


class Client(GraphQLView):

    def get_middleware(self, request):
        return self.middleware
