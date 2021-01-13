#import requests
import sys
import re
import urllib.request
from bs4 import BeautifulSoup
#from urllib import urlopen
import re
from urllib.request import Request, urlopen

req = Request('https://www.sanfoundry.com/operating-system-questions-answers/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read()
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    x = re.search("-answers-", str(link))
    if x:
        links.append(link.get('href'))
    
for link in links:
    with open("output.txt", "a") as f:
         
        print(link, file=f)
        print('\n', file=f)

'''NOTE: The Text file will be saved @ Users>Your_Username>output.txt'''