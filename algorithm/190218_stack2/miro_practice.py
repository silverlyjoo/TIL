import sys
sys.stdin = open('miro_input.txt')


def iswall(y, x, N):
    if x < 0 or x>= N: return True
    if y < 0 or y>= N: return True
    return False

def findstart(N):
    for i in range(N):
        for j in range(N):
            if L[i][j] == 2:
                return (i,j)

def go(x, y, N):
    global result
    L[y][x] = 9
        


    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not iswall(nx, ny, N) and L[ny][nx] == 3:
            result = 1
            return
        elif not iswall(nx, ny, N) and L[ny][nx] == 0:
            go(nx, ny, N)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 0
    L = [list(map(int, input())) for _ in range(N)]
    y, x = findstart(N)
    go(x, y, N)
    print('#{} {}'.format(tc, result))

