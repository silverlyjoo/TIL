import sys
from pprint import pprint
sys.stdin = open('hosu.txt')


def go(x, y):
    cnt = 0
    while True:
        u = y + cnt
        d = y - cnt
        l = x - cnt
        r = x + cnt
        if L[u][x] == 0 or L[d][x] == 0 or L[y][l] == 0 or L[y][r] == 0:
            return cnt
        cnt += 1

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            result += go(j, i)
print(result)

