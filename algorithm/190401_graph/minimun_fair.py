import sys
sys.stdin = open('minimun_fair.txt')


def iswall(y, x):
    if y < 0 or y >= N: return True
    if x < 0 or x >= N: return True
    return False


def fair():

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    queue = [[0, 0]]

    D[0][0] = 0

    while queue:

        y, x = queue.pop(0)

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if not iswall(ny, nx):

                if H[y][x] < H[ny][nx]:
                    if D[ny][nx] > D[y][x] + (H[ny][nx] - H[y][x]) + 1:
                        D[ny][nx] = D[y][x] + (H[ny][nx] - H[y][x]) + 1
                        queue.append([ny, nx])
                else:
                    if D[ny][nx] > D[y][x] + 1:
                        D[ny][nx] = D[y][x] + 1
                        queue.append([ny, nx])



T = int(input())


for tc in range(1, T+1):

    N = int(input())

    H = [list(map(int, input().split())) for _ in range(N)]
    D = [[0xfffff for _ in range(N)] for _ in range(N)]
    fair()
    print('#{} {}'.format(tc, D[N-1][N-1]))



