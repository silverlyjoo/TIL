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

{
  "totSellamnt": 76614176000,
  "returnValue": "success",
  "drwNoDate": "2018-12-15",
  "firstWinamnt": 3144449125,
  "drwtNo6": 45,
  "drwtNo4": 30,
  "firstPrzwnerCo": 6,
  "drwtNo5": 33,
  "bnusNo": 6,
  "firstAccumamnt": 18866694750,
  "drwNo": 837,
  "drwtNo2": 25,
  "drwtNo3": 28,
  "drwtNo1": 2
}

# # 837회 로또 숫자 가져오기

# #로또 당첨숫자와 보너스숫자 리트스 생성
# lot_lst = []
# bo_lst = []
# numbers = [1, 2, 3, 4, 5, 6]
# b_num = lotto.get("bnusNo")
# for i in numbers:
#     to_lst = lotto.get(f"drwtNo{i}")
#     lot_lst.append(to_lst)
# bo_lst.append(b_num)

# #리스트 세트화
# l_list_set = set(lot_lst)
# bo_list_set = set(bo_lst)

# #나만의 숫자 
# my_num = sorted(random.sample(range(1, 46), 6))
# my_list_set = set(my_num)

# #당첨과정
# inter_lotto = l_list_set & my_list_set
# lotto_result = len(inter_lotto)

# # # 당첨번호 확인
# if lotto_result <= 2:
#     print(f"당신의 번호는 {my_num}이며, 결과는 꽝입니다")
# elif lotto_result == 3:
#     print(f"당신의 번호는 {my_num}이며, 결과는 5등입니다")
# elif lotto_result == 4:
#     print(f"당신의 번호는 {my_num}이며, 결과는 4등입니다")
# elif lotto_result == 5:
#     if b_num in my_list_set:
#         print(f"당신의 번호는 {my_num}이며, 결과는 2등입니다")
#     else:
#         print(f"당신의 번호는 {my_num}이며, 결과는 3등입니다")
# else:
#     print(f"당신의 번호는 {my_num}이며, 결과는 1등입니다")



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