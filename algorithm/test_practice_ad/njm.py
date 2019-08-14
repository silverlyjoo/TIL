import sys
sys.stdin = open('njm.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    data = [list(map(int, input())) for _ in range(N)]

    result = []

    for i in range(N//2+1):
        for j in range(N//2-i, N//2 +i+1):
            result.append(data[i][j])


    for i in range(N//2+1, N):
        row2 = []
        for j in range(i-N//2,N-i+N//2):
            result.append(data[i][j])

    print('#{} {}'.format(tc, sum(result)))
