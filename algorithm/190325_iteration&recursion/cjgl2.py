import sys, time
sys.stdin = open('cjgl.txt')

start_time = time.time()

def perm(n, k, sums):
    global min_sum
    if sums > min_sum:
        return

    if n == k:
        sums += (abs(data3[-2][0]-data3[-1][0]) + abs(data3[-2][1]-data3[-1][1]))
        if min_sum > sums:
            min_sum = sums


    else:
        for i in range(k, n):
            data3[i], data3[k] = data3[k], data3[i]
            a = (abs(data3[k-1][0]-data3[k][0]) + abs(data3[k-1][1]-data3[k][1]))
            perm(n, k+1, sums+a)
            data3[i], data3[k] = data3[k], data3[i]


T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    company = [data.pop(0),data.pop(0)]
    house = [data.pop(0),data.pop(0)]
    data2 = [[data[i], data[i+1]] for i in range(0, len(data), 2)]
    data3 = [company] + data2 + [house]
    min_sum = float('inf')
    perm(N+1, 1, 0)
    print('#{} {}'.format(tc, min_sum))

print(time.time() - start_time, 'seconds')




