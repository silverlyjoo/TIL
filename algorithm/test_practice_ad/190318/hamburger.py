import sys
sys.stdin = open('hamburger.txt')


def diet(N, K, mm, kk):
    if kk <= K:
        result.append(mm)
        for i in range(N):
            if not visit[i]:
                visit[i] = 1
                diet(N, K, mm+mat[i], kk+kal[i])


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mat = []
    kal = []
    for i in range(N):
        m, k = map(int, input().split())
        mat.append(m)
        kal.append(k)

    result = []
    for i in range(N):
        visit = [0] * N
        visit[i] = 1
        diet(N, K, mat[i], kal[i])
    mats = max(result)
    print('#{} {}'.format(tc, mats))

