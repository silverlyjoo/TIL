import sys
sys.stdin = open('building.txt')


def perm(k, sums):
    global msums
    if sums > msums:
        return
    if k >= N:
        if sums < msums:
            msums = sums
            return
    else:
        for i in range(N):
            if not chk[i]:
                chk[i] = 1
                perm(k+1, sums + data[k][i])
                chk[i] = 0




N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
chk = [0 for _ in range(N)]
msums = float('inf')
perm(0,0)

print(msums)