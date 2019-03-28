import sys
sys.stdin = open('home.txt')


def iswall(y, x, N):
    if y<0 or y >= N: return True
    if x < 0 or x >= N: return True
    return False

def bfs(sy, sx, N):

    queue = [[sy, sx]]
    data[sy][sx] = 2
    cnt = 1

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    while queue:

        y, x = queue.pop(0)
        for idx in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]

            if not iswall(ny, nx, N) and data[ny][nx] == 1:
                queue.append([ny, nx])
                data[ny][nx] = 2
                cnt += 1
    result.append(cnt)

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
result = []

for y in range(N):
    for x in range(N):
        if data[y][x] == 1:
            bfs(y, x, N)
result.sort()
print(len(result))
for i in result:
    print(i)