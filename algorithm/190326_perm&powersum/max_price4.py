import sys
sys.stdin = open('max_price.txt')


def gonum(L):
    return int(''.join(map(str, L[:])))

def changeprice(n, cnt, N, data):
    L = []

    if cnt == N:
        result.append(gonum(data))
        return

    for i in range(n):
        for j in range(i+1, n):
            data[i], data[j] = data[j], data[i]
            if data not in L:
                L.append(data[:])
            data[i], data[j] = data[j], data[i]

    for ls in L:
        changeprice(n, cnt + 1, N, ls)




T = int(input())

for tc in range(1, T+1):
    nums, N = input().split()
    N = int(N)
    data = list(map(int, nums))
    result = []
    changeprice(len(data), 0, N, data)
    R = list(map(int, result))
    print(max(R))
    # print(R)