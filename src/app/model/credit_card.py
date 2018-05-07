from graphene import ObjectType, String, ID


class CreditCard(ObjectType):
    id = ID()
    number = String()
    expiration_date = String()
