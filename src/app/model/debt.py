from graphene import ObjectType, String, ID, Float


class Debt(ObjectType):
    id = ID()
    name = String()
    value = Float()