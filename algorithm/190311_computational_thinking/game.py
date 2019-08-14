import sys
from pprint import pprint
sys.stdin = open('game.txt')

def iswall(y, x, N):
    if y <0 or y>=N: return True
    if x < 0 or x >= N: return True
    return False


def putstone(K):
    x, y, team = K
    board[y-1][x-1] = team


def changestone(K, N):
    x, y, team = K

    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for idx in range(8):
        stack = []
        ny, nx = y-1 + dy[idx], x-1 + dx[idx]
        while True:
            if not iswall(ny, nx, N) and board[ny][nx] != team and board[ny][nx] != 0:
                stack.append([ny, nx])
                ny, nx = ny + dy[idx], nx + dx[idx]
            if not iswall(ny, nx, N) and board[ny][nx] == team:
                if stack:
                    for change in stack:
                        cy, cx = change
                        board[cy][cx] = team



                    break
                else:
                    break
            if iswall(ny, nx, N) or board[ny][nx] == 0:
                break


def checkstone(N):
    cnt = [0,0]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt[0] += 1
            if board[i][j] == 2:
                cnt[1] += 1
    return cnt









T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(M)]
    board = [[0 for _ in range(N)] for _ in range(N)]

    board[N//2-1][N//2-1] = board[N//2][N//2] = 2
    board[N // 2][N // 2-1] = board[N // 2-1][N // 2] = 1

    for i in L:
        putstone(i)
        changestone(i, N)
        print('#')
        for i in board:
            print(i)

    print('#{} {} {}'.format(tc, *checkstone(N)))




    # for i in board:
    #     print(*i)

