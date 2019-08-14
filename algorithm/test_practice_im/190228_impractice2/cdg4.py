import sys
sys.stdin = open('cdg.txt')

N = int(input())
L = tuple(float(input()) for i in range(N))


m = [0]*N
m[0] = L[0]

for i in range(1, N):
	if m[i-1] * L[i] > L[i]:
		m[i]=m[i-1] * L[i]
	else:
		m[i]=L[i]

print('{:.3f}'.format(max(m)))