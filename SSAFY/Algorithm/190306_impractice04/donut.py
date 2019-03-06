import sys
sys.stdin = open('donut.txt')


def donut(x, y, k):
    nums = []
    for i in range(0, k):
        nums.append(L[y][x+i])
        nums.append(L[y+k-1][x+i])
    for j in range(1, k-1):
        nums.append(L[y+j][x])
        nums.append(L[y+j][x+k-1])
    return sum(nums)

N, K = map(int, input().split())

L = [list(map(int, input().split())) for _ in range(N)]
result = []
for i in range(0, N-K+1):
    for j in range(0, N-K+1):
        result.append(donut(j, i, K))
print(max(result))