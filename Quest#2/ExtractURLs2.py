from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

page = urlopen('http://www.xkcd.com/')
soup = BeautifulSoup(page, 'lxml')

for link in soup.findAll('a', attrs={'href': re.compile('^http://')}):
    print(link.get('href'))

print('SUCCESS!')