import sys
sys.stdin = open('ejs.txt')


T = int(input())

for tc in range(1, T+1):

    N, num16 = input().split()

    nums = list(num16)
    nums2 = []

    for num in nums:
        a = bin(int(num, 16))[2:]

        dif = 4-len(a)
        nums2.append('0'*dif+a)

    result = ''.join(nums2)


    print('#{} {}'.format(tc, result))
