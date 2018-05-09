from graphene import ObjectType, String, ID, Float, Field
from app.model import buy


class Event(ObjectType):
    id = ID()
    last_query = String()
    financial_movement = Float()
    last_buy = Field(buy.Buy)
