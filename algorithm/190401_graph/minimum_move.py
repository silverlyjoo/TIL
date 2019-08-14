import sys
sys.stdin = open('minimum_move.txt')


def getminidx():
    minV = 0xffffff
    minidx = 0

    for i in range(N+1):
        if not visited[i] and D[i] < minV:
            minidx = i
            minV = D[i]

    return minidx



def shortway_d(goal):

    D[0] = 0

    for i in range(N+1):
        if data[0][i]:
            D[i] = data[0][i]

    visited[0] = 1

    while True:
        node = getminidx()
        visited[node] = 1

        if node == goal:
            return D[goal]

        for x in range(N+1):
            if data[node][x]:
                if D[x] > (D[node] + data[node][x]):
                    D[x] = D[node] + data[node][x]

T = int(input())

for tc in range(1, T+1):

    N, E = map(int, input().split())

    data = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        data[s][e] = w

    visited = [0 for _ in range(N+1)]

    D = [0xfffffff for _ in range(N+1)]

    print('#{} {}'.format(tc, shortway_d(N)))









