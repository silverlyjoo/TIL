import sys
sys.stdin = open('cdg.txt')

N = int(input())
L = [float(input()) for i in range(N)]
R = []

for i in range(N-2):
    R.append(L[i]*L[i+1]*L[i+2])
R.sort()
print(f'{R[-1]:.4f}')