

def iswall(y, x):
    if y < 0 or y >= N: return True
    if x < 0 or x >= N: return True
    return False


def check(y, x):
    dy = [-1, -1, -1]
    dx = [-1, 0, 1]
    for i in range(3):
        for k in range(1, N):
            ny = y + dy[i] * k
            nx = x + dx[i] * k
            if not iswall(ny, nx) and data[ny][nx]:
                return False
    return True


def queen(idx):
    global cnt
    if idx >= N:
        cnt += 1
        return

    for i in range(N):
        if check(idx, i):
            data[idx][i] = 1
            queen(idx+1)
            data[idx][i] = 0

N = int(input())

data = [[0 for _ in range(N)] for _ in range(N)]
chk = [0 for _ in range(N)]
P = [0 for _ in range(N)]
cnt = 0
queen(0)
print(cnt)


