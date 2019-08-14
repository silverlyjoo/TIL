from pprint import pprint
import sys
sys.stdin = open("ladder_input.txt")

# def isrl(v, h, L):
#     L[v][h] = 2
#     if v == 0:
#         return h
#     else:
#         if h != 0 and h != 99:
#             if L[v][h-1] ==1:
#                 return isrl(v, h-1, L)
#             elif L[v][h+1] == 1:
#                 return isrl(v, h+1, L)
#             else:
#                 return isrl(v-1, h, L)
#         elif h == 0:
#             if L[v][h+1] == 1:
#                 return isrl(v, h+1, L)
#             else:
#                 return isrl(v-1, h, L)
#         else:
#             if L[v][h-1] == 1:
#                 return isrl(v, h-1, L)
#             else:
#                 return isrl(v-1, h, L)
#
# for _ in range(10):
#     N = int(input())
#     L = [list(map(int, input().split())) for _ in range(100)]
#     T = 0
#
#     for t in range(100):
#         if L[99][t] == 2:
#             T = t
#     print(f'#{N} {isrl(99, T, L)}')


for _ in range(10):
    tc = '#' + input()
    sadari = [list(map(int, input().split())) for i in range(100)]
    p = sadari[99].index(2)

    for i in sadari[::-1]:
        if