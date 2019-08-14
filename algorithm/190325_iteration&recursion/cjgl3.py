import sys, time
sys.stdin = open('cjgl.txt')

start_time = time.time()

def perm(n, k, sums):
    global min_sum

    if sums > min_sum:
        return


    if n == k:
        if min_sum > sums:
            sums += memo[A[k-1]][A[-1]]
            min_sum = sums


    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]

            perm(n, k+1, sums + memo[A[k]][A[k-1]])

            A[k], A[i] = A[i], A[k]






T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    company = [data.pop(0),data.pop(0)]
    house = [data.pop(0),data.pop(0)]
    data2 = [[data[i], data[i+1]] for i in range(0, len(data), 2)]
    data3 = [company] + data2 + [house]
    A = [_ for _ in range(N+2)]


    memo = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            memo[i][j] = (abs(data3[i][0]-data3[j][0]) + abs(data3[i][1]-data3[j][1]))

    min_sum = float('inf')
    perm(N+1, 1, 0)
    print('#{} {}'.format(tc, min_sum))

print(time.time() - start_time, 'seconds')




