import sys
sys.stdin = open('miro_bomb.txt')


def iswall(y, x):
    if y < 0 or y >= Y: return True
    if x < 0 or x >= X: return True
    if maps[y][x] == 1: return True
    return False


def escape():
    global result
    que = [[sy, sx, 3, 0]]
    visit[3][sy][sx] = 1

    while que:
        y, x, bomb, turn = que.pop(0)

        for i in range(4):

            ny, nx = y + dy[i], x + dx[i]

            if iswall(ny, nx): continue
            if visit[bomb][ny][nx]: continue

            if maps[ny][nx] == 4:
                result = turn + 1
                return

            if maps[ny][nx] == 0:
                que.append([ny, nx, bomb, turn+1])
                visit[bomb][ny][nx] = 1

            if maps[ny][nx] == 2 and bomb:
                que.append([ny, nx, bomb-1, turn+1])
                visit[bomb-1][ny][nx] = 1



Y, X = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(Y)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for y in range(Y):
    for x in range(X):
        if maps[y][x] == 3:
            sy, sx = y, x
        if maps[y][x] == 4:
            ey, ex = y, x

visit = [[[0 for _ in range(X)] for _ in range(Y)] for _ in range(4)]
result = -1
escape()
print(result)



