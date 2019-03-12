

def myprint(q):
    while q != 0:
        q -= 1
        print(" %d" % (T[q]), end='')
    print()


def combination(n, r, q):
    if r==0:
        myprint(q)
    else:
        if n < r:
            return
        else:
            T[r-1] = A[n-1]
            combination(n-1, r-1, q)
            combination(n-1, r, q)


A = [1, 2, 3, 4]
T = [0] * 3

combination(4, 3, 3)