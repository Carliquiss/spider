import requests
import sys
import getopt
from parsel import Selector



"""
Funcion para clasificar los enlaces en locales o en externos según una URL dada

Los parámetros son:
    enlaces:lista: Conjunto de todos los enlaces a clasificar
    baseURL:string: URL a la que se hace el crawling
"""
def selectLocalOrExternalLinks(enlaces, baseURL):

    urlsLocales = []
    urlsExternas = []
    for enlace in enlaces:

        if(enlace.split("/")[0] == 'http:' or enlace.split("/")[0] == 'https:'):
            comparacion = enlace.split("/")[2]

            if (comparacion == baseURL):
                urlsLocales.append(enlace)

            else:
                urlsExternas.append(enlace)

        else:
            urlsLocales.append("http://" + baseURL + enlace)




    return urlsLocales, urlsExternas

"""
Función que toma una URL, selecciona todos los enlaces a páginas que encuentra
y llama a la funcion para clasificarlos en externos o en locales

Los parámetros son:
    url:string: Url a la que se quiere hacer el crawling
"""
def getLinks(url):
    #Accedemos a la páginas y nos quedamos con los href a otras urls
    response = requests.get(url)
    selector = Selector(response.text)
    href_links = selector.xpath('//a/@href').getall()
    print(*href_links, sep="\n")

    #Clasificamos los enlaces en externos o locales
    baseURL = url.split("/")[2]
    (enlacesLocales, enlacesExternos) = selectLocalOrExternalLinks(href_links, baseURL)

    print("\n\nEnlaces locales: ")
    print(*enlacesLocales, sep = "\n")
    print("\n\nEnlaces externos: ")
    print(*enlacesExternos,sep = "\n")


"""
Función principal donde se comprueban los parámetros de la función y
se ejecutan las acciones acorde a estos.

Los parámetros son
    -u <url> : URL (con http://) a la que se quiere hacer el crawling
    -l : Si se quieren guardar solo los enlaces locales
    -e : Si se quieren guardar solo los enlaces externos

"""
def main():
    ## Configuramos los parametros que se puedan usar:
    URL = ''
    local = False
    externas = False

    options, remainder = getopt.getopt(sys.argv[1:], 'u:leh',["url=","local=","externas","help"])

    for opt, arg in options:
        if opt in ('-u', '--url'):
            URL = arg
        elif opt in ('-l', '--local'):
            local = True
        elif opt in ('-e', '--externas'):
            externas = True
        elif opt in ('-h', '--help'):
            print('''Los parámetros son
                -u <url> : URL (con http://) a la que se quiere hacer el crawling
                -l : Si se quieren guardar solo los enlaces locales
                -e : Si se quieren guardar solo los enlaces externos''')


    if(URL != ''):
        getLinks(URL)


if __name__ == "__main__":
    main()
