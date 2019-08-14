import random
import requests
import json
from pprint import pprint

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

#당첨될때까지 몇번을 뽑아야하는가

lot_lst = []
bo_lst = []
numbers = [1, 2, 3, 4, 5, 6]
b_num = lotto.get("bnusNo")
for i in numbers:
    to_lst = lotto.get(f"drwtNo{i}")
    lot_lst.append(to_lst)
bo_lst.append(b_num)

#리스트 세트화
l_list_set = set(lot_lst)
bo_list_set = set(bo_lst)

#나만의 숫자 
my_num = sorted(random.sample(range(1, 46), 6))
my_list_set = set(my_num)

#당첨과정

lotto_result = 0
inter_lotto = set()
count = 0

while  lotto_result < 6:
    my_num = sorted(random.sample(range(1, 46), 6))
    my_list_set = set(my_num)
    inter_lotto = l_list_set & my_list_set
    lotto_result = len(inter_lotto)
    count += 1

    if lotto_result <= 2:
        print(f"결과는 꽝입니다{my_num}")
    elif lotto_result == 3:
        print(f"결과는 5등입니다{my_num}")
    elif lotto_result == 4:
        print(f"결과는 4등입니다{my_num}")
    elif lotto_result == 5:
        if b_num in my_list_set:
            print(f"결과는 2등입니다{my_num}")
        else:
            print(f"결과는 3등입니다{my_num}")
    else:
        print(f"결과는 1등입니다{my_num}")

    print(count)