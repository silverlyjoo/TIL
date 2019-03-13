
# 자연수 입력하면 입력한 자연수까지 출력되는 문제

# 정답
item = int(input("번호를 입력하세요 : "))
for i in range(1,item+1):
    print(i)

# 투자 경고 종목 리스트가 있을 때

# warn_inv_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
# item = input('투자 종목이 무엇입니까? : ')

# if item.lower() in warn_inv_list:
#     print('투자 경고 종목입니다')
# else:
#     print('투자 경고 종목이 아닙니다')

# 0,4,5번째 요소 지우기

# colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

# fruit = []

# for i in range(len(colors)):
#     if i in [0, 4, 5]:
#         pass
#     else:
#         colors2.append(colors[i])
# print(colors2)


# colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
# fruit = []
# deleteindex = [0, 4, 5]

# for i in range(0, len(colors)):
#     if i not in deleteindext:
#         fruit.append(colors[i])

# print(fruit)


# ssafy = {
#     "location": ["서울", "대전", "구미", "광주"],
#     "language": {
#         "python": {
#             "frameworks": {
#                 "flask": "micro",
#                 "django": "full-functioning"
#             },
#             "data_science": ["numpy", "pandas", "scipy", "sklearn"]
#         }
#     },
#     "duration": {
#         "semester1": "6월까지"
#     },
#     "classes": {
#         "seoul":  {
#             "lecturer": "john",
#             "manager": "pro",
#         },
#         "daejeon":  {
#             "lecturer": "tak",
#             "manager": "yoon",
#         }
#     }
# }

# #ssafy의 semester1의 기간을 출력하세요
# #ssafy dictionary 안에 들어있는 '대전'을 출력하세요
# #daejeon의 매니저의 이름을 출력하세요

# print(ssafy["duration"]["semester1"])

# print(ssafy["location"][1])
# print(ssafy["location"][ssafy["location"].index('대전')])

# print(ssafy["classes"]["daejeon"]["manager"])

