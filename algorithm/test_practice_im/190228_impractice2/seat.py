import sys
from pprint import pprint
sys.stdin = open('seat.txt')


def iswall(x, y, C, R):
    if x < 0 or x >= C: return False
    if y < 0 or y >= R: return False
    if L[y][x] != 0: return False
    return True



C, R = map(int, input().split())
K = int(input())

L = [[0 for _ in range(C)] for _ in range(R)]
pprint(L)


y, x = 0, 0
L[y][x] = 1
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d_index = 0
item = 2
cnt = K
y += dy[d_index]
x += dx[d_index]

while cnt > 0:
    
    if iswall(x, y, C, R):
        L[y][x] = item
        item += 1
        cnt -= 1
    else:
        if d_index != 3:
            d_index += 1
        else:
            d_index = 0
    pprint(L)

print(L)


