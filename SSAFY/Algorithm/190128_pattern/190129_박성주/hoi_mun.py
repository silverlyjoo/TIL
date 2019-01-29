import sys
from pprint import pprint
sys.stdin = open("hoi_mun_input.txt", "r")

def ishoimun(stdata, n, m):
    for y in range(n):
        for x in range(n-m+1):
            if stdata[y][x:x+m] == stdata[y][x:x+m][::-1]:
                return stdata[y][x:x+m]
T = int(input())
for t_case in range(T):
    N, M = map(int, input().split())
    data = [ _ for _ in [input() for x in range(N)]]
    data2 = [''.join([data[y][x] for y in range(N)]) for x in range(N)]
    a = ishoimun(data, N, M)
    b = ishoimun(data2, N, M)
    if a: print(f'#{t_case+1} {a}')
    else: print(f'#{t_case + 1} {b}')



