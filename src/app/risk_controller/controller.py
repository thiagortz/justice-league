from flask_graphql import GraphQLView


class Risk(GraphQLView):

    def get_middleware(self, request):
        return self.middleware
