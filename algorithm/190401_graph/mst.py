import sys
sys.stdin = open('mst.txt')


def findset(x):
    if P[x] == x: return x
    else: return findset(P[x])


def mst_k():

    global V

    cnt = 0
    idx = 0
    sums = 0

    while cnt < V:
        p1 = findset(data[idx][0])
        p2 = findset(data[idx][1])
        if p1 != p2:
            P[p1] = p2
            sums += data[idx][2]
            cnt += 1
        idx += 1
    return sums


T = int(input())


for tc in range(1, T+1):

    V, E = map(int, input().split())
    data = []
    P = list(range(V+1))
    for i in range(E):
        n1, n2, w = map(int, input().split())
        data.append([n1, n2, w])



    data.sort(key=lambda x:x[2])
    print('#{} {}'.format(tc, mst_k()))
