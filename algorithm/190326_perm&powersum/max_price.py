import sys
sys.stdin = open('max_price.txt')


T = int(input())

for tc in range(1, T+1):
    nums, N = input().split()
    N = int(N)
    data = list(map(int, nums))
    data.reverse()

    L = []

    for i in range(N):
        max_num = max(data)
        max_idx = data.index(max_num)
        for j in range(len(data)-1, max_idx, -1):
            if data[j] < max_num:
                data[j], data[max_idx] = data[max_idx], data[j]
                L.append(data.pop(-1))
                break

    data.reverse()
    print(L)
    print(data)
    print()
    # result = ''.join(map(str, L))
    # print('#{} {}'.format(tc, result))




