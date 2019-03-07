import sys
sys.stdin = open('ndgl_input.txt')

def BFS(S,G):

    queue = []
    queue.append(S)
    while queue:
        node = queue.pop(0)
        for go in L[node]:
            if not visit[go]:
                queue.append(go)
                visit[go] = visit[node]+1


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())
    visit = [0]*(V+1)
    L = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        L[s].append(e)
        L[e].append(s)
    
    S, G = map(int, input().split())

    BFS(S,G)
    print(visit[G])
