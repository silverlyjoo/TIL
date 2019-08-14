import sys

sys.stdin = open('line.txt')

N = int(input())
L = list(map(int, input().split()))
result = []

for idx, value in enumerate(L):
    result.insert(value, idx+1)

print(*result[::-1])
