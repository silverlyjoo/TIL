import sys
sys.stdin = open('binarysearch.txt')


def bns(num, data):
    start, end = 0, len(data)-1
    while start <= end:
        mid = (start+end)//2
        if data[mid] == num:
            return mid
        elif data[mid] < num:
            start = mid
        else:
            end = mid
    return 0

N = int(input())
data = list(map(int, input().split()))
T = int(input())
nums = list(map(int, input().split()))
for num in nums:
    a = bns(num, data)
    print(a)