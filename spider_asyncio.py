import requests
import aiohttp
import asyncio
from parsel import Selector
import time


URL = 'http://dtstc.ugr.es/it/itt_st/'

start = time.time()
all_urls  = {} # website links as "keys" and images link as "values"

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as exp:
        return '<html> <html>' #empty html for invalid uri case

async def main(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)
        for index, html in enumerate(htmls):
            selector = Selector(html)
            image_links = selector.xpath('//a/@href').getall()
            all_urls[urls[index]] = image_links
        #print('*** Todas las URLs: ', all_urls)
        for enlaces in all_urls:
            print(enlaces)


response = requests.get(URL)
selector = Selector(response.text)
href_links = selector.xpath('//a/@href').getall()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(href_links))


print ("All done !")
end = time.time()
print("Time taken in seconds : ", (end-start))
