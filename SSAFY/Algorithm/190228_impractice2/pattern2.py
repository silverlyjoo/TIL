import sys
from pprint import pprint
sys.stdin = open('pattern2.txt')

def check1(y, x, P):
    for i in range(P):
        for j in range(P):
            if mL[y+i][x+j] != pL1[i][j]:
                return False
    return True

def check2(y, x, P):
    for i in range(P):
        for j in range(P):
            if mL[y+i][x+j] != pL2[i][j]:
                return False
    return True

def check3(y, x, P):
    for i in range(P):
        for j in range(P):
            if mL[y+i][x+j] != pL3[i][j]:
                return False
    return True

def check4(y, x, P):
    for i in range(P):
        for j in range(P):
            if mL[y+i][x+j] != pL4[i][j]:
                return False
    return True

M = int(input())
mL = [input() for i in range(M)]

P = int(input())
pL1 = [input() for i in range(P)]
pL2 = ['']*P
pL3 = ['']*P
pL4 = ['']*P

for i in range(P-1, -1, -1):
    for j in range(P):
        pL2[j] += pL1[i][j]

for i in range(P-1, -1, -1):
    for j in range(P):
        pL3[j] += pL2[i][j]

for i in range(P-1, -1, -1):
    for j in range(P):
        pL4[j] += pL3[i][j]

cnt = 0
for i in range(0, M-P+1):
    for j in range(0, M-P+1):
        if check1(i, j, P):
            cnt += 1
        if check2(i, j, P):
            cnt += 1
        if check3(i, j, P):
            cnt += 1
        if check4(i, j, P):
            cnt += 1

print(cnt)

pprint(pL1)
pprint(pL2)
pprint(pL3)
pprint(pL4)