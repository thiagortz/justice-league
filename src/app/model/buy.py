from graphene import ObjectType, ID, Float, Field
from app.model import credit_card


class Buy(ObjectType):
    id = ID()
    value = Float()
    credit_card = Field(credit_card.CreditCard)
