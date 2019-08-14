import sys
from pprint import pprint
sys.stdin = open("hoimun2_input.txt", "r")

def ishoimun(stdata, n, m):
    for y in range(n):
        for x in range(n-m+1):
            if stdata[y][x:x+m] == stdata[y][x+m-1:x-1:-1]:
                return m

for fc in range(10):
    T = int(input())
    data = [input() for i in range(100)]
    data2 = [''.join([data[y][x] for y in range(100)]) for x in range(100)]
    result1 = 0
    result2 = 0
    for M in range(99, -1, -1):
        if ishoimun(data, 100, M):
            result1 = M
            break
    for M in range(99, -1, -1):
        if ishoimun(data2, 100, M):
            result2 = M
            break
    if result1 > result2:
        print(f'#{T} {result1}')
    else:
        print(f'#{T} {result2}')
    # print(f'#{T} {max(result1, result2)}')