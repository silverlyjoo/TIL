import sys
sys.stdin = open('guncho.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    data = [int(input()) for _ in range(N)]
    a = sum(data)//N
    for i in data:
        cnt += abs(a-i)
    print('#{} {}'.format(tc, cnt//2))
