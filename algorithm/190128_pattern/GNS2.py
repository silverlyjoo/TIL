import sys

sys.stdin = open("GNS_input.txt", "r")

T = int(input())
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
for t_case in range(T):
    N = input()
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = {}
    data = list((map(str, input().split())))
    for i in data:
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1
    print(f'#{t_case + 1}')
    for j in num_list:
        print(f'{j} '*result[j], end=' ')
    print()


    # print(f'#{t_case+1}\n{result.lstrip()}')

