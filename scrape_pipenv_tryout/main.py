import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#headers = {‘User-Agent’: ‘Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3’}
#reg_url = “https:XXXXOOOO"
#req = Request(url=reg_url, headers=headers)
#html = urlopen(req).read()

# specify the url
quote_page = "https://www.kilo.lt"

# query the website and return the html to the variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")

print(page)

#with open("scrape_test.html") as html_file:
#    soup = BeautifulSoup(html_file, "lxml")
#
#print(soup)
