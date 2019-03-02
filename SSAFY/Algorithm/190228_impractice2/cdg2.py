import sys
sys.stdin = open('cdg.txt')

def mul(start, end, L):
    l = 1
    for idx in range(start, end+1):
        l *= L[idx]
    return l

N = int(input())
L = tuple(float(input()) for i in range(N))
R = []

popoint=[]
for idx, val in enumerate(L):
    if val > 1: popoint.append(idx)
max_num = 0
for i in range(len(popoint)):
    for j in range(i+1, len(popoint)):
        l = mul(popoint[i], popoint[j], L)
        if max_num < l: max_num = l
print(f'{max_num:.3f}')
