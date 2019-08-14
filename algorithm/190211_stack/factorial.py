# def fact(num):
#     if num < 2:
#         return 1
#     else:
#         return num * fact(num-1)
#
#
#
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)


def fibo1(n):
    memo = [0,1]
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

print(fibo1(10))


def fibo2(n):
    f = [ 0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]










