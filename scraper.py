from bs4 import BeautifulSoup
import requests
from models import Product
 
def get_title(soup):
     
    try:
        title = soup.find("span", attrs={"id":'productTitle'})
 
        title_value = title.string
 
        title_string = title_value.strip()
 
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()
 
    except AttributeError:
        title_string = ""   
 
    return title_string
 
def get_price(soup):
 
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
 
        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
 
        except:     
            price = ""  
 
    return price
 
def get_rating(soup):
 
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
         
    except AttributeError:
         
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = "" 
 
    return rating
 
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
         
    except AttributeError:
        review_count = ""   
 
    return review_count
 
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()
 
    except AttributeError:
        available = "Not Available"
 
    return available  

def make_item(name, price, rating, reviews, availability, link):
  item = Product()
  item.name=name
  item.price=price
  item.rating=rating
  item.reviews=reviews
  item.availability=availability
  item.link=link

  return item


def scrape(product_name):
    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})
 
    # The webpage URL
    URL = "https://www.amazon.com/s?k=" + product_name + "+4&ref=nb_sb_noss_2"
     
    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
 
    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")
 
    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
 
    # Store the links
    links_list = []
 
    # Loop for extracting links from Tag Objects
    for link in links:
        links_list.append(link.get('href'))

    items_list = []
 
 
    # Loop for extracting product details from each link 
    for index, link in enumerate(links_list):

        if index <= 19:

          new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
  
          new_soup = BeautifulSoup(new_webpage.content, "lxml")

          item = make_item(
            get_title(new_soup),
            get_rating(new_soup),
            get_rating(new_soup),
            get_review_count(new_soup),
            get_availability(new_soup),
            link
            )

          items_list.append(item)
          
          # Function calls to display all necessary product information
          ''' print("Product Title =", get_title(new_soup))
          print("Product Price =", get_price(new_soup))
          print("Product Rating =", get_rating(new_soup))
          print("Number of Product Reviews =", get_review_count(new_soup))
          print("Availability =", get_availability(new_soup))
          print("Link = ", link)
          print()  ''' 

        return items_list
 
 
if __name__ == '__main__':
 scrape()