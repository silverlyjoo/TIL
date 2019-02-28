import sys
sys.stdin = open("maul.txt")

T = int(input())
data = [list(map(int, input())) for _ in range(T)]

max = 0

