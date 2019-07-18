# Web Crawler
_Web crawler to look for local or external links from an especified URL_



## Installing - Instalación 🚀
Run the following command to install needed libs:
```
pip install -r requirements.txt
```

## Usage ⚙️
The URL is givem by the -u param: -u <url>  
If you want to crawl that URL for looking for local links just use the "-l" option: 
```
python spider.py -u <url> -l
```
You can also use the "-c" param to clear all folders and files created by the crawler 
```
python spider.py -u <url> -l
```
 Or
```
python spider.py -u <url> -lc
```
