import sys
sys.stdin = open('jangis.txt')


def iswall(y, x):
    if y < 0 or y >= Y: return True
    if x < 0 or x >= X: return True
    return False


def bfs(sy, sx, ey, ex):

    queue = [(sy, sx, 0)]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]

    while queue:
        y, x, turn = queue.pop(0)
        for idx in range(8):
            ny = y + dy[idx]
            nx = x + dx[idx]
            if not iswall(ny, nx):
                if data[ny][nx] == 2:
                    return turn + 1
                elif data[ny][nx] == 0:
                    queue.append((ny, nx, turn + 1))
                    data[ny][nx] = 1

Y, X = map(int, input().split())
sy, sx, ey, ex = map(lambda x:int(x)-1, input().split())

data = [[0 for _ in range(X)] for _ in range(Y)]
data[ey][ex] = 2
print(bfs(sy, sx, ey, ex))

