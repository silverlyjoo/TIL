import sys
sys.stdin = open('sumnode.txt')

T = int(input())

for tc in range(1, T+1):

    N, M, L = map(int, input().split())
    Q = [0] * (N+1)
    data = []
    for i in range(M):
        data += map(int, input().split())

    for i in range(0, len(data), 2):
        Q[data[i]] = data[i+1]
    # print(Q)
    for i in range(len(Q)-M, 0, -1):
        if not Q[i]:
            if (i*2+1) < len(Q):
                Q[i] = Q[i*2] + Q[i*2+1]
            else:
                Q[i] = Q[i*2]
    print('#{} {}'.format(tc, Q[L]))