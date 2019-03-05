import sys
sys.stdin = open('binarysearch.txt')


def inorder_by(node):
    global N, Q, node_num
    if node <= N:
        inorder_by(node*2)
        Q[node] = node_num
        node_num += 1
        inorder_by(node*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Q = [0] * (N+1)
    # for i in range(1, N+1):
    #     Q[i] = i
    node_num = 1
    inorder_by(1)
    print('#{}'.format(tc),Q[1], Q[N//2])