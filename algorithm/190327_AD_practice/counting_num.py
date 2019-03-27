import sys
sys.stdin = open('counting_num.txt')


def bns(num, data):
    start, end = 0, len(data)-1

    while start <= end:
        mid = (start+end)//2
        if data[mid] == num:
            return mid
        elif data[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 'F'

def countingnum(idx, data):

    idxu, idxd = idx+1, idx-1
    cnt = 1
    while idxu <= len(data)-1 and data[idxu] == data[idx]:
        cnt += 1
        idxu += 1
    while idxd >= 0 and data[idxd] == data[idx]:
        cnt += 1
        idxd -= 1
    return cnt

N = int(input())
data = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    a = bns(num, data)
    if a == 'F':
        print(0, end=" ")
    else:
        print(countingnum(a, data), end=" ")



