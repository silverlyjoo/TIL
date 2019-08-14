import sys
sys.stdin = open('cg.txt')


N = int(input())

idx = []
hi = []

for tc in range(N):
    L, H = map(int, input().split())
    idx.append(L)
    hi.append(H)

# 인덱스 당기기
dif = min(idx)
for i in range(len(idx)):
    idx[i] -= dif

# 면적
prearea = max(hi) * (max(idx) - min(idx) + 1)

# 가장 높은 곳 인덱스
hidx = idx[hi.index(max(hi))]
# 가장 높은곳 값
hival = max(hi)
idxval = max(idx)

maxhi = 0
maxhi2 = 0

for i in range(hidx):
    if i in idx and hi[idx.index(i)] > maxhi:
        maxhi = hi[idx.index(i)]
        prearea -= (hival - maxhi)
    else:
        prearea -= (hival - maxhi)

for j in range(idxval, hidx, -1):
    if j in idx and hi[idx.index(j)] > maxhi2:
        maxhi2 = hi[idx.index(j)]
        prearea -= (hival - maxhi2)
    else:
        prearea -= (hival - maxhi2)

print(prearea)