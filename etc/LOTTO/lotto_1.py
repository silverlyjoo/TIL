#로또를 만들어보자

from bs4 import BeautifulSoup
import requests
import random

numbers = random.sample(range(800, 838), 2)

for times in numbers:
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={times}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    w_number = soup.select("#article .ball_645")
    count = 0

    print(f"{times}회차 당첨번호")
    for i in w_number:
        print(i.text, end=" ")
        count += 1
        if count == 6:
            print("+", end=" ")
    print()


    # for i in soup.select(".nums"):
    #     first_num = i.select(".win .ball_645")
    #     print
    #     # result_text = f"{times}회차 당첨번호는 {first_num}이며, 보너스 번호는  입니다."
    #     for res in first_num:

    #     print(first_num)