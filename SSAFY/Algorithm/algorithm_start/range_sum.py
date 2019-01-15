import sys
sys.stdin = open("range_sum_input.txt")

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list_min = num_list[:]
    max_list = [0]*M
    min_list = [0]*M
    max_count = (0, 0) #숫자, 인덱스
    min_count = (10001, 0)

    # num_list[0] = 1000000
    # print(num_list_min)

    for k in range(M):
        for j in range(len(num_list)):
            if num_list[j] > max_count[0]:
                max_count = (num_list[j], j)
        num_list[max_count[1]]=0
        max_list[k] = max_count[0]
        max_count = 0, 0

    for min_range in range(M):
        for min_num in range(len(num_list_min)):
            if num_list_min[min_num] < min_count[0]:
                min_count = (num_list_min[min_num], min_num)
        num_list_min[min_count[1]]=10001
        min_list[min_range] = min_count[0]
        min_count = 10001, 0

    result_max = 0
    result_min = 0

    for sum_max in max_list:
        result_max += sum_max
    for sum_min in min_list:
        result_min += sum_min

    # print(N, M)
    # print(num_list)
    print(result_max)
    print(result_min)