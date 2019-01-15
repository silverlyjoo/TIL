import sys
sys.stdin = open("e_bus_input.txt")

T = int(input())

for i in range(T):
    dist, length, cj_num = map(int, input().split())
    cj_points = list(map(int, input().split()))
    cj_point = dist
    count = 0
    re_count = dist
    while cj_point < length:
        if cj_point in cj_points:
            cj_point += dist
            count += 1
            re_count = dist
        else:
            cj_point -= 1
            re_count -= 1
        if re_count == 0:
            count = 0
            break
    print(f'#{i+1} {count})



