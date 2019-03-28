


def comb(k):
    if k >= N:
        print(*b)
        return
    b[k] = a[k]
    comb(k+1)
    b[k] = 0
    comb(k+1)

N = 3
a = [1, 2, 3]
b = [0 for _ in range(len(a))]

comb(0)

