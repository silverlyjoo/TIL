import sys
sys.stdin = open("range_sum_input.txt")

T = int(input())

for times in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_list = [0]*(len(num_list)-M+1)
    sum_result = 0
    for i in range(len(num_list)-M+1):
        for j in range(i, M+i):
            sum_result = sum_result + num_list[j]
        sum_list [i]= sum_result
        sum_result = 0

    max_num = 0
    min_num = 10001 * M

    for num in sum_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f'#{times+1} {max_num-min_num}')
