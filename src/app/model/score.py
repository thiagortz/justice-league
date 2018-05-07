from graphene import ObjectType, String, Float, ID


class Score(ObjectType):
    id = ID()
    pointing = Float()
    last_query = String()
