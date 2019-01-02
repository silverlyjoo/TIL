#3

# scores = {
#     "국어" : 87,
#     "영어" : 92,
#     "수학" : 40
# }

# for key, value in scores.items():
#     print(key)
#     print(value)

# print(scores.items())


#도시중 3일중에 가장 추웠던 곳, 가장 더웠던 곳은?

cities = {
    "서울" : [-6, -10, 5],
    "대전" : [-3, -5, 2],
    "광주" : [0, -2, 10],
    "부산" : [2, -2, -9],
}

#강사님 정답

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        #최저 온도가 cold보다 더 추우면, cold에 넣고
        if min(temp) < cold:
                cold = min(temp)
                cold_city = name
        if max(temp) > hot:
                hot = max(temp)
                hot_city = name
    count += 1

print(f"{hot_city}, {hot}, {cold_city}, {cold}")
print(count)


coldest_temp = 100
hotest_temp = -100
coldest_name = ""
hotest_name = ""
for name, temp in cities.items():
    min_temp = min(temp)
    max_temp = max(temp)
    if min_temp < coldest_temp:
        coldest_temp = min_temp
        coldest_name = name
    else:
        pass
    if max_temp > hotest_temp:
        hotest_temp = max_temp
        hotest_name = name
    else:
        pass


print(f"3일중 가장 추운 지역은 {coldest_name}이며 섭씨 {coldest_temp}도 입니다.")
print(f"3일중 가장 추운 지역은 {hotest_name}이며 섭씨 {hotest_temp}도 입니다.")




# # 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
# cities = {
#     "서울": [-6, -10, 5],
#     "대전": [-3, -5, 2],
#     "광주": [0, -2, 10],
#     "부산": [2, -2, 9]
# }

# hot = 0
# cold = 0
# hot_city = ""
# cold_city = ""
# count = 0

# for name, temp in cities.items():
#     # name = "서울"
#     # temp = [-6, -10, 5]
#     if count == 0:
#         hot = max(temp)
#         cold = min(temp)
#         hot_city = name
#         cold_city = name
#     else:
#         # 최저 온도가  cold 보다 더 추우면, cold  에 넣고
#         if min(temp) < cold:
#             cold = min(temp)
#             cold_city = name
#         # 최고 온도가 hot 보다 더 더우면, hot  에 넣고
#         if max(temp) > hot:
#             hot = max(temp)
#             hot_city = name
#     count += 1

# print(f"{hot_city}, {cold_city}")











# # ref 값 : 3-서울 2-대전 1-광주 0-부산

# coldest_temp = 100
# hotest_temp = -100
# ref_lst = ["부산", "광주", "대전", "서울"]
# ref_c = 0
# ref_h = 0
# for name, temp in cities.items():
#     min_temp = min(temp)
#     max_temp = max(temp)
#     if min_temp < coldest_temp:
#         coldest_temp = min_temp
#         ref_c = 0
#     else:
#         ref_c += 1
#     if max_temp > hotest_temp:
#         hotest_temp = max_temp
#         ref_h = 0
#     else:
#         ref_h += 1

# coldest_name = ref_lst[ref_c]
# hotest_name = ref_lst[ref_h]

# print(f"3일중 가장 추운 지역은 {coldest_name}이며 섭씨 {coldest_temp}도 입니다.")
# print(f"3일중 가장 추운 지역은 {hotest_name}이며 섭씨 {hotest_temp}도 입니다.")

# print(f"ref {ref}")
# print(f"dif {dif}")

# dif = 100
# for name, temp in cities.items():
#     ref = 0
#     change = 0
#     a = min(temp)
#     if a > dif:
#         ref += 1
#     else:
#         dif = a
#         change = change + 1 + ref
        
        



    # dif = min(temp)
    # print(temp)

    # for coldest in temp:
    #     a = min(coldest_t)

