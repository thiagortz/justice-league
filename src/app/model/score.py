from graphene import ObjectType, String, Float


class Score(ObjectType):
    pointing = Float()
    last_query = String()
