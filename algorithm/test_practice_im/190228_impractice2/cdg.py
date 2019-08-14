import sys
sys.stdin = open('cdg.txt')

def mul(start, end, L):
    l = 1
    for idx in range(start, end+1):
        l *= L[idx]
    return l

N = int(input())
L = tuple(float(input()) for i in range(N))
startpoints=[]
for idx, val in enumerate(L):
    if val > 1:
        startpoints.append(idx)
endpoints = startpoints[:]

max_num = 0
for start in range(len(startpoints)):
    for end in range(start, len(endpoints)):
        l = mul(startpoints[start], endpoints[end], L)
        if l > max_num:
            max_num = l

print(f'{max_num:.3f}')