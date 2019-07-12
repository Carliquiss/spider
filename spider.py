import requests
from parsel import Selector
import time


URL = 'http://dtstc.ugr.es/it/itt_st/'

start = time.time()

### Crawling to the website

# GET request to recurship site
response = requests.get(URL)

## Setup for scrapping tool

# "response.txt" contain all web page content
selector = Selector(response.text)

# Extracting href attribute from anchor tag <a href="*">
href_links = selector.xpath('//a/@href').getall()

for enlaces in href_links:
    print(enlaces)


end = time.time()
print("Ha tardado : ", (end-start))
