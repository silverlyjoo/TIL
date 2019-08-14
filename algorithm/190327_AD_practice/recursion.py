

def summing(N):

    if N == 1:
        return 1
    else:
        return summing(N-1) + N

N = int(input())
print(summing(N))