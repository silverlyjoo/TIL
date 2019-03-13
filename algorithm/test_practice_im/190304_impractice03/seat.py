import sys
sys.stdin = open('seat.txt')

def iswall(x, y, C, R):
    if x < 0 or x >= C: return False
    if y < 0 or y >= R: return False
    if L[y][x] != 0 : return False
    return True

C, R = map(int, input().split())
K = int(input())

L = [[0 for _ in range(C)] for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
idx = 0
val = 1
result = False

while val<=C*R:
    if iswall(x, y, C, R):
        L[y][x] = val
        val += 1
    else:
        x -= dx[idx]
        y -= dy[idx]
        idx = (idx + 1) %4
    x += dx[idx]
    y += dy[idx]
    if val == K:
        result = x+1, y+1
if result:
    print(*result)
else:
    print(0)