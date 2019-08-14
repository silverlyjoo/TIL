import sys
sys.stdin = open("jackup_input.txt")

def workhard2(i):
    visit[i] = 1
    for j in G[i]:
        if not visit[j]:
            workhard2(j)
    result.append(i)

for N in range(10):
    V, E = map(int, input().split())
    L = list(map(int, input().split()))
    G = [[] for _ in range(V + 1)]
    NS = [L[_] for _ in range(1, len(L), 2)]
    SP = [i for i in range(1, V + 1) if i not in NS]
    visit = [0]*(V+1)
    result = []
    for i in range(0, len(L), 2):
        G[L[i]].append(L[i + 1])
    for i in SP:
        workhard2(i)
    result2 = ' '.join(map(str, result[::-1]))
    print(f'#{N+1} {result2}')

def workhard(G, V):
    while len(result) < V:
        for j in SP:
            result.append(j)
            for i in G[j]:
                NS.pop(NS.index(i))
                if i not in NS:
                    SP.append(i)
            SP.pop(SP.index(j))

    return ' '.join(map(str, result))

for N in range(10):
    V, E = map(int, input().split())
    L = list(map(int, input().split()))
    G = [[] for _ in range(V + 1)]
    NS = [L[_] for _ in range(1, len(L), 2)]
    SP = [i for i in range(1, V + 1) if i not in NS]
    result = []
    for i in range(0, len(L), 2):
        G[L[i]].append(L[i + 1])
    print(f'#{N + 1} {workhard(G, V)}')
