import sys
sys.stdin = open('juice.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()
    data = ['1/'+N]*int(N)
    print('#{}'.format(tc), *data)