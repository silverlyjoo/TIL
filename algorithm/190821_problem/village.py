import sys
from pprint import pprint
sys.stdin = open('village.txt')


def iswall(y, x, N):
    if y >= N or y < 0: return True
    if x >= N or x <0: return True
    return False

def bfs(st, N):
    global housecnt

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    queue = [st]

    while queue:
        sy, sx = queue.pop(0)
        housecnt += 1

        for idx in range(4):
            ny = sy + dy[idx]
            nx = sx + dx[idx]

            if iswall(ny, nx, N):
                continue
            if maps[ny][nx] == 0:
                continue
            maps[ny][nx] = 0
            queue.append((ny, nx))

N = int(input())
housecnt = 0
maps = [list(map(int, input())) for _ in range(N)]
result = []

for y in range(N):
    for x in range(N):
        if maps[y][x] == 1:
            maps[y][x] = 0
            bfs((y, x), N)
            result.append(housecnt)
            housecnt = 0
result.sort()

print(len(result))
for data in result:
    print(data)
