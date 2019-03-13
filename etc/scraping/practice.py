#내가 해낸다

import requests
from bs4 import BeautifulSoup

url = "http://finance.daum.net/domestic/kospi/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

kospi =  soup.select(".boxDashboard > div.currentStk > div.currentStk > span.numB > strong")
print(kospi)