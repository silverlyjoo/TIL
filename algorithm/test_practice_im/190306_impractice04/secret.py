import sys
sys.stdin = open('secret.txt')



N = int(input())

data = [[] for _ in range(2*N-1)]

L = list(range(N))

L2 = L + L[len(L)-2::-1]

print(L2)