from collections import namedtuple
from graphene import ObjectType, String, Schema, Field

ProductValueObject = namedtuple("Product", ["item_name", "item_price"])

class Product(ObjectType):
  item_name=String()
  item_price=String()


class Query(ObjectType):
  hello = String(item=String(default_value="stranger"))
  goodbye = String()

  item=Field(Product)

  def resolve_item(parent, info):
    return ProductValueObject(item_name="Xbox360", item_price="$300")

  def resolve_hello(root, info, item):
    return f'Hello {item}!'

  def resolve_goodbye(root, info):
    return 'See ya'

schema = Schema(query=Query)



