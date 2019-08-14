import sys
sys.stdin = open("sje2.txt")



T = int(input())
P = [[0 for i in range(102)] for i in range(102)]

for tc in range(T):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            P[i][j] = 'Z'

cnt = 0
for i in range(len(P)-1):
    for j in range(len(P[i])-1):
        if P[i][j] != P[i][j+1]:
            cnt += 1
        if P[i][j] != P[i+1][j]:
            cnt += 1

for i in P[:30]:
    print(*i[:30])
print(cnt)