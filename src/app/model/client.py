from graphene import ObjectType, String, ID, Field, List
from app.model import debt, score, event, address


class Client(ObjectType):
    id = ID()
    name = String()
    birth = String()
    CPF = String()
    address = Field(address.Address)
    list_debts = List(debt.Debt)
    score = Field(score.Score)
    events = List(event.Event)
