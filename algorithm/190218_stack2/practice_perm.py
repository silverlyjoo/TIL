data = [1, 2, 3]
result = [False] * len(data)

R = []
L = []

def backtrack(result, k, R, data, L):
    if k == len(data):
        # print(R)
        L.append(R[:])

    else:
        for i in range(0, len(data)):
            if result[i] == False:
                R.append(data[i])
                result[i] = True
                backtrack(result, k + 1, R, data, L)
                result[i] = False
                R.pop()

backtrack(result, 0, R, data, L)
print(L)
