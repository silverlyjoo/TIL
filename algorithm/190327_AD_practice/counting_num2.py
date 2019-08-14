import sys
sys.stdin = open('counting_num.txt')


def bns(num, data):
    start, end = 0, len(data)-1
    cnt = 0


    while start <= end:
        mid = (start+end)//2
        if data[mid] == num:
            for i in range(start, end+1):
                if data[i] == num:
                    cnt += 1
            return cnt
        elif data[mid] > num:
            end = mid - 1
        else:
            start = mid +1
    return 'F'


N = int(input())
data = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    a = bns(num, data)
    if a == 'F':
        print(0, end=" ")
    else:
        print(a, end=" ")



