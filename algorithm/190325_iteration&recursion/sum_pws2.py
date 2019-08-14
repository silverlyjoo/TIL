
L = list(range(1, 11))

A = [0 for _ in range(len(L))]
cnt = 0
result = []

def powerset(n, k, sums):
    global cnt
    cnt += 1
    if sums>10:
        return
    # cnt += 1
    if n == k:
        if sums == 10:
            for i in range(len(A)):
                if A[i]:
                    print(L[i], end=" ")
            print()

    else:
        A[k] = 1
        powerset(n, k+1, sums + L[k])
        A[k] = 0
        powerset(n, k+1, sums)

powerset(len(L), 0, 0)
print('#', cnt)