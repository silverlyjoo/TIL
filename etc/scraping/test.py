
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')
search = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")

print(search)