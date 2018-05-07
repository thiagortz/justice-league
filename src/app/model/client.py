from graphene import ObjectType, String, ID, Field
from .score import Score


class Client(ObjectType):
    id = ID()
    CPF = String()
    score = Field(Score)
