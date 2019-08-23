import sys
sys.stdin = open('con_com.txt')


def findstart(N):
    global cnt
    for _ in range(1, N+1):
        if not visit[_]:
            cnt += 1
            return _
    return False

def dfs(v):
    visit[v] = True
    for node in data[v]:
        if not visit[node]:
            dfs(node)
    return


N, M = map(int, input().split())
data = [[] for _ in range(N+1)]
visit = [False] * (N+1)
visit[0] = True
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())

    data[u].append(v)
    data[v].append(u)

a = findstart(N)

while a:
    dfs(a)
    a = findstart(N)

print(cnt)


