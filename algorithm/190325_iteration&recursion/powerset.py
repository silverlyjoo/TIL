


N = 3
A = [0 for _ in range(N)]
data = [1,2,3]



def powerset(n, k):
    if n == k:
        for j in range(len(A)):
            if A[j]:
                print(data[j], end=" ")
        print()
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

powerset(N, 0)