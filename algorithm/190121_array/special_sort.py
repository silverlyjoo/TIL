import sys
sys.stdin = open("special_sort_input.txt")


T = int(input())
for Case in range(T):
    N = int(input())
    case_ls = list(map(int, input().split()))
    for i in range(len(case_ls)):
        if not i%2:
            max = 0
            for j in range(i, len(case_ls)):
                if case_ls[j] > case_ls[i]:
                    case_ls[i] , case_ls[j] = case_ls[j], case_ls[i]
        else:
            min = 100
            for k in range(i, len(case_ls)):
                if case_ls[k] < case_ls[i]:
                    case_ls[i], case_ls[k] = case_ls[k], case_ls[i]
    result = " ".join(map(str, case_ls[:10]))
    print(f'#{Case+1} {result}')
















    # while len(sort_list) != len(case_ls):
    #     max_num = 0, 0
    #     min_num = 100, 0
    #     for i in range(len(case_ls)):
    #         if case_ls[i] > max_num:
    #             max_num = case_ls[i], i
    #
    #         if case_ls[i] < min_num:
    #             min_num = case_ls[i], i

