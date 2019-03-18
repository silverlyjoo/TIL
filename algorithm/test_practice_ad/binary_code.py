import sys
sys.stdin = open('binary_code.txt')

code = ['0001101',
        '0011001',
        '0010011',
        '0111101',
        '0100011',
        '0110001',
        '0101111',
        '0111011',
        '0110111',
        '0001011']

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = [input() for _ in range(N)]
    num = ''
    for i in data:
        if int(i):
            num = i
            break
    nums = []
    while num and len(num) >= 7:
        patt = num[-7:]
        if patt in code:
            nums.append(code.index(patt))
            num = num[:-7]
        else:
            num = num[:-1]
    nums = nums[::-1]

    result = 0
    for i in range(0, 8, 2):
        result += int(nums[i+1]) + int(nums[i])*3

    if result%10:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, sum(nums)))