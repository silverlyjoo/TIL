import sys
from pprint import pprint
sys.stdin = open('robot.txt')


def iswall(x, y, N):
    if x < 0 or x >= N: return True
    if y < 0 or y >= N: return True
    if L[y][x] == 1: return True
    return False


def end(x, y):
    if L[y][x] == 2:
        return True


N = int(input())
L = [list(map(int, input())) for _ in range(N)]
go = list(map(int, input().split()))


dx = [0, 0, -1, 0, 1]
dy = [0, 1, 0, -1, 0]

x, y = 0, 0
cnt = 0
L[x][y] = 2
idx = 0

while True:
    x += dx[go[idx%4]]
    y += dy[go[idx%4]]
    if not iswall(x, y, N):
        if end(x, y):
            break
        cnt += 1
        L[y][x] = 2
    else:
        x -= dx[go[idx%4]]
        y -= dy[go[idx%4]]
        idx += 1

print(cnt)

