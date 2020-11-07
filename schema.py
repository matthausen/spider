from collections import namedtuple
from graphene import ObjectType, String, Schema, Field
from models import Product
from scraper import scrape

ProductValueObject = namedtuple("Product", ["name", "price", "rating", "reviews", "availability", "link"])

class Query(ObjectType):
  item=Field(Product, name=String(required=True))

  def resolve_item(parent, info, name):
    # Call the scraper here
    items = scrape(product_name)
    
    for item in items:
      print(item.name)
      print(item.price)
    
    return ProductValueObject(name=name, price="$300", rating="", reviews="", availability="", link="")


schema = Schema(query=Query)



