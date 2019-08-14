def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min_n = i
        for j in range(i+1, n):
            if A[j] < A[min_n]:
                min_n = j
        A[min_n], A[i] = A[i], A[min_n]

def recselectionsort(A, s, e):
    min_idx = s

    if s == e:
        return

    for j in range(s+1, e, 1):
        if A[j] < A[min_idx]:
            min_idx = j

    A[s], A[min_idx] = A[min_idx], A[s]

    recselectionsort(A, s+1, e)


A = [5,4,32,5,26,6,43,9,8,7,51,123]

recselectionsort(A, 0, len(A))
print(A)