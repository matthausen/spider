from graphene import ObjectType, String, Schema, Field, List
from models import Product
from scraper import scrape

product_list = []

class Query(ObjectType):
  item=List(Product, name=String(required=True))

  def resolve_item(parent, info, name):
    items = scrape(name)
    
    for item in items:
      item = Product(name=item.name, price=item.price, rating=item.rating, reviews=item.reviews, availability=item.availability, link=item.link)
      product_list.append(item)

    return product_list

schema = Schema(query=Query)



