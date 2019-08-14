
import sys
sys.stdin = open("bi_gyo_input.txt", "r")

T = int(input())
for N in range(T):
    a = str(input())
    b = str(input())
    result = 0
    if a in b: result = 1
    print(f'#{N+1} {result}')