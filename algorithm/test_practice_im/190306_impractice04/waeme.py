import sys, math
sys.stdin = open('waeme.txt')



def bgl(x, y, i, j):
    return ((x-j)**2 + (y-i)**2)**0.5

def findtwo(N):
    for i in range(N):
        for j in range(N):
            if L[i][j] == 2:
                return (i, j)


N = int(input())

L = [list(map(int, input())) for _ in range(N)]
result = []
y, x = findtwo(N)

for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            result.append(math.ceil(bgl(x, y, i, j)))
print(max(result))
