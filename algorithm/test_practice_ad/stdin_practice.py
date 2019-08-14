import sys
sys.stdin = open('stdin_practice.txt')

N = int(input())
a, b = map(int, input().split())
data = [list(map(int, input())) for _ in range(a)]

print(N)
print(a, b)
for i in data:
    print(*i)