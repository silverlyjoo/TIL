import sys
sys.stdin = open("jackup_input.txt")

def workhard(G, NS, SP, result):
    for i in SP:
        result.append(SP.pop(SP.index(i)))
        for j in G[i]:
            NS.pop(NS.index(j))
            if j not in NS:
                SP.append(j)
            workhard(G, NS, SP, result)
    return result






for N in range(10):
    V, E = map(int, input().split())
    L = list(map(int, input().split()))
    NS = [L[_] for _ in range(1, len(L),2)]
    SP = [i for i in range(1, len(L)//2+1) if i not in NS]
    G = [[] for _ in range(V+1)]
    result = []
    for i in range(0, len(L), 2):
        G[L[i]].append(L[i+1])


    # print(G)
    # print(sorted(NS))
    # print(SP)
    print(workhard(G, NS, SP, result))

