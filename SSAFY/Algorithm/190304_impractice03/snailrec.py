import sys
sys.stdin = open('snailrec.txt')


def iswall(x, y, n):
    if x < 0 or x >= n: return False
    if y < 0 or y >= n: return False
    if L[y][x] != 0 : return False
    return True


n = int(input())

L = [[0 for _ in range(n)] for _ in range(n)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
iidx = 0
idx = iidx%4


for tc in range(n*n):
    if iswall(x, y, n):


    while iswall(x, y, n):

