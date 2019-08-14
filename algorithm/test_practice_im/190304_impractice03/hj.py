import sys
sys.stdin = open('hj.txt')


def hj(n):
    global L
    L2 = [[] for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            L2[j].append(L[i][j])
    L = L2


n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]

G = int(input())
while True:
    if G == 90:
        hj(n)
        for i in L:
            print(*i)
    elif G == 180:
        hj(n)
        hj(n)
        for i in L:
            print(*i)
    elif G == 270:
        hj(n)
        hj(n)
        hj(n)
        for i in L:
            print(*i)
    elif G == 360:
        for i in L:
            print(*i)
    G = int(input())
    if G == 0:
        break