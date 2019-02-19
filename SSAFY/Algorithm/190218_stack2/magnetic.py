import sys
from pprint import pprint
sys.stdin = open("magnetic_input.txt")


T = 10
for N in range(1, T+1):
    E = int(input())
    T = [list(map(int, input().split())) for _ in range(E)]
    iT = [[T[y][x] for y in range(100)] for x in range(100)]
    result = 0

    for i in range(E):
        stack = []
        for j in iT[i]:
            if j != 0:
                stack.append(j)

        for j in range(len(stack)-1):
            if stack[j] == 1 and stack[j+1] == 2:
                result += 1
    print(f'#{N} {result}')


T = 10
for N in range(1, T+1):
    E = int(input())
    T = [list(map(int, input().split())) for _ in range(E)]
    iT = [[T[y][x] for y in range(100)] for x in range(100)]
    result = 0

    for i in range(E):
        stack = []
        for j in iT[i]:
            if j == 1:
                stack.append(j)
            elif j == 2:
                if stack:
                    result += 1
                    stack = []

    print(f'#{N} {result}')