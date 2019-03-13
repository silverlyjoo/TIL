import sys
sys.stdin = open('gsw.txt')


def findone(sx, sy, ex, ey):
    cnt = 0
    for y in range(sy, ey):
        for x in range(sx, ex):
            if data[y][x] == 1:
                cnt += 1
    return cnt


N = int(input())

data = [list(map(int, input())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if findone(0,0,j,i) == findone(0,i,j,N) == findone(j,0,N,i) == findone(j,i,N,N):
            result += 1
if result:
    print(result)
else:
    print(-1)