import sys
from pprint import pprint
sys.stdin = open('snake.txt')

# 벽 또는 자기 자신 일경우 끝
def iswall(x, y, N):
    if x <= 0 or x > N: return False
    if y <= 0 or y > N: return False
    return True


def bam(x, y, idx, N):
    global result
    if iswall(x, y, N) and pan[y][x] == 1:
        pan[y][x] = 2
        queue.append((x, y))
    else:
        if not iswall(x, y, N) or pan[y][x] == 2:
            result = False
            return
        else:
            pan[y][x] = 2
            queue.append((x, y))
            ex, ey = queue.pop(0)
            pan[ey][ex] = 0


# 입력
N = int(input())
K = int(input())

# 게임판
pan = [[0 for _ in range(N+1)]for _ in range(N+1)]

# 과일배치
for i in range(K):
    r, c = map(int, input().split())
    pan[r][c] = 1

# 시작지점, 뱀 == 2
pan[1][1] = 2

# 뱀 정보 저장
queue = [(1, 1)]

# 델타검색

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

idx = 0

L = int(input())
time = 0
x, y = 1, 1
result = True

go = []

for i in range(L):
    X, C = input().split()
    go.append([int(X), C])

ts, tc = go.pop(0)

while result:
    x += dx[idx]
    y += dy[idx]
    bam(x, y, idx, N)
    time += 1
    if ts == time:
        if tc == 'L':
            idx = (idx+1)%4
        elif tc == 'D':
            idx = (idx-1)%4
        if go:
            ts, tc = go.pop(0)

print(time)