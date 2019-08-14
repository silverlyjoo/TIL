import sys
sys.stdin = open('paintgraph.txt')


def check(idx, color):
    for item in range(0, len(data[idx])):
        if data[idx][item] == 1 and color == colors[item]: return False
    return True


def paint(idx):
    global flag
    if not flag:
        return
    if idx >= N:
        return
    if idx == 0:
        colors[idx] = 1
        paint(idx+1)
        return
    for color in range(1, M):
        if check(idx, color):
            colors[idx] = color
            break
    else:
        flag = False
    paint(idx+1)


N, M = map(int, input().split())
M+=1
data = [list(map(int, input().split())) for _ in range(N)]
flag = True
colors = [0 for _ in range(N)]
paint(0)

if flag:
    print(*colors)
else:
    print(-1)
