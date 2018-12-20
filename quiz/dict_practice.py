'''
파이썬 dictionary 활용 기초!
'''

#평균 구하기

scores = {
    "국어" : 87,
    "영어" : 92,
    "수학" : 40
}

# print(type(score.values()))

##sum 활용
# s_value = score.values()
# average = sum(s_value)/len(s_value)
# print(int(average))


#for 구문 및 빈 변수 생성 활용
s_value = scores.values()
score = 0
for i in s_value:
    score += i
    #score = score + i
# print(val/len(s_value))

ave_score = score / len(scores)
print(ave_score)


#3

scores = {
    "국어" : 87,
    "영어" : 92,
    "수학" : 40
}

for key, value in scores.items():
    print(key)
    print(value)