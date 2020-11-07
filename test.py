from urllib.request import urlopen, build_opener
from bs4 import BeautifulSoup, SoupStrainer

url = "https://www.amazon.co.uk/s?k=iphone+X&ref=nb_sb_noss_2"
opener = build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
website = opener.open(url)

html = website.read()
soup = BeautifulSoup(html, "html.parser")

for element in soup.find_all(['a','link']):
  link = element.get('href')
  print(link)