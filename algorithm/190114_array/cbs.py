import sys
sys.stdin = open("cbs_input.txt")


T = int(input())

for times in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    score_dict = {}

    for score in scores:
        if score in score_dict:
            score_dict[score] += 1
        else:
            score_dict[score] = 1

    less_score = 0
    less_times = 0

    for key, value in score_dict.items():
        if less_times <= value:
            if less_times < value:
                less_score = key
                less_times = value
            elif less_score < key:
                less_score = key

    print(f'#{times+1} {less_score}')