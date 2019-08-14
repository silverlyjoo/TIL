
import sys
sys.stdin = open("workshop_input.txt")
#
#
#
#
# for N in range(10):
#     T = int(input())
#     case_ls = []
#     for nums in range(100):
#         case_ls.append(list(map(int, input().split())))
#     result_ls = []
#     for x in range(len(case_ls)):
#         sum_ls = []
#         for y in range(len(case_ls[x])):
#             sum_ls.append(case_ls[x][y])
#         result_ls.append(sum(sum_ls))
#     for y in range(len(case_ls[0])):
#         sum_ls = []
#         for x in range(len(case_ls)):
#             sum_ls.append(case_ls[x][y])
#         result_ls.append(sum(sum_ls))
#     sum_z = []
#     for z in range(len(case_ls)):
#         sum_z.append(case_ls[z][z])
#     result_ls.append(sum(sum_z))
#     sum_z2 = []
#     for z2 in range(len(case_ls)):
#         sum_z2.append(case_ls[99-z2][z2])
#     result_ls.append((sum(sum_z2)))
#     max_result = 0
#     for maxnum in result_ls:
#         if maxnum > max_result:
#             max_result = maxnum
#     print(f'#{N+1} {max_result}')


for N in range(10):
    T = int(input())
    case_ls = []
    for nums in range(100):
        case_ls.append(list(map(int, input().split())))
    result_ls = []
    for x in range(len(case_ls)):
        sum_lsx = []
        sum_lsy = []
        for y in range(len(case_ls[x])):
            sum_lsx.append(case_ls[x][y])
            sum_lsy.append(case_ls[y][x])
        result_ls.append(sum(sum_lsx))
        result_ls.append(sum(sum_lsy))
    sum_lsz1 = []
    sum_lsz2 = []
    for z in range(len(case_ls)):
        sum_lsz1.append(case_ls[z][z])
        sum_lsz2.append(case_ls[99-z][z])
    result_ls.append(sum(sum_lsz1))
    result_ls.append(sum(sum_lsz2))
    max_result = 0
    for maxnum in result_ls:
        if maxnum > max_result:
            max_result = maxnum
    print(f'#{N+1} {max_result}')


