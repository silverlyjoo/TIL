import sys
sys.stdin = open("hrcg_input.txt")


def findstart(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == 1:
                return (i,j)


def findnp(L, sp):
    nx = 0
    ny = 0
    for i in range(sp[1], len(L)):
        if L[sp[0]][i] != 1:
            nx = i-1
            break
    else:
        nx = len(L)-1
    for i in range(sp[0], len(L)):
        if L[i][nx] != 1:
            ny = i-1
            break
    else:
        ny = len(L)-1
    return (ny,nx)


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
    RL = [[] for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if L[i][j]:
                RL[i].append(1)
            else:
                RL[i].append(0)
    while iszero(RL):
        sp = findstart(RL)
        np = findnp(L, sp)
        result.append(putresult(sp, np))
        bezero(sp, np, RL)
    result.sort()
    l = len(result)
    k = [l]
    for i in range(l):
        k.append(result[i][1])
        k.append(result[i][2])
    print(f'#{tc}', *k)
