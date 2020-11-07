from collections import namedtuple
from graphene import ObjectType, String, Schema, Field
from scraper import scrape

ProductValueObject = namedtuple("Product", ["name", "price", "rating", "reviews", "availability", "link"])

class Product(ObjectType):
  name=String()
  price=String()
  rating=String()
  reviews=String()
  availability=String()
  link=String()



class Query(ObjectType):
  item=Field(Product, name=String(required=True))

  def resolve_item(parent, info, name):
    # Call the scraper here
    scrape()
    return ProductValueObject(name=name, price="$300", rating="", reviews="", availability="", link="")


schema = Schema(query=Query)



