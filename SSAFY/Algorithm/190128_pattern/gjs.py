import sys
sys.stdin = open("gjs_input.txt", "r")


T = int(input())
for N in range(T):
    str1, str2 = input(), input()
    st_dic = {}
    for f in str1:
        st_dic[f] = 0
    for s in str2:
        if s in st_dic:
            st_dic[s] += 1
    a = sorted(list(st_dic.values()))
    print(f'#{N+1} {a[-1]}')