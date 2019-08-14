import sys
sys.stdin = open("elec_cart.txt")


def perm(n, k, sums):
    global result
    if sums > result:
        return

    if n == k:
        sums += memo[A[k-1]][A[k]]
        if result > sums:
            result = sums

    for i in range(k, n):
        A[k], A[i] = A[i], A[k]
        perm(n, k+1, sums + memo[A[k-1]][A[k]])
        A[k], A[i] = A[i], A[k]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    memo = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    A = [_ for _ in range(N)] + [0]

    perm(N, 1, 0)
    print('#{} {}'.format(tc, result))
