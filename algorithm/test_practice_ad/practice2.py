import sys
sys.stdin = open('practice2.txt')

T = 2
for tc in range(1, T+1):

    data = list(input())
    data2 = []
    for i in data:
        data2.append(int(i, 16))
    nums = ''
    for i in data2:
        a =  bin(i)[2:]
        dif = 4-len(a)
        nums += '0'*dif + a
    L = []
    while len(nums) > 0:
        num = nums[:7]
        nums = nums[7:]
        L.append(num)
    for i in L:
        print(int(i, 2), end=" ")
    print()

