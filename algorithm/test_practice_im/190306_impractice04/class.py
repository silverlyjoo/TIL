import sys
sys.stdin = open('class.txt')


def divclass(T1, T2, Kmin, Kmax):
    R = [[] for _ in range(3)]
    for i in L:
        if i >= T2:
            R[2].append(i)
        elif i < T1:
            R[0].append(i)
        else:
            R[1].append(i)
    r = [len(R[0]), len(R[1]), len(R[2])]
    if max(r) <= Kmax and min(r) >= Kmin:
        return max(r) - min(r)


T = int(input())

for tc in range(1, T+1):

    N, Kmin, Kmax = map(int, input().split())
    L = list(map(int, input().split()))
    dif = []
    for T1 in range(1, 101):
        for T2 in range(T1+1, 101):
            di = divclass(T1, T2, Kmin, Kmax)
            if di:
                dif.append(di)
    if dif:
        print(min(dif))
    else:
        print(-1)


