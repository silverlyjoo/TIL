
arr = [[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11]]

# i : 행의 좌표, n = len(arr)
# j : 열의 좌표, m = len(arr[0])

# 행우선

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = " ")
    print()
print()

# 열우선
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end = " ")
    print()
print()


# 지그재그 순회

n = len(arr)
m = len(arr[0])

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j+(m-1-2*j) * (i%2)], end = " ")
    print()
print()