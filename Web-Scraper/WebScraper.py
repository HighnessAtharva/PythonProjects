import sys
import re
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
'''NOTE:Arbitary Links for Reference (Only works for 1000 MCQs homepage)
https://www.sanfoundry.com/1000-python-questions-answers/

https://www.sanfoundry.com/1000-digital-image-processing-questions-answers/
'''
req = Request('https://www.sanfoundry.com/1000-fluid-mechanics-questions-answers/',
              headers={'User-Agent': 'Mozilla/5.0'})
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

'''NOTE: The Text file will be saved @ TermainlPath>output.txt so change you can cd from terminal and execute script there'''
