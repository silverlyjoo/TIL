import sys
sys.stdin = open('tape.txt')


def perm(k):

    if k >= N:

        return
    for i in range(k, N):

        if not chk[i]:
            chk[i] = 1
            perm(k+1)
            chk[i] = 0
            perm(k+1)





N = int(input())

data = list(map(int, input().split())
chk = [0 for _ in range(N)]

