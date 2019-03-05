import sys
from pprint import pprint
sys.stdin = open('subtree.txt')

def travel(node):
    global cnt
    if node != 0:
        travel(R[node][0])
        travel(R[node][1])
        cnt += 1

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    L = list(map(int, input().split()))
    R = [[ 0 for _ in range(2)] for _ in range(E+2)]

    for i in range(0, len(L), 2):
        if R[L[i]][0]:
            R[L[i]][1] = L[i+1]
        else:
            R[L[i]][0] = L[i+1]
    cnt = 0
    travel(N)
    print('#{} {}'.format(tc, cnt))
