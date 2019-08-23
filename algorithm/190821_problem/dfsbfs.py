import sys
sys.stdin = open('dfsbfs.txt')


def dfs(v):
    visitDFS[v] = True
    print(v, end=" ")
    data[v].sort()
    for node in data[v]:
        if not visitDFS[node]:
            dfs(node)
    return

def bfs(v, N):

    visit = [False] * (N+1)

    visit[v] = True
    print(v, end=' ')
    que = [v]

    while que:
        st = que.pop(0)
        data[st].sort()
        for ed in data[st]:
            if not visit[ed]:
                print(ed, end=' ')
                que.append(ed)
                visit[ed] = True

N, M, V = map(int, input().split())

data = [[] for _ in range(N+1)]
visitDFS = [False]*(N+1)
for _ in range(M):
    n1, n2 = map(int, input().split())
    data[n1].append(n2)
    data[n2].append(n1)

dfs(V)
print()
bfs(V, N)