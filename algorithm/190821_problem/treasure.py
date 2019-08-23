import sys
sys.stdin = open("treasure.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = N//4
    result = []
    L = list(input())
    for sub in range(0, n): # 빼는 수
        for start in range(0, -N, -n):
            letter = ''
            for i in range(n):
                letter += L[start+i-sub]
            letter = int(letter, 16)
            if letter not in result:
                result.append(letter)
    result.sort(reverse=True)
    print('#{} {}'.format(tc, result[K-1]))





            

