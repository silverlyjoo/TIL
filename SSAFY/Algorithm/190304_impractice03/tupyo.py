import sys
sys.stdin = open('tupyo.txt')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

result = [[0 for _ in range(5)] for _ in range(3)]

for num in range(3):
    result[num][4] = num+1

for i in range(N):
    for j in range(3):
        if L[i][j] == 3:
            result[j][1] += 1
        if L[i][j] == 2:
            result[j][2] += 1
        if L[i][j] == 1:
            result[j][3] += 1

result1 = 3*result[0][1] + 2*result[0][2] + result[0][3]
result2 = 3*result[1][1] + 2*result[1][2] + result[1][3]
result3 = 3*result[2][1] + 2*result[2][2] + result[2][3]

result[0][0] = result1
result[1][0] = result2
result[2][0] = result3

result.sort()
result.reverse()

if result[0][0] != result[1][0] or result[0][1] != result[1][1] or result[0][2] != result[1][2]:
    print(result[0][4], result[0][0])
else:
    print(0, result[0][0])
