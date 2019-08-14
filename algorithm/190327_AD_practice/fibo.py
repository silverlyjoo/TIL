


def fibo(N):

    for i in range(3, N+1):
        memo[i] = memo[i-1] + memo[i-2]


N = int(input())
memo = [0 for _ in range(N+3)]
memo[1] = 1
memo[2] = 1
fibo(N)
print(memo[N])

