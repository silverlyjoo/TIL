import sys
sys.stdin = open('zerg.txt')


def iswall(y, x, Y, X):
    if y<0 or y>=Y: return True
    if x<0 or x>=X: return True
    return False


def bfs():

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    while queue:

        y, x = queue.pop(0)

        for idx in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]

            if not iswall(ny, nx, Y, X) and data[ny][nx] == 1:
                queue.append([ny, nx])
                data[ny][nx] = data[y][x] + 1


def chkresult():
    global live, time
    for y in range(Y):
        for x in range(X):
            if data[y][x] == 1:
                live += 1
            elif data[y][x] > time:
                time = data[y][x]

X, Y = map(int, input().split())

data = [list(map(int, input())) for _ in range(Y)]
sx, sy =  map(int, input().split())
sy -= 1
sx -= 1
queue = [[sy, sx]]
live = 0
time = 0
data[sy][sx] = 3
bfs()
chkresult()
print(time)
print(live)






