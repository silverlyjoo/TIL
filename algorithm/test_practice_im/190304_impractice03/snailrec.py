import sys
from pprint import pprint
sys.stdin = open('snailrec.txt')


def iswall(x, y, n):
    if x < 0 or x >= n: return False
    if y < 0 or y >= n: return False
    if L[y][x] != 0 : return False
    return True


n = int(input())

L = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
idx = 0
val = 1

while val<=n*n:
    if iswall(x, y, n):
        L[y][x] = val
        val += 1
    else:
        x -= dx[idx]
        y -= dy[idx]
        idx = (idx + 1) %4
    x += dx[idx]
    y += dy[idx]

for i in L:
    print(*i)
