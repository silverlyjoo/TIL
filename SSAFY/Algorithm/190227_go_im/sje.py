import sys
sys.stdin = open("sje.txt")

T = int(input())
P = [[0 for i in range(101)] for i in range(101)]

for tc in range(T):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            P[i][j] = 1
cnt = 0
for i in range(len(P)):
    for j in range(len(P[i])):
        if P[i][j] :
            cnt += 1

print(cnt)