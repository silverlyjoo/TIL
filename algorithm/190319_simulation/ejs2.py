import sys
sys.stdin = open('ejs2.txt')


T = int(input())

for tc in range(1, T+1):
    N = float(input())

    data = []
    for i in range(13):
        N *= 2
        if N >= 1:
            data.append('1')
            N -= 1
        else:
            data.append('0')
        if not N:
            break

    data = ''.join(data)

    if N:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, data))