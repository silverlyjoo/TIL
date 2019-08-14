import sys
sys.stdin = open("nasa_input.txt")

T = int(input())
for N in range(T):
    Case = int(input())
    case_ls = list(map(int, input().split()))
    front_ls = []
    back_ls = []
    result_ls = []
    for i in range(len(case_ls)):
        if not i%2:
            front_ls.append(case_ls[i])
        else:
            back_ls.append(case_ls[i])
    for j in range(Case):
        if front_ls[j] not in back_ls:
            result_ls.append(front_ls[j])
            result_ls.append(back_ls[j])
    count = 0
    while count < Case-1:
        count += 1
        for k in range(Case):
            if front_ls[k] == result_ls[-1]:
                result_ls.append(front_ls[k])
                result_ls.append(back_ls[k])
    print(f'#{N+1}',*result_ls)





    # print(front_ls)
    # print(back_ls)
    # print(result_ls)


