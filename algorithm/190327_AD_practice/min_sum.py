import sys
sys.stdin = open('min_sum.txt')


def dfs1(k, sums):
    global result1
    if sums > result1:
        return

    if k >= N:
        if sums < result1:
            result1 = sums
        return

    for i in range(N):
        dfs1(k+1, sums + data[k][i])


def dfs2(k, sums):
    global result2
    if sums > result2:
        return

    if k >= N:
        if sums < result2:
            result2 = sums
        return

    for i in range(N):
        if not chk[i]:
            chk[i] = 1
            dfs2(k+1, sums + data[k][i])
            chk[i] = 0



N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

chk = [0 for _ in range(N)]
result1 = float('inf')
result2 = float('inf')
dfs1(0, 0)
print(result1)
dfs2(0, 0)
print(result2)