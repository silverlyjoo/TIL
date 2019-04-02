import sys
sys.stdin = open('minimun_fair.txt')


T = int(input())


for tc in range(1, T+1):

    N = int(input())

    H = [list(map(int, input().split())) for _ in range(N)]
    D = [[0xfffff for _ in range(N)] for _ in range(N)]
    maps = list(range(N**2))


