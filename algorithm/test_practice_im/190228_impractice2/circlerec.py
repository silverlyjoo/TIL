from pprint import pprint

T = int(input())
L = [[0 for _ in range(T*2+1)]for _ in range(T*2+1)]
cnt = 0
# for i in range(T+1):
#     for j in range(T+1):
#         if ((T-i)**2 + (T-j)**2)**(1/2) <= T:
#             L[i][j] = 1

# for i in range(T):
#     for j in range(T):
#         if L[i][j] == 1 and L[i][j+1] == 1 and L[i+1][j] ==1 and L[i+1][j+1] ==1:
#             cnt += 1
# print(cnt*4)


# for i in range(T*2+1):
#     for j in range(T*2+1):
#         if ((T-i)**2 + (T-j)**2)**(1/2) <= T:
#             L[i][j] = 1
#         if L[i][j] == 1 and L[i][j-1] == 1 and L[i-1][j] ==1 and L[i-1][j-1] ==1:
#             cnt += 1
# print(cnt)


for i in range(T+1):
    for j in range(T+1):
        if ((T-i)**2 + (T-j)**2)**(1/2) <= T:
            L[i][j] = 1
        if L[i][j] == 1 and L[i][j-1] == 1 and L[i-1][j] ==1 and L[i-1][j-1] ==1:
            cnt += 1

print(cnt*4)