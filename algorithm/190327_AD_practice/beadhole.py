import sys
sys.stdin = open('beadhole.txt')


def hole(blue, red, cnt):

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]


    redqueue = [red]



    for i in range(4):
        y = y + dy[i]








T = int(input())

for tc in range(1, T+1):

    Y, X = map(int, input().split())

    pan = [list(input()) for _ in range(Y)]



    for y in range(Y):
        for x in range(X):
            if pan[y][x] == 'B':
                blue = [y, x, 0]
            if pan[y][x] == 'R':
                red = [y, x, 0]
