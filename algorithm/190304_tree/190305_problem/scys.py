import sys
sys.stdin = open('scys.txt')

def inorder(node):
    if node != 0:
        G.append('(')
        inorder(int(L[node][2]))
        G.append(str(L[node][1]))
        inorder(int(L[node][3]))
        G.append(')')

T = 10
for tc in range(1, T+1):
    N = int(input())
    L = [[0 for _ in range(4)] for _ in range(N+1)]
    for data in range(1,N+1):
        k = list(input().split())
        if len(k) == 4:
            L[data] = k
        else:
            L[data][0] = k[0]
            L[data][1] = k[1]
    G = []
    inorder(1)
    gss = int(eval(''.join(G)))
    print('#{} {}'.format(tc, gss))