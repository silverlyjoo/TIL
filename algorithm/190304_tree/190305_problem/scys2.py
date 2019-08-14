import sys
sys.stdin = open('scys.txt')


def gs(a, b, c):
    if b == '+':
        return a+c
    if b == '-':
        return a-c
    if b == '*':
        return a*c
    if b == '/':
        return a/c


def inorder(node):
    if type(L[node][1]) == int:
        return L[node][1]
    else:
        a = inorder(L[node][2])
        b = inorder(L[node][3])
        return gs(a, L[node][1], b)


T = 10
for tc in range(1, T+1):
    N = int(input())
    L = [[0 for _ in range(4)] for _ in range(N+1)]
    for data in range(1,N+1):
        k = list(input().split())
        if len(k) == 4:
            L[data] = [int(k[0]), k[1], int(k[2]), int(k[3])]
        else:
            L[data][0] = int(k[0])
            L[data][1] = int(k[1])
    print('#{} {}'.format(tc, int(inorder(1))))