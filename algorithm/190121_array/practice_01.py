

arr = [[1,3,4,5,9],[10,11,2,13,14],[15,6,7,8,16],[17,18,12,19,20],[21,22,23,24,25]]
# arr.append(map(int, input().split()))

arr = [[0 for ze in range(5)] for ro in range(5)]

for i in range(5):
    arr[i] = list(map(int, input().split()))


def iswall(testX, testY):
    if testX < 0 or testX >=5:
        return False
    if testY <0 or testY >= 5:
        return False
    return True





def my_abs(num):
    if num < 0:
        return num *= -1

ans_list = []

for i in range(len(arr)):
    for j in range(len(arr[i])):


