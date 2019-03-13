import sys
sys.stdin = open("pattern.txt")


T = int(input())
L = [list(map(str, input())) for _ in range(T)]
r = int(input())
pattern = [list(map(str, input())) for _ in range(r)]


imsipattern = []

cnt = 0
for i in range(0,T-r+1):
    for j in range(0,T-r+1):
        for l in range(r):
            imsipattern.append(L[i+l][j:j+r])
        if imsipattern == pattern:
            cnt += 1
        imsipattern = []

print(cnt)