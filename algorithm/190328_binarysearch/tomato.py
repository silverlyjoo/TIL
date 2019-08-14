import sys
sys.stdin = open('tomato.txt')


def iswall(Y, X, y, x):
    if y<0 or y>= Y: return True
    if x<0 or x>= X: return True
    return False


def findstart(Y, X):
    global zero
    for y in range(Y):
        for x in range(X):
            if data[y][x] == 1:
                queue.append([y, x])
            if data[y][x] == 0:
                zero += 1

def bfs():
    global zero, maxday
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    while queue:
        ey, ex = queue.pop(0)
        for idx in range(4):
            ny = ey + dy[idx]
            nx = ex + dx[idx]

            if not iswall(Y, X, ny, nx) and data[ny][nx] == 0:
                zero -= 1
                queue.append([ny, nx])
                data[ny][nx] = data[ey][ex] + 1
                maxday = data[ny][nx]

    if zero == 0:
        return maxday - 1
    else:
        return -1


X, Y = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(Y)]
queue = []
zero = 0
maxday = 0
findstart(Y, X)
print(bfs())