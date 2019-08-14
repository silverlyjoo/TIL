import sys
sys.stdin = open('hap.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    chk = [0]*N
    chk[0] = data[0]
    for i in range(1, N):
        if chk[i-1] + data[i] > data[i]:
            chk[i] = chk[i-1]+data[i]
        else:
            chk[i] = data[i]

    print('#{} {}'.format(tc, max(chk)))