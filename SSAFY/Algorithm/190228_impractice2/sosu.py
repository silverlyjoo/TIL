
import sys
sys.stdin = open('sosu.txt')

def issosu(a, b):
    result = []
    for i in range(a, b+1):
        for j in range(2, i):
            if not i%j:
                break
        else:
            result.append(i)
    return result



a, b = map(int, input().split())
m, n = min(a, b), max(a, b)

L = sorted(issosu(m,n))

t = len(L)
k = L[0]+L[-1]


print(t)
print(k)


