#2nd. quiz with scraping

import requests
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/sise/siseList.nhn?menu=market_sum&sosok=0"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')


# for i in 
#     for i in soup.select('#content > div > div.ct_box.major_index._index_wrapper > ul .stock_item'):



#     for i in soup.select('#content > div > div.ct_box.major_index._index_wrapper > ul .stock_price'):

for i in soup.select('#content > div > div.ct_box.major_index._index_wrapper > ul'):
    item = i.select(" .stock_item")
    price = i.select(" .stock_price")
    # print(f"{item}의 현재 수치는 {price}입니다.")
    # print(item)

for t in item:
    print(t.text)



# print(soup.select("#content > div > div.ct_box.major_index._index_wrapper > ul"))