# Scraping

import requests
from bs4 import BeautifulSoup

# print(requests.get("https://www.naver.com"))
# print(requests.get("https://www.naver.com").text)
# print(requests.get("https://www.naver.com").status_code)

# req = requests.get("https://finance.naver.com/sise/").text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#KOSPI_now")

# print(kospi.text)

# req = requests.get("https://search.daum.net/search?w=tot&DA=Z8T&q=%EB%8C%80%EC%A0%84%20%EC%98%A4%EB%8A%98%20%EB%82%A0%EC%94%A8&rtmaxcoll=Z8T").text
# soup = BeautifulSoup(req, 'html.parser')
# weather = soup.select_one("#weatherColl > div.coll_cont > div > div.wrap_region.today > div.cont_weather > div.cont_today > div.info_temp > div > span > span.desc_temp > strong")
# print(weather.text)


#failed case
# req = requests.get("http://finance.daum.net/domestic/kospi").text
# soup = BeautifulSoup(req, 'html.parser')
# weather = soup.select_one("#boxDashboard > div.currentStk > div > span.numB_down > strong")
# print(weather)

#real-time searched list
# req = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# weather = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")
# print(weather.text)


# req = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# weather = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")

req = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')
search = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")


# i = search.select_one(search)
print(search)




# for i in search:
#     i.select_one("")
#     print(i.text)

# print()