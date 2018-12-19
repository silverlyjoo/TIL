#op.gg 를 가져오자

import requests
from bs4 import BeautifulSoup

username = str(input("닉네임을 입력하세요 : "))

url = f"http://www.op.gg/summoner/userName={username}"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

if username is not False:
    print(soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierRank > span').text)
else:
    pass

# print(soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierRank > span').text)

#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierRank > span
# req = requests.get(url).text