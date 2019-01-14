
def countingsort(A, B, C):
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1


A = [1,4,5,1,2,4,5,7,9,3]
B = [0]*len(A)
C = [0]*10

countingsort(A, B, C)
print(A)
print(B)
print(C)