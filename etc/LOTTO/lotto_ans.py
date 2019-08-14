#강사 선생님 해답

import random
import requests
import json
from pprint import pprint

"""
0.  random 으로 로또 번호를 생성합니다.
1. api  를 통해 우승 번호를 가져옵니다.
0 번과 1번을 비교하여 나의 등수를 알려준다
---------------

1. url 요청 보내서 정보를 가져옵니다
  - json으로 받는다 (딕셔너리로 접근가능)
2. api의 당첨번호와 보너스 번호를 저장하고.
3. 뽑은게 몇등인지 

"""

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1, 7):
    winner.append(lotto[f"drwtNo{i}"])

bonus = lotto["bnusNo"]
print(f"이번 주 당첨번호 : {winner}")
print("보너스번호: " + str(bonus))
count = 0
while True:
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))
    print(count, end=" ")
    if matched == 6:
        print("1st", end= " ")
        money = format(count*1000, ',')
        print("쓴 돈은", money, end= " ")
        print(count, "번만에 당첨되셨습니다", end= " ")
        break
    elif matched == 5:
        if bonus in my_numbers:
            print("2nd")
        else:
            print("3rd")
    elif matched == 4:
        print("4th")
    elif matched == 3:
        print("5th")
        
    else:
        print("damn it!")