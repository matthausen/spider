from urllib.request import urlopen, build_opener
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


try:

  url = "https://www.amazon.co.uk/s?k=iphone+X&ref=nb_sb_noss_2"
  opener = build_opener()
  opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
  website = opener.open(url)

  html = website.read()
  
  #html = urlopen("https://www.amazon.co.uk/s?k=iphone+X&ref=nb_sb_noss_2")

except HTTPError as e:

    print(e)

except URLError:

    print("Failed to scrape Amazon")

else:

  #res = BeautifulSoup(html.read(),"html.parser")

  res = BeautifulSoup(html, "html.parser")

  titles = res.findAll("h2", {"class": "a-size-mini"})

  links = res.findAll("a", {"class": "a-link-normal"})

  prices = res.findAll("span", {"class": "a-price"})

  for i in range(len(titles)):
    
    print(titles[i].getText())
    print("https://www.amazon.co.uk/" + links[i]['href'])
    print(prices[i].getText())
