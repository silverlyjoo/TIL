import sys
sys.stdin = open('cdg.txt')

def mul():
    max_num = 0
    for i in range(len(L)):
        l = 1
        for j in range(i, len(L)):
            l *= L[j]
            if l > max_num:
                max_num = l
    return max_num

N = int(input())
L = tuple(float(input()) for i in range(N))

print(f'{mul():.3f}')