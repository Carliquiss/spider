# Web Crawler (⚠️Under construction⚠️)
_Web crawler to look for local or external links from an especified URL_


## How does it works ⚙️
The crawler gets and URL especified by the user and starts to looks for the links in that page by the "href" tag. Once it has all the links, it clasifies them as Local or External to the main url given. Then, the crawler takes all those URLs and repeats the process getting all the URLs related to the main one.  
  
The URLs are saved on two folders:
  * URLS_locales: Where all the local links are saved in "url_.txt" file
  * URLS_externas: Where all the external links are saved in "url_.txt" file
  
## Installing 🔧
First clone the repo: 
```
git clone https://github.com/Carliquiss/spider
```
Then run the following command to install needed libs:
```
pip install -r requirements.txt
```

## Usage ⌨️
The URL is givem by the "-u" param: -u url (in format http://www.example.com)
  
If you want to crawl that URL for looking for local links just use the "-l" option: 
```
python spider.py -u <url> -l
```
You can also use the "-c" param to clear all folders and files created by the crawler 
```
python spider.py -u <url> -l -c
```
 Or
```
python spider.py -u <url> -lc
```
