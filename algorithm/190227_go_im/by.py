import sys
sys.stdin = open("by.txt")


# Y, X = map(int, input().split())
#
# L = [list(map(int, input().split())) for i in range(Y)]
# R = [[0 for _ in range(X)] for _ in range(Y)]
#
# for i in range(Y):
#     for j in range(X):
#         if j == 0 and L[i][j]:
#             R[i][j] = 1
#         elif L[i][j-1] and L[i][j]:
#             R[i][j] = R[i][j-1] + 1
#         elif L[i][j]:
#             R[i][j] = 1
# for i in R:
#     print(*i)



Y, X = map(int, input().split())

L = [list(map(int, input().split())) for i in range(Y)]
R = [[0 for _ in range(X)] for _ in range(Y)]

for i in range(Y):
    for j in range(X):
        if j != 0 and L[i][j-1] and L[i][j]:
            R[i][j] = R[i][j-1] + 1
        elif L[i][j]:
            R[i][j] = 1
for i in R:
    print(*i)