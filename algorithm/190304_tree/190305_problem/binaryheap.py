import sys
sys.stdin = open('binaryheap.txt')

def inQ(num):
    global last
    last += 1
    c = last
    p = c // 2
    Q[last] = num
    while c > 1 and Q[p] > Q[c]:
        Q[p], Q[c] = Q[c], Q[p]
        c, p = p, p//2

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    Q = [0]*(N+1)
    last = 0
    for i in L:
        inQ(i)


    result = []
    while last:
        last //= 2
        result.append(Q[last])
    print('#{} {}'.format(tc, sum(result)))
