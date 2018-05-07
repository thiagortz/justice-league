from graphene import ObjectType, String, ID


class CreditCard(ObjectType):
    id = ID()
    number = String()
    validity = String()
