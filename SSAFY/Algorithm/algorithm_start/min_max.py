import sys
sys.stdin = open("min_max_input.txt")

#메소드 비사용
T = int(input())
for i in range(T):
    N = int(input())
    numbers = (list(map(int,input().split())))
    max_num = 0
    min_num = 1000001
    for j in numbers:
        if j>max_num:
            max_num = j
    for k in numbers:
        if k<min_num:
            min_num = k
    print(f'#{i+1} {max_num-min_num}')

# 메소드 사용
# T = int(input())
# for i in range(T):
#     N = int(input())
#     numbers = sorted(list(map(int,input().split())))
#     diff = numbers[-1]-numbers[0]
#     print(f'#{i+1} {diff}')