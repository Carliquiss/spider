import requests
import sys
import getopt
import os
from parsel import Selector
from colorama import init, Fore, Back, Style



"""
 __          __  _        _____                    _
 \ \        / / | |      / ____|                  | |
  \ \  /\  / /__| |__   | |     _ __ __ ___      _| | ___ _ __
   \ \/  \/ / _ \ '_ \  | |    | '__/ _` \ \ /\ / / |/ _ \ '__|
    \  /\  /  __/ |_) | | |____| | | (_| |\ V  V /| |  __/ |
     \/  \/ \___|_.__/   \_____|_|  \__,_| \_/\_/ |_|\___|_|

                                                    by: Carliquiss


"""

init(autoreset=True) # Para que los colores se reseten tras un print
PATH_LOCALES = "./URLS_locales"
PATH_EXTERNAS = "./URLS_externas"


def initFolders():
    """
    Función para crear carpetas donde se guardan las URLs encontradas
    """
    if os.path.exists(PATH_LOCALES) == False:
        os.mkdir(PATH_LOCALES)
    if os.path.exists(PATH_EXTERNAS) == False:
        os.mkdir(PATH_EXTERNAS)


def removeDuplicatedLines(nombre_archivo):

    lineas_comprobadas = set()
    archivo = open(nombre_archivo[:-4] + "_.txt" , "w")
    for linea in open(nombre_archivo, "r"):
        if linea not in lineas_comprobadas:
            archivo.write(linea)
            lineas_comprobadas.add(linea)


    archivo.close()
    os.remove(nombre_archivo)


def selectLocalOrExternalLinks(enlaces, baseURL):
    """
    Funcion para clasificar los enlaces en locales o en externos según una URL dada

    Los parámetros son:
        enlaces:lista:  Conjunto de todos los enlaces a clasificar
        baseURL:string: URL a la que se hace el crawling
    """

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
            if(enlace[0] != "/"):
                enlace = "/" + enlace
            urlsLocales.append("http://" + baseURL + enlace)


    return urlsLocales, urlsExternas




def getLinks(url):
    """
    Función que toma una URL, selecciona todos los enlaces a páginas que encuentra
    y llama a la funcion para clasificarlos en externos o en locales

    Los parámetros son:
        url:string: Url a la que se quiere hacer el crawling
    """
    #Accedemos a la páginas y nos quedamos con los href a otras urls
    response = requests.get(url)
    selector = Selector(response.text)
    href_links = selector.xpath('//a/@href').getall()

    #Clasificamos los enlaces en externos o locales
    baseURL = url.split("/")[2]
    return selectLocalOrExternalLinks(href_links, baseURL)





def CrawlerInsidersPages(url_principal, modo):
    """
    Función para ir haciendo el crawling a las páginas encontradas

    Los parámetros son:
        url:string:  Pagina a la que se quiere hacer el crawling de forma iterativa
        modo:string: Local o Externo para hacer crawling solo a las webs locales
                     o tambien a las externas.
    """

    linksLocales, linksExternos = getLinks(url_principal)

    print(Fore.MAGENTA + "Analizando: " +  url_principal + "\n")

    if modo == "Local":
        print(Fore.RED + "------------- Modo Local -------------")

        baseURL = url_principal.split("/")[2]
        print(*linksLocales, sep = "\n", file=open(PATH_LOCALES + "/" + baseURL + "_URL_LOCALES.txt", "a"))
        removeDuplicatedLines(PATH_LOCALES + "/" + baseURL + "_URL_LOCALES.txt")

    elif modo == "Externo":
        print(Fore.RED + "------------- Modo Externo -------------")

        baseURL = url_principal.split("/")[2]
        print(*linksExternos, sep = "\n", file=open(PATH_EXTERNAS + "/" + baseURL + "_URL_EXTERNAS.txt", "a"))
        removeDuplicatedLines(PATH_EXTERNAS + "/" + baseURL + "_URL_EXTERNAS.txt")

    else:
        print("Modo mixto, aun no funciona")




def main():
    """
    Función principal donde se comprueban los parámetros de la función y
    se ejecutan las acciones acorde a estos.

    Los parámetros son:
        -u <url> : URL (con http://) a la que se quiere hacer el crawling
        -l       : Si se quieren guardar solo los enlaces locales
        -e       : Si se quieren guardar solo los enlaces externos

    """
    ## Configuramos los parametros que se puedan usar:
    URL = ''
    modo = ''

    options, remainder = getopt.getopt(sys.argv[1:], 'u:leh',["url=","local=","externas=","help"])

    for opt, arg in options:
        if opt in ('-u', '--url'):
            URL = arg
        elif opt in ('-l', '--local'):
            modo += 'Local'
        elif opt in ('-e', '--externas'):
            modo += 'Externo'
        elif opt in ('-h', '--help'):
            print('''Los parámetros son
                -u <url> : URL (con http://) a la que se quiere hacer el crawling
                -l       : Si se quieren guardar solo los enlaces locales
                -e       : Si se quieren guardar solo los enlaces externos''')


    if(URL != ''):
        initFolders()
        CrawlerInsidersPages(URL, modo)


if __name__ == "__main__":
    print(Fore.GREEN + """
     __          __  _        _____                    _
     \ \        / / | |      / ____|                  | |
      \ \  /\  / /__| |__   | |     _ __ __ ___      _| | ___ _ __
       \ \/  \/ / _ \ '_ \  | |    | '__/ _` \ \ /\ / / |/ _ \ '__|
        \  /\  /  __/ |_) | | |____| | | (_| |\ V  V /| |  __/ |
         \/  \/ \___|_.__/   \_____|_|  \__,_| \_/\_/ |_|\___|_|


    """)

    main()
