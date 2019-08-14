

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def bubblesort(L):
    for idx in reversed(range(len(L))):
        for idx2 in range(idx):
            if L[idx2] > L[idx2+1]:
                swap(L, idx2, idx2+1)


L = [14213,213,24,52141,64253,12]
print(L)
bubblesort(L)
print(L)