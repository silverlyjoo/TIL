arr = [1,2,3]
n = len(arr)


for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=",")
    print()


# arr = [-7, -3, -2, 5, 8]
# n = len(arr)
#
# for i in range(1, 1<<n):
#     sum_ls = []
#     for j in range(n):
#         if i & (1<<j):
#             sum_ls.append(arr[j])
#     if sum(sum_ls) == 0:
#         print(sum_ls)