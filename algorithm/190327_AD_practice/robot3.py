import sys
sys.stdin = open('robot2.txt')


def iswall(y, x):
    if y < 0 or y >= Y: return True
    if x < 0 or x >= X: return True
    if maps[y][x] == 1: return True
    return False


def robot(sy, sx, sdir, ey, ex, edir):
    global result
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    turns = [[2, 3], [2, 3], [0, 1], [0, 1]]

    que = [[sy, sx, sdir, 0]]
    # visit = [[sy, sx, sdir]]
    visit[sy][sx][sdir] = 1

    while que:

        y, x, ddir, turn = que.pop(0)
        if y == ey and x == ex and ddir == edir:
            result = turn
            return

        for idx1 in range(1, 4):

            ny = y + dy[ddir]*idx1
            nx = x + dx[ddir]*idx1

            if iswall(ny, nx):
                break

            if not iswall(ny, nx) and not visit[ny][nx][ddir]:
                que.append([ny, nx, ddir, turn+1])
                visit[ny][nx][ddir] = 1
        
        if not visit[y][x][turns[ddir][0]]:
            que.append([y, x, turns[ddir][0], turn+1])
            visit[y][x][turns[ddir][0]] = 1
        if not visit[y][x][turns[ddir][1]]:
            que.append([y, x, turns[ddir][1], turn+1])
            visit[y][x][turns[ddir][1]] = 1
        

Y, X = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(Y)]

sy, sx, sdir = map(lambda x:int(x)-1, input().split())
ey, ex, edir = map(lambda x:int(x)-1, input().split())
visit = [[[0 for _ in range(4)] for _ in range(X)] for _ in range(Y)]
result = 0
robot(sy, sx, sdir, ey, ex, edir)
print(result)
