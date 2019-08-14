import sys
from pprint import pprint
sys.stdin = open("miro_input.txt")

def findstart(N, L):
    for i in range(N):
        for j in range(N):
            if L[i][j] == '2':
                return (j, i)

def notwall(x, y, N):
    if x > N-1 or x < 0: return False
    if y > N-1 or y < 0: return False
    return True

def miro(x, y, L, N):
    queue = [(x,y)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited = [[0 for i in range(N+1)] for i in range(N+1)]
    visited[y][x]=1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if notwall(nx, ny, N) and L[ny][nx] == '3':
                return visited[y][x]-1
            elif notwall(nx, ny, N) and L[ny][nx] == '0' and not visited[ny][nx]:
                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(input()) for _ in range(N)]
    x, y = findstart(N, L)
    a = miro(x, y, L, N)
    if a:
        print(f'#{tc} {a}')
    else:
        print(f'#{tc} 0')

    # pprint(L)
    # print(x, y)
    # print(a)