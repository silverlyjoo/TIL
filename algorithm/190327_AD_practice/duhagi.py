import sys
sys.stdin = open('duhagi.txt')


def comb(k, sums):
    global flag
    if sums > K or flag:
        return
    if sums == K:
        flag = True
        return
    if k >= N:
        return
    comb(k+1, sums + data[k])
    comb(k+1, sums)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    flag = False
    comb(0, 0)
    if flag:
        print('YES')
    else:
        print('NO')

