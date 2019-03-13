import sys
sys.stdin = open("view_input.txt")

T = 1
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0
    for num in range(2, len(data)-2):
        data_num = sorted([data[num-2], data[num-1], data[num], data[num+1], data[num+2]])
        print(data_num)
        if data[num] == data_num[-1]:
            result += data[num]-data_num[-2]
    print("#{} {}".format(tc+1, result))