import sys, time
sys.stdin = open('cjgl.txt')
start_time = time.time()

def howlong():
    global min_sum
    sums = 0
    x, y = data3[0]
    for j in data3:
        sums += (abs(x-j[0]) + abs(y-j[1]))
        x, y = j
    if min_sum > sums:
        min_sum = sums

def perm(n, k):
    if n == k:
        howlong()
    else:
        for i in range(k, n):
            data3[i], data3[k] = data3[k], data3[i]
            perm(n, k+1)
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
    perm(N+1, 1)
    print('#{} {}'.format(tc, min_sum))

print(time.time() - start_time, 'seconds')
