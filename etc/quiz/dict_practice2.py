#반 평균 구하기

scores = {
    "철수" : {
        "수학" : 80,
        "국어" : 90,
        "음악" : 100
    },
    "영희" : {
        "수학" : 70,
        "국어" : 60,
        "음악" : 50
    }
}
# print(scores.values())


#강사님 풀이 

total_score = 0
count = 0
for score_t in scores.values():
    for score_i in score_t.values():
        total_score += score_i
        count += 1
ave = total_score/count
print(ave)


# #두번째 풀이 

# total_score = 0
# for score_t in scores.values():

#     total = 0
#     for score_i in score_t.values():
#         total += score_i
#         ave_i = total/len(score_t)
    
#     total_score += ave_i
#     ave = total_score/len(scores)

# print(ave)


# #첫번째 풀이 

# c_scores = scores["철수"]
# y_scores = scores["영희"]

# total_score = 0
# for score_t in scores.values():

#     total_c = 0
#     for score_c in c_scores.values():
#         total_c += score_c
#         ave_c = total_c/len(scores["철수"])

#     total_y = 0
#     for score_y in y_scores.values():
#         total_y += score_y
#         ave_y = total_y/len(scores["영희"])
    
#     total_score = total_score + ave_c + ave_y

# print(total_score/len(scores))




# print(ave_c)
# print(ave_y)
# print(range(len(scores)))
