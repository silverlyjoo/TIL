import sys
from pprint import pprint
sys.stdin = open("miro_input.txt")

def iswall(nx, ny, E):
    if nx < 0 or nx > E-1 : return False
    if ny < 0 or ny > E-1 : return False
    return True

def isgil(L, x, y, E):
    L[y][x] = '9'
    global result
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if iswall(nx, ny, E) and L[ny][nx] == '2':
            result = 1
            return
        elif iswall(nx, ny, E) and L[ny][nx] == '0':
            isgil(L, nx, ny, E)

T = int(input())
for N in range(1, T+1):
    E = int(input())
    L = [list(input()) for i in range(E)]
    result = 0
    # 시작점 찾기
    for fdx, fval in enumerate(L):
        for idx, val in enumerate(fval):
            if val == '3':
                x, y = idx, fdx
    isgil(L, x, y, E)
    print(f'#{N} {result}')