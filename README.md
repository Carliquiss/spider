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
The URL is given by the "-u" param: -u url (in format http://www.example.com)
  
If you want to crawl that URL for looking for local links just use the "-l" option: 
```
python spider.py -u <url>
```
You can also use the "-c" param to clear all folders and files created by the crawler 
```
python spider.py -u <url> -c
```
This also save the externasl URLs from the local links under the "URLS_externas" folder.    
  If you want to get the urls from a file just use "-i input_file":
```
python spider.py -i <input_file>
```
For all the options you can add the verbose mode with "-v"
```
python spider.py -i <input_file> -v
```
Or
```
python spider.py -u <url> -v
```
```
python spider.py -i <input_file> -cv
```


