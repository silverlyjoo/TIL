import sys
sys.stdin = open('chicken.txt')

def howlong(node1, node2):
    return abs(node1[0]-node2[0]) + abs(node1[1]-node2[1])


def comb(idx, start):

    if idx >= M:
        cnt = 0

        for home in house:
            min_length = 0xffffff
            for dark in chk:
                length = howlong(home, chicken[dark])
                if min_length > length:
                    min_length = length
            cnt += min_length
        result.append(cnt)
        return
    
    for i in range(start, len(chicken)):
        chk[idx] = i
        comb(idx+1, i+1)
        



N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for y in range(N):
    for x in range(N):
        if city[y][x] == 1:
            house.append([y, x])
        if city[y][x] == 2:
            chicken.append([y, x])


chk = [0 for _ in range(M)]
result = []
comb(0, 0)
print(min(result))

