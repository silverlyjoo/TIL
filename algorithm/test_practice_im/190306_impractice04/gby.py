import sys
sys.stdin = open('gby.txt')


C, R = map(int, input().split())

N = int(input())

L = [[] for _ in range(N)]
for shop in range(N):
