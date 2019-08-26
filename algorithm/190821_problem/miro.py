import sys
sys.stdin = open('miro.txt')


def iswall(y, x, N, M):
    if y>=N or y<0: return True
    if x>=M or x<0: return True
    if data[y][x] == 0: return True
    return False

def bfs(N, M):


    ey, ex = N-1, M-1

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    data[0][0] = 0
    queue = [(0, 0, 1)]

    while queue:
        sy, sx, val = queue.pop(0)

        for idx in range(4):
            ny = sy + dy[idx]
            nx = sx + dx[idx]

            if iswall(ny, nx, N, M):
                continue
            if ny == ey and nx == ex:
                return val+1
            data[ny][nx] = 0
            queue.append((ny, nx, val+1))











N, M = map(int, input().split())

data = [list(map(int, input())) for _ in range(N)]

print(bfs(N, M))
