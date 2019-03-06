import sys
from pprint import pprint
sys.stdin = open('bead.txt')


def findstart(C, R):
    for i in range(C):
        for j in range(R):
            if L[i][j] == 2:
                return i, j


def iswall(x, y, R, C):
    if x < 0 or x >= R: return True
    if y < 0 or y >= C: return True
    if L[y][x] == 1: return True
    return False


def bead(x, y, go, R, C):

    dx = [0, 0, 0, -1, 1]
    dy = [0, -1, 1, 0, 0]

    nx, ny = x, y
    for i in go:

        nx = nx + dx[i]
        ny = ny + dy[i]

        while not iswall(nx, ny, R, C):

            L[ny][nx] = 2
            nx = nx + dx[i]
            ny = ny + dy[i]

        nx = nx - dx[i]
        ny = ny - dy[i]












R, C = map(int, input().split())
L = [list(map(int, input())) for _ in range(C)]

N = int(input())
go = list(map(int, input().split()))


y, x = findstart(C, R)


bead(x, y, go, R, C)
cnt = 0
for i in range(C):
    for j in range(R):
        if L[i][j] == 2:
            cnt += 1
print(cnt)
