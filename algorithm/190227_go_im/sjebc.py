import sys
sys.stdin = open("sjebc.txt")



def sje():
    for i in range(101):
        for j in range(101):
            if M[i][j] == 3:
                return 3

    for i in range(101):
        for j in range(101):
            if M[i][j] != 0:
                if (M[i][j+1] != 0 and M[i][j+1] != M[i][j]) or (M[i+1][j] != 0 and M[i+1][j] != M[i][j]):
                    return 2

    for i in range(101):
        for j in range(101):
            if M[i][j] != 0:
                if (M[i+1][j+1] != 0 and M[i+1][j+1] != M[i][j]) or (M[i+1][j-1] != 0 and M[i+1][j-1] != M[i][j]):
                    return 1
    return 4

M = [[0 for _ in range(103)] for _ in range(103)]

L = [list(map(int, input().split())) for _ in range(2)]

for l in range(1, len(L)+1):
    x, y, a, b = L[l-1]
    cnt = l
    for i in range(x, x+a):
        for j in range(y, y+b):
            M[i][j] += cnt

for i in M:
    print(*i)
# print(sje())
