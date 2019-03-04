import sys
sys.stdin = open('numcheck.txt')

n = int(input())

L = [list(map(int, input().split())) for _ in range(n)]

result = [[] for _ in range(n)]

for i in range(3):
    for j in range(n):
        check = True
        for k in range(n):
            if j != k and L[j][i] == L[k][i]:
                check = False
        if check:
            result[j].append(L[j][i])

k = []
for re in range(n):
    k.append(sum(result[re]))
for r in k:
    print(r)

