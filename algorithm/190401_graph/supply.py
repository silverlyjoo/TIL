import sys
sys.stdin = open('supply.txt')


def iswall(y, x, N):
    if y < 0 or y >= N: return True
    if x < 0 or x >= N: return True
    return False


def full(N):

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    queue = [[0,0]]

    D[0][0] = 0

    while queue:

        y, x = queue.pop(0)

        

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]
            
            if not iswall(ny, nx, N) and D[ny][nx] > data[ny][nx] + D[y][x]:
                queue.append([ny, nx])
                D[ny][nx] = data[ny][nx] + D[y][x]


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    data = [list(map(int, input())) for _ in range(N)]

    D = [[0xffffff for _ in range(N)] for _ in range(N)]
    full(N)

    print('#{} {}'.format(tc, D[N-1][N-1]))

    
