
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')


for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank} 는 {name} 입니다.')
    print(tag.text)

# tag = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item')
# tag2 = tag.select_one(".ah_k")
# print(tag2)