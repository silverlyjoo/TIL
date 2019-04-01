import sys
sys.stdin = open('kruskal.txt')


def findset(x):
    if x==p[x]: return x
    else: return findset(p[x])


def mst():
    global V
    c = 0 # 간선갯수
    s = 0
    i = 0

    while c < V:
        p1 = findset(edge[i][0])
        p2 = findset(edge[i][1])

        if p1 != p2:
            s += edge[i][2]
            c += 1
            p[p1] = p2

        i += 1
    return s


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x:x[2])
    p = list(range(V+1))

    print(mst())
