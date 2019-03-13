
import sys
sys.stdin = open('sosu.txt')

def issosu(a, b):
    result = []
    for i in range(a, b+1):
        if i == 2:
            result.append(i)
        elif i > 2:
            for j in range(2, int(i**0.5)+1):
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


