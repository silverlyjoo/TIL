import sys
from pprint import pprint
sys.stdin = open('village.txt')


def findstart(N):
    global vilcnt
    for yi in range(N):
        for xi in range(N):
            if maps[yi][xi] == 1:
                vilcnt += 1
                return (yi, xi)
    return False

def iswall(y, x, N):
    if 0<= y < N or 0<= x < N:
        return False
    return True

def dfs(st, N):
    
    global result, housecnt
    sy, sx = st
    housecnt += 1
    print('hc', housecnt)
    maps[sy][sx] = 0

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    for idx in range(4):
        ny, nx = sy + dy[idx], sx + dx[idx]

        if iswall(ny, nx, N) or maps[ny][nx] == 0:
            continue

        if maps[ny][nx] == 1:
            dfs((ny, nx), N)
    

N = int(input())

maps = [list(map(int, input())) for _ in range(N)]
result = []
vilcnt = 0
housecnt = 0

# pprint(maps)

a = findstart(N)

while a:
    dfs(a, N)
    pprint(maps)
    result.append(housecnt)
    housecnt = 0
    a = findstart(N)
    print(vilcnt)

print(vilcnt)
print(result)
