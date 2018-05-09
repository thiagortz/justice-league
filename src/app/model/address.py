from graphene import ObjectType, String, ID


class Address(ObjectType):
    id = ID()
    neighborhood = String()
    zipcode = String()
    city = String()
    complement = String()
    state = String()
    district = String()
    district_number = String()
    district_type = String()
    country = String()
    region = String()
