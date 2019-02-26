import sys
sys.stdin = open("hj_input.txt")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [_ for _ in map(int, input().split())]
    print(f'#{tc} {L[M%N]}')