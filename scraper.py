from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://baroque.pk/collections/lawn')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find('script', {'type':'text/template'})
print(nameList)