import sys
sys.stdin = open('bomb.txt')

K = int(input())
N = int(input())
t = 210
L = [list(map(str, input().split())) for _ in range(N)]
idx = [_ for _ in range(K, K+N)]
ridx = list(map(lambda x:x%8 if x%8 else 8, idx))


for i in range(N):
    t -= int(L[i][0])
    if t <= 0:
        break
    if L[i][1] == 'T':
        ridx.pop(0)

print(ridx[0])






# print(L)
# print(idx)