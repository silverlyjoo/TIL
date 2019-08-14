import sys
sys.stdin = open('dividegroup.txt')


def findset(x):

    if P[x] == x:
        return x
    else:
        return findset(P[x])




T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    P = list(range(N+1))
    visited=[0]*(N+1)

    for i in range(0, 2*M, 2):

        p1 = findset(data[i])
        p2 = findset(data[i+1])

        if p1 != p2:
            P[p1] = p2
    for i in P:
        if i:
            visited[findset(i)] = 1

    cnt = 0
    for idx, p3 in enumerate(P):
        if idx == p3:
            cnt +=1
    print(cnt-1)

    print('#{} {}'.format(tc, sum(visited)))


