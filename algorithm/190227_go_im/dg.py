import sys
sys.stdin = open("dg.txt")

T = int(input())

M = 10
N = 3

for tc in range(T):
    m, n = map(str, input().split())
    i = int(m)

    if n == 'Y' and i <= M:
        M = int(m)

    if n == 'N' and i >= M:
        N = int(m)

if M <= N or M == 10:
    print('F')
else:
    print(M)



# T = int(input())
# pig = [list(map(str, input().split())) for _ in range(T)]
#
# for i in pig:
#     i[0] = int(i[0])
# min = 10
# man = 0
#
# for i in range(T):
#     if pig[i][1] == 'Y':
#         if min > pig[i][0]:
#             min = pig[i][0]
#     else:
#         if man < pig[i][0]:
#             man = pig[i][0]
# if min<= man:
#     print('F')
# elif min == 10:
#     print('F')
# else:
#     print(min)