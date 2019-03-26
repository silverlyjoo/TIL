import sys
sys.stdin = open("csh.txt")

def iswall(y, x, N):
    if y<0 or y>=N: return True
    if x < 0 or x >= N: return True
    return False


def go(y, x, distance, N):
    global result
    if distance > result:
        return
    if y == N-1 and x == N-1:
        if result > distance:
            result = distance

    ey, ex = y, x
    dy = [0, 1]
    dx = [1, 0]

    for idx in range(2):
        ny = ey + dy[idx]
        nx = ex + dx[idx]
        if not iswall(ny, nx, N):
            go(ny, nx, distance+data[ny][nx], N)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    sy, sx = 0, 0
    go(sy, sx, data[0][0], N)
    print("#{} {}".format(tc, result))