import sys
sys.stdin = open('max_price.txt')


def gonum(L):
    return int(''.join(map(str, L[:])))

def changeprice(n, tg, cnt, N, data):


    if cnt == N:
        result.append(gonum(data))
        return

    if tg >= n:
        return
        # tg = n-1
        # data[tg-1], data[tg] = data[tg], data[tg-1]
        # changeprice(n, tg + 1, cnt + 1, N, data)
        # data[tg - 1], data[tg] = data[tg], data[tg - 1]
    else:
        for i in range(n):
            data[i], data[tg] = data[tg], data[i]
            changeprice(n, tg+1, cnt+1, N, data)
            data[i], data[tg] = data[tg], data[i]


T = int(input())

for tc in range(1, T+1):
    nums, N = input().split()
    N = int(N)
    data = list(map(int, nums))
    result = []
    changeprice(len(data), 0, 0, N, data)
    R = list(map(int, result))
    print(max(R))
    # print(R)