from graphene import ObjectType, String

class Product(ObjectType):
  name=String()
  price=String()
  rating=String()
  reviews=String()
  availability=String()
  link=String()