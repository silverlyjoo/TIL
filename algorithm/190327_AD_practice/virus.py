import sys
sys.stdin = open('virus.txt')


def findset(x):
    if P[x] == x: return x
    else: return findset(P[x])


N = int(input())
M = int(input())
links = []
P = list(range(N+1))
for i in range(M):
    s, e = map(int, input().split())
    links.append([s, e])

for i in links:
    p1 = findset(i[0])
    p2 = findset(i[1])

    if p1 != p2:
        P[p1] = p2

cnt = 0
for j in P:

    if findset(j) == findset(1):
        cnt += 1
print(cnt-1)

