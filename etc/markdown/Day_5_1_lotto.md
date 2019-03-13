## Day_5_1_lotto

1. 로또 심화 1
2. 로또 심화 2

---

### 1. 로또 심화 1

[동행복권](https://dhlottery.co.kr/gameResult.do?method=byWin)

- url 을 통해 회차별 당첨번호 가져오기.

```python
import random
import requests
from bs4 import BeautifulSoup


numbers = random.sample(range(800, 838), 8)
for num in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    lucky = soup.select(".ball_645")
    print(f"{num} 회차 당첨번호")
    for i in lucky:
        print(i.text, end=" ")
        count += 1
        if count == 6:
            print("+", end=" ")
    print()
```

### 2. 로또 심화 2

```python
import random
import requests
import json
from pprint import pprint


"""
0. random 으로 로또번호를 생성합니다.
1. api 를 통해 우승 번호 번호를 가져옵니다.
2. 0 번과 1번을 비교하여 나의 등수를 알려준다.
--------
1. url 요청 보내서 정보를 가져옵니다.
    - json 으로 받는다. (딕셔너리로 접근 가능)
2. api 의 당첨번호와 보너스 번호를 저장하고.
3. 뽑은게 몇등인지, 몇번만에 당첨된건지 하는거 뽑으세요.
"""

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1, 7):
    winner.append(lotto[f"drwtNo{i}"])

bonus = lotto["bnusNo"]

count = 0
while True:
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))

    if matched == 6:
        print("1등")
        # print(count, "번만에 당청되셨습니다.")
        # money = format(count*1000, ',')
        # print("쓴 돈은", money)
        break
    elif matched == 5 and bonus in my_numbers:
        print("2등")
    elif matched == 5:
        print("3등")
    elif matched == 4:
        print("4등")
    elif matched == 3:
        print("5등")
    else:
        print("응 안돼")
        
print("이번 주 당첨번호: " + str(winner))
print("보너스 번호: " + str(bonus))
print("내 번호: " + str(my_numbers))
```

> 원화로 표기하기(₩)
>
> ```python
> money = format(금액, ',')
> ```