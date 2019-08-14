import sys
sys.stdin = open('miro.txt')


def iswall(y, x, N, M):
    if y<0 or y>=M: return True
    if x < 0 or x >= N: return True
    return False


def bfs():

    queue = []

    dy = [1, 0, 0, -1]
    dx = [0, -1, 1, 0]

    queue.append((sy, sx, 0))
    data[sy][sx] = 1
    while queue:

        ny, nx, time = queue.pop(0)

        if ny == ey and nx == ex:
            return time

        for idx in range(4):
            nny = ny + dy[idx]
            nnx = nx + dx[idx]

            if not iswall(nny, nnx, N, M) and data[nny][nnx] == 0:
                queue.append((nny, nnx, time+1))
                data[nny][nnx] = 1
    return -1


N, M = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1
data = [list(map(int, input())) for _ in range(M)]

print(bfs())