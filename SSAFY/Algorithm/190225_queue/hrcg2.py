import sys
sys.stdin = open("hrcg_input.txt")

def findstart(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] != 0:
                return (i, j)

def findnp(L, sp):
    nx = 0
    ny = 0
    for i in range(sp[1], len(L)):
        if L[sp[0]][i] == 0:
            nx = i-1
            break
    for i in range(sp[0], len(L)):
        if L[i][nx] == 0:
            ny = i-1
            break
    return (ny, nx)

def putresult(sp, np):
    height = (np[1]-sp[1])+1
    width = (np[0]-sp[0])+1
    ar = height*width
    return [ar, width, height]

def bezero(sp, np, L):
    for i in range(sp[0], np[0]+1):
        for j in range(sp[1], np[1]+1):
            L[i][j] = 0

def iszero(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] != 0:
                return True
    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [[1 if _ != 0 else _ for _ in map(int, input().split())] for _ in range(N)]
    result = []
    while iszero(L):
        sp = findstart(L)
        np = findnp(L, sp)
        result.append(putresult(sp, np))
        bezero(sp, np, L)
    result.sort()
    l = len(result)
    k = [l]
    for i in range(l):
        k.append(result[i][1])
        k.append(result[i][2])
    print(f'#{tc}',*k)

