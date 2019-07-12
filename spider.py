import requests
from parsel import Selector


#URL = 'http://dtstc.ugr.es/it/itt_st/'
URL = 'https://hmedieval.ugr.es/'

def selectLocalOrExternalLinks(enlaces, baseURL):

    urlsLocales = []
    urlsExternas = []
    for enlace in enlaces:

        if(enlace.split("/")[0] == 'http:'):
            comparacion = enlace.split("/")[2]

            if (comparacion == baseURL):
                urlsLocales.append(enlace)

            else:
                urlsExternas.append(enlace)

        else:
            urlsLocales.append(enlace)

    print("Enlaces locales: ")
    print(urlsLocales)
    print("Enlaces externos: ")
    print(urlsExternas)


def getLinks(url):
    #Accedemos a la páginas y nos quedamos con los href a otras urls
    response = requests.get(url)
    selector = Selector(response.text)
    href_links = selector.xpath('//a/@href').getall()

    for enlaces in href_links:
        print(enlaces)


    #Nos quedamos con los enlaces locales:
    baseURL = url.split("/")[2]
    selectLocalOrExternalLinks(href_links, baseURL)
    #Nos quedamos con los enlaces externos:


getLinks(URL)
