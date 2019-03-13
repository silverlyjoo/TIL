import sys
from pprint import pprint
sys.stdin = open("maul.txt")

def ishigh(y, x, data):
    if data[y][x] != 0 and data[y][x] <= data[y-1][x] and data[y][x] <= data[y+1][x] and data[y][x] <= data[y][x-1] and data[y][x] <= data[y][x+1]:
        return True




T = int(input())
data = [list(map(int, input())) for _ in range(T)]

max = 0
cnt = True

while cnt:
    cnt = False
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):
            if ishigh(i, j, data):
                data[i][j] += 1
                cnt = True
            if data[i][j] > max:
                max = data[i][j]

print(max)

    




# pprint(data)
