import requests
import sys
import getopt
from parsel import Selector


#URL = 'http://dtstc.ugr.es/it/itt_st/'
URL = 'http://tstc.ugr.es/'

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

    return urlsLocales, urlsExternas


def getLinks(url):
    #Accedemos a la páginas y nos quedamos con los href a otras urls
    response = requests.get(url)
    selector = Selector(response.text)
    href_links = selector.xpath('//a/@href').getall()

    #Clasificamos los enlaces en externos o locales
    baseURL = url.split("/")[2]
    (enlacesLocales, enlacesExternos) = selectLocalOrExternalLinks(href_links, baseURL)

    print("\n\nEnlaces locales: ")
    print(*enlacesLocales, sep = "\n")
    print("\n\nEnlaces externos: ")
    print(*enlacesExternos,sep = "\n")
    

def main():
    ## Configuramos los parametros que se puedan usar:
    URL = ''
    local = False
    externas = False

    options, remainder = getopt.getopt(sys.argv[1:], 'u:le', ['URL=',
                                                             'local',
                                                             'externas=',
                                                             ])

    for opt, arg in options:
        if opt in ('-u', '--url'):
            URL = arg
        elif opt in ('-l', '--local'):
            local = True
        elif opt in ('-e', '--externas'):
            externas = True


    getLinks(URL)


if __name__ == "__main__":
    main()
