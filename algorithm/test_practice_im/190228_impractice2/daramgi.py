import sys
sys.stdin = open('daramgi.txt')

def fool(N, L):
    m = [0]* N
    m[0] = L[0]
    for i in range(1, N):
        m[i] = max(L[i], m[i-1]+L[i])
    return max(m)

def smart(N, L):
    m = 0
    n = -999
    for i in range(N):
        if L[i] > 0:
            m += L[i]
        else:
            if L[i] > n:
                n = L[i]
    if m:
        return m
    else:
        return n

N = int(input())
L = list(map(int, input().split()))

print(fool(N, L), smart(N, L))