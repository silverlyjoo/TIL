import sys
sys.stdin = open('wall.txt')
from pprint import pprint


def iswall(y, x, N, M):
    if y >= N or y < 0: return True
    if x >= M or x < 0: return True
    return False


def bfs(N, M):

    global result

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    queue = [(0, 0, 1, 1)]

    if N == 1 and M == 1:
        result.append(2)
        return

    while queue:
        sy, sx, bomb, val = queue.pop(0)

        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]

            if ny == N-1 and nx == M-1:
                result.append(val+1)
                continue

            if iswall(ny, nx, N, M):
                continue

            if bomb == 0: # 폭탄이 없을때

                if data[ny][nx] == 1:
                    continue

                if visit[bomb][ny][nx] <= val+1:
                    continue

                queue.append((ny, nx, bomb, val+1))
                visit[bomb][ny][nx] = val+1

            else: # 폭탄이 있을때

                if data[ny][nx] == 1: # 가려는곳이 벽일때

                    if visit[bomb-1][ny][nx] <= val+1:
                        continue

                    queue.append((ny, nx, bomb-1, val+1))
                    visit[bomb-1][ny][nx] = val+1
                else:
                    if visit[bomb][ny][nx] <= val +1:
                        continue

                    queue.append((ny, nx, bomb, val + 1))
                    visit[bomb][ny][nx] = val + 1


N, M = map(int, input().split())

data = [list(map(int, input())) for _ in range(N)]
visit = [[[float('inf') for _ in range(M)] for _ in range(N)] for _ in range(2)]
result = []
bfs(N, M)

result.sort()
if result:
    print(result[0])
else:
    print(-1)

