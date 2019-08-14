T = [0]*10
A = [_ for _ in range(1, 11)]


def myprint(q):
    while q:
        q -= 1
        print('{}'.format(T[q]), end=' ')
    print()




def perm(n, r, q):

    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            A[i], A[n-1] = A[n-1], A[i]
            T[r-1] = A[n-1]
            perm(n-1, r-1, q)
            A[i], A[n - 1] = A[n - 1], A[i]

perm(4, 3, 3)