import sys
from pprint import pprint
sys.stdin = open('hunter.txt')


def iswall(x, y, N):
    if x < 0 or x >= N: return True
    if y < 0 or y >= N: return True
    if L[y][x] == 0 or L[y][x] == 1: return True
    return False


def rabbit(x, y, N):
    cnt = 0
    idx = 0

    nx, ny = x, y
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    while idx < 8:
        nx += dx[idx]
        ny += dy[idx]
        if not iswall(nx, ny, N):
            if L[ny][nx] == 2:
                cnt += 1
                L[ny][nx] = 3
        else:
            nx, ny = x, y
            idx += 1

    return cnt

result = 0
N = int(input())
L = [list(map(int, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            result += rabbit(j, i, N)
print(result)




# print(L)
