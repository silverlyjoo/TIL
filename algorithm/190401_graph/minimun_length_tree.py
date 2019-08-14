import sys
sys.stdin = open('minimun_length_tree.txt')


def prim():
    global V
    total = 0
    u = 0
    D[u] = 0
    PI[u] = 0

    for i in range(V+1):
        min = 0xffffffffff
        for v in range(V+1):
            if visit[v] == 0 and min > D[v]:
                min = D[v]
                u = v

    visit[u] = 1
    total += L[PI[u]][u]

    for v in range(V+1):
        if L[u][v] != 0 and visit[v] == 0 and L[u][v] < D[v]:
            D[v] = L[u][v]
            PI[v] = u

    return total


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())

    L = [[0 for _ in range(V+1)] for _ in range(V+1)]
    D = [0xfffffffff] * (V+1)
    PI = list(range(V+1))
    visit = [0]*(V+1)

    for line in range(E):
        n1, n2, w = map(int, input().split())

        L[n1][n2] = w
        L[n2][n1] = w


    print(L)




