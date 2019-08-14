import sys
sys.stdin = open('jusawi.txt')




# def dfs(no):
#     if no > N:
#         for i in range(1, N+1): print(rec[i], end=' ')
#         print()
#         return
#
#     for i in range(1, 7): # 눈
#         rec[no] = i
#         dfs(no + 1)
#
#
# def dfs2(no):
#     if no > N:
#         for i in range(1, N + 1): print(rec[i], end=' ')
#         print()
#         return
#
#     for i in range(1, 7):  # 눈
#         if chk[i] : continue
#         chk[i] = 1
#         rec[no] = i
#         dfs(no + 1)
#         chk[i] = 0

# def dfs3(no, nsum):
#     if no>N:
#         if nsum==M:
#             for i in range(1, N+1):
#                 print(rec[i], end=" ")
#             print()
#         return
#     for i in range(1, 7):
#         rec[no] = i
#         dfs3(no+1, nsum+i)

def DFS3(no, sums):
    if no > N:
        return
    if no == N:
        if sums == M:
            for i in range(N):
                print(rec[i], end=" ")
            print()
        return
    for i in range(1, 7):
        rec[no] = i
        DFS3(no+1, sums + i)


N, M = map(int, input().split())
rec = [0 for _ in range(N+1)]
chk = [0]*7

DFS3(0, 0)
# dfs3(1,0)