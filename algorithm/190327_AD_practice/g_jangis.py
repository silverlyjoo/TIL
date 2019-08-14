import sys
sys.stdin = open('jangis.txt')


def iswall(y, x):
    if y < 0 or y >= N: return True
    if x < 0 or x >= M: return True
    return False


def BFS(y, x):
    
    q = [(y, x, 0)]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    
    while q:
        r, c, n = q.pop(0)
        for i in range(8):
            nr = r + dy[i]
            nc = c + dx[i]

            if not iswall(nr, nc) and ppan[nr][nc] == 2:
                print(n+1)
                return
            elif not iswall(nr, nc) and ppan[nr][nc] == 0:
                q.append((nr, nc, n+1))
                ppan[nr][nc] = 1
                
N, M = map(int, input().split())
R, C, S, K = map(lambda x:int(x)-1, input().split())
ppan = [[0]* M for _ in range(N)]
ppan[S][K] = 2

BFS(R, C)